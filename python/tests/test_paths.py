import os

from snippets.paths import top_folder, tests_folder


def test_paths():
  print(top_folder())
  assert(os.path.exists(top_folder()))
  assert(os.path.exists(top_folder("../README.md")))

  print(tests_folder())
  assert(os.path.exists(tests_folder()))
  assert(os.path.exists(tests_folder("conftest.py")))
