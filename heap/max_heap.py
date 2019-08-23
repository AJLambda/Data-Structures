class Heap:
  def __init__(self):
    # constructor to initialize a heap
    self.storage = []

  # 0(log n)
  def insert(self, value):
    # put the value at the end of the list(append)
    self.storage.append(value)  #0(1)
    # compare index to parent and swap
    self._bubble_up(len(self.storage) - 1)   # 0(log n)

  def delete(self):
    # delete(): Deleting a key also takes 0(Logn) time.
    # We replace the key to be deleted with the minimum infinite by calling decreaseKey().
    # After decreaseKey(), the minus infinite value must reach root, so we call extractMin() to remove the key.
    # removes and returns the 'topmost' value from the heap;
    # this method needs to ensure that the heap property is maintained after the topmost element has been removed.
    pass

  # 0(1)
  def get_max(self):
    return self.storage[0] # or 1 if you decide to do the 1 index method

  # 0(1)
  def get_size(self):
    # Traverse through and count all of the elements
    # This is an array - len(self.storage)
    # For stretch practice, do this with a traversal similar to BST

    # return len(self.storage)
    pass

  # 0(log n)
  def _bubble_up(self, index):
    # up-heap operation
    # helper function for insert to compare to parent node and switch if appropriate
    # moves the element at the specified index "up" the heap
    # by swapping it with its parent if the parents value is less than index value

    # while index exists
    while index:
      # get parent node
      parent = (index - 1) // 2
      # if current index is greater than parent
      if self.storage[index] > self.storage[parent]:
        # move element "up" by swapping
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      else:
          return None

  def _sift_down(self, index):
    # down-heap operation
    # helper function for delete
    # grabs the index of the elements children
    while index:
      parent = (index - 1) // 2
      l_child = (2 * index) + 1
      r_child = (2 * index) + 2
      # determines which child has larger value
      if self.storage[l_child] > self.storage[r_child]:
        child = [l_child]
      else:
        child = [r_child]
      # if larger child's value is greater than the parent
      if self.storage[child] > self.storage[parent]:
      # swap child with parent
        self.storage[child], self.storage[parent] = self.storage[parent], self.storage[child]
    else:
      return None

