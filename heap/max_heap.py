class Heap:
  def __init__(self):
    # constructor to initialize a heap
    self.storage = []

  def insert(self, value):
    # put the value at the end of the list(append)
    self.storage.append(value)
    # if Arr[i] > Arr[i/2] (current is bigger than parent) then swap
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # delete(): Deleting a key also takes 0(Logn) time.
    # We replace the key to be deleted with the minimum infinite by calling decreaseKey().
    # After decreaseKey(), the minus infinite value must reach root, so we call extractMin() to remove the key.
    pass

  def get_max(self):
    return self.storage[0] # or 1 if you decide to do the 1 index method

  def get_size(self):
    # Traverse through and count all of the elements
    # This is an array - len(self.storage)
    # For stretch practice, do this with a traversal similar to BST
    pass

  def _bubble_up(self, index):
    # up-heap operation
    # helper function to compare to parent node and switch if appropriate
    # while index exists
    while index:
      # get parent node
      parent = (index - 1) // 2
      # if current index is greater than parent node
      if self.storage[index] > self.storage[parent]:
        # swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # update new index
        index = parent
      else:
          return None

  def _sift_down(self, index):
    #
    pass
