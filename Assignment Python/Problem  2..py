# Build a Tree
## Why does this code go in an infinite loop?
'''
Ans:
As the children list is made as a class variable instead of an instance variable, 
thus making a single copy of the children list for all the object instances of the class. 
Now, when the printer function calls the following line executes

        for node in root.children:
                printer(node, level+1)
it makes, again and again, starting call of the same children's list thus calling the first node
recursively and falling in an infinite loop i.e Recursion Error.
To handle this issue, just make the children list as an instance variable 
i.e object instance instead of a class variable.

'''
'''
 (b) Provide a fix:
 Ans: Please find the below corrected code. In this solution, children list is changed to instance variable.
 
 '''
class Node:
        
        def __init__(self, name, parent=None):
                self.name = name
                self.parent = parent
                self.children = []
                if parent is not None:
                        parent.children.append(self)
        def __str__(self):
                return self.name
def printer(root, level=0):
        if root==None:
                return
        print(" "*level + "|-", root.name)
        for node in root.children:
                printer(node, level+1)
if __name__ == "__main__":
        root = Node("Root")
        node1 = Node("1",root)
        node11 = Node("1.1", node1)
        node12 = Node("1.2", node1)
        node13 = Node("1.3", node1)
        node14 = Node("1.4", node1)
        node15 = Node("1.5", node1)
        node2 = Node("2",root)
        node21 = Node("2.1", node2)
        node22 = Node("2.2", node2)
        node23 = Node("2.3", node2)
        node24 = Node("2.4", node2)
        node25 = Node("2.5", node2)
        printer(root)
        # print(Node.children[2].name)
# Output:
'''
|- Root
 |- 1
  |- 1.1
  |- 1.2
  |- 1.3
  |- 1.4
  |- 1.5
 |- 2
  |- 2.1
  |- 2.2
  |- 2.3
  |- 2.4
  |- 2.5
  
 '''       