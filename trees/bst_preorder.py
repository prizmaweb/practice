class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None
    def __str__(self):
        leftstr,rightstr="",""
        if self.left != None:
            leftstr="left:{}".format(self.left.__str__())
        if self.right !=None:
            rightstr="right:{}".format(self.right.__str__())
        return "{},root:{},{}".format(leftstr,self.value,rightstr)            

def  rebuildBST(nodes):
    return rebuild(nodes)

def rebuild(nodes):
    root=Node(nodes[0])
    if( len(nodes)==1):
        return root
    
    left=filter(lambda x: x<nodes[0],nodes)
    if( len(left)>0):
        left_tree=rebuild(left)
        root.left=left_tree
    right=filter(lambda x: x>nodes[0],nodes)
    if( len(right)>0):
        right_tree=rebuild(right)
        root.right=right_tree
    return root


if __name__== '__main__':
    mylist=[43,23,37,29,31,41,47,53]
    root=rebuildBST(mylist)
    print(str(root))
     
