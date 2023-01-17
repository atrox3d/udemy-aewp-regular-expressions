import re


with open('urls.txt') as file:
    content = file.read()

print(content)

regexp = r'[^ \n]+\.com'
regexp = r'https?://(?:www.)?[^ \n]+\.com'
matches = re.findall(regexp, content)
print(matches)
