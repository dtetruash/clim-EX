from src.preprocess import ERA5MonthlyMeanPreprocessor
from pathlib import pathlib


data_dir = Path('/soge-home/projects/crop_yield/ml_drought/data/')
hack_dir = Path('/soge-home/projects/crop_yield/hackathon')
out_dir = hack_dir / 'v_wind'

processor = ERA5MonthlyMeanPreprocessor(data_dir)

print('Opening dataset')
ds = xr.open_dataset(hack_dir / 'BAD_vwind_data.nc')

print('Resampling time from MONTHLY -> DAILY')
ds = processor.resample_time(ds, resample_length='D', upsampling=True)

print(f'Saving file to {out_dir}')
ds.to_netcdf(out_dir / 'data_africa.nc')