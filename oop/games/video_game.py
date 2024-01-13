
class VideoGame:
    # all video games have titles and some are multiplayer
    def __init__(self, title: str, multiplayer: bool):
        self.title = title
        self.multiplayer = multiplayer
        
    # session is an integer since it represents time played
    def play(self, player_name: str, session: int,):
        self.player_name = player_name
        session = ''
        player_name + "has played" + self.title + "for" + session
        
        return session