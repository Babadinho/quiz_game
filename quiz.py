from art import logo, vs
from quiz_data import data
import random

currentData = []
gameEnd = False
points = 0
pointNotice = ""

def initialize():
	for option in data:
		if len(currentData) < 2 and option not in currentData:
			currentData.append(random.sample(data, 1))	
initialize()

while gameEnd == False:
	print(logo)
	print(pointNotice)
	print(f"Compare A: {currentData[-2][0]['name']}, a {currentData[-2][0]['description']}, from {currentData[-2][0]['country']}")
	print(vs)
	print(f"Compare B: {currentData[-1][0]['name']}, a {currentData[-1][0]['description']}, from {currentData[-1][0]['country']}\n")
	
	def myAnswer(answer):
		clear()
		optionA = currentData[-2][0]
		optionB = currentData[-1][0]
		global points
		global gameEnd
		global pointNotice

		if len(currentData) == len(data):
			print(logo)
			print(f"Game over! You completed the game with Total points: {points} \n")
			gameEnd = True

		if answer == "A" and optionA['follower_count'] < optionB['follower_count'] or answer == "B" and optionB['follower_count'] < optionA['follower_count']:
			print(logo)
			print(f"You lost! Total points: {points}")
			gameEnd = True
		elif answer == "A" and optionA['follower_count'] > optionB['follower_count']:
			points += 1
			pointNotice = f"Correct! You gained 1 Point. Total points: {points}\n\n"
			currentData.insert(-2, currentData.pop(-1))
			for i in currentData:
				newData = random.sample(data, 1)
				if newData not in currentData:
					return currentData.append(newData)
		elif answer == "B" and optionB['follower_count'] > optionA['follower_count']:
			points += 1
			pointNotice = f"Correct! You gained 1 Point. Total points: {points}\n\n"
			currentData.insert(-1, currentData.pop(-2))
			for i in currentData:
				newData = random.sample(data, 1)
				if newData not in currentData:
					return currentData.append(newData)
		else: 
			pointNotice = "Invalid input! Try again. \n"			

	myAnswer(input("Who has more followers? Type 'A' or 'B': "))