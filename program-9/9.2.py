file_path="output.txt"
with open(file_path,"w")as file:
    file.write("Hello,world\n")
    file.write("this is a sample text.")
    print("content written to",file_path)
