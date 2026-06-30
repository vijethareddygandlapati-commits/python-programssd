import re
text="Devops 123"
if re.match(r'^[a-z,A-Z,0-9]+$',text):
           print("Alphanumeric string")
else:
           print("Not Alphanumeric")
