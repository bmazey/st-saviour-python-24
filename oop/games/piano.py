from oop.games.instrument import Instrument

# new class under instruments 
class Piano(Instrument):
    # defining the following instances 
    # defining the instances in the class and their properties
    # the new properitiy in piano is scale
    # to represent how it differs from Dance
    # it has more musical based elements and thus aspects of music theory
    # like scales, notes and octives
    # scale is a list to represent the different scales you can play on a piano
    def __init__(self, title: str, multiplayer: bool, note: int, scale: []):
        # super because it inherits properties from the parent class
        super().__init__(title, multiplayer, note,)
        # the ideal scale will be represented by "scale"
        self.scale = scale

    # creating a method to add an octave to the list of scales
    # because one scale is one octave
    # but different scales can be played in different octaves
    # me when im a music theory nerd ୨୧
    def add_scale(self, octave: str):
        # adding the the octave the scale is in
        self.scale.append(octave)
    