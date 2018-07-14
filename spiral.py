
def spiral(n):
    matrix=[[0 for x in range(n)] for y in range(n)]
    draw_borders(1,(0,0),n,matrix)
    for x in range(n):
        for y in range(n):
            print matrix[x][y],
        print("")

def draw_borders(start,offset,width,matrix):
    print offset
    if width <1: 
        return
    x=offset[0]
    y=offset[1]
    #if width ==1:
     #   matrix[x][y]=start
      #  return
    while(y<offset[1]+width-1):
        matrix[x][y]=start
        start+=1
        y+=1
    while(x<offset[0]+width-1):
        matrix[x][y]=start
        start+=1
        x+=1
    while(y>offset[1]):
        matrix[x][y]=start
        start+=1
        y-=1
    while(x>offset[0]):
        matrix[x][y]=start
        start+=1
        x-=1
    draw_borders(start,(offset[0]+1,offset[1]+1),width-2,matrix)



if __name__ =="__main__":
    spiral(5)
