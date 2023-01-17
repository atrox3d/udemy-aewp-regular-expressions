import re
from pathlib import Path

files = Path('files/')
filenames = files.iterdir()
filenames = [filename.name for filename in filenames]
print(filenames)

pattern = re.compile(r'nov[a-z]*-(?:[1-9]|1[0-9]|20).txt', re.IGNORECASE)
matches = [filename for filename in filenames if pattern.findall(filename)]
print(matches)
