class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val} -> {self.next}"


class LinkedList():
    def __init__(self, head):
        self.head = head
        self.size = 1

    def is_empty(self):
        return self.head is None

    def search(self, index):
        counter = 0
        node = self.head
        while node:
            if index == counter: return node
            counter += 1
            if not node.next: break
            node = node.next
        return None

    def add(self, new_node):
        last_index = self.size - 1
        node = self.search(last_index)
        node.next = new_node
        self.size += 1

    def add_at(self, new_node, index):
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        prev = self.search(index - 1)
        new_next = prev.next
        prev.next = new_node
        new_node.next = new_next
        self.size += 1

    def delete_at(self, index):
        if index == 0:
            prev_head = self.head
            new_head = self.head.next
            self.head = new_head
            del prev_head
            self.size -= 1
            return
        prev = self.search(index - 1)
        node_to_delete = prev.next
        next_node = prev.next.next
        prev.next = next_node
        del node_to_delete
        self.size -= 1

    def __str__(self):
        s = ''
        node = self.head
        while node:
            s += f"{node.val} -> "
            node = node.next
        return s + f"(size: {self.size})"


n1, n2, n3, n4 = Node(15), Node(30), Node(45), Node(60)
ll = LinkedList(n1)
ll.add(n2)
ll.add(n3)
ll.add_at(n4, 0)
ll.delete_at(1)
print(ll)
