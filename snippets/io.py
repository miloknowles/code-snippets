import json


def read_lines(filename: str):
  """Read all the lines in a text file and return as a list."""
  with open(filename, 'r') as f:
    lines = f.read().splitlines()
  return lines


def pretty_print_dict(d: dict, indent: int = 2):
  """Prints out a `dict` in a nice format."""
  print(json.dumps(d, indent=indent))
