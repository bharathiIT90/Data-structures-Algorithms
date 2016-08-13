# /*********************************************************************************** 
#   *                                                                    *
#   *                                                                                *
#   *  Problem: Binary Search Tree                                                   *
#   *                                                                                *
#   *  Prompt: Create a BinarySearchTree class/constructor.                          *
#   *          Name it binarySearchTree (js) or binary_search_tree (rb/py).          *
#   *                                                                                *
#   *          Part 1: Create a node class for your binarySearchTree.                *
#   *                  Your node class will take an integer value and output         *
#   *                  an object with the following properties:                      *
#   *                                                                                *
#   *                  node.value: input value                                       *
#   *                  node.leftChild: a pointer to the left child Node              * 
#   *                  node.rightChild: a pointer to the right child Node            *
#   *                                                                                *
#   *                  Example: { value: 1, leftChild: null, rightChild: null }      *
#   *                                                                                *
#   *          Part 2: Create the BinarySearchTree class.                            *
#   *                  It should contain the following properties:                   *
#   *                                                                                *
#   *                  root: pointer to the root node                                *
#   *                  size: number of nodes in the BinarySearchTree                 *
#   *                                                                                *
#   *                  The BinarySearchTree will also have the following properties: *
#   *                                                                                *
#   *                  insert: method that takes takes an input value, and creates a *
#   *                          new node with the given input.  The method will then  *
#   *                          find the correct place to add the new node. (Remember *
#   *                          that nodes with values larger than the parent node go *
#   *                          to the right, and smaller values go to the left.)     *
#   *                                                                                *
#   *                  search: method that will search to see if a node with a       *
#   *                          specified value exists.  If present returns true,     *
#   *                          else returns false.                                   *
#   *                                                                                *
#   *  Input:  N/A                                                                   *
#   *  Output: A BinarySearchTree instance                                           *
#   *                                                                                *
#   *  What are the time and auxilliary space complexities of the various methods?   *
#   *                                                                                *
#   **********************************************************************************/


#  /**
#   *  Extra Credit: Remove
#   *
#   *  Prompt: Create a remove method on your BinarySearchTree that will remove and
#   *          return a given value from the tree and retie the tree so it remains
#   *          properly sorted.
#   **/

class Node:
  def __init__(self, data=0):
    self.value = data
    self.left = None
    self.right = None

class Binary_Search_Tree:
  def __init__(self): 
    self.root = None
    self.size = 0

  def insert(self, val=None):
    if(self.root == None):
      self.root = Node(val)
      self.size+=1

    else:
      def findAndInsert(current):
        if(val > current.value):
          if(current.right == None):
            current.right = Node(val)
          else:
            findAndInsert(current.right)
          

        elif(val < current.value):
          if(current.left == None):
            current.left = Node(val)
          else:
            findAndInsert(current.left)
          
      findAndInsert(self.root)
      self.size+=1

  def search(self, searchVal=None):
    check = False
    def traverse(current):
      if(current == None):
        return
      elif(current.value == searchVal):
        check = True
        return
      
      if(current.value < searchVal):
        traverse(current.right)
      elif(current.value > searchVal):
        traverse(current.left)


    traverse(self.root)
    return check
 

  def remove(self, removeval=None):
    temp = []

    def Roundup(current):
      if ( current == None):
        return

      if(current.value!=removeval):
        temp.append(current.value)

      Roundup(current.right)
      Roundup(current.left)
    Roundup(self.root)

    if(temp.length == self.size):
      print "Remove value doesnot exist!!!!"
      return
    self.root = Null
    self.size = 0

    for i in range(i,len(temp)):
      Insertval = temp[i]
      self.insert(Insertval)
    

    
test = Binary_Search_Tree()
test.insert(5)
test.insert(8)
test.insert(4)
test.insert(3)
test.insert(2)
test.search(2)
test.remove(5)


