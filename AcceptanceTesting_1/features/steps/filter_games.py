from behave import *
from src.Game import *
from src.Catalogue import *
import ast

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("a set of games")
def step_impl(context):
	game_list = []

	for row in context.table:
		game = Game(row['NAME'], row['RELEASE DATE'], row['DEVELOPER'], row['RATE'])
		game_list.append(game)

	context.games = game_list

@given('the user enters the name: {name}')
def step_impl(context, name):
	context.name = name

@given("the user chooses ratings {list_ratings}")
def step_impl(context, list_ratings):
    context.ratings = ast.literal_eval(list_ratings)

@when("the user search games by {criteria}")
def step_impl(context, criteria):
	if(criteria == 'name'):
		result, message = get_game_name(context.games, context.name)
	elif(criteria == 'ratings'):
		result, message, error = get_game_rating(context.games, context.ratings)
		if(error == None):
			context.error = 'None'
		else:
			context.error = error
	context.result = result
	context.message = message

@then("{total} games will match")
def step_impl(context, total):
	assert len(context.result) == int(total)


@then("the names of these games are")
def step_impl(context):
	expected_games = True
	result_games = []
	for row in context.table:
		result_games.append(row['NAME'])
	for game in context.result:
		if game.name not in result_games:
			print("No game " + game.name)
			expected_games = False
	assert expected_games is True

@then("the following message is displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message


@then("the following error is captured: {error}.")
def step_impl(context, error):
    print(error)
    print(context.error)
    assert context.error == error
