capitals = {} #create an empty dictionary then add values
capitals["name"] = "Bo"
capitals["age"] = 23
capitals["country"] = "USA"
capitals["language"] = "Italian"

def dicts(mon):
    for i in capitals:
        print "MY ", i, "is ", capitals[i]
dicts(capitals)