one = [1]
two = ['a', 'b', 'c']


print(one)
print(two)

# print(list(one,two))

print(list(zip(one, two)))

# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]
years = [2009, 2010, 2009, 2010, 2011]

# printing players and scores.
for pl, sc, yr in zip(players, scores, years):
    print("Player :  %s     Score : %d   Year:%d" % (pl, sc, yr))
