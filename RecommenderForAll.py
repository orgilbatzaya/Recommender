'''
Created on Dec 3, 2017

@author: Orgil Batzaya
ob29
'''


def averages(itemlist,dictratings):
    '''averages returns an ordered list of tuples (item,avg rating) from itemlist, a list of consumables(book,food,movie)
    and from dictratings, a dictionary with users as keys and a list of their int ratings on itemlist'''
    ans = []
    for i,x in enumerate(itemlist):
        inner = [] #I use an inner list to compute the sum at each index of itemlist 
        for k in dictratings.values():
            if k[i] != 0:#if the rating at the i-th index of the k-th rater is nonzero then add to inner
                #because we don't want to count rates which mean 'not rated'
                inner.append(k[i])
        if len(inner)>0:# make sure number of raters is more than zero before dividing
            avg = 1.0*sum(inner)/len(inner)
            ans.append((avg,x))
        else:
            ans.append((0,x)) #if no one rated the item, it is by default a rating of 0
    order = sorted(ans,reverse=True) #sort by highest rating first
    return [(a,b) for (b,a) in order] #reswap restaurant and rating for correct format

def similarities(name,dictratings):
    '''similarities returns an ordered list of tuples (person,similarity index) based on str parameter name
    and dictratings. The list of tuples is the other users with similar ratings'''
    start = dictratings[name] #list of name's ratings 
    sims = [] 
    for i in dictratings.keys(): #i is other users
        ind = sum([start[x]*dictratings[i][x] for x in range(len(start))])#compute a dot-product, multiplying at each index the two lists
        sims.append((ind,i))
    sims = [(a,b) for (b,a) in sorted(sims,reverse=True)]#first sort list of tuples by descending similarity index and then swap for correct format
    sims = [x for x in sims if name not in x]#eliminate the tuple with name in it because we don't want one's own similarity
    return sims

def recommended(simlist,itemlist,dictratings,n):
    '''recommended returns a list of tuples (item,sim index) where item is obtained the elements
     from itemlist that is based on n users most similar and shows recommended items that similr users
     liked'''
    if n <= len(simlist): #make sure n is less than length of itemlist or it doesn't make sense
        weights = [] 
        for i in range(n): #iterate only through n, which is how far we look into simlist from similarities
            (name,sim) = simlist[i]
            weight = [sim*dictratings[name][x] for x in range(len(itemlist))]#scale each entry of list of ratings for each user in simlist by sim index
            weights.append(weight)#do this for each tuple in simlist up to n times
            #weights is now a list of lists of scaled ratings for the users in simlist
        
        total = []#I know compute the weighted values
        for k in range(len(itemlist)): #iterate through length of itemlist
            subtotal = [] #each index has a subtotal I want to compute
            for j in range(len(weights)): #for  each index of itemlist I iterate through weighted lists
                if weights[j][k] != 0:
                    subtotal.append(weights[j][k])# I only count nonzero rates because 0 is no rate
            if len(subtotal) == 0:
                total.append(0)#if no one rated at this particular index then total is appended a 0 at this k-th index
            else:
                total.append(1.0*sum(subtotal)/len(subtotal)) #average at each index
        
        ans = []
        for t in range(len(total)):
            ans.append((total[t],itemlist[t])) #make tuples, each index of total lines up with each index of itemlist
        ans = [(a,b) for (b,a) in sorted(ans,reverse=True)] #order them
        return ans
            
            
        
        
        
    
    
    
    
if __name__ == '__main__':
    print averages(['IlForno', 'TheCommons', 'FarmStead', 'DivinityCafe', 'PandaExpress', 'TheSkillet', 'Tandoor', 'LoopPizzaGrill', 'McDonalds'],{'Sung-Hoon': [-1, 1, -1, 0, 3, -3, -3, 5, 1], 'Wei': [0, 3, 1, 1, 0, 0, 5, 3, -1], 'Sly one': [1, 3, 0, 5, 0, 3, 3, 3, 0], 'Nana Grace': [3, 3, 0, 5, 0, 0, 1, -5, -1], 'Melanie': [3, 3, 0, 5, 3, 1, 3, 0, 1], 'J J': [0, 0, 1, 0, 1, 1, 3, -1, 1], 'Harry': [0, 5, 3, 5, -5, 1, 0, -1, -3], 'Sarah Lee': [3, 0, 3, 3, -3, -3, 5, 3, 0]
                                                                                                                         })