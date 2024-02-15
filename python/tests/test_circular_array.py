from snippets.circular_array import CircularArray


def test_circular_array():
  arr = CircularArray(3)

  for i in range(5):
    arr.append(i)
    assert(len(arr) == min(i + 1, 3))

  # Should contain 0, 1, [2, 3, 4] at this point.
  assert(arr.median() == 3)
  assert(arr.mean() == 3)