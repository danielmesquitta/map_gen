import geopandas as gpd
from shapely.wkt import loads
from google.cloud import bigquery

client = bigquery.Client(project='moss-forest')


def queryToGDF(query: str) -> gpd.GeoDataFrame:
  query_job = client.query(query)
  df = query_job.to_dataframe()
  df['geometry'] = df['geometry'].apply(loads)
  gdf = gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')
  return gdf
