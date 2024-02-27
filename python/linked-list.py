class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, data):
        newNode = Node(data)
        
        current = self.head
        if current is None:
            self.head = newNode
            return

        while current.next:
            current = current.next

        current.next = newNode

    def appendToHead(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head = newNode

    def deleteFromTail(self):    
        node = self.head

        if node is None:
            # Empty LL
            return        
        elif node.next is None:
            self.head = None
            return
        
        while node.next.next:
            node = node.next

        node.next = None       

    def deleteFromHead(self):        
        if self.head is None:
            return
        
        self.head = self.head.next        

    def printLL(self):
        current = self.head
        ans = ""
        while current:
            ans += f"{current.data}->"
            current = current.next        
        print(ans)

    def size(self):
        current = self.head
        ans = 0
        while current:
            ans += 1
            current = current.next
        return ans

if __name__ == "__main__":
    # Initialize linked list
    myLL = LinkedList()

    for i in range(5):
        myLL.appendToTail(i)
    
    myLL.printLL()

    for i in range(10, 15):
        myLL.appendToHead(i)

    myLL.printLL()
    
    myLL.deleteFromTail()    
    myLL.printLL()
    myLL.deleteFromTail()
    myLL.printLL()
    myLL.deleteFromTail()    
    myLL.printLL()

    n = myLL.size()
    print(n)
    for _ in range(n):
        myLL.deleteFromHead()
        myLL.printLL()