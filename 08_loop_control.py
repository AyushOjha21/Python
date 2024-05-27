#break : it used to terminate loop
while True:
	name = input("Enter your name")
	if name!="":
		break

#continue : skips to the next iteration

phone_number = "123-456-7890"

for i in phone_number:
	if(i=="-"):
		continue
	print(i,end="")

#pass : does nothing and act as a place holder

for i in range(1,21):
	if i ==13:
		pass
	else:
		print(i)