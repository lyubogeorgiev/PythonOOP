class Test:
    text = "Hello"

    def do_smth():
        return 'doing something'


print(Test.text)
print(Test.do_smth())

class Dog:
    dog_counter = 0

    def __init__(self, name: str, breed):
        self.name = name
        self.breed = breed

        Dog.dog_counter += 1


first_dog = Dog("Max", "Rhodesian Ridgeback")
second_dog = Dog("Nini", "Pitbull")

print(f'Count of dogs: {Dog.dog_counter}')
