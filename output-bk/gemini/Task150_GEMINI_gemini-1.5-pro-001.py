# Singly Linked List in Python

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def delete(self, data):
    if self.head is None:
      return
    if self.head.data == data:
      self.head = self.head.next
      return
    last = self.head
    while last.next:
      if last.next.data == data:
        last.next = last.next.next
        return
      last = last.next

  def search(self, data):
    current = self.head
    while current:
      if current.data == data:
        return True
      current = current.next
    return False

  def print_list(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert_at_beginning(5)
linked_list.insert_at_end(10)
linked_list.insert_at_beginning(2)
linked_list.print_list()  # Output: 2 -> 5 -> 10 -> None

linked_list.delete(5)
linked_list.print_list()  # Output: 2 -> 10 -> None

print(linked_list.search(10))  # Output: True
print(linked_list.search(15))  # Output: False
