import re
import json

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:\+91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}'

with open("resumes.txt", "r") as file:
    text = file.read()

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

data = {
    "emails": list(set(emails)),
    "phone_numbers": list(set(phones))
}

with open("output.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("Extraction completed. Saved to output.json")
