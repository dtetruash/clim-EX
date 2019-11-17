import xarray as xr
from pathlib import Path

dir_ = Path('/lustre/soge1/projects/crop_yield/ml_drought/data/interim/ndvi_interim')
out_dir = Path('/lustre/soge1/projects/crop_yield/hackathon')

files = [d for d in dir_.glob('*_2018*.nc')]
files.sort()

ds = xr.open_mfdataset(files)
ds.to_netcdf(out_dir / 'ndvi_2018.nc')