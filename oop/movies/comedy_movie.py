from oop.movies.movie import Movie

# Define a subclass ComedyMovie that inherits from the Movie class
class ComedyMovie(Movie):
    """A class which defines all comedy movies."""

    # Constructor method to initialize a ComedyMovie object
    def __init__(self, title: str, duration: float):
        # Call the constructor of the parent class (Movie) using super()
        super().__init__(title, duration)

        # Additional attribute for comedy movies
        # All comedy movies aim to make people laugh
        self.makes_people_laugh = True

    # Override the watch method for comedy movies
    def watch(self):
        # Provide a specific message for watching comedy movies
        return f"Watching {self.title} for {str(self.duration)} hours and having a good laugh!"


