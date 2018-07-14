from itertools import *

def multiples(n):
    a=sum(x for x in range(n) if ((x % 3) ==0 or  (x % 5)==0))
    return a

if __name__ =="__main__":
    print(multiples(1000))



