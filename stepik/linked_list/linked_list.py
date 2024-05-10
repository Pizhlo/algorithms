class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        self.top = Node()
        self.tail = None

    def append_to_start(self, value):
        """
        Добавление нового элемента в начало связного списка.
        Время работы O(1).
        """

        new_node = Node(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        if self.tail is None:
            self.tail = new_node

    def append_to_end(self, value):
        """
        Добавление нового элемента в конец связного списка.
        Время работы O(1).
        """

        new_node = Node(value)

        if self.tail is not None:
            self.tail.next_node = new_node
            self.tail = new_node
            return
        
        self.top.next_node = new_node
        self.tail = new_node

    def append_after_target(self, target, value):
        """
        Добавление элемента после некоторого значения.
        """

        current = self.top.next_node
        node = Node(value)

        while current is not None:
            if current.value == target:
                node.next_node = current.next_node
                current.next_node = node
            current = current.next_node

    def delete(self, value):
        """
        Удаление элемента по значению.
        Время работы O(N).
        """

        # Задаем текущий и предыдущие элементы.
        current = self.top.next_node
        prev = self.top

        # Перебираем элементы и ищем тот, который надо удалить
        while current is not None:
            if current.value == value:
                # Если нашли, то просто меняем ссылку.
                prev.next_node = current.next_node
                return

            # Обновляем текущий и предыдущий элементы.
            prev = current
            current = current.next_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
    
l = List()
l.append_to_start(1)
l.append_to_end(2)
l.append_to_end(3)
l.append_after_target(1, 4)
print(l)