import math
def prime(n):
  for i in range(n,2,-1):
    prime= True
    for j in range(int(math.sqrt(i)),2,-1):
      if i % j ==0:
        prime=False
        break
    if prime is  True:
      yield i


def factors(x):
  maxfactor =1
  for i in prime(int(math.sqrt(x))+1):
    if x % i ==0:
      x=x/i
      newmax=i
      print("new:"+ str(newmax))
      if newmax  >maxfactor:
        maxfactor=newmax
  return maxfactor 


if __name__ =="__main__":
   print(prime(19).next())
   #print(factors(600851475143))
