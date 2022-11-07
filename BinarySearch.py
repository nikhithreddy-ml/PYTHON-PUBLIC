class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data ==self.data:
            return
        if data <self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)
    
    def InOrder(self):
        ele=[]

        if self.left:
            ele +=self.left.InOrder()
        
        ele.append(self.data)

        if self.right:
            ele +=self.right.InOrder()
        
        return ele
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(ele):
    root=BinarySearchTree(ele[0])

    for i in range(1,len(ele)):
        root.add_child(ele[i])

    return root



if __name__== '__main__':
    numbers=build_tree(['india','usa','uk','canada'])
    print(numbers.search('india'))
    print(numbers.InOrder())
