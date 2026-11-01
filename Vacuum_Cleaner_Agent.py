
environment = {
    "A" : "Clean",
    "B" : "Dirty"
}

class VacuumAgent:
    def __init__(self, environment):
        self.environment=environment
        self.current_room="A"

    def sense(self):
        print(f"Room {self.current_room} is {self.environment[self.current_room]}")

    def clean(self):
        if self.environment[self.current_room]=="Dirty":
            print(f"Cleaning {self.current_room}")
            self.environment[self.current_room]="Clean"

    def move(self):
        if self.current_room=="A":
            self.current_room="B"
        else:
            self.current_room="A"

        print(f"Moving to room {self.current_room}")


agent=VacuumAgent(environment)

agent.sense()
agent.clean()
agent.move()
agent.sense()
agent.clean()
