# person.py

class Person:
    """
    A class to represent a person.
    """

    def __init__(self, name, age):
        """
        Initialize a new Person instance.

        :param name: str - The person's name.
        :param age: int - The person's age.
        """
        self.name = name
        self.age = age
        

    def display_info(self):
        """
        Display the person's information.
        """
        
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("displayed the info") #feature change
        # resolved the conflict

    def birthday(self):
        """
        Increment the person's age by 1.
        """
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")
        print("This is comment added by Gaurav")

    def update_name(self, new_name):
        """
        Update the person's name.

        :param new_name: str - The new name.
        """
        old_name = self.name
        self.name = new_name
        print(f"Name changed from {old_name} to {self.name}.")


# Example usage
if __name__ == "__main__":
    person = Person("Alice", 30)
    person.display_info()
    person.birthday()
    person.update_name("Alicia")
    person.display_info()
