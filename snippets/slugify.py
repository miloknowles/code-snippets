import re
import unidecode


def slugify(text: str) -> str:
  """Convert text to a suitable URL slug (words with hyphens)."""
  text = unidecode.unidecode(text).lower()
  slug = re.sub(r'[\W_]+', '-', text)
  if len(slug) >= 1 and slug[0] == "-": # remove leading -
    slug = slug[1:]
  elif len(slug) >= 1 and slug[-1] == "-": # remove trailing -
    slug = slug[:-1]
  if len(slug) == 0:
    raise ValueError(f"Could not convert '{text}' to a valid hyphenated slug.")
  return slug