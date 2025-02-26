import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_choice = random.randint(0, len(friends) - 1)
print(f"{friends[rand_choice]} pays the bill this time!")


# OR

print(f"{random.choice(friends)} pays the bill this time!")