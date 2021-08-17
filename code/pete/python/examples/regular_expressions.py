import re

phone_numbers_raw = '(666)420-6969 (123)1234-123 (123)456-7890'
phone_numbers_validated = re.findall(r'\([0-9]{3}\)[0-9]{3}-[0-9]{4}', phone_numbers_raw)

print(phone_numbers_validated) # ['(666)420-6969', '(123)456-7890']