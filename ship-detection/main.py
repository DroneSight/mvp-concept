import os
import openeo
from ultralytics import YOLO
import rasterio
from PIL import Image
import folium
import numpy as np

# Connect to Copernicus Data Space Ecosystem
def connect_openeo():
    connection = openeo.connect("openeo.dataspace.copernicus.eu")
    connection.authenticate_oidc()
    return connection

# Define Area of Interest (AOI) and Time Period
aoi = {
    "type": "Polygon",
    "coordinates": [[
        [-5.0, 35.0],
        [0.0, 35.0],
        [0.0, 40.0],
        [-5.0, 40.0],
        [-5.0, 35.0]
    ]]
}
time_period = ("2024-10-01", "2024-10-31")

# Export Sentinel-1 data
def get_sentinel1_data(aoi, time_period, connection, output_path="sentinel1_output.tif"):
    process = connection.load_collection(
        "SENTINEL1_GRD",
        spatial_extent=aoi,
        temporal_extent=time_period,
        bands=["VV"],
    ).sar_backscatter(
    coefficient="sigma0-ellipsoid", elevation_model="COPERNICUS_30")
    process = process.apply(lambda x: 10 * x.log(base=10))
    result = process.save_result(format="GTiff")
    job = result.execute_batch(outputfile=output_path)
    job.get_results().download_files(target=os.path.dirname(output_path))

# Convert GeoTIFF to JPEG
def geotiff_to_jpeg(input_path, output_path):
    with rasterio.open(input_path) as src:
        array = src.read(1)
        normalized_array = (255 * (array - np.min(array)) / (np.max(array) - np.min(array))).astype(np.uint8)
        img = Image.fromarray(normalized_array)
        img_resized = img.resize((640, 640))  # Resize for YOLOv11
        img_resized.save(output_path, format='JPEG', quality=90)

# Extract ship locations
def extract_ship_locations(detections, geotiff_path):
    with rasterio.open(geotiff_path) as src:
        transform = src.transform
    ship_locations = []
    for detection in detections.xyxy[0]:
        x_min, y_min, x_max, y_max, _, _ = detection.tolist()
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        lon, lat = rasterio.transform.xy(transform, y_center, x_center)
        ship_locations.append([lat, lon])
    return ship_locations

# Visualize hazards on a map
def visualize_hazards(aoi, ship_locations, pollution_areas):
    m = folium.Map(location=[37.0, -3.0], zoom_start=8)
    folium.GeoJson(aoi).add_to(m)
    for ship in ship_locations:
        folium.Marker(location=ship, icon=folium.Icon(color="blue", icon="ship")).add_to(m)
    for area in pollution_areas:
        folium.Circle(location=area, radius=5000, color="red", fill=True).add_to(m)
    return m

# Workflow
connection = connect_openeo()
get_sentinel1_data(aoi, time_period, connection, output_path="sentinel1_image.tif")
geotiff_to_jpeg("sentinel1_image.tif", "sentinel1_image.jpg")

model = YOLO('miscellenious/weights/best.pt')
results = model("sentinel1_image.jpg")
ship_locations = extract_ship_locations(results, "sentinel1_image.tif")
pollution_areas = [[37.5, -3.5], [37.6, -3.6]]
map_hazards = visualize_hazards(aoi, ship_locations, pollution_areas)
map_hazards.save("sea_hazards_map.html")
