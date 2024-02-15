from lib.recipe_repository import *
from lib.recipe import *

"""
When we call ArtistRepository#all
we get a list of Artist objects reflecting the seed data.
"""

def test_get_all_recipes(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)
    recipes = repository.all()

    assert recipes == [
        Recipe('Beef Stew', 120, 5),
        Recipe('Veg Burrito', 30, 5),
        Recipe('Pancake', 40, 5),
        Recipe('Mixed veg', 120, 3)
    ]

"""
When we call RecipeRepository#find
we get a single Recipe object reflecting the seed data.
"""
def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(40)
    assert recipe == Recipe('Pancake', 40, 5)