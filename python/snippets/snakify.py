import re


def camel_to_snake(s: str) -> str:
  """Converts camel case strings to snake.

  Examples
  --------
  ```python
  camel_to_snake("helloWorld") # hello_world

  camel_to_snake("HelloWorld") # hello_world

  camel_to_snake("BECOMES_LOWERCASE") # becomes_lowercase
  ```

  References
  ----------
  https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
  """
  s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def snakify(text: str) -> str:
  """Converts arbitrary text into `lower_camel_case`.

  This is useful for translating variable names into a more "Pythonic" format.

  You might also use this to convert column names in a Pandas dataframe into
  Pythonic names so that you can access them more easily:
  ```python
  df["Column Name (units)"] # annoying
  df.column_name_units # a bit nicer
  ```
  
  Examples
  --------
  ```python
  snakify("helloWorld") # hello_world

  snakify("This is a sentence with spaces") # this_is_a_sentence_with_spaces

  snakify("DataFrame Column Name (units)") # data_frame_column_name_units
  ```
  """
  # Convert camel case to snake case.
  text = camel_to_snake(text)

  # Replace any special characters with underscores.
  text = re.sub(r'[\W_]+', '_', text)

  # Remove leading and trailing _.
  if len(text) >= 1 and text[0] == "_": # remove leading _
    text = text[1:]
  elif len(text) >= 1 and text[-1] == "_": # remove trailing _
    text = text[:-1]
  if len(text) == 0:
    raise ValueError(f"Could not convert '{text}' to a valid hyphenated text.")

  return text