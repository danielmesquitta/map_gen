def style_function(feature):
  return {
      'fillColor': 'white',
      'color': 'white',
      'weight': 1.5
  }


def get_center(coordinates: list[list[float]]):
  total_lat = 0
  total_lon = 0
  count = 0

  for coord_array in coordinates:
    for coord in coord_array:
      total_lat += coord[1]
      total_lon += coord[0]
      count += 1

  return {
      'latitude': total_lat / count,
      'longitude': total_lon / count
  }
