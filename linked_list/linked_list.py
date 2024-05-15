class Node:
  def __init__(self,value):
    
    self.value = value  
    self.next = None  
    
    
     
class LinkedList:
  def __init__(self):
    
    self.head = None
    
 # required Lab Methods  
  def __getitem__(self,index):
    """ get item from the list using [](indexer) operators method."""
    if self.head is None:
      raise IndexError("empty list")
    elif index >= self.__len__() or index < 0: # index 5, length 5 
      raise IndexError("list index out of range")
    counter = 0
    current_node = self.head
    while current_node:
      if counter == index:
        return current_node.value
      current_node = current_node.next
      counter+=1
  
  def __len__(self):
    """return the length of the list"""
    if self.head is None:
      return 0
    
    counter = 1
    current_node = self.head
    while current_node.next:
      counter += 1
      current_node = current_node.next
    return counter
  
  def __str__(self):
      """ return string representation of the list items"""
      elements = []
      current =  self.head
      while current:
        elements.append(str(current.value))
        current = current.next
      return ' -> '.join(elements) + " -> None"
 
 
 # additional methods, read the README.md file for more info.
  def append(self,value):
    
    """Append a new node with the given data to the end of the linked list."""
    
    new_node = Node(value) 
 
    if self.head is None:
      self.head = new_node
      return 
    
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node 
  
  def prepend(self,value):
    """add item to the first index in the list"""
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    new_node.next = self.head
    self.head = new_node
   
  def delete(self,value):
    """delete the first ccurence of value in the list"""
    if self.head is None: # empty list
      return
    
    if self.head.value == value:
      self.head = self.head.next
      
    current_node = self.head
    while current_node.next :
      if current_node.next.value == value:
        current_node.next = current_node.next.next
        return
      current_node = current_node.next
       
  def last(self):
    """return the last item in a given list"""
    if self.head is None:
      raise ValueError("list is empty")
    
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    return last_node.value
      
  def replacebyindex(self,substitute,index):
    """ replace an item in a list, replacebyindex take substitute an as int and the index of the originl item """
    if self.head is None:
      raise IndexError("list is empty")

    target_index = index
    counter = -1
    target_node = self.head
    previous_node = None
    while counter != target_index:
      previous_node = target_node
      target_node = target_node.next
      
      counter+=1
    previous_node.value = substitute
    string_representation = self.__str__()
    return(string_representation)
  
  
    
 
    
    new_node.next = self.head
    self.head = new_node
    
    string_representation = self.__str__()
    return(string_representation)

  
















