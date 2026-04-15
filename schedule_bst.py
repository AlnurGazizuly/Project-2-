class BSTNode:
    def __init__(self, time_block):
        self.time_block = time_block
        self.reservations = []
        self.left=None
        self.right=None


class ScheduleBST:
    def __init__(self):
        self.root=None

    def insert(self, reservation):
        self.root=self._insert(self.root, reservation)

    def _insert(self, node, reservation):
        if node is None:
            new_node=BSTNode(reservation.time_block)
            new_node.reservations.append(reservation)
            return new_node
        if reservation.time_block < node.time_block:
            node.left= self._insert(node.left, reservation)
        elif reservation.time_block > node.time_block:
            node.right= self._insert(node.right, reservation)
        else:
            node.reservations.append(reservation)
        return node

    def search(self, time_block):
        node= self._search(self.root,time_block)
        if node is None:
            return []
        return node.reservations

    def _search(self, node, time_block):
        if node is None:
            return None
        if time_block==node.time_block:
            return node
        if time_block <node.time_block:
            return self._search(node.left, time_block)
        return self._search(node.right,time_block)

    def remove_reservation(self, reservation_id, time_block):
        node = self._search(self.root, time_block)
        if node is None:
            return False
        for i, reservation in enumerate(node.reservations):
            if reservation.reservation_id == reservation_id:
                node.reservations.pop(i)
                if len(node.reservations) ==0:
                    self.root = self._delete_node(self.root, time_block)
                return True
        return False

    def _delete_node(self, node,time_block):
        if node is None:
            return None
        if time_block < node.time_block:
            node.left = self._delete_node(node.left, time_block)
        elif time_block > node.time_block:
            node.right = self._delete_node(node.right, time_block)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_value_node(node.right)
            node.time_block = successor.time_block
            node.reservations = successor.reservations
            node.right = self._delete_node(node.right, successor.time_block)
        return node

    def _min_value_node(self, node):
        current=node
        while current.left is not None:
            current=current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder(self.root,result)
        return result

    def _inorder(self, node,result):
        if node is not None:
            self._inorder(node.left,result)
            result.append((node.time_block, node.reservations))
            self._inorder(node.right,result)