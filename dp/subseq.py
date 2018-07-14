def max_seq(list1,list2):
    solutions=[0]*(len(list1)+1)
    for i in range(len(list1)+1): 
        solutions[i]=[0]*(len(list2)+1)
    for i in range(len(list1)): 
        for j  in range(len(list2)): 
            if i==0 and j==0:
                if list1[i]==list2[j]:       
                    solutions[i+1][j+1]=1
                else:
                    solutions[i+1][j+1]=0
            else:
                if list1[i]==list2[j]:       
                     solutions[i+1][j+1]=solutions[i][j]+1
                else:
                    solutions[i+1][j+1]=max(solutions[i+1][j],solutions[i][j+1])
    for i in range(len(list1)+1): 
        for j  in range(len(list2)+1): 
            print solutions[i][j],
        print ""
    return solutions[len(list1)][len(list2)]   
if __name__=="__main__":
    a=raw_input("E NTER first sequence:")
    b=raw_input("second sequence:")
    list1=a.split()
    list2=b.split()
    result=max_seq(list1,list2)
    print result
