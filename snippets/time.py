from datetime import datetime, timedelta

from pytz import UTC


def get_utc_now() -> datetime:
  """Get the current datetime with the UTC `tzinfo` attached."""
  return datetime.utcnow().replace(tzinfo=UTC)


def datetime_range(
  start: datetime,
  end: datetime,
  delta: timedelta = timedelta(hours=1),
  inclusive: bool = True,
) -> list[datetime]:
  """Returns the range of datetimes between `start` and `end`, incrementing by `delta`.
  
  Parameters
  ----------
  * `start` : The start datetime (included)
  * `end` : The end datetime (included if `inclusive` is on)
  * `delta` : The timedelta to increment by
  * `inclusive` : Whether to include the end datetime in the returned range
  """
  if not isinstance(start, datetime) or not isinstance(end, datetime):
    raise TypeError("Expected 'datetime' instances")

  if start >= end:
    raise ValueError("The 'start' must be before the 'end' datetime.")

  output = []
  dt = start
  is_before = (lambda a, b: a <= b) if inclusive else (lambda a, b: a < b)
  while is_before(dt, end):
    output.append(dt)
    dt += delta

  return output
