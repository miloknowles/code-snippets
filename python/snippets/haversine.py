from math import radians, sin, cos, asin, sqrt


def haversine_distance(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
  """Implements the Haversine distance formula.

  Notes
  -----
  The input values should be in decimal degrees.

  Returns
  -------
  The distance between the two points in km.

  References
  ----------
  https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
  """
  # convert decimal degrees to radians
  lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

  # haversine formula
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a))
  r = 6371 # Radius of earth in kilometers. Use 3956 for miles

  return c * r
