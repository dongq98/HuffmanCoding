class Heap:  # Min heap
  def __init__(self):
    self._list = []

  def __len__(self):
    return len(self._list)

  # Checks whether the heap is empty.
  def is_empty(self):
    return len(self._list) == 0

  # Inserts an item.
  def insert(self, item):
    i = len(self)
    self._list.append(None)
    # Sink operation
    while i > 0:
      p = (i-1) / 2  # Parent
      if item < self._list[p]:
        self._list[i] = self._list[p]
      else:
        break
      i = p
    self._list[i] = item

  # Returns the smallest item from the heap.
  def min(self):
    return self._list[0]

  # Removes and returns the smallest item from the heap.
  def pop(self):
    if self.is_empty(): return None
    if len(self) == 1: return self._list.pop()
    top = self.min()
    last = self._list.pop()
    p = 0
    # Swim operation
    while p*2 + 1 < len(self):
      i = p*2 + 1  # Left child
      if i + 1 < len(self) and self._list[i+1] < self._list[i]:
        i = i + 1
      if last < self._list[i]:
        break
      self._list[p] = self._list[i]
      p = i
    self._list[p] = last
    return top