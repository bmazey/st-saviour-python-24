from oop.movies.movie import Movie

# Define a subclass HorrorMovie that inherits from the Movie class
class HorrorMovie(Movie):
    """A class which defines all horror movies."""

    # Constructor method to initialize a HorrorMovie object
    def __init__(self, title: str, duration: float):
        # Call the constructor of the parent class (Movie) using super()
        super().__init__(title, duration)

        # Additional attribute for horror movies
        # All horror movies create fear
        self.creates_fear = True

    # Override the watch method for horror movies
    def watch(self):
        # Provide a specific message for watching horror movies
        return f"Watching {self.title} for {str(self.duration)} hours and getting scaredddd!"
