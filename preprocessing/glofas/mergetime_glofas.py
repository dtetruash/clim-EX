from pathlib import Path
import xarray as xr
import pprint

base_data_dir = Path("/lustre/soge1/projects/crop_yield/hackathon")

data_dir = base_data_dir / "glofas_africa"
out_file = base_data_dir / "glofas/glofas_africa.nc"

in_files = [f for f in data_dir.glob('*.nc')]
# in_files = [f for f in data_dir.glob('*.nc') if '1979' not in str(f)]

# ds = xr.open_mfdataset(
#     (data_dir / '*.nc').as_posix(), chunks={'time': 1}
# )

def catch(func, handle=lambda e : None, *args, **kwargs):
    """https://stackoverflow.com/a/8915613/9940782"""
    try:
        return func(*args, **kwargs)
    except ValueError as e:
        return None


# list_ds = [xr.open_dataset(f) for f in in_files]

failed = []
list_ds = []
for f in in_files:
    try:
        list_ds.append(xr.open_dataset(f))
    except:
        failed.append(f)

print('Data Loaded')


pprint(ds)

ds.to_netcdf(out_file)
print(f'Data saved to \n{out_file}')