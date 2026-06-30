file_path="output.txt"
with open(file_path,"r")as file:
           content=file.read()
           words=content.split()
           word_count=len(words)
print("Total words in",file_path,":",word_count)
