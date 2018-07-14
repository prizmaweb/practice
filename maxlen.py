def maxlen(arr):
    l=len(arr)
    max_len=[1]*l
    for i in range(1,l):
        for j in range(0,i):
            if arr[j] < arr[i] :
                max_len[i]=max(max_len[i],max_len[j]+1)
    return max(max_len)

if __name__ =="__main__":
    #arr=[0,8,4,12,2,10,6,14,1,9]
    arr=[50, 3, 10, 7, 40, 80]    
    print(maxlen(arr))


