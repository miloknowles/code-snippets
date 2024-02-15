from snippets.snakify import snakify


def test_snakify():
  assert(snakify("helloWorld") == "hello_world")
  assert(snakify("This is a sentence with spaces") == "this_is_a_sentence_with_spaces")
  assert(snakify("DataFrame Column Name (units)") == "data_frame_column_name_units")
  assert(snakify("string with 123") == "string_with_123")
  assert(snakify("string with123") == "string_with123")
  assert(snakify("SpecialCharacters#$*&#$@)*)") == "special_characters")