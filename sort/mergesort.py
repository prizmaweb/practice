def merge(left,right,x):
 i,j,k=0,0,0
 while i< len(left) and j<len(right):
   if left[i] < right[j]:
     x[k]=left[i]
     i +=1
   else:
     x[k]=right[j]
     j+=1
   k+=1
 if k< (len(left)+len(right)) :
   if i<len(left):
     x[k]= left[i]
     i+=1
   if j< len(right):
     x[k]=right[j]
     j+=1
   k+=1
   
def mergesort(x):
 if len(x) == 1:
   return 
 l=len(x)/2
 left = x[:l]
 right= x[l:]
 print("left"+str(left))
 print("right"+str(right))

 mergesort(left)
 mergesort(right)
 merge(left,right,x)
 print(x)

if __name__ =="__main__":
  x=[5,4,3,2,10,-2]
  mergesort(x)
