class VideoGames:
    # this class defines video games
    def __init__(self, title: str, multiplayer: bool):
        # all games have a title
        self.title = title
        # defines if the game has more than one player
        self.multiplayer = multiplayer
    
    def play(self, player_name: str, session: int):
        self.player_name = player_name
        session = ''
        player_name + "has played" + self.title + "for" + session 
