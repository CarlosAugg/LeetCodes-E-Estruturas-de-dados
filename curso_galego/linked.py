class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_to_end(self, value): 
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:  
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_front(self): 
        if not self.head:
            return None
        
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value 

    def remove_from_end(self): 
        if not self.tail:
            return None
        
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None  
        else:
            self.head = None
        return removed_value  


# Criando a lista duplamente encadeada
dll = DoublyLinkedList()

# Adicionando elementos na frente e no final
dll.add_to_front(10)  # Lista: 10
dll.add_to_front(20)  # Lista: 20 <-> 10
dll.add_to_end(30)    # Lista: 20 <-> 10 <-> 30
dll.add_to_end(40)    # Lista: 20 <-> 10 <-> 30 <-> 40

# Removendo do início e do final
print(dll.remove_from_front())  # Saída: 20, Lista: 10 <-> 30 <-> 40
print(dll.remove_from_end())    # Saída: 40, Lista: 10 <-> 30

# Testando remoção até esvaziar a lista
print(dll.remove_from_front())  # Saída: 10, Lista: 30
print(dll.remove_from_front())  # Saída: 30, Lista vazia
print(dll.remove_from_front())  # Saída: None (Lista já vazia)
