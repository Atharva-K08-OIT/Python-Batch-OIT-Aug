import re

text = '''
Client IP: 192.168.0.1
Request received from 10.0.0.1
Server IP: 172.16.0.1
'''
pattern = r"\b(?:\d{1,3}\.){3}\d{1}\b"


matches = re.findall(pattern, text)

print(matches)


userdata = '''
username: Atharva
password: 08june2002@ak
username: Aditya
password: aditya_$100
'''

newpatturn = r"username: (\w+[^\n])\npassword: ([\w@_$]+[^\n])"

newMatches = re.findall(newpatturn, userdata)

# print(newMatches)
count = 1
for user in newMatches:
    print(f"user {count}: {user[0]} having pass {user[1]}")
    count += 1
