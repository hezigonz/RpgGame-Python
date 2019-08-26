import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# Player Setup #
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
myPlayer = player()

# Title #
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		start_game() # wip #
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid action.")
		option = input("> ")
		if option.lower() == ("play"):
			start_game() # wip #
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('clear')
	print("############################")
	print("# Welcome to Bocchies RPG! #")
	print("############################")
	print("#	     - Play -   	  #")
	print("#         - Help -         #")
	print("#         - Quit -         #")
	print("# Copyright 2019 Bocchi.me #")
	print("############################")
	title_screen_selections()

def help_menu():
	print("##################################")
	print("# Welcome to Bocchies help menu! #")
	print(" # Use up, down, left, right to #")
	print("  # move the character, u know #")
	print("   # This game is hard. Good- #")
	print("    # luck with killing them #")
	print("     ########################")
	title_screen_selections()
