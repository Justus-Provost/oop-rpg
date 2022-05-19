# main.py
# the main game might go here
# for now, let's just test some stuff

# import out objects
import character

# test our code
if __name__ == '__main__':
	# create a Character
	player1 = character.Player("Benaconda", 300)

	# print a Character
	print(player1.name)
	print(player1.get_stats())