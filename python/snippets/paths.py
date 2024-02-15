import os


def top_folder(relative_path: str = "") -> str:
  """Returns the path to the top of the repository.
  
  Notes
  -----
  Assumes that this script is one directory down from the top of the repository.

  Usage
  -----
  * Get the absolute path to the repository with `top_folder()`
  * Get the path to a subfolder in the repository with `top_folder("relative/path/...")`
  * You can go into parent directories using `top_folder("../parent/...")`
  """
  return os.path.join(os.path.abspath(os.path.join(os.path.realpath(__file__), "../../")), relative_path)


def data_folder(relative_path: str = "") -> str:
  """Returns a path relative to the `data` folder."""
  return os.path.join(top_folder('data'), relative_path)


def models_folder(relative_path: str = "") -> str:
  """Returns a path relative to the `models` folder."""
  return os.path.join(top_folder('models'), relative_path)


def tests_folder(relative_path: str = "") -> str:
  """Returns a path relative to the `tests` folder."""
  return os.path.join(top_folder('tests'), relative_path)


def make_directory(filepath: str):
  """Makes the containing directory of a file."""
  pardir = os.path.abspath(os.path.join(filepath, os.pardir))
  os.makedirs(pardir, exist_ok=True)


def containing_folder(filepath: str) -> str:
  """Returns the folder containing `filepath`."""
  return os.path.dirname(os.path.realpath(filepath))
