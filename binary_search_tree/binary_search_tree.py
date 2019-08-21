class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      # if the new node's value is less than current node's value
      if value < self.value:
        # if no left child
        if not self.left:
          # put the new node to the left
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      # if the new node's value is greater than current node's value
      elif value > self.value:
        # if no right child
        if not self.right:
          # put the new node to the right
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)

  def contains(self, target):
      # if the target is less than the current node's value
      if target < self.value:
          # if no left child
          if not self.left:
              # nothing here
              return None
          else:
              return self.left.contains(target)
      elif target > self.value:
          # if no right child
          if not self.right:
              # nothing here
              return None
          else:
              return self.right.contains(target)
      else:
          return self


  def get_max(self):
      # if right child
      if self.right:
          # return max value on right
          return self.right.get_max()
      else:
          # return root value
          return self.value


  def for_each(self, cb):
      cb(self.value)

      if self.left:
        self.left.for_each(cb)
      if self.right:
        self.right.for_each(cb)
