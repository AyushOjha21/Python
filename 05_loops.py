import time
 #while loop
name = ""

while len(name) == 0:
	name = input("Enter your name")

print("Hello " + name)

#for loop

for i in range(10):
	print(i)

for i in range(0,21,2):
	print(i)

for sec in range(10,0,-1):
	print(sec)
	time.sleep(1)
print("Happy birthday")
