states = ["Illinois", "Missouri"]

print(states[0])
print(states[-1])
states[1] = "Ohio"
print(states)

states.append("Florida")
print(states)

states.extend(["Michigan", "Delaware", "Maine"])
print(states)

fruits = ["Strawberries", "Nectarines", "Apples"]
vegitables = ["Potatoes", "Tomatoes", "Carrots"]
foods = [fruits, vegitables]
print(foods)
print(foods[1][1])