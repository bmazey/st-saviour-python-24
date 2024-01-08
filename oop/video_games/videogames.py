class VideoGames:
    # this class defines video games
    def __init__(self, title: str, multiplayer: bool):
        # all games have a title
        self.title = title
        # defines if the game has more than one player
        self.multiplayer = multiplayer
    
    def play(self, player_name: str, session: int):
        # states the amount of time a player plays the game
        self.player_name = player_name
        # gives the player a username
        session = ''
        player_name + "has played" + self.title + "for" + session 
        # gives back the player name, the game title and the time that the game was beign played
