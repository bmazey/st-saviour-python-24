class Movie:
    """A base class for all movies."""
    def __init__(self, title: str, duration: float):
        # All movies have tile and duration. Use float for during.
        self.title = title
        self.duration = duration

    def watch(self):
        return f"Watching {self.title} for {str(self.duration)} hours!"

