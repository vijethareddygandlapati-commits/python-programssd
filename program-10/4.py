try:
           file=open("my file.txt,"r")
except to error:
          print("Error:unable to read file!")
finally:
           file.close()
