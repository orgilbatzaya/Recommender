'''
Created on Dec 4, 2017

@author: Orgil Batzaya
ob29
'''
def processdata(filename):
    temp = []#temp is just a list of each line 
    f = open(filename)
    for line in f:
        line = line.strip()
        temp.append(line)
    f.close()
    
    itemlist = []
    i = 0
    while i<len(temp):
        if i%3 == 1: #I append the items in the list that are remainder 1 because those are the movies
            itemlist.append(temp[i])
        i += 1
    itemlist = list(set(itemlist))#make sure to set since it is alot of repeated titles

    ratingsdict = {}
    for x in range(len(temp)):
        if x % 3 == 0:#indices in temp divisble by 3 are the raters names 
            if temp[x] not in ratingsdict:
                ratingsdict[temp[x]] = []#empty list
            
            ratingsdict[temp[x]].extend([temp[x+1],int(temp[x+2])])#extend list to movie,rate,movie,rate,and so on for each rater
    
    for k in ratingsdict:#I iterate through ratingsdict
        items = itemlist[:]#make a copy of itemlist that I can alter
        for i,mov in enumerate(itemlist):
            if mov in ratingsdict[k]:
                pos = ratingsdict[k].index(mov) #find its index in the list
                score = ratingsdict[k][pos+1] #add one because each rate follows its corresponding movie
                items[i] = score #I switch out the movie for its score in items
            else:
                items[i] = 0
        ratingsdict[k] = items #I assign each key its list of ratings based on itemlist
           
    
    return itemlist,ratingsdict
    
if __name__ == '__main__':
    print processdata('AllMoviesRatings.txt')