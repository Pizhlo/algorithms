class Node:
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        self.top = Node()

    def append(self, value):
        """
        Добавление нового элемента в конец двунаправленного связного списка.
        Время работы O(N).
        """

        current = self.top

        while current.next_node is not None:
            current = current.next_node

        node = Node(value, current, current.next_node)
        current.next_node = node

    def append_after_target(self, target, value):
        """
        Добавление элемента после некоторого значения target.
        """

        current = self.top.next_node

        while current is not None:
            if current.value == target:
               node = Node(value, current, current.next_node)
               if current.next_node is not None:
                   current.next_node.prev_node = node
               current.next_node = node
            
            current = current.next_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
    
lst = List()
lst.append(75)
lst.append(12)
lst.append(28)
lst.append(6)
print(lst)

lst.append_after_target(75, 750)
lst.append_after_target(12, 120)
lst.append_after_target(28, 280)
lst.append_after_target(6, 60)

print(lst)