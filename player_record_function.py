# Soccer Player Function

def record(player = '<unknown>', goals = 0):
	"""
	Displays a soccer player's profile. :param player: The player's name. :param goals: The total number of goals.
	"""
	print(f'The player {player} scored {goals} goals')
	
n = str(input('Player Name:'))
g = input('Goals Scored:')
if g.isnumeric():
	g = int(g)
else:
	g = 0
if n.strip() == '':
	record(goals = g)
else:
	record(n, g)
	
help(record)



