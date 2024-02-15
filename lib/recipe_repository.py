from lib.recipe import *

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            item = Recipe(row['name'], row['cooking_time'], row['rating'])
            recipes.append(item)
        return recipes
    
    def find(self, cooking_time):
        rows = self._connection.execute('SELECT * FROM recipes WHERE cooking_time = %s', [cooking_time])
        row = rows[0]
        return Recipe(row['name'], row['cooking_time'], row['rating'])