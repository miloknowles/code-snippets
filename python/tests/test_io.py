from snippets.io import read_lines, pretty_print_dict
from snippets.paths import tests_folder


def test_read_lines():
  lines = read_lines(tests_folder("resources/lines.txt"))
  print(lines)
  assert(lines == ['a', 'b', 'c', 'd', 'e', 'f'])


def test_pretty_print_dict():
  pretty_print_dict({
    "key": "value",
    "world": ["a", "b", "c"],
    "nested": {
      "hello": 123,
    }
  })