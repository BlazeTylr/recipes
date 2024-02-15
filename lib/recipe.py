class Recipe():
    def __init__(self, name, cooking_time, rating):
        self.name = name
        self.cooking_time = cooking_time
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Recipe({self.name}, {self.cooking_time}, {self.rating})"

    