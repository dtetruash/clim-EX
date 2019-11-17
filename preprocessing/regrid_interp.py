import xarray as xr
from pathlib import Path

# load datasets into memory
data_dir = Path('')

reference_nc_filepath = data_dir / 'precip_doy.nc'
reference_nc = xr.open_dataset(reference_nc_filepath)

filepath = data_dir / 'precip_doy.nc'
ds = xr.open_dataset(filepath)

output_path = data_dir / 'output.nc'

# use xarray interpolate
ds = ds.interp(lon=reference_nc.lon, lat=reference_nc.lat)

