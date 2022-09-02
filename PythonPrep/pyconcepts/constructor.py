class A:

    def __init__(self):

        self.name = input("Enter First_name: ")
        self.age = input("Age: ")
        self.location = input("Location: ")

    def person_details(self):
        print(f"{self.name}, {self.age}, {self.location}")


A().person_details()