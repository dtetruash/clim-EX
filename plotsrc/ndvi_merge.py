from pathlib import Path
import xarray as xr

#
base_dir = Path('/soge-home/projects/crop_yield')
data_path = base_dir / 'ml_drought/data/interim/ndvi_interim'
ndvi_files = [f for f in data_path.glob('*19_2010*.nc')]
ndvi_files.sort()

#
ds = xr.open_mfdataset(ndvi_files)
ds.to_netcdf(base_dir / 'hackathon/ndvi/ndvi_2010.nc')