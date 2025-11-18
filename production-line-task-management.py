# Excel:
    #task_name,duration,priority
    #Assemble Parts,30,2
    #Inspect Quality,15,1
    #Paint Product,25,3
    #Package Product,10,2
    #Ship Product,20,4

class Node:
    def __init__(self, task_name:str, duration:int, priority:int):
        self.task = task_name
        self.duration = duration
        self.priority = priority #1 is highest priority
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            task = self.current.task
            self.current = self.current.next
            return task

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    def add_task(self, task_name, duration, priority): #Adds a new task to the end of the list.
        newNode = Node(task_name, duration, priority)

        if self.__tail == None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next

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
            return temp.task

    def remove_task(self, task_name): #Removes a task with the given name from the list.
        if self.__size == 0:
            return False

            # Case: first element matches
        if self.__head.task == task_name:
            self.removeFirst()
            return True

        previous = self.__head
        current = self.__head.next

        while current != None:
            if current.task == task_name:
                previous.next = current.next
                if current == self.__tail:
                    self.__tail = previous
                self.__size -= 1
                return True
            previous = current
            current = current.next

        return False


    def display_tasks(self): #Prints all tasks in the linked list in the order they appear.
        current = self.__head
        while current != None:
            print(current.task)
            current = current.next


    def find_task(self,task_name): #Searches for a task by name and returns its details.
        current = self.__head
        while current is not None:
            if current.task == task_name:
                return current.task, current.duration, current.priority
            current = current.next
        return None  #(of raise ValueError) , task_name niet in list


    def calculate_total_duration(self): #Calculates the total duration of all tasks in the current order.
        total_duration = 0
        current = self.__head
        while current != None:
            total_duration += current.duration
            current = current.next
        return total_duration


    def read_tasks_from_csv(self, file_path): #Reads tasks from a CSV file and adds them to the linked list.
        file = open(file_path, 'r')
        file.readline()  # header overslaan
        for line in file: #Houdt rekening met pointer !!!
            line = line.strip() #verwijdert alle spaties, tabs, nieuwe lijnen (\n) aan beide uiteinden
            if not line: #lege string Falsey, dus: "" → False / "abc" → True
                continue
            task_name, duration, priority = line.split(',') #creert lijst
            self.add_task(task_name, int(duration), int(priority))
        file.close()

#########################################################

    def sorted_insert_by_priority(self, head, node):
        if head == None or head.priority > node.priority:
            node.next = head
            return node

        current = head
        while current.next is not None and current.next.priority <= node.priority:  # = WANT bovenaan alleen >
            current = current.next #verklaart current.next in while, anders None.next
        node.next = current.next
        current.next = node
        return head

    def reorder_tasks_by_priority(self):  # Reorders the tasks in the linked list based on priority. (lowest priority number comes first).
        new_head = None  # Nieuwe list, != self.__head WANT nog NIET losgeKNIPt

        current = self.__head
        while current is not None:
            volgende = current.next  # volgende onthouden
            current.next = None  # knippen
            new_head = self.sorted_insert_by_priority(new_head, current)
            current = volgende
        # Head bepalen
        self.__head = new_head

        # Tail bepalen
        if self.__head is None:
            self.__tail = None
        else:
            tail = self.__head
            while tail.next is not None:
                tail = tail.next
            self.__tail = tail

    def sorted_insert_by_priority_duration(self, head, node):

        def node_moet_voor(head,node):
            if head.priority != node.priority:
                return head.priority > node.priority
            else:
                return head.duration > node.duration

        if head == None or node_moet_voor(head,node):
            node.next = head
            return node

        current = head
        while current.next is not None and not node_moet_voor(current.next,node): #current.next !!!
            current = current.next
        node.next = current.next
        current.next = node
        return head

    def reorder_tasks_by_priority_duration(self): #Reorders the tasks in the linked list based on priority, then duration.
        new_head = None # Nieuwe list, != self.__head WANT nog NIET losgeKNIPt

        current = self.__head
        while current is not None:
            volgende = current.next #volgende onthouden
            current.next = None #knippen
            new_head = self.sorted_insert_by_priority_duration(new_head, current)
            current = volgende
        self.__head = new_head

        # Head bepalen
        self.__head = new_head

        # Tail bepalen
        if self.__head is None:
            self.__tail = None
        else:
            tail = self.__head
            while tail.next is not None:
                tail = tail.next
            self.__tail = tail

    ###################################################################################################################

# Met PriorityQueue:

    def Reorder_met_PriorityQueue(self):
        # 1) op basis van enkel priority
        pq = PriorityQueue(sortkey=lambda node: node.priority)

        # 1) op basis van (priority, duration)
        pq = PriorityQueue(sortkey=lambda node: (node.priority, node.duration))

    #STEL dat 1 de laagste prioriteit is voor Priority:
        # pq = PriorityQueue(sortkey=lambda node: -node.priority)
        #pq = PriorityQueue(sortkey=lambda node: (-node.priority, node.duration))

        current = self.__head
        while current is not None:
            pq.add(current)
            current = current.next

        # 2) Nieuwe lijst bouwen
        new_head = None
        new_tail = None

        while not pq.is_empty():
            node = pq.poll()
            node.next = None

            if new_head is None:
                new_head = new_tail = node
            else:
                new_tail.next = node
                new_tail = node

        # 3) head en tail updaten
        self.__head = new_head
        self.__tail = new_tail


import heapq
from functools import total_ordering

@total_ordering
class SpecialSorted:
    def __init__(self, element, value):
        self.element = element   # hier komt bv. een Node in
        self.value = value       # hier komt de sortkey(element) in

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class PriorityQueue:
    def __init__(self, sortkey=lambda x: x):
        self.content = []
        self.sortkey = sortkey   # functie die de prioriteit bepaalt

    def add(self, item):
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def poll(self):
        # geeft het element met kleinste sortkey terug
        return heapq.heappop(self.content).element if self.content else None

    def is_empty(self):
        return len(self.content) == 0