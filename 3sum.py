def threesum(array):
    array.sort()
    sumtable={}
    for i in range(len(array)):
        sumtable[array[i]]=i
    print sumtable 
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            total=-1* (array[i]+array[j])
            if total in sumtable:
                yield (a[i],a[j],total)

if __name__ =="__main__":
    a=[1,4,6,-7,9,-10,12,2,11,5,3,-14]
    for v in threesum(a):
        print(v)
