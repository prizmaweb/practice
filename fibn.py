
def fib(n):
    index=n-1
    if index==0:
        return 1
    elif index==1:
        return 1
    else:
        if index in  sol:
             print "using cache for {}".format(index)
             return sol[index]
        else:
            result= fib(n-1)+fib(n-2)
            sol[index]=result
        return result

if __name__=="__main__":
    sol={}
    for i in range(1,10):
        print "{} fib is {}".format(i,fib(i))
        print sol
