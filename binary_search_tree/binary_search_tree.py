# class BinarySearchTree:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None
#
#   def insert(self, value):
#       # if the new node's value is less than current node's value
#       if value < self.value:
#         # if no left child
#         if not self.left:
#           # put the new node to the left
#           self.left = BinarySearchTree(value)
#         else:
#           self.left.insert(value)
#       # if the new node's value is greater than current node's value
#       elif value > self.value:
#         # if no right child
#         if not self.right:
#           # put the new node to the right
#           self.right = BinarySearchTree(value)
#         else:
#           self.right.insert(value)
#
#   def contains(self, target):
#       # if the target is less than the current node's value
#       if target < self.value:
#           # if no left child
#           if not self.left:
#               # nothing here
#               return None
#           else:
#               return self.left.contains(target)
#       elif target > self.value:
#           # if no right child
#           if not self.right:
#               # nothing here
#               return None
#           else:
#               return self.right.contains(target)
#       else:
#           return self
#
#
#   def get_max(self):
#       # if right child
#       if self.right:
#           # return max value on right
#           return self.right.get_max()
#       else:
#           # return root value
#           return self.value
#
#
#   def for_each(self, cb):
#       cb(self.value)
#
#       if self.left:
#         self.left.for_each(cb)
#       if self.right:
#         self.right.for_each(cb)

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # insertion of a key
    # a new key is always inserted at leaf.
    # we start searching a key from root till we hit a leaf node.
    if value < self.value:
      # go left
      if not self.left:
        # add as a new leaf
        self.left = BinarySearchTree(value)
      else:
        # check again, this time against self.left.value
        # use recursion
        self.left.insert(value)
    if value > self.value:
      # go right
      if not self.right:
        # add as new leaf
        self.right = BinarySearchTree(value)
      else:
        # check again, this time against self.right.value
        self.right.insert(value)


  def contains(self, target):
    # searching a key
    # to search a given key in a binary search tree, we first compare it with root
    # if the key is present at root, return root.
    # if key is greater than root, recur for right subtree of root node
    # else recur for left subtree
    # base case, will return true once done
    if self.value == target:
      return True
    # decide if we are going left or right
    if target < self.value:
      if not self.left:
        return False
      else:
        # use recursion
        return self.left.contains(target)
    else:
      # handle the right side
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    # keep going right until you find a node without a child to the right
      if not self.right:
        return self.value
      else:
        # if there is something on the right, keep going
        return self.right.get_max()

  def for_each(self, callback):
    # we need to traverse the tree similar to how print works in the demo
    # call the function that is passed as an argument, using the value in current node
    callback(self.value)
    if self.left:
      # if left node, call the function on left node, using recursion
      self.left.for_each(callback)
    if self.right:
      self.right.for_each(callback)

# print the value of every node, order doesnt matter
bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
cb = lambda x: print(x)
bst.for_each(cb)


