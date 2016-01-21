##Daniel Lee
##CSCI 1101 section 1

from Myro import*

def menu():
    answer = askQuestion("choose 1", ["Create actor-title dictionary","Create title-actor dictionary","Enter 2 movie titles and find ALL the actors in those movies","Enter 2 movie titles and find the common actors in the 2 movies","Enter 2 movie titles and find the actors who are in either of the movies but not both","Enter an actor's name, find all the actors with whom he/she has acted. i.e. find all the co-actors of the given actor", "Nothing, I wish to quit"])
    if (answer == "Create actor-title dictionary"):
        answer = 1
    elif (answer == "Create title-actor dictionary"):
        answer = 2
    elif (answer == "Enter 2 movie titles and find ALL the actors in those movies"):
        answer = 3
    elif (answer == "Enter 2 movie titles and find the common actors in the 2 movies"):
        answer = 4
    elif (answer == "Enter 2 movie titles and find the actors who are in either of the movies but not both"):
        answer = 5
    elif (answer == "Enter an actor's name, find all the actors with whom he/she has acted. i.e. find all the co-actors of the given actor"):
        answer = 6
    elif (answer == "Nothing, I wish to quit"):
        answer = 7
    return answer
    
def actorTitle():

    infile = open('movies.txt', 'r')
    dictionary = {}
    for line in infile:
        ##print(line)
        line = line.rstrip('\r\n')
        actorsMovie = line.split(',')
        dictionary[actorsMovie[0]] = actorsMovie[1:]
        actorsMovie = []
    
    infile.close()

    return dictionary

def titleActor(actorDict):
    dictionary = {}
    movieList = list(actorDict.values())
    ##print(movieList)
    movies = []
    for key in movieList:
        for film in key:
            if film in movies:
                continue
            else:
                movies.append(film)
                
    for movie in movies:
        dictionary[movie] = []
    
    for movieFilm in movies:
        for key in actorDict:
            if movieFilm in actorDict[key]:
                dictionary[movieFilm] += [key]

    return dictionary

def findActors(movie1,movie2,dictionary):
    ##note: the input are very case sensitive
    ##please type in the movie exactly as its written
    
    actors = []
    if movie1 and movie2 in dictionary:
        actors += dictionary[movie1] + dictionary[movie2]
    else:    
        return 'Error! One or both of the movies were not found (input is case sensitive)'
    ##print(actors)
    
    myList = list(set(actors))
    
    return myList

def commonActors(movie1,movie2,dictionary):
    ##note: the input are very case sensitive
    ##please type in the movie exactly as its written
    
    actors = []
    if movie1 and movie2 in dictionary:
        ##print(actors)
        actors += dictionary[movie1] + dictionary[movie2]
    else:
        return 'Error! One or both of the movies were not found (input is case sensitive)'
    ##print(actors)
    aList = list(set(actors))
    ##print(aList)
    myList = []
    for actor in aList:
        if (actor in dictionary[movie1]) and (actor in dictionary[movie2]):
            myList.append(actor)
    if myList == []:
        return 'No common actors.'
    
    return list(set(myList))

def eitherActors(movie1,movie2,dictionary):   
    ##note: the input are very case sensitive
    ##please type in the movie exactly as its written
    
    actors = []
    if movie1 and movie2 in dictionary:
        ##print(actors)
        actors += dictionary[movie1] + dictionary[movie2]
    else:
        return 'Error! One or both of the movies were not found (input is case sensitive)'
    ##print(actors)
    aList = list(set(actors))
    ##print(aList)
    myList = []
    print(myList)
    for actor in aList:
        if (actor in dictionary[movie1]) and (actor not in dictionary[movie2]):
            myList.append(actor)
        if (actor in dictionary[movie2]) and (actor not in dictionary[movie1]):
            myList.append(actor)
    
    return list(set(myList))
    
def coActors(actor,dictionary):
    ##note: the input are very case sensitive
    ##please type in the movie exactly as its written
    
    if actor not in dictionary:
        return 'Error! Actor was not found (input is case sensitive)'
    movies = list(dictionary[actor])
    ##print(movies)
    ##print(dictionary)
    actors = []
        
    myList = list(set(movies))
    ##print(myList)
    
    for movie in movies:
        for coactors in dictionary:
            if (movie in dictionary[coactors]) and (coactors != actor):
                actors.append(coactors)
    
    return list(set(actors))
        
def main():
    ##note: the input are very case sensitive
    ##please type in the movie exactly as its written
    ##or else None will be returned
    choice = menu()
    while choice != 7:
        if choice == 1:
            title = actorTitle()
            print(title)
        elif choice == 2:
            dictionary = actorTitle()
            print(titleActor(dictionary))
        elif choice == 3:
            movie1 = input("Type a movie here")
            movie2 = input("Type another movie here")
            dictionary = titleActor(actorTitle())
            print(findActors(movie1,movie2,dictionary))
        elif choice == 4:
            movie1 = input("Type a movie here")
            movie2 = input("Type another movie here")
            dictionary = titleActor(actorTitle())
            print(commonActors(movie1,movie2,dictionary))
        elif choice == 5:
            movie1 = input("Type a movie here")
            movie2 = input("Type another movie here")
            dictionary = titleActor(actorTitle())
            print(eitherActors(movie1,movie2,dictionary))
        elif choice == 6:
            actor = input("Type an actors name here")
            dictionary = actorTitle()
            print(coActors(actor,dictionary))
        choice = menu()