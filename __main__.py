import folium
from utils import queryToGDF, tmp_dir, delete_file, style_function, get_center
import os
import time
from selenium import webdriver
import math


def main(car: str):
  gdf = queryToGDF(f"""
                    SELECT * FROM `moss-forest.forest_production.moss_forest_dashboard` WHERE car = "{car}"
                    """)

  if gdf.empty:
    return

  minx, miny, maxx, maxy = gdf.total_bounds

  x_center = (maxx + minx) / 2
  y_center = (maxy + miny) / 2

  x_distance: float = abs(maxx - minx)
  y_distance: float = abs(maxy - miny)

  greater_distance = x_distance if x_distance > y_distance else y_distance

  k = 930
  zoom = math.ceil(math.log(k / greater_distance, 2))

  print({
      'car': car,
      'greater_distance': greater_distance,
      'zoom': zoom
  })

  map = folium.Map([y_center, x_center], zoom_start=zoom,
                   zoom_control=False, tiles=None)

  folium.TileLayer('Esri WorldImagery', control=False).add_to(map)
  folium.GeoJson(gdf, style_function=style_function, control=False).add_to(map)

  file_name = car
  html_file_path = os.path.join(tmp_dir, f'{file_name}.html')
  map.save(html_file_path)

  opts = webdriver.FirefoxOptions()
  opts.add_argument("--headless")
  opts.add_argument("--width=1440")
  opts.add_argument("--height=1440")

  browser = webdriver.Firefox(opts)
  html_file_url = f'file://{html_file_path}'
  browser.get(html_file_url)

  delay = 5
  time.sleep(delay)

  browser.execute_script(
      """document.querySelector(".leaflet-bottom.leaflet-right").remove();""")

  png_file_path = os.path.join(tmp_dir, f'{file_name}.png')
  delete_file(png_file_path)

  browser.save_screenshot(png_file_path)
  browser.quit()

  delete_file(html_file_path)


if __name__ == "__main__":
  main("CAR_0000000001")
