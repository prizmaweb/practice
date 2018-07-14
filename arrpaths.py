def no_of_paths(rows,cols):
    solution=[[-1 for y in range(cols)] for x in range(rows)]
    return paths(solution,rows-1,cols-1)

def paths(solution,x,y):
    # if dest =(0,0): paths is 1.
    if x==0 and y==0:
        return 1   
    #if dest is (m,n): paths=  path(arr,m-1,n)+path(arr,m,n-1)
    if solution[x][y] >-1 :
        return solution[x][y]
    else:
        result=0
        if x > 0: result=paths(solution,x-1,y)
        if y > 0: result +=paths(solution,x,y-1)
        solution[x][y]=result
        return result

if __name__ =="__main__":
    rows=5
    cols=5
    print(str(no_of_paths(rows,cols)))
