from oop.movies.movie import Movie

# Define a subclass RomanceMovie that inherits from the Movie class
class RomanceMovie(Movie):
    """A class which defines all romance movies."""

    # Constructor method to initialize a RomanceMovie object
    def __init__(self, title: str, duration: float):
        # Call the constructor of the parent class (Movie) using super()
        super().__init__(title, duration)

        # Additional attribute for romance movies
        # All romance movies create a warm, fuzzy feeling
        self.creates_warmth = True

    # Override the watch method for romance movies
    def watch(self):
        # Provide a specific message for watching romance movies
        return f"Watching {self.title} for {str(self.duration)} hours and feeling all warm and fuzzy inside!"
