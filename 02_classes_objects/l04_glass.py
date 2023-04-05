class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int):
        new_content = self.content + ml

        if new_content <= Glass.capacity:
            self.content += ml
            return f'Glass filled with {ml} ml'
        else:
            return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0

        return 'Glass is now empty'

    def info(self):
        free_capacity = Glass.capacity - self.content

        return f'{free_capacity} ml left'


glass = Glass()

print(glass.fill(100))

print(glass.fill(200))

print(glass.empty())

print(glass.fill(200))

print(glass.info())