class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def next_second(self):
        self.seconds += 1

        if self.seconds > 59:
            self.seconds -= 60
            self.minutes += 1
            if self.minutes > 59:
                self.minutes -= 60
                self.hours += 1
                if self.hours > 23:
                    self.hours -= 24

        return self.get_time()


time = Time(9, 30, 59)

print(time.next_second())