from behave import *
from src.Game import *
from src.Catalogue import *
import ast

def before_scenario(context, scenario):
    context = {}

@given("the user chooses ratings {list_ratings}")
def step_impl(context, list_ratings):
    print(context.games)
    context.ratings = ast.literal_eval(list_ratings)

@when("the user chooses '{option}' option")
def step_impl(context, option):
    if (option == 'search by ratings'):
        result, message, error = get_game_rating(context.games, context.ratings)
        print(result)
        context.result = result
        context.message = message
        if error == None:
            context.error = 'None'
        else:
            context.error = error

@then("the following error is captured: {error}.")
def step_impl(context, error):
    print(error)
    print(context.error)
    assert context.error == error
