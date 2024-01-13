from oop.games.dance import Dance

# creating new class under the parent class Dance
class Just_Dance(Dance):
    # defining that the class has the folllowing instances
    # and that those instances in the class have the following properties
    # put the data types of the instances after the :
    # the last two are going to be lists (epic :3)
    def __init__(self, title: str, multiplayer: bool, step: [], console: []):
        # super to get so Just_Dance inherits the properties of Dance
        super().__init__(title, multiplayer, step)
        # the ideal instance of a console is going to be represented by the variable console
        self.console = console
    # defining a new method so we can add more consoles to the list of consoles 
    # that way it can show the list of consoles the game is available on
    def add_console(self, device: str):
        # a console is like also a gaming device
        # so we add the gaming device to the list of consoles
        self.console.append(device)
    
