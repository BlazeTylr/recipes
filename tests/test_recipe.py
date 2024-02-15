from lib.recipe import *

"""
Recipe constructs with an id, name and genre.
"""
def test_recipe_constructs():
    recipe = Recipe('Test Recipe', 45, 5)
    assert recipe.name == 'Test Recipe'
    assert recipe.cooking_time == 45
    assert recipe.rating == 5

"""
We can format recipe to strings nicely
"""
def test_recipe_format_nicely():
    recipe = Recipe('Test Recipe', 45, 5)
    assert str(recipe) == "Recipe(Test Recipe, 45, 5)"

"""
We can compare two identical artists
and have them be equal
"""
def test_recipe_are_equal():
    recipe1 = Recipe('Test Recipe', 45, 5)
    recipe2 = Recipe('Test Recipe', 45, 5)
    assert recipe1 == recipe2