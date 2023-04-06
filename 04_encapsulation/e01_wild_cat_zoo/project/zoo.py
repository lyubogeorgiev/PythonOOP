from project.animal import Animal
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        if not [x for x in self.workers if x.name == worker_name]:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove([x for x in self.workers if x.name == worker_name][0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        money_needed = sum(s.salary for s in self.workers)

        if money_needed >= self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= money_needed
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_needed = sum(a.money_for_care for a in self.animals)

        if money_needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= money_needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        animals_available = {
            "Lions": [x for x in self.animals if x.__class__.__name__ == 'Lion'],
            "Tigers": [x for x in self.animals if x.__class__.__name__ == 'Tiger'],
            "Cheetahs": [x for x in self.animals if x.__class__.__name__ == 'Cheetah']
        }

        message = [f"You have {len(self.animals)} animals"]

        for key in animals_available.keys():
            message.append(f"----- {len(animals_available[key])} {key}:")

            for animal in animals_available[key]:
                message.append(repr(animal))

        return '\n'.join(message)

    def workers_status(self):
        workers_available = {
            "Keepers": [k for k in self.workers if k.__class__.__name__ == 'Keeper'],
            "Caretakers": [c for c in self.workers if c.__class__.__name__ == 'Caretaker'],
            "Vets": [v for v in self.workers if v.__class__.__name__ == 'Vet']
        }

        message = [f"You have {len(self.workers)} workers"]

        for key in workers_available.keys():
            message.append(f"----- {len(workers_available[key])} {key}:")

            for worker in workers_available[key]:
                message.append(repr(worker))

        return '\n'.join(message)
