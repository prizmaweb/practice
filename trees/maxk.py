class Node:
	def __init__(self,value,left=None,right=None):
		self.value=value
		self.right=right
		self.left=left

def maxk(tree,result,k):
	postorder(tree,result,k)	
def postorder(curr,result,k):
	if curr.right!=None:
		postorder(curr.right,result,k)
	if len(result)==k:
		return
	result.append(curr.value)
	if len(result)==k:
		return
	if curr.left!=None:
		postorder(curr.left,result,k)

if __name__=='__main__':
	root=Node(5)
	root.right=Node(7,Node(6),Node(9,None,Node(10)))
	root.left=Node(3)
	result=[]
	maxk(root,result,4)
	print result		
