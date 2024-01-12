from oop.movies.movie import Movie

# Define a subclass FantasyMovie that inherits from the Movie class
class FantasyMovie(Movie):
    """A class which defines all fantasy movies."""

    # Constructor method to initialize a FantasyMovie object
    def __init__(self, title: str, duration: float):
        # Call the constructor of the parent class (Movie) using super()
        super().__init__(title, duration)

        # Additional attribute for fantasy movies
        # All fantasy movies take audiences to magical worlds
        self.takes_to_magical_world = True

    # Override the watch method for fantasy movies
    def watch(self):
        # Provide a specific message for watching fantasy movies
        return f"Watching {self.title} for {str(self.duration)} hours and entering a magical world!"


