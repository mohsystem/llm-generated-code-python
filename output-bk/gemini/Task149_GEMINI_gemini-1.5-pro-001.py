class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            dequeued_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.front.data


# Example usage
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
print(my_queue.peek())  # Output: 10
print(my_queue.dequeue())  # Output: 10
print(my_queue.dequeue())  # Output: 20
print(my_queue.dequeue())  # Output: Queue is empty