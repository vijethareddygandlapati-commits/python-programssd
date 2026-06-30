class MyClass:
    def __init__(self):
        self.public_attribute = "I am a public attribute"
        self._protected_attribute = "I am a protected attribute"
        self.__private_attribute = "I am a private attribute"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    # Access private method inside class
    def access_private(self):
        print(self.__private_attribute)
        self.__private_method()


# Object creation
obj = MyClass()

# Public access (allowed)
print(obj.public_attribute)
obj.public_method()

print()

# Protected access (allowed but not recommended)
print(obj._protected_attribute)
obj._protected_method()

print()

# Private access (not directly allowed)
obj.access_private()
