import re
tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

a=r'#\w+'

print(re.findall(a,tweet))