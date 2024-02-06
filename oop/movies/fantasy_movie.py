from oop.movies.movie import Movie

class FantasyMovie(Movie):
    """A class which defines all fantasy movies."""
    #     # All fantasy movies have title and duration.Use float for duration
    def __init__(self, title: str, duration: float):
        super().__init__(title, duration)

        # All fantasy movies take audiences to magical worlds
        self.takes_to_magical_world = True

    # Override the watch method for fantasy movies
    def watch(self):
        return f"Watching {self.title} for {str(self.duration)} hours and entering a magical world!"