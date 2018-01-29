'''
Created on Dec 3, 2017

@author: Orgil Batzaya
ob29
'''
def processdata(booktitles,bookratings):
    itemlist = []
    f = open(booktitles)
    n = 0 # counter to check if previous number is same as current one on line
    bookinfo = "" #initial string input of itemlist
    for line in f:
        line = line.strip().split('.')
        (num,info) = (line[0],''.join(line[1:]))#info can be either the title or the author
        if num != n: #checking if line is referring to a new book
            n = num #then reassign n and add to bookinfo the title
            bookinfo += info
        else: #if we are still referring to same book
            bookinfo += ","+info #then add the author
            itemlist.append(bookinfo)
            bookinfo = "" #reset bookinfo
    f.close()
    
    raterdict = {}
    f = open(bookratings)
    name = ''
    for line in f:
        line = line.strip().split(':')
        if line[0] == 'RATER': #check is the line has word RATER in it, signifying a line that has a dict key 
            if line[1] not in raterdict:
                raterdict[line[1]] = []
                if name != line[1]:
                    name = line[1] #reassign a place checker name, same technique as before
                for rate in line[2:]: #append each rate in the line with RATER in it 
                    raterdict[line[1]].append(int(rate))        
        else:#lines with no rater on it 
            for rate in line:
                raterdict[name].append(int(rate)) #because name has not been reset, all successive lines refer to same rater
    return itemlist,raterdict
if __name__ == '__main__':
    booktitles = "AllBooksAuthors.txt"
    bookratings = "AllBooksRatings.txt"
    print processdata(booktitles,bookratings)