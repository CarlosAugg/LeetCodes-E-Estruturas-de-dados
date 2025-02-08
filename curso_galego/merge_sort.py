class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    
def find_middle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next        
        fast = fast.next.next  
    return slow

def merge(l1, l2):
    
    dummy = Node()
    tail = dummy 

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1   
            l1 = l1.next 
        else:
            tail.next = l2  
            l2 = l2.next    
        tail = tail.next   

    tail.next = l1 if l1 is not None else l2
    return dummy.next

def mergesort(head):
    if not head or not head.next:
        return head

    middle = find_middle(head)
    after_middle = middle.next  
    middle.next = None
    left = mergesort(head)
    right = mergesort(after_middle)

    return merge(left, right)

node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)

my_list = mergesort(node_9)

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None") 

print_list(my_list)
