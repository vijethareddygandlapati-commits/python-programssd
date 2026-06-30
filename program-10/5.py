try:
    x = int(input("Enter a number upto 100: "))
    if x > 100:
        raise ValueError("Number out of allowed range")
except ValueError as e:
    print("Error:", e)
else:
    print(x, "is within allowed range")
