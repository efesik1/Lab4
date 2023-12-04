class Person:
    # Метод экземпляра
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Еще один метод экземпляра
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Статический метод
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Метод класса
    @classmethod
    def create_adult(cls, name):
        return cls(name, 18)



if __name__ == "__main__":
    person1 = Person("Alice", 25)

    person1.introduce()

    is_adult = Person.is_adult(20)
    print(f"Is 20 years old an adult? {is_adult}")

    adult_person = Person.create_adult("Bob")
    adult_person.introduce()
