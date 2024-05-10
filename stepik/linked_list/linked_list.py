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

    def append_to_end(self, value):
        """
        Добавление нового элемента в конец связного списка.
        Время работы O(1).
        """

        tail = self.tail
        if tail is None:
            tail = Node()
            
        tail.next_node = Node(value)

    def append_to_start(self, value):
        """
        Добавление нового элемента в начало связного списка.
        Время работы O(1).
        """

        node = Node(value=value, next_node=self.top.next_node)
        self.top.next_node = node

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

print(l)