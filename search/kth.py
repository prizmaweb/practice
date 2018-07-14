import random
def findkitem(arr,k):
    n=len(arr)
    pivot=random.randint(0,n-1)
    print "pivot:{}".format(pivot)
    left=filter(lambda x: x < arr[pivot],arr)
    right=filter(lambda x: x>  arr[pivot],arr)
    if (len(right)==(k-1)):
        return arr[pivot]
    elif len(right) < (k-1):
        return findkitem(left,k-len(right)-1)
    else:
        return findkitem(right,k)

if __name__ =='__main__':
    arr=[1,3,5,7,11,17,19,23] 
    val=findkitem(arr,3)
    print(val)
        
