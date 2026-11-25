stack = []

def push(item): #adds to top of stack
    stack.append(item)

def pop(): #removes and returns the top item
    if is_empty():
        return None
    return stack.pop()

def peek(): #returns the top item without removing it
    if is_empty():
        return None
    return stack[-1]

def is_empty(): #checks if the stack is empty
    return len(stack) == 0

def size(): #returns the number of items in the stack
    return len(stack)

for _ in range(4): #asks for input and pushes it onto the stack
    word = input("Type a word: ")
    push(word)

print("Current document:", " ".join(stack))

for _ in range(2): #asks if the user wants to undo the last action and pops the top item if they do
    undo = input("Do you want to undo the last action? (yes/no): ")
    if undo == "yes" and not is_empty():
        pop() #removes and returns top item
        print("Undo last action...")

print("Updated document:", " ".join(stack))