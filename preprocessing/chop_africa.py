import xarray as xr
from pathlib import Path

print("Chop Africa")
# AFRICA bounding box
lonmin=-31.6
lonmax=51.8
latmin=-35.8
latmax=37.2
inverse_lat = inverse_lon = False

filepath = Path('')
ds = xr.open_dataset(filepath)

ds = ds.elevation.sel(
    lat=slice(latmin, latmax),
    lon=slice(lonmin, lonmax)
)
