'''
Created on Dec 3, 2017

@author: Orgil Batzaya
ob29
'''
from ProcessAllFood import processdata
from RecommenderForAll import averages
from RecommenderForAll import similarities
from RecommenderForAll import recommended



if __name__ == '__main__':
    foodfile = "AllFoodRatings.txt"
    fooditems, fooddict = processdata(foodfile)
    resultavg = averages(fooditems,fooddict)
    sungSim = similarities("Sung-Hoon", fooddict)
    sarahSim = similarities("Sarah Lee", fooddict)
    melanieSim = similarities("Melanie", fooddict)
    print "RESTAURANTS"
    for i in fooditems:
        print i 
    print
    print "Restaurants and their average ratings: \n","-"*35
    for i in resultavg:
        print i
    print
    print "Raters similar to Sung-Hoon \n","-"*30
    for i in sungSim:
        print i
    print
    print "Recommendations for Sung-Hoon with 3 most similar raters \n","-"*40
    sungChoices = recommended(sungSim,fooditems,fooddict,3)
    for i in sungChoices:
        print i
    print 
    print "Raters similar to Sarah Lee \n","-"*30
    for i in sarahSim:
        print i
    print 
    print "Recommendations for Sarah Lee with 3 most similar raters \n","-"*40
    sarahChoices = recommended(sarahSim,fooditems,fooddict, 3)
    for i in sarahChoices:
        print i
    print
    print "Raters similar to Melanie \n","-"*30
    for i in melanieSim:
        print i
    print
    print "Recommendations for Melanie with 3 most similar raters \n","-"*40
    melanieChoices = recommended(melanieSim,fooditems,fooddict,3)
    for i in melanieChoices:
        print i
    