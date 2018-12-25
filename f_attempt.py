from pprint import pprint

def getBinaryNode(data):
    #A function that represents an individual node   
    node = {}
    node['left'] = None
    node['right'] = None
    node['data'] = data
    return node

def appendNode(root, node):
    #A funcation to append node
    if not root:
        return

    left = root['left']
    right = root['right']
    if root['data'] > node['data']:
        if left == None:
            root['left'] = node
        else:
            appendNode(left, node)
    else:
        if right == None:
            root['right'] = node
        else:
            appendNode(right, node)
    return 


def createBinaryTree(elements):
    i = 0
    root = None
    while i < len(elements):        
        node = getBinaryNode(elements[i])
        if root == None:
            root = node
        else:
            appendNode(root, node)
        i = i+1
    
    print(root)

elements = [8, 5, 3, 1, 3, 2, 10, 12, 11, 4, 6, 7, 15, 16, 18]
createBinaryTree(elements)
