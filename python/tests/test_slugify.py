import pytest

from snippets.slugify import slugify


def test_slugify():
  assert(slugify("hi my name is") == "hi-my-name-is")
  assert(slugify("already-in-nice-format") == "already-in-nice-format")
  assert(slugify("thisisalongsingleword") == "thisisalongsingleword")
  assert(slugify("test test 123") == "test-test-123")
  assert(slugify("lots_of_underscores") == "lots-of-underscores")
  assert(slugify("@#$#($*&$*) word") == "word")
  
  with pytest.raises(ValueError):
    slugify("")

  with pytest.raises(ValueError):
    slugify("*&^#&^#$&^#$")