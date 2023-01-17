import re

text = 'hi there, you here exa_mple@example.com @blabla and there another@example.de'

matches = re.findall('[^ ]+@[^ ]+[.][^ ]+', text)

for match in matches:
    print(f'sending email to {match}...')
