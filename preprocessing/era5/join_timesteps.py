from pathlib import Path
import xarray as xr

in_base_dir = Path('/soge-home/projects/crop_yield/hackathon/africa')
base_out_dir = Path('/soge-home/projects/crop_yield/hackathon/')

variables = ['t2m', 'tp']
out_vars = ['temp', 'precip']

for variable, out_var in zip(variables, out_vars):
    ds = xr.open_mfdataset(str(in_base_dir / variable /  '*.nc'))

    out_dir = base_out_dir / out_var
    if not out_dir.exists():
        out_dir.mkdir(exist_ok=True, parents=True)

    ds.to_netcdf(out_dir / 'data_africa.nc')