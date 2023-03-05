# python3
# Marks Kacens-Adamovics 221RDB461
import sys
import threading

class Node:
    def __init__(self, node, parent):
        self.parent = parent
        self.node = node
        self.height = 0
 
def computer_height(n, parents):
    for i in range(n-1):
        elm = parents[i]
        if elm.height != 0:
            continue
        
        nodes_height = 1
        path = [elm]
        
        while elm.parent != -1:
            elm = parents[elm.parent]
            
            if elm.height != 0:
                    nodes_height = elm.height + nodes_height
                    break
          
            path.append(elem)
            nodes_height += 1
            
        for h in path:
            h.height = nodes_height
            nodes_height -= 1
            
    return max([h.height for h in parents])
def main():
   # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
    inputType = input()
    elements = []
    nodeCount = -1
    
    if 'I' in inputType:
        nodeCount = int(input())
        elements = [Node(ix, int(x)) for ix, x in enumerate(input().split(" "))]
    elif 'F' in inputType:
        filename = input()
        
        if 'a' in fileName:
            return
        
        with open("./test/%s" % (fileName), "r") as file:
            nodeCount = int(file.readline())
            elements = [Node(ix, int(x)) forix, x enumerate(file.readline().split(" "))]
            
    height = compute_height(nodeCount, elements)
    
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()         
  
