import math
def factor(n):
    print("find factor for {}".format(n))
    maxfactor=0    
    for i in range (int(math.sqrt(n))+1,1,-1):
        print i
	# if i is a factor
        if n % i == 0:
            print("{}is a factor".format(i))
	    j=factor(n/i)
            if j ==0:
                j=n/i
            if i < j:
	        maxfactor=j
                break

    return maxfactor

if __name__ == "__main__":
    print(factor(30))
