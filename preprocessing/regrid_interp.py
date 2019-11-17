import xarray as xr
from pathlib import Path

# load datasets into memory
reference_nc_filepath = Path('')
reference_nc = xr.open_dataset(reference_nc_filepath)

filepath = Path('')
ds = xr.open_dataset(filepath)

# use xarray interpolate
ds = ds.interp(lon=reference_nc.lon, lat=reference_nc.lat)
