from oop.games.rhythm import Rythym

# new class under Rythym
class Dance(Rythym):
    # steps represesnts the steps in dancing
    def __init__(self, title: str, multiplayer: bool, step: []):
        # super to inherit the properties from the parent class
        super().__init__(title, multiplayer)
        # list of steps in the dance
        self.step = step
    # add step so to add another step of the instructions in the dance
    def add_step(self, movemet: str):
        # use append to add to the list
        self.step.append(movemet)