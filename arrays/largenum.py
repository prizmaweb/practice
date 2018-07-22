def largenum(a,b):
	temp={}
	result={}
	prefix=""
	arr1=a.split(".")
    	arr2=b.split(".")
	result=add_integers(arr1[1],arr2[1],1)
	temp=add_integers(arr1[0],result['carry'],0)
	if temp['carry'] =="1":
		prefix="1"+temp['sum']
	else:
		prefix=temp['sum']
	temp=add_integers(arr2[0],prefix,0)
	prefix=temp['sum']+"."+result['sum']
	if temp['carry'] =="1":
		prefix="1"+prefix
	return prefix

	
def add_integers(str1,str2,direction):
	a=len(str1)-len(str2)
        if a >0:
		if direction ==1:
			str2=str2.ljust(len(str1),'0')
		else:
			str2=str2.zfill(len(str1))
	else:
		if direction ==1:
			str1=str1.ljust(len(str2),'0')
		else:
			str1=str1.zfill(len(str2))
	carry=0
	result=[]
	for x,y in zip(reversed(str1),reversed(str2)):
		total=int(x)+int(y)+carry
		if total> 9 :
			total%=10
			carry=1
		else:
			carry=0
		result.append(str(total))
	tmp={}
	tmp['sum']="".join(reversed(result))
	tmp['carry']=str(carry)
	print tmp
	return tmp

if __name__=="__main__":
	out=largenum("11111.91","99999988.1")
	#out=largenum("11.91","8.1")
	print out


