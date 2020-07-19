class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  
  def __init__(self):
    self.head = None
   
  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.data
      
if __name__ == "__main__":
  
  llist = LinkedList()
  llist.head = Node(8)
  second = Node(5)
  third = Node(1)
  fourth = Node(20)
  fifth = Node(44)
  
  llist.head.next = second
  second.next = third
  third.next = fourth
  fourth.next = fifth
  
  llist.printList()
