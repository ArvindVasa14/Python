# A class that represents the individual node in a BST.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

# Function to insert a new node with the given key.
def new_key_insert(root, new_key):
    if root is None:
        root = TreeNode(new_key)
        return root
    if new_key < root.key:
        root.l = new_key_insert(root.l, new_key)
    else:
        root.r = new_key_insert(root.r, new_key)
    return root

# Function to display the output of the tree
def display(root):
    #print(root)
    if root:
        print('Root', root.l)
        display(root.l)
        print(root.key)
        display(root.r)


r = new_key_insert(None,50)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)
r = new_key_insert(r, 30)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)
r = new_key_insert(r, 20)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)
r = new_key_insert(r, 40)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)
r = new_key_insert(r, 70)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)
r = new_key_insert(r, 60)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)
r = new_key_insert(r, 80)
print('Key = ',r.key, 'Left =', r.l,'Right =',r.r)

display(r)