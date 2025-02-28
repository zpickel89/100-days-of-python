scores = [99, 1, 49, 20, 59]

total_score = sum(scores)
print(total_score)
print(max(scores))

highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
print(highest_score)