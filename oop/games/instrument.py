from oop.games.rhythm import Rythym
# instrument representing games with components that are instruments or represent instruments
# or generally has instrumental themes
# creating instrument as a class under the parent class of Rythym
class Instrument(Rythym):
    # defining how an instance of an game under the class of instrument has these properties
    # the properties being, title, multiplayer, and note
    # the words in orange after the : represent their data type (str, bool, int)
    def __init__(self, title: str, multiplayer: bool, note: int):
        # super so that this class inherits properties from the parent class
        super().__init__(title, multiplayer)
        # showing how the ideal instance of a note will be represented by a list
        # right now the list is empty
        self.note = []

    # creating a method to add notes to the list
    # combo represents like a the combination of notes the player needs play in game
    def add_note(self, combo: int):
        # apppend to add the combination of notes into the list
        self.note.append(combo)

    # me attempting to do a __repr__ :0 (scary)  
    # defining bpm as something with the following properties
    # they are both str data types
    def bpm(self, notes: str, song: str):
        # using variable of "notes" to represent the ideal instance of notes
        self.notes = notes
        # using the same logic to creat the variable "song" for self.song
        self.song = song                        

    # (trying) using __repr__ to create a printable representation of the str data above
    # (repr)esntation... makes sense (i think)
    def __repr__(self):
        # returning the instances with the class but in a message
        # so that it (hopefully) says "(what ever note self.notes is) per (whatever song self.songs is )"
        # they way i kind of understand it is like *instert note here* per *inster song here*
        # im likely completely wrong in the way of thinking though T-T ¯\_(ツ)_/¯
        return f"({'self.notes'}) per ({'self.song'})"
    
    