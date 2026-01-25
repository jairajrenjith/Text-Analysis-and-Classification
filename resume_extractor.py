import re
import os
import json

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
RAW_PHONE_PATTERN = r'[\+\(\)\d][\d\-\s\(\)]{8,}\d'

def extract_name(lines):
    for line in lines:
        line = line.strip()
        if line and len(line.split()) <= 4 and not any(char.isdigit() for char in line):
            return line
    return "Not Found"

def extract_role(lines, name):
    for line in lines:
        clean = line.strip()

        if (
            clean
            and clean != name
            and "email" not in clean.lower()
            and "phone" not in clean.lower()
            and "mobile" not in clean.lower()
            and not re.search(EMAIL_PATTERN, clean)
            and not re.search(RAW_PHONE_PATTERN, clean)
            and len(clean.split()) <= 6
        ):
            return clean
    return "Not Found"

def extract_contacts(text):
    emails = re.findall(EMAIL_PATTERN, text)
    raw_phones = re.findall(RAW_PHONE_PATTERN, text)

    cleaned_phones = []
    for phone in raw_phones:
        digits_only = re.sub(r'\D', '', phone)
        if 10 <= len(digits_only) <= 15:
            cleaned_phones.append(phone.strip())

    return list(set(emails)), list(set(cleaned_phones))

def extract_info(text):
    lines = text.strip().split("\n")

    name = extract_name(lines)
    role = extract_role(lines, name)
    emails, phones = extract_contacts(text)

    return {
        "name": name,
        "role": role,
        "emails": emails,
        "phone_numbers": phones
    }

def process_resumes(folder_path):
    results = {}

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                results[file_name] = extract_info(text)

    return results

if __name__ == "__main__":
    resume_folder = "resumes"
    extracted_data = process_resumes(resume_folder)

    with open("output.json", "w", encoding='utf-8') as json_file:
        json.dump(extracted_data, json_file, indent=4)

    print("Extraction complete! Data saved to output.json")
