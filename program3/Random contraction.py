import random  
import copy  
import time  
  
def contract(ver, e):   
    while len(ver) > 2: #create a new graph every time (not efficient)  
        ind = random.randrange(0, len(e))        
        [u, v] = e.pop(ind)   #pick a edge randomly  
        ver.remove(v)    #remove v from vertices  
        newEdge = list()  
        for i in range(len(e)):  
            if e[i][0] == v: e[i][0] = u    #if e[u, v] one of them is the one removed
            elif e[i][1] == v: e[i][1] = u  
            if e[i][0] != e[i][1]: newEdge.append(e[i])   # remove self-loops, if equal then it's self-loop
        e = newEdge  
    return(len(e))  #return the number of the remained edges, at last it represents the min cut resulting edges num
  
if __name__ == '__main__':   #means call the function by itself HERE not from somewhere else
    f = open('/Users/wengsheng_/Desktop/kargerMinCut.txt')  
    _f = list(f)   
    edges = list()          #initialize vertices and edges  
    vertices = list()  
    for i in range(len(_f)):     #num of edges  
        s = _f[i].split()  #split into each line, The split function splits a single string into a string array using the separator
                                #defined. 
        vertices.append(int(s[0]))  
        for j in range(1, len(s)):  
            if [int(s[j]), int(s[0])] not in edges:  
                edges.append([int(s[0]), int(s[j])])    
  
    result = list()  
    starttime = time.clock()   #running time
    for i in range(2000):  #we take n^2logn times so that the Pr(allfail) <= 1/n where n is the number of vertics
        # need to do it many times to get right min cut since we have random in contract function
        v = copy.deepcopy(vertices)   #notice: deepcopy  
        e = copy.deepcopy(edges)  
        r = contract(v, e)  
        result.append(r)  
    endtime = time.clock()  
    #print(result)  
    print(min(result))  
    print(endtime - starttime)  
