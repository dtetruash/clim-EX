"""
- subset Africa from the global era5 v_wind data
- resample the hourly era5 v_wind data to DAILY timesteps
"""

from pathlib import Path
import xarray as xr
from src.preprocess import ERA5MonthlyMeanPreprocessor

data_dir = Path('/soge-home/projects/crop_yield/ml_drought/data/')
base_out_dir = Path('/soge-home/projects/crop_yield/hackathon/')
final_out_dir = Path('/soge-home/projects/crop_yield/hackathon/v_wind')
v_wind_dir = Path('/soge-home/data/analysis/era5/0.28125x0.28125/hourly/v_component_of_wind/nc')

# make directories
out_dir = base_out_dir / 'africa' / 'v_component_of_wind_hourly'
if not out_dir.exists():
    out_dir.mkdir(exist_ok=True, parents=True)
if not final_out_dir.exists():
    final_out_dir.mkdir(exist_ok=True, parents=True)

processor = ERA5MonthlyMeanPreprocessor(data_dir)

# # SUBSET AFRICA from hourly files
# nc_files = [f for f in v_wind_dir.glob('*.nc')]

# for netcdf_filepath in nc_files:
#     ds = xr.open_dataset(netcdf_filepath).rename(
#         {'longitude': 'lon', 'latitude': 'lat'}
#     )
#     ds = processor.chop_roi(ds, subset_str='africa', inverse_lat=True)
#     ds.to_netcdf(out_dir / file.name)
#     print(f'Done for {file.name}')

# JOIN ALL FILES AND MAKE DAILY
ds = xr.open_mfdataset(str(out_dir / '*.nc'), chunks={'time': 1})
ds = processor.resample_time(ds, resample_length='D', upsampling=False)
ds.to_netcdf(final_out_dir / 'data_africa.nc')

# JOIN ALL FILES AND MAKE DAILY
