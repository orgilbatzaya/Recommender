'''
Created on Dec 2, 2017

@author: Orgil Batzaya
ob29
'''

def processdata(filename):
    itemlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        if line.count('(')>0:
            rest = line.split(')(')[0][1:]
            itemlist.append(rest)
    itemlist = list(set(itemlist))
    f.close()
    
    dictratings = {}
    f = open(filename)
    for x in f: #x refers to each line in f
        x = x.strip()
        if x.count('(') == 0: #the lines with no parentheses, i.e, names
            if x not in dictratings: #creating dictionary
                name = x
                dictratings[name] = [] #empty list
            
        else: # lines with ratings on them
            rest = x.split(')(')[0][1:]
            rate = int(x.split(')(')[1][:-1])
            dictratings[name].extend([rest,rate]) #I add restaurant followed by rating and so on and so forth
    
    for i in dictratings:
        items = itemlist[:] #I make a copy of itemlist that I can alter by putting in scores for each restaurant
        for (j,k) in enumerate(itemlist):
            if k in dictratings[i]: #if a restaurant is in the value,
                pos = dictratings[i].index(k) #find its index in the list
                score = dictratings[i][pos+1] #add one because each rate follows its corresponding restaurant
                items[j] = score #I switch out the restaurant for its score in items
            else:
                items[j] = 0
        dictratings[i] = items #I assign each key its list of ratings based on itemlist
           
            
           
    return itemlist,dictratings
if __name__ == '__main__':
    print processdata('AllFoodRatings.txt')
    