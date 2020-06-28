import random
print("Welcome to the randomizer v0.4\n")
i = 1
while i == 1:
	items = input("\n\nEnter the things that you want to mix, separated with spaces: ").split()
	lag=int(input("How many groups? "))
	n = len(items)
	print(f"Mixing {n} things into {lag} groups.")
	used = []
	j = 1
	b = 0
	if lag >= 1:
		print("Team 1:\n")
		b = 1
	while j < n + 1:
		y = random.randint(1, n)
		if str(y) not in used:
			used.insert(j-1, str(y))
			print(items[y-1], "\n")
			j = j + 1
			if j % (round(n/lag)) == 1 and lag > 1 and b < lag:
				b += 1
				print("\n\nTeam", f"{b}:", "\n")
	redo = input("Mix again? (Y/N) ")
	while redo == "Y":
		used = []
		j = 1
		if lag >= 1:
			print("Team 1:\n")
			b = 1
		while j < n + 1:
			y = random.randint(1, n)
			if str(y) not in used:
				used.insert(j-1, str(y))
				print(items[y-1], "\n")
				j = j + 1
				if j % (round(n/lag)) == 1 and lag > 1 and b < lag:
					b += 1
					print("\n\nTeam", f"{b}:", "\n")
		redo = input("Mix again? (Y/N) ")
