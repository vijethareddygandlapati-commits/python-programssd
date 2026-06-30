file_path="Example.txt"
with open(file_path,"w")as file:
           file.write("Hello,world")
with open(file_path,"r")as file:
            content=file.read()
            print("File content:",content)
