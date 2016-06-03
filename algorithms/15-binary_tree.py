class TreeNode:
    def __init__(self, item, left, right):
        self.item = item
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item, binary_str):
        binary_str_itr = iter(binary_str)
        self.root = self.add_aux(self.root, item, binary_str_itr)

    def add_aux(self, current, item, binary_str_itr):
        if current is None:
            current = TreeNode(None, None, None)
        try:
            bit = next(binary_str_itr)
            if bit == "0":
                current.left = self.add_aux(current.left, item, binary_str_itr)
            elif bit == "1":
                current.right = self.add_aux(current.right, item, binary_str_itr)
        except StopIteration:
            current.item = item
        return current

    def get(self, binary_str):
        binary_str_itr = iter(binary_str)
        return self.get_aux(self.root, binary_str_itr)

    def get_aux(self, current, binary_str_itr):
        try:
            bit = next(binary_str_itr)
            if bit == '0':
                return self.get_aux(current.left, binary_str_itr)
            elif bit == '1':
                return self.get_aux(current.right, binary_str_itr)
        except StopIteration:
            try:
                return current.item
            except:
                print("No item exists here!")

    def print_inorder(self):
        self.print_inorder_aux(self.root)
        print("")

    def print_inorder_aux(self, current):
        if current is not None:
            self.print_inorder_aux(current.left)
            if current.item is not None:
                print(current.item,end="")
            self.print_inorder_aux(current.right)

    def __len__(self):
        return self.len_aux(self.root)

    def len_aux(self, current):
        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def get_leaves(self, current):
        a_list = []
        self.get_leaves_aux(self.root, a_list)
        return a_list

    def get_leaves_aux(self, current, a_list):
        if current is not None:
            if self.is_leaf(current):
                a_list.append(current.item)
            else:
                self.get_leaves_aux(current.left, a_list)
                self.get_leaves_aux(current.right, a_list)

    def is_leaf(self, current):
        return current.left is None and current.right is None