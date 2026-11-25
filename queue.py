queue = []

# Enqueue
def enqueue(customer):
    queue.append(customer)

# Dequeue
def dequeue():
    if is_empty():
        return None
    return queue.pop(0)


# Peek
def peek():
    if is_empty():
        return None
    return queue[0]

# isEmpty
def is_empty():
    return not bool(queue)

# Size
def size():
    return len(queue)

# Add customers in order
enqueue("Alice")
enqueue("Bob")
enqueue("Charlie")
enqueue("Diana")

# Peek
print("Next customer:", peek())

# Dequeue
while not is_empty():
    print("Serving:", dequeue())

# isEmpty
if is_empty():
    print("Queue is empty")