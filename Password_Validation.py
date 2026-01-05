import re

# Read comma separated passwords
passwords = input("Enter passwords: ").split(',')

valid_passwords = []

for pwd in passwords:
    pwd = pwd.strip()
    
    if (len(pwd) >= 6 and len(pwd) <= 12 and
        re.search("[a-z]", pwd) and
        re.search("[A-Z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[$#@]", pwd)):
        
        valid_passwords.append(pwd)

# Print valid passwords separated by comma
print(",".join(valid_passwords))
