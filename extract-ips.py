import re


with open('ips.txt') as file:
    content = file.read()

print(content)

# regexp = r'[0-9]{1,3}\.+[0-9]{1,3}\.+[0-9]{1,3}\.+[0-9]{1,3}'
# regexp = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
# regexp = r'https?://(?:www.)?[^ \n]+\.com'

regexp = r'[0-9]{1,3}\.[0-9]{1,3}\.12[0-9]{1}\.[0-9]{1,3}'
matches = re.findall(regexp, content)
print(matches)
