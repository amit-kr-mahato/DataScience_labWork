# 5. Use the re module to write a script that searches through a paragraph and extracts all
# words that start with an uppercase letter (e.g., "London", "Python") to identify proper
# nouns or sentence starters.

import re

paragraph = "Python is Popular. London is a City. Amit Studies Computer Science."
words = re.findall(r'\b[A-Z][a-zA-Z]*\b', paragraph)
print(words)