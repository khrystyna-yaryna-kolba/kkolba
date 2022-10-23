from kkolba.helpers import *
import random

def get_group_num(group):
    if group>0:
        return random.randrange(1, 50)
    elif group<0:
        return random.randrange(-50, -1)
    else:
        return 0

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0
    def __len__(self):
        return self._len
    def append(self, data):
        if self.tail == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self._len += 1
    def insert(self,position, data):
        if position>self._len or position<0:
            raise IndexError("invalid position. can`t perform inserting in list")
        if position == 0:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head
            if self._len == 0:
                self.tail = self.head
        elif position == self._len:
            new_tail = Node(data)
            self.tail.next = new_tail
            self.tail = new_tail
        else:
            cur_node = self.head
            for i in range(position-1):
                cur_node = cur_node.next
            temp = cur_node.next
            cur_node.next = Node(data)
            cur_node.next.next = temp
        self._len += 1

    def remove(self, position):
        if position > self._len-1 or position<0:
            return
        if position == 0:
            temp = self.head
            self.head = self.head.next
            if self._len ==1:
                self.tail =self.head
            del temp
        else:
            cur_node = self.head
            for i in range(position-1):
                cur_node = cur_node.next
            to_del = cur_node.next
            cur_node.next = cur_node.next.next
            del to_del
            if position == self._len - 1:
                self.tail = self.tail.next
        self._len -= 1

    def remove_in_range(self, position1, position2):
        if position1 > self._len-1 or position1<0 or position2<position1 or position2> self._len-1:
            raise IndexError("invalid range. can`t perform deleting in list")
        for i in range(position2-position1+1):
            self.remove(position1)

    def __str__(self):
        #for i in self:
        #    print(i, end = " ")
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkedListIterator(self.head)


    """Задано масив з N цілих чисел. Сформувати масив таким чином, щоб спочатку були всі від’ємні
     елементи масиву, потім додатні і, після них нульові, зберігши порядок. Якщо якоїсь групи
      чисел не існує, то після кожного числа, що дорівнює K вставити рандомне число х цієї
       групи. Наприклад, -5 0 -4 0 -5 -6 0. K= -5. Немає додатних чисел. -5 7 -4 -5 6 -6 0 0 0.
        Числа 7 і 6 - рандомні, після кожного -5.
    """
    @classmethod
    def transform(cls,li, k):
        negative = LinkedList()
        positive = LinkedList()
        zeros = LinkedList()
        # filling three lists to maintain the order
        for i in li:
            if i < 0:
                negative.append(i)
            elif i > 0:
                positive.append(i)
            else:
                zeros.append(0)
        # checking if there is missing group, if yes, than what is that
        # (doesn't handle the situation when there are two missing groups, just chooses one)
        missing_group = None  # -1, 0, 1
        if len(negative)== 0:
            missing_group = -1
        elif len(positive) == 0:
            missing_group = 1
        elif len(zeros) == 0:
            missing_group = 0
        # inserting random elements of missing group after each k
        # (as in the instructions)
        if missing_group != None:
            i = 0
            if k > 0:
                for el in positive:
                    if el == k:
                        positive.insert(i + 1, get_group_num(missing_group))
                        i+=1
                    i+=1
            elif k < 0:
                for el in negative:
                    if el == k:
                        negative.insert(i + 1, get_group_num(missing_group))
                        i+=1
                    i+=1
            else:
                for el in zeros:
                    if el == k:
                        zeros.insert(i + 1, get_group_num(missing_group))
                        i+=1
                    i+=1
        # concatenating parts to get final result
        for i in positive:
            negative.append(i)
        for i in zeros:
            negative.append(i)
        return negative


    @classmethod
    def input_int_list(cls, n):
        result = LinkedList()
        for i in range(n):
            data = input_int("list[{}]".format(i))
            result.append(data)

        return result

    @classmethod
    def random_generating(cls, n, a, b):
        result = LinkedList()
        for i in range(n):
            data= random.randrange(a, b + 1)
            result.append(data)


        return result
