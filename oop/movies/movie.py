# Define a base class Movie for all movies
class Movie:
    """A base class for all movies."""

    # Constructor method to initialize a Movie object
    def __init__(self, title: str, duration: float):
        self.title = title  # Set the title attribute
        self.duration = duration  # Set the duration attribute

    # Method to simulate watching the movie
    def watch(self):
        return f"Watching {self.title} for {str(self.duration)} hours!"

