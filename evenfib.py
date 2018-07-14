from itertools import *

def fib(n):
    i=0
    prev=0
    curr=1
    while( i<n):
        i+=1
        nextval=curr+prev
        yield nextval
        prev=curr
        curr=nextval


def evenfib(n):
    return sum(x for x in fib(n) if (x % 2 ) ==0 )

if __name__ =="__main__":
    print(evenfib(10))



