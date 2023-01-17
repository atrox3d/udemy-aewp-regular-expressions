"""
.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    uMatches a single character or a range that is contained within brackets
         _- -_ order does not matter but without brackets order does matter
+        Matches the preeceding element one or more times
?        Matches the preeceding pattern element zero or one time
*        Matches the preeceding element zero or more times
{m,n}    Matches the preeceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression
"""
import re

text = 'hi there, you here exa_mple@example.com @blabla and there another@example.de excludeme@example.ne'

regexp = (
    r'[^ ]+'        # anything non whitespace, one or more occurrences
    r'@'            # at
    r'[^ ]+'        # anything non whitespace, one or more occurrences
    r'\.'           # literal dot
    r'('            # BEGIN capturing group
    r'?:'           # turn off capturing -> non-capturing group
    r'com|de'       # com OR de
    r')'            # END (non)-capturing group
)
regexp = r'[^ ]+@[^ ]+\.(?:com|de)'

matches = re.findall(regexp, text)
print(matches)
