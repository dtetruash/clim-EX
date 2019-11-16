"""NOTE: https://github.com/esowc/ml_drought for the `src` code"""
from pathlib import Path
import xarray as xr
from src.preprocess import CHIRPSPreprocessor

data_dir = Path('/lustre/soge1/projects/crop_yield/hackathon')
# data_dir = Path('/Volumes/Lees_Extend')
out_dir = data_dir
ml_drought_dir = Path('/lustre/soge1/projects/crop_yield/ml_drought/data')
# ml_drought_dir = Path('/users/tommylees/github/ml_drought/data')

ds = xr.open_dataset(data_dir / 'topo.nc')
# ds['nlon'] = ds.latitude
# ds['nlat'] = ds.longitude
# ds = ds.rename({'nlon': 'lon', 'nlat': 'lat'})

# topo = ds.elevation
# topo.to_netcdf(data_dir / 'topo_clean.nc')

regrid_path = data_dir / 'temp/temp_doy.nc'
# regrid_path = data_dir / 'precip/precip_africa.nc'
assert regrid_path.exists()

print("Reading in topo data for regridding")
processor = CHIRPSPreprocessor()

ds = xr.open_dataset(out_dir / 'topo.nc')
regrid_da = processor.load_reference_grid(regrid_path)

print("Chop Africa")
# AFRICA bounding box
lonmin=-31.6
lonmax=51.8
latmin=-35.8
latmax=37.2
inverse_lat = inverse_lon = False

# processor.chop_roi(
#     ds=ds,
#     subset_str='africa',
#     inverse_lat=True,
# )

ds = ds.elevation.sel(
    lat=slice(latmin, latmax),
    lon=slice(lonmin, lonmax)
)

print("Starting topo Regridding")
ds = processor.regrid(ds, regrid_da)

print("Saving the regrid data")
ds.to_netcdf(out_dir / 'topo_regrid_africa.nc')