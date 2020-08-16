class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:

  def __init__(self):
    self.head = None

# Inserting into Linked list

  def insertAtHead(self, newData):
    newNode = Node(newData)
    newNode.next = self.head
    self.head = newNode

  def insertAtEnd(self, newData):
    newNode = Node(newData)
    if self.head is None:
      self.head = newNode
      return
      last = self.head
      while last.next:
        last = last.next
      last.next = newNode

  def insertInBetween(self, middleNode, newData):
    if middleNode is None:
      print("The mentioned node is absent")
      return
    newNode = Node(newData)
    newNode.next = middleNode.next
    middleNode.next = newNode

#Removing from Linked list

  def removeAtHead(self, dataIn):
    newNode = Node(dataIn)
    newNode.next = self.head
    self.head = newNode

  def removeNode(self, removeKey):
    headData = self.head
    if headData is not None:
      if headData.data == removeKey:
        self.head = headData.next
        headData = None
        return

    while headData is not None:
      if headData.data == removeKey:
        break
      previous = headData
      headData = headData.next

    if headData == None:
      return
    previous.next = headData.next
    headData = None 

  def printList(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

if __name__ == "__main__":

  llist = SinglyLinkedList()
  llist.head = Node(8)
  second = Node(5)
  third = Node(1)
  fourth = Node(20)
  fifth = Node(44)
  
  llist.head.next = second
  second.next = third

  #Inserts the node 2 to the head of the list
  llist.insertAtHead(2)
  
  third.next = fourth
  fourth.next = fifth

  #Remove the node with key 1 from the list
  llist.removeNode(1)
  
  #Prints the linked list 
  llist.printList()
