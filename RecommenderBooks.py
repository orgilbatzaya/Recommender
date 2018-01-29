'''
Created on Dec 4, 2017

@author: Orgil Batzaya
ob29
'''
from ProcessAllBooks import processdata
from RecommenderForAll import averages
from RecommenderForAll import similarities
from RecommenderForAll import recommended

if __name__ == '__main__':
    booktitles = "AllBooksAuthors.txt"
    bookratings = "AllBooksRatings.txt"
    bookitems,bookdict = processdata(booktitles,bookratings)
    resultavg = averages(bookitems,bookdict)
    brixSim = similarities("Brix", bookdict)
    brianSim = similarities("Brian", bookdict)
    hideoSim = similarities("Hideo", bookdict)
    print
    print "Top 20 books and their average ratings: \n","-"*35
    for i,x in enumerate(resultavg[:20]):
        print i+1,x
    print
    print "Top 20 Raters similar to Brix \n","-"*30
    for i,j in enumerate(brixSim[:20]):
        print i+1,j
    print
    print "Top 10 Recommendations for Brix with 20 most similar raters \n","-"*40
    brixChoices = recommended(brixSim,bookitems,bookdict,20)
    for i,k in enumerate(brixChoices[:10]):
        print i+1,k
    print 
    print "Top 20 Raters similar to Brian \n","-"*30
    for i,s in enumerate(brianSim[:20]):
        print i+1,s
    print 
    print "Top 10 Recommendations for Brian with 20 most similar raters \n","-"*40
    brianChoices = recommended(brianSim,bookitems,bookdict, 20)
    for i,t in enumerate(brianChoices[:10]):
        print i+1,t
    print
    print "Top 20 Raters similar to Hideo \n","-"*30
    for i,m in enumerate(hideoSim[:20]):
        print i+1,m
    print
    print "Top 10 Recommendations for Hideo with 20 most similar raters \n","-"*40
    hideoChoices = recommended(hideoSim,bookitems,bookdict,20)
    for i,c in enumerate(hideoChoices[:10]):
        print i+1,c