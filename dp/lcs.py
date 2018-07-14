def max_seq(S,T):
    solution=[ [0 for i in range(len(T))] for j in range(len(S))  ]
    return lcs(S,T,len(S)-1,len(T)-1,solution)

def lcs(S,T,i,j,solution):
    print i
    print j
    if i==-1 and j==-1 :
        return 0 
    if solution[i][j] > -1: 
        return solution[i][j]  
    if S[i]==T[j]:
        if i ==0 and j ==0:
            solution[i][j]=1
        else:
            solution[i][j]= lcs(S,T,i-1,j-1)+1
    else:
        if i ==0 and j ==0:
            solution[i][j]=0
        else:
            solution[i][j]= max(lcs(S,T,i-1,j),lcs(S,T,i,j-1))
    return solution[i][j]  

          
if __name__=="__main__":
    a=raw_input("E NTER first sequence:")
    b=raw_input("second sequence:")
    list1=a.split()
    list2=b.split()
    result=max_seq(list1,list2)
    print result
                     

