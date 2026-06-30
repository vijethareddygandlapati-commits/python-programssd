import re
text = "my phone number is 9876543210"
print(re.findall(r'\d', text))         
print(re.findall(r'\d{10}', text))       
print(re.findall(r'my', text))        
print(re.findall(r'phone', text))      
