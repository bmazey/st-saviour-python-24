from oop.movies.movie import Movie

class ComedyMovie(Movie):
    """A class which defines all comedy movies."""
    # All comedy movies have title and duration.Use float for duration
    def __init__(self, title: str, duration: float):
        super().__init__(title, duration)

        # All comedy movies aim to make people laugh
        self.makes_people_laugh = True

    # Override the watch method for comedy movies
    def watch(self):
        return f"Watching {self.title} for {str(self.duration)} hours and having a good laugh!"