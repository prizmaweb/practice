
def permutation(string):
    l=len(string)
    result=[]
    #initialize to default
    x=[-1]*l
    level=0
    while(level>=0):    
        getNext(string,level,x)
        if x[level]==-1:
            level-=1
        elif level ==(l-1):
            output=""
            for j in range(l):
                output+=string[x[j]]
            print output
            result.append(output)
        else:
            level+=1
    return result
        
def getNext(string,level,x):
    x[level]=x[level]+1
    while x[level] <len(string):
        if bound(x,level) ==True:
            return
        x[level]=x[level]+1
    #no valid value found
    x[level]=-1

def bound(x,level):
    for i in range(level):
        if x[i]==x[level]:
            return False
    return True
             
if __name__=="__main__":
    print(permutation("abc"))

