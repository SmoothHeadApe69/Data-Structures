class Node:

  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:

  def __init__(self):
    self.head = None

  
  #Adding to head of list
  def addToList(self, newValue):
    newNode = newValue(Node)
    newNode.next = self.head
    if self.head is not None:
      self.head.prev = newNode
      self.head = newNode

  def printList(self, node):
    while (node is not None):
      print (node.data)
      last = node
      node = node.next

doublyLL = DoublyLinkedList()

