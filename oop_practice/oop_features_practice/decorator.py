class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating

        else:
            print("Entery is not valid")


overrated_movie = Movie("Titanic", 5)
print(overrated_movie.rating)

overrated_movie.rating = 4.1
print(overrated_movie.rating)