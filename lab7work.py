class BTNode:
    def __init__(self,d,l,r):
        self.data = d
        self.left = l
        self.right = r
          
    def updateChild(self, oldChild, newChild):
        if self.left == oldChild:
            self.left = newChild
        elif self.right == oldChild:
            self.right = newChild
        else: raise Exception("updateChild error")

    # prints the node and all its children in a string
    def __str__(self):  
        st = str(self.data)+" -> ["
        if self.left != None:
            st += str(self.left)
        else: st += "None"
        if self.right != None:
            st += ", "+str(self.right)
        else: st += ", None"
        return st + "]"

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __str__(self):
        return str(self.root)

    def search(self, d):   
        ptr = self.root
        while ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False    
    
    def add(self, d):
        if self.root == None:
            self.root = BTNode(d,None,None)
        else:
            ptr = self.root
            while True:
                if d < ptr.data:
                    if ptr.left == None:
                        ptr.left = BTNode(d,None,None)
                        break
                    ptr = ptr.left
                else:
                    if ptr.right == None:
                        ptr.right = BTNode(d,None,None)
                        break
                    ptr = ptr.right
        self.size += 1
    
    def count(self, d):
        ptr = self.root
        count = 0
        while ptr != None:
            ptr = self._searchNode(ptr,d)
            if ptr != None:
                count += 1
                ptr = ptr.right
        return count

    def _searchNode(self, ptr, d):
        while ptr != None:
            if d == ptr.data:
                return ptr
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return None

    def remove(self,d):
        if self.root == None: return
        if self.root.data == d: 
            self.size -= 1
            return self._removeRoot()
        parentPtr = None
        ptr = self.root
        while ptr != None and ptr.data != d:
            parentPtr = ptr                
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        if ptr != None:
            self.size -= 1
            self._removeNode(ptr,parentPtr)
            
    # removes the node ptr from the tree
    def _removeNode(self, ptr, parentPtr):
        # there are 3 cases to consider:
        # 1. the node to be removed is a leaf (no children)
        if ptr.left == ptr.right == None:
            parentPtr.updateChild(ptr,None)
        # 2. the node to be removed has exactly one child            
        elif ptr.left == None:
            parentPtr.updateChild(ptr,ptr.right)
        elif ptr.right == None:
            parentPtr.updateChild(ptr,ptr.left)
        # 3. the node to be removed has both children
        else:
            # find the min node at the right of ptr -- and its parent
            parentMinRNode = ptr
            minRNode = ptr.right
            while minRNode.left != None:
                parentMinRNode = minRNode
                minRNode = minRNode.left
            # replace the data of ptr with that of the min node
            ptr.data = minRNode.data
            # bypass the min node
            parentMinRNode.updateChild(minRNode,minRNode.right)
        
    def _removeRoot(self):
        # this is essentially a hack: we are adding a dummy node at 
        # the root and call the previous method -- it allows us to
        # re-use code
        parentRoot = BTNode(None,self.root,None)
        self._removeNode(self.root,parentRoot)
        self.root = parentRoot.left

t = BST()
t.add("cat")
t.add("car")
t.add("cav")
t.add("cat")
t.add("put")
t.add("cart")
t.add("cs")
print(t)
print(t.count("cat"),t.remove("cat"),t.count("cat"),t.size)
print(t)

# this is copied and pasted from Lecture 5
# needed in order to implement BFS with queue
# and DFS with stack in top cell of this notebook

class Node:
    def __init__(self, d, n):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        st = ""
        ptr = self.head
        while ptr != None:
            st = st + str(ptr.data)
            st = st+" -> "
            ptr = ptr.next
        return st+"None"
        
    def append(self, d):
        if self.head == None:      
            self.head = Node(d,None) 
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(d,None)
        self.length += 1

    def insert(self, i, d):
        if self.head == None or i == 0:
            self.head = Node(d,self.head)
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            ptr.next = Node(d,ptr.next)
        self.length += 1

    def remove(self, i): # removes i-th element and returns it
        if self.head == None:
            return None
        if i == 0:
            val = self.head.data
            self.head = self.head.next
            self.length -= 1
            return val
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            if i == 1:
                val = ptr.next.data
                ptr.next = ptr.next.next
                self.length -= 1
                return val
            return None

class Stack:
    def __init__(self):
        self.inList = LinkedList()

    def __str__(self):
        return str(self.inList)
        
    def size(self):
        return self.inList.length

    def push(self, e):
        self.inList.insert(0,e)

    def pop(self):
        return self.inList.remove(0)
    
class Queue:
    def __init__(self):
        self.inList = LinkedList()

    def __str__(self):
        return str(self.inList)
        
    def size(self):
        return self.inList.length

    def enq(self, e):
        self.inList.append(e)

    def deq(self):
        return self.inList.remove(0)
    


# recursive implementation of BSTs
class BTNode:
    def __init__(self,d,l,r):
        self.data = d
        self.left = l
        self.right = r
          
    def updateChild(self, oldChild, newChild):
        if self.left == oldChild:
            self.left = newChild
        elif self.right == oldChild:
            self.right = newChild
        else: raise Exception("updateChild error")
           
    # prints the node and all its children in a string
    def __str__(self):  
        st = str(self.data)+" -> ["
        if self.left != None:
            st += str(self.left)
        else: st += "None"
        if self.right != None:
            st += ", "+str(self.right)
        else: st += ", None"
        return st + "]"

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __str__(self):
        return str(self.root)

    def search(self, d):   
        return self._searchRec(self.root, d)
    
    def _searchRec(self, ptr, d):
        if ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                return self._searchRec(ptr.left, d)
            else:
                return self._searchRec(ptr.right, d)
        return False    
    
    def add(self, d):
        if self.root == None:
            self.root = BTNode(d,None,None)
        else:
            self._addRec(self.root,d)
        self.size += 1
            
    def _addRec(self, ptr, d):
        if d < ptr.data:
            if ptr.left == None:
                ptr.left = BTNode(d,None,None)
                return
            self._addRec(ptr.left, d)
        else:
            if ptr.right == None:
                ptr.right = BTNode(d,None,None)
                return
            self._addRec(ptr.right, d)

    def count(self, d):
        ptr = self.root
        count = 0
        while ptr != None:
            ptr = self._searchNodeRec(ptr,d)
            if ptr != None:
                count += 1
                ptr = ptr.right
        return count

    def _searchNodeRec(self, ptr, d):
        if ptr != None:
            if d == ptr.data:
                return ptr
            if d < ptr.data:
                return self._searchNodeRec(ptr.left, d)
            else:
                return self._searchNodeRec(ptr.right, d)
        return None
                
    def remove(self, d):
        if self.root == None:
            return
        self.root = self._removeRec(self.root, d)
        
    def _removeRec(self, ptr, d):
        if ptr == None: return None
        if ptr.data == d: 
            return self._removeNodeRec(ptr)
        if ptr.data < d:
            ptr.right = self._removeRec(ptr.right, d)
        else:
            ptr.left = self._removeRec(ptr.left, d)
        return ptr
    
     
    # removes the node ptr from the tree and returns the remaining tree
    def _removeNodeRec(self, ptr):
        self.size -= 1
        # there are 3 cases to consider:
        # 1. the node to be removed is a leaf (no children)
        if ptr.left == ptr.right == None:
            return None
        # 2. the node to be removed has exactly one child
        elif ptr.right == None:
            return ptr.left
        elif ptr.left == None:
            return ptr.right
        # 3. the node to be removed has both children
        else:
            parentMinRNode = ptr
            minRNode = ptr.right
            while minRNode.left != None:
                parentMinRNode = minRNode
                minRNode = minRNode.left
            ptr.data = minRNode.data
            parentMinRNode.updateChild(minRNode,minRNode.right)
            return ptr         
        
t = BST()
t.add("cat")
t.add("car")
t.add("cav")
t.add("cat")
t.add("put")
t.add("cart")
t.add("cs")
print(t)
print(t.count("cat"),t.remove("cat"),t.count("cat"),t.size)
print(t)

# this is copied and pasted from Lecture 5
# needed in order to implement BFS with queue
# and DFS with stack in top cell of this notebook

class Node:
    def __init__(self, d, n):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        st = ""
        ptr = self.head
        while ptr != None:
            st = st + str(ptr.data)
            st = st+" -> "
            ptr = ptr.next
        return st+"None"
        
    def append(self, d):
        if self.head == None:      
            self.head = Node(d,None) 
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(d,None)
        self.length += 1

    def insert(self, i, d):
        if self.head == None or i == 0:
            self.head = Node(d,self.head)
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            ptr.next = Node(d,ptr.next)
        self.length += 1


    def remove(self, i): # removes i-th element and returns it
        if self.head == None:
            return None
        if i == 0:
            val = self.head.data
            self.head = self.head.next
            self.length -= 1
            return val
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            if i == 1:
                val = ptr.next.data
                ptr.next = ptr.next.next
                self.length -= 1
                return val
            return None
        
class Stack:
    def __init__(self):
        self.inList = LinkedList()

    def __str__(self):
        return str(self.inList)
        
    def size(self):
        return self.inList.length

    def push(self, e):
        self.inList.insert(0,e)

    def pop(self):
        return self.inList.remove(0)
    
class Queue:
    def __init__(self):
        self.inList = LinkedList()

    def __str__(self):
        return str(self.inList)
        
    def size(self):
        return self.inList.length

    def enq(self, e):
        self.inList.append(e)

    def deq(self):
        return self.inList.remove(0)
    
# recursive implementation of BSTs

class BTNode:
    def __init__(self,d,l,r):
        self.data = d
        self.left = l
        self.right = r
          
    def updateChild(self, oldChild, newChild):
        if self.left == oldChild:
            self.left = newChild
        elif self.right == oldChild:
            self.right = newChild
        else: raise Exception("updateChild error")
           
    # prints the node and all its children in a string
    def __str__(self):  
        st = str(self.data)+" -> ["
        if self.left != None:
            st += str(self.left)
        else: st += "None"
        if self.right != None:
            st += ", "+str(self.right)
        else: st += ", None"
        return st + "]"


class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __str__(self):
        return str(self.root)

    def search(self, d):   
        return self._searchRec(self.root, d)
    
    def _searchRec(self, ptr, d):
        if ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                return self._searchRec(ptr.left, d)
            else:
                return self._searchRec(ptr.right, d)
        return False    
    
    def add(self, d):
        if self.root == None:
            self.root = BTNode(d,None,None)
        else:
            self._addRec(self.root,d)
        self.size += 1

            
    def _addRec(self, ptr, d):
        if d < ptr.data:
            if ptr.left == None:
                ptr.left = BTNode(d,None,None)
                return
            self._addRec(ptr.left, d)
        else:
            if ptr.right == None:
                ptr.right = BTNode(d,None,None)
                return
            self._addRec(ptr.right, d)

    def count(self, d):
        ptr = self.root
        count = 0
        while ptr != None:
            ptr = self._searchNodeRec(ptr,d)
            if ptr != None:
                count += 1
                ptr = ptr.right
        return count

    def _searchNodeRec(self, ptr, d):
        if ptr != None:
            if d == ptr.data:
                return ptr
            if d < ptr.data:
                return self._searchNodeRec(ptr.left, d)
            else:
                return self._searchNodeRec(ptr.right, d)
        return None
            
            
    def remove(self, d):
        if self.root == None:
            return
        self.root = self._removeRec(self.root, d)
        
    def _removeRec(self, ptr, d):
        if ptr == None: return None
        if ptr.data == d: 
            return self._removeNodeRec(ptr)
        if ptr.data < d:
            ptr.right = self._removeRec(ptr.right, d)
        else:
            ptr.left = self._removeRec(ptr.left, d)
        return ptr
    
    
    # removes the node ptr from the tree and returns the remaining tree
    def _removeNodeRec(self, ptr):
        self.size -= 1
        # there are 3 cases to consider:
        # 1. the node to be removed is a leaf (no children)
        if ptr.left == ptr.right == None:
            return None
        # 2. the node to be removed has exactly one child
        elif ptr.right == None:
            return ptr.left
        elif ptr.left == None:
            return ptr.right
        # 3. the node to be removed has both children
        else:
            parentMinRNode = ptr
            minRNode = ptr.right
            while minRNode.left != None:
                parentMinRNode = minRNode
                minRNode = minRNode.left
            ptr.data = minRNode.data
            parentMinRNode.updateChild(minRNode,minRNode.right)
            return ptr
        
t = BST()
t.add("cat")
t.add("car")
t.add("cav")
t.add("cat")
t.add("put")
t.add("cart")
t.add("cs")
print(t)
print(t.count("cat"),t.remove("cat"),t.count("cat"),t.size)
print(t)

def niceStr(self): # this goes in the BTNode class
    S = ["├","─","└","│"]
    angle = S[2]+S[1]+" "
    vdash = S[0]+S[1]+" "
        
    def niceRec(ptr,acc,pre):
        if ptr == None: return acc+pre+"None"
        if ptr.left==ptr.right==None: return acc+pre+str(ptr.data)
        if pre == vdash: pre2 = S[3]+"  "
        elif pre == angle: pre2 = "   "
        else: pre2 = ""
        left = niceRec(ptr.right,acc+pre2,vdash)
        right = niceRec(ptr.left,acc+pre2,angle)
        return acc+pre+str(ptr.data)+"\n"+left+"\n"+right
            
    return niceRec(self,"","")