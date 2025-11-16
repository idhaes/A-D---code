class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e)
        newNode.next = self.__head
        self.__head = newNode
        self.__size += 1

        if self.__tail == None:
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e)
    
        if self.__tail == None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next
    
        self.__size += 1

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert element at index
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index >= self.__size:
            self.addLast(e)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove first element
    def removeFirst(self):
        if self.__size == 0:
            return None
        else:
            temp = self.__head
            self.__head = self.__head.next
            self.__size -= 1
            if self.__head == None:
                self.__tail = None
            return temp.element

    # Remove last element
    def removeLast(self):
        if self.__size == 0:
            return None
        elif self.__size == 1:
            temp = self.__head
            self.__head = self.__tail = None
            self.__size = 0
            return temp.element
        else:
            current = self.__head
            for i in range(self.__size - 2):
                current = current.next
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove element at index
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None
        elif index == 0:
            return self.removeFirst()
        elif index == self.__size - 1:
            return self.removeLast()
        else:
            previous = self.__head
            for i in range(1, index):
                previous = previous.next
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["
        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", "
            else:
                result += "]"
        return result

    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0

    # -------------------------
    # COMPLETED FUNCTIONS BELOW
    # -------------------------

    # Return true if the list contains element e
    def contains(self, e):
        current = self.__head
        while current != None:
            if current.element == e:
                return True
            current = current.next
        return False

    # Remove the first occurrence of e (return True if removed)
    def remove(self, e):
        if self.__size == 0:
            return False

        # Case: first element matches
        if self.__head.element == e:
            self.removeFirst()
            return True

        previous = self.__head
        current = self.__head.next

        while current != None:
            if current.element == e:
                previous.next = current.next
                if current == self.__tail:
                    self.__tail = previous
                self.__size -= 1
                return True
            previous = current
            current = current.next

        return False

    # Return element at index
    def get(self, index):
        if index < 0 or index >= self.__size:
            return None
        current = self.__head
        for i in range(index):
            current = current.next
        return current.element

    # Return index of first occurrence of e, or -1
    def indexOf(self, e):
        index = 0
        current = self.__head
        while current != None:
            if current.element == e:
                return index
            current = current.next
            index += 1
        return -1

    # Return index of last occurrence of e, or -1
    def lastIndexOf(self, e):
        index = 0
        last = -1
        current = self.__head
        while current != None:
            if current.element == e:
                last = index
            current = current.next
            index += 1
        return last

    # Replace element at index
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            return None
        current = self.__head
        for i in range(index):
            current = current.next
        old = current.element
        current.element = e
        return old

    def __getitem__(self, index):
        return self.get(index)

    def __iter__(self):
        return LinkedListIterator(self.__head)


class Node:
    def __init__(self, e):
        self.element = e
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element
