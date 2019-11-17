import xarray as xr
from pathlib import Path


def clean_nc_files(dir_: str, var: str) -> None:
    da = xr.open_dataset(data_dir / dir_ / 'data_africa.nc')[var]
    print(f'Read data in for variable: {var}')

    # rename to lat lon
    coords = [c for c in da.coords]
    if ('latitude' in coords) or ('longitude' in coords):
        da = da.rename({'longitude': 'lon', 'latitude': 'lat'})

    # save to netcdf
    da.to_netcdf(data_dir / dir_ / f'{dir_}_africa.nc')
    print(f'Done for variable: {var}')

if 'cdsuser' in [p.name for p in Path('.').resolve().parents]:
    data_dir = Path('/home/cdsuser/hackathon')
else:
    data_dir = Path('/lustre/soge1/projects/crop_yield/hackathon')
assert data_dir.exists()

dirs = ['precip', 'temp', 'u_wind', 'v_wind', 'ndvi']
vars = ['tp', 't2m', 'u', 'v', 'ndvi']

dir_ = var = 'ndvi'
dir_ = 'v_wind'; var = 'v'

for dir_, var in zip(dirs, vars):
    clean_nc_files(dir_, var)
