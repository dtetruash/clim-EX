"""NOTE: https://github.com/esowc/ml_drought for the `src` code"""
from pathlib import Path
from src.preprocess.base import BasePreProcessor

era5_dir = Path('/soge-home/data/analysis/era5/0.28125x0.28125/hourly/')
winds = ['u_component_of_wind', 'v_component_of_wind']
wind_component = ['u', 'v']

base_our_dir = Path('/soge-home/projects/crop_yield/hackathon/')



processor = BasePreProcessor(Path('/soge-home/users/chri4118')))

for wind, component in zip(winds, wind_component):
    out_dir = base_our_dir / wind + '_surface'
    if not out_dir.exists():
        out_dir.mkdir(exist_ok=True, parents=True)

    ds = xr.open_mfdataset(base_our_dir / wind /  '*.nc')
    ds = ds.isel(level=0)
    ds.to_netcdf(out_dir / 'data_africa.nc')