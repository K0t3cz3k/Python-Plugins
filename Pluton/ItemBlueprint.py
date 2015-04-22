__author__ = 'DreTaX'
__version__ = '1.0'

"""
    This file was created for plugin developers to be able to use the correct functions
    without looking at the wiki or the api.
    API showoff purposes only, and nothing else.
"""
import ItemDefinition
import Rarity

class ItemBlueprint:

    ingredients = []
    amountToCreate = 1
    userCraftable = True
    targetItem = ItemDefinition
    time = 0.0
    defaultBlueprint = None
    rarity = Rarity