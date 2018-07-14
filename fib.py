from itertools import *
def fib(n):
   curr=1
   prev=0
   while (curr < n):
    temp=curr 
    curr=curr+prev
    prev=temp
    if curr % 2 == 0:
      yield curr

if __name__ =="__main__":
    print(sum(fib(20)))
