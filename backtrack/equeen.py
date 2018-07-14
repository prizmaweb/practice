
def eightqueens():
    # X stores all possible solutions
    x=[-1]*8 
    level=0
    while level >=0:
	getNext(level,x)
	if x[level] == -1:
	    #backtrack
	    level -=1
	elif level == (len(x)-1):
	    #print solution
	    return x
	else:
            level+=1


def getNext(level,x):
    x[level]+=1
    while x[level] <64:
    	if bound(x,level) == True:
            return
    	else:
    	    x[level]+=1
    x[level]=-1

def bound(x,level):
    curr_col=x[level]%8
    curr_row=x[level]/8
    if level == 0:
        return True

    # for the queens placed so far
    for index in range(level):
        #if there is a queen at this position
        if x[index]> -1:
	    row=x[index]/8
            col=x[index]%8
            # same row or column
            if row==curr_row or col== curr_col:
		return False
	    # diagonal case 1
            if row+col== curr_row+curr_col:
		return False
            
	    # diagonal case 2
            if col-row== (curr_col-curr_row):
		return False
    
    return True


if __name__ == "__main__":
  solution=eightqueens()
  print solution

