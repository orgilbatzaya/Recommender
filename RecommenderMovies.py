'''
Created on Dec 4, 2017

@author: Orgil Batzaya
ob29
'''
from ProcessAllMovies import processdata
from RecommenderForAll import averages
from RecommenderForAll import similarities
from RecommenderForAll import recommended

if __name__ == '__main__':
    movietitles = "AllMoviesRatings.txt"
    movieitems,moviedict = processdata(movietitles)
    resultavg = averages(movieitems,moviedict)
    student1367Sim = similarities("student1367", moviedict)
    student1008Sim = similarities("student1008", moviedict)
    student1256Sim = similarities("student1256", moviedict)
    print
    print "Top 30 movies and their average ratings: \n","-"*35
    for i,x in enumerate(resultavg[:30]):
        print i+1,x
    print
    print "Top 30 Raters similar to student1367 \n","-"*30
    for i,x in enumerate(student1367Sim[:30]):
        print i+1,x
    print
    print "Top 20 Recommendations for student1367 with 50 most similar raters \n","-"*40
    student1367Choices = recommended(student1367Sim,movieitems,moviedict,50)
    for i,x in enumerate(student1367Choices[:30]):
        print i+1,x
    print 
    print "Top 30 Raters similar to student1008 \n","-"*30
    for i,x in enumerate(student1008Sim[:30]):
        print i+1,x
    print 
    print "Top 20 Recommendations for student1008 with 50 most similar raters \n","-"*40
    student1008Choices = recommended(student1008Sim,movieitems,moviedict, 50)
    for i,x in enumerate(student1008Choices[:30]):
        print i+1,x
    print
    print "Top 30 Raters similar to student1256 \n","-"*30
    for i,x in enumerate(student1256Sim[:30]):
        print i+1,x
    print
    print "Top 20 Recommendations for student1256 with 50 most similar raters \n","-"*40
    student1256Choices = recommended(student1256Sim,movieitems,moviedict,50)
    for i,x in enumerate(student1256Choices[:20]):
        print i+1,x