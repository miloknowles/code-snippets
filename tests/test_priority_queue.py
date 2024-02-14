from snippets.priority_queue import PriorityQueue


def test_priority_queue():
  N = 5
  pq = PriorityQueue(N, behavior='min', dedup=True)

  assert(pq.add('item1', 1, 'item1'))
  assert(pq.add('item2', 2, 'item2'))
  assert(pq.add('item3', 3, 'item3'))
  assert(pq.add('item4', 4, 'item4'))
  assert(pq.size() == 4)

  # Don't duplicate
  assert(not pq.add('item1', 0, 'item1'))
  assert(pq.size() == 4)

  # Reaches max size
  assert(pq.add('item5', 5, 'item5'))
  assert(pq.size() == 5)

  # Should be added and displace an item
  assert(pq.add('item6', -6, 'item6'))
  assert(pq.add('item7', -7, 'item7'))
  assert(pq.size() == 5)

  # Should NOT be added due to worse score.
  assert(not pq.add('item8', 8, 'item8'))

  expect_item7 = pq.pop() # (priority, uid, item)
  assert(expect_item7[0] == -7)
  assert(expect_item7[1] == 'item7')
  assert(expect_item7[2] == 'item7')