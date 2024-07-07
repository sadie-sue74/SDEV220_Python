#Carly Grubbs, July 7th
# M03 Programming Assignment - Lists and Functions

# 7.4
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# 7.5
things[1] = "Cinderella"
print(things)

# 7.6
things[0] = things[0].upper()
print(things)

# 7.7
del things[-1]
print(things)

# 9.1
def good():
    return ["Harry", "Ron", "Hermione"]
print(good())

# 9.2
def get_odds():
    for x in range(1, 10, 2):
        yield x

count = 1
for x in get_odds():
    if count == 3:
        print("The third number is: ", x)
        break
    count += 1