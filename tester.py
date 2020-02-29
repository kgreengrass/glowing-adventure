word = ["A", "B", "B", "A"]
guess = "A"
indices = [i for i, x in enumerate(word) if x == guess]
print(indices)