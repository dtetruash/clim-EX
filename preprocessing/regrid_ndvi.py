"""
regrid the NDVI data to the same spatial grid
as the ERA5 reanalysis data
"""
from src.preprocess import CHIRPSPreprocessor
from pathlib import Path
import xarray as xr

if 'cdsuser' in [p.name for p in Path('.').resolve().parents]:
    data_dir = Path('/home/cdsuser/hackathon')
elif 'soge1' in [p.name for p in Path('.').resolve().parents]:
    data_dir = Path('/lustre/soge1/projects/crop_yield/hackathon')
else:
    data_dir = Path('/home/cdsuser/hackathon')
assert data_dir.exists()
out_dir = data_dir / 'ndvi'

processor = CHIRPSPreprocessor(data_dir)

regrid_path = data_dir / 'precip/precip_africa.nc'
assert regrid_path.exists()

print("Reading in NDVI data for regridding")
ds = xr.open_dataset(out_dir / 'data_africa.nc')
regrid_da = processor.load_reference_grid(regrid_path)

print("Starting NDVI Regridding")
ds = processor.regrid(ds, regrid_da)

print("Saving the regrid data")
ds.to_netcdf(out_dir / 'ndvi_regrid_africa.nc')