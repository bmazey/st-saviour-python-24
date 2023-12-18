class VideoGames:
    def __init__(self, title: str, multiplayer: bool):
        self.title = title
        self.multiplayer = multiplayer
    
    def play(self, player_name: str, session: int):
        self.player_name = player_name
        session = ''
        player_name + "has played" + self.title + "for" + session 
