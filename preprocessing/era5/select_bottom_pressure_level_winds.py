from pathlib import Path
import xarray as xr

# era5_dir = Path('/soge-home/data/analysis/era5/0.28125x0.28125/hourly/')
base_out_dir = Path('/soge-home/projects/crop_yield/hackathon/')
# winds = ['u_component_of_wind', 'v_component_of_wind_hourly']
winds = ['v_component_of_wind_hourly']
# wind_component = ['u', 'v']
wind_component = ['v']

for wind, component in zip(winds, wind_component):
    print(f"** READING {wind} data **")
    ds = xr.open_mfdataset(str(base_out_dir / wind /  '*.nc'), chunks={'level': 1})
    ds = ds.isel(level=0)

    out_dir = base_out_dir / f"{wind}_surface"
    if not out_dir.exists():
        out_dir.mkdir(exist_ok=True, parents=True)

    print(f"** WRITING {wind} data **")
    ds.to_netcdf(out_dir / f'{wind}_africa.nc')