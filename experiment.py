# Student number: 17200844
# Name: Jeet Banerjee
import connect_four

numberOfIterations = [80,150,500,2000]

# CASE 1
connect_four.BOARDWIDTH = 6
connect_four.ARRAYOFCOLUMNS = [6,5,4,6,5,3]
connect_four.BOARDHEIGHT = max(connect_four.ARRAYOFCOLUMNS)
connect_four.DONTCARE = [[2,2],[4,3]]
arrayOfWins = []
for i in range(len(numberOfIterations)):
	connect_four.PLAYER1ITERATIONS = numberOfIterations[i]
	for j in range(len(numberOfIterations)):
		connect_four.PLAYER2ITERATIONS = numberOfIterations[j]
		for k in range(10):
			connect_four.main()
		arrayOfWins.append([connect_four.PLAYER1WINS, connect_four.PLAYER2WINS, connect_four.NUMBEROFDRAWS])
		connect_four.PLAYER1WINS = 0;connect_four.PLAYER2WINS = 0; connect_four.NUMBEROFDRAWS = 0 
print("Resultant array with all the wins is : {}".format(arrayOfWins))


# CASE 2
connect_four.BOARDWIDTH = 8
connect_four.ARRAYOFCOLUMNS = [6,5,6,4,5,4,6,5]
connect_four.BOARDHEIGHT = max(connect_four.ARRAYOFCOLUMNS)
connect_four.DONTCARE = [[4,4],[6,5]]
arrayOfWins = []
for i in range(len(numberOfIterations)):
	connect_four.PLAYER1ITERATIONS = numberOfIterations[i]
	for j in range(len(numberOfIterations)):
		connect_four.PLAYER2ITERATIONS = numberOfIterations[j]
		for k in range(10):
			connect_four.main()
		arrayOfWins.append([connect_four.PLAYER1WINS, connect_four.PLAYER2WINS, connect_four.NUMBEROFDRAWS])
		connect_four.PLAYER1WINS = 0;connect_four.PLAYER2WINS = 0; connect_four.NUMBEROFDRAWS = 0 
print("Resultant array with all the wins is : {}".format(arrayOfWins))


# CASE 3
connect_four.BOARDWIDTH = 9
connect_four.ARRAYOFCOLUMNS = [6,5,4,5,3,6,6,5,6]
connect_four.BOARDHEIGHT = max(connect_four.ARRAYOFCOLUMNS)
connect_four.DONTCARE = [[5,5],[7,3]]
arrayOfWins = []
for i in range(len(numberOfIterations)):
	connect_four.PLAYER1ITERATIONS = numberOfIterations[i]
	for j in range(len(numberOfIterations)):
		connect_four.PLAYER2ITERATIONS = numberOfIterations[j]
		for k in range(10):
			connect_four.main()
		arrayOfWins.append([connect_four.PLAYER1WINS, connect_four.PLAYER2WINS, connect_four.NUMBEROFDRAWS])
		connect_four.PLAYER1WINS = 0;connect_four.PLAYER2WINS = 0; connect_four.NUMBEROFDRAWS = 0 
print("Resultant array with all the wins is : {}".format(arrayOfWins))


# CASE 4
connect_four.BOARDWIDTH = 11
connect_four.ARRAYOFCOLUMNS = [6,5,4,5,3,6,6,5,6,5,6]
connect_four.BOARDHEIGHT = max(connect_four.ARRAYOFCOLUMNS)
connect_four.DONTCARE = [[5,4],[11,2]]
arrayOfWins = []
for i in range(len(numberOfIterations)):
	connect_four.PLAYER1ITERATIONS = numberOfIterations[i]
	for j in range(len(numberOfIterations)):
		connect_four.PLAYER2ITERATIONS = numberOfIterations[j]
		for k in range(10):
			connect_four.main()
		arrayOfWins.append([connect_four.PLAYER1WINS, connect_four.PLAYER2WINS, connect_four.NUMBEROFDRAWS])
		connect_four.PLAYER1WINS = 0;connect_four.PLAYER2WINS = 0; connect_four.NUMBEROFDRAWS = 0 
print("Resultant array with all the wins is : {}".format(arrayOfWins))

