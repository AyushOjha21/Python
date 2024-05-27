# loops inside loops

rows = int(input("How many rows? "))
column = int(input("How many column? "))
symbol = input("Which symbol you want to choose? : ")

for i in range(0,rows):
	for j in range(0,column):
		print(symbol, end="")
	print()

