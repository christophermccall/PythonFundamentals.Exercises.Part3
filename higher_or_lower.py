from random import randrange


def get_input():
	num = input("enter a number: ")
	return int(num)


def rand_num():
	rand = randrange(1, 10)
	return rand	


def high_or_low(user, random):
	print("Goal: "+str(random))
	print("Your number: "+str(user))
	if user > random:
		print("Too high")
	elif user < random:
		print("Too Low")
	elif user == random:
		print("Correct!")


for i in range(10):
	high_or_low(get_input(), rand_num())
