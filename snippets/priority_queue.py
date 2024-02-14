import heapq


class PriorityQueue(object):
  def __init__(self, max_size: int, behavior: str = 'min', dedup: bool = True):
    """A generalized priority queue.

    Notes
    -----
    This data structure stores arbitrary items with an attached `priority`. The
    priority value determines where an item sits in the queue. 

    Parameters
    ----------
    * `max_size` (int) : The maximum number of items to store in the buffer.
    * `behavior` ('min' or 'max') : Whether this the minimum or maximum priority score is considered first.
    """
    if behavior not in ['min', 'max']:
      raise ValueError(f"The behavior must be 'min' or 'max'.")
    self.max_size = max_size
    self.dedup = dedup
    self.multiplier = 1 if behavior == 'min' else -1
    self.uuids = set()
    self.buf = [] # stores (priority, uid, item)

  def add(self, item: any, priority: float, uid: str | int | None = None) -> bool:
    """Add an item with `value` to the priority queue.
    
    Returns
    -------
    Whether the item was included in the priority queue or not.
    """
    if self.dedup and uid is None:
      raise ValueError("A `uuid` is required for items in a deduplicated priority queue.")

    # Avoid duplicating items.
    if self.dedup and uid in self.uuids:
      return False

    # If buffer hasn't reached max size, always add the new item.
    if len(self.buf) < self.max_size:
      heapq.heappush(self.buf, [self.multiplier * priority, uid, item])
      self.uuids.add(uid)
      return True

    # If buffer is at full size, replace an item only if it would make the heap WORSE.
    # For a MIN heap, add item if its value is SMALLER than that of any existing item.
    # For a MAX heap, add item if its value is LARGER than that of any existing item.
    largest_item = heapq.nlargest(1, self.buf)[0]
    if (self.multiplier * priority) < largest_item[0]:
      # Remove the largest (worst) item.
      self.buf.remove(largest_item)
      self.uuids.remove(largest_item[1])

      # Restore heap.
      heapq.heapify(self.buf)

      # Push the new item.
      heapq.heappush(self.buf, [self.multiplier * priority, uid, item])
      self.uuids.add(uid)

      return True

    return False

  def size(self) -> int:
    """The current size (number of items)."""
    return len(self.buf)

  def pop(self) -> tuple[float, str | int | None, any]:
    """Get the top item in the queue (highest if a max heap, lowest if a min heap)."""
    return heapq.heappop(self.buf)

  def average_value(self) -> float:
    """Returns the average value of items in the buffer."""
    total = 0
    for i in range(len(self.buf)):
      total += self.multiplier * self.buf[i][0]
    return total / len(self.buf)
