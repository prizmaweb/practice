
def med(ar):
    arr.sort()
    current=None
    median=arr[0]
    maxfrequency=0
    frequency=0
    i=0
    while  i <  len(arr)-1:
        print "read value is {}".format(arr[i])
        if arr[i]==current:
            frequency+=1
            print "inc"
        else:
            if frequency> maxfrequency:
		maxfrequency=frequency
                frequency=1
                median=current
            current=arr[i]
            print frequency
        i+=1 
        print "median is {}".format(median)
    return median

if __name__=="__main__":
    arr=[1,2,10,8,6,7,5,6,33,11,11,13,4,11]
    r=med(arr)
    print r

        
