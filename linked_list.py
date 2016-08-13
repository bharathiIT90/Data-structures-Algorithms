# /********************************************************************************** 
#  *                                                                    *
#  *                                                                                *
#  *  Problem: Linked List                                                          *
#  *                                                                                *
#  *  Prompt: Create a Linked List class/constructor.                               *
#  *          Name it LinkedList (js) or Linked_List(rb/py).                        *
#  *                                                                                *
#  *          Part 1: Create a node class for your LinkedList.                      *
#  *                  Your node class will take an integer value and output         *
#  *                  and output and object with the following properties:          *
#  *                                                                                *
#  *                  node.value: input value                                       *
#  *                  node.next: a pointer to the next value (initiall null)        * 
#  *                                                                                *
#  *                  Example: { value: 1, next: null }                             *
#  *                                                                                *
#  *          Part 2: Create the LinkedList class.                                  *
#  *                  It should contain the following properties:                   *
#  *                                                                                *
#  *                  head: pointer to the head node                                *
#  *                  tail: pointer to the tail node                                *
#  *                  length: number of nodes in the linked list                    *
#  *                                                                                *
#  *                  The LinkedList should also contain the following properties   *
#  *                                                                                *
#  *                  append: function that adds a node to the tail                 *
#  *                                                                                *
#  *                  insert: function that takes in two values, one to be inserted *
#  *                          and one to search.  It searches the list for the      *
#  *                          search value, and if found, adds a new node with the  *
#  *                          insert value after the node with the search value.    *
#  *                                                                                *
#  *                  delete: function that removes a node at a specified location, *
#  *                          with a default action of deleting the head            *
#  *                                                                                *
#  *                  contains: function that checks to see if a value is contained *
#  *                            in the list                                         *
#  *                                                                                *
#  *  Input:  N/A                                                                   *
#  *  Output: A LinkedList instance                                                 *
#  *                                                                                *
#  *  What are the time and auxilliary space complexities of the various methods?   *
#  *                                                                                *
#  **********************************************************************************/

class Node: 
  def __init__(self, data = 0): 
    self.value = data
    self.next = None

class Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
      
  def append(self, val=None):
    if(self.length == 0):
      self.head = Node(val)
      self.tail = self.head
 
    else:
      self.tail.next = Node(val)
      self.tail = self.tail.next

    self.length+=1
      
  def insert(self, insertVal=None, searchVal=None):
    work = self.head
    while(work!=None):
      if(work.value == searchVal):
        reference = work.next
        work.next = Node(insertVal)
        work.next.next = reference
        if(reference == None):
          self.tail = work.next
          
        self.length+=1
        return;
        
      work = work.next
      
    print "Search Value not found"
    
    
  
  def delete(self, loc=None):
     if(loc == 0 and self.length ==0):
       self.head = null
       self.tail = null
       self.length-=1
       return
     else:
       self.head = self.head.next
       self.length-=1
       return

     work=self.head
     counter=0

     while(work!=None):
      if (counter == loc-1 and work.next!=None and work.next == self.nail):
          work.next = work.next.next
          self.tail = work
          self.length-=1
      elif(counter == loc-1 and work.next!=None):
          work.next = work.next.next
          self.length-=1

      counter+=counter
      work=work.next
      print "Error index" + loc + "out of range"
    
    
    
      
  def contains(self, searchVal=None):
    work = self.head
    while(work.value != None):
      if(work.value == searchVal):
        return True
      work = work.next
    return False

  def printlist(self):
    curr = self.head
    while(curr!=None):
      print curr.value
      curr = curr.next
      
    
l = Linked_List()
l.append(1)
l.append(2)
l.insert(3,1)
l.delete(2)
print l.contains(3)
l.printlist()


