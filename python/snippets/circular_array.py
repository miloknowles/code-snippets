import numpy as np


class CircularArray(object):
  """Implements a circular array of fixed size.."""
  def __init__(self, size: int):
    self.buf = np.zeros(size)
    self.idx = 0
    self.n = 0

  def append(self, value: float | int):
    """Append `value` to the array."""
    if self.n < self.buf.shape[0]:
      self.n += 1
    self.buf[self.idx] = value
    self.idx = (self.idx + 1) % self.buf.shape[0]

  def __len__(self) -> int:
    return self.n

  def mean(self) -> float | int:
    """Returns the mean of the array."""
    return np.mean(self.buf[:self.n])

  def median(self) -> float | int:
    """Returns the median of the array."""
    return np.median(self.buf[:self.n])