

class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movei: str) -> None:
        print(f'{self.name} is watching "{movei}".')
