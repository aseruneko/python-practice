# list and tapple
# set
# dictionary

# list

scores = [40,50]
print(scores[0]) # 40
scores[0] = 45
print(len(scores)) # 2
scores.append(100)
print(scores)

for score in scores:
    print(score)

for i, score in enumerate(scores):
    print("{0}: {1}".format(i, score))