import random
z=0
y=random.randint(1,10)
while z != 1:
	x=int(input('Gissa nummret!'))
	if x > y :
		print('För högt')
	elif x < y:
		print('För lågt')
	else:
		print('Du vinner!')
		z=1