"""!ls -U glofas_africa| head -4"""
"""NOTE: https://github.com/esowc/ml_drought for the `src` code"""
from pathlib import Path
import xarray as xr
import pprint

from src.preprocess.utils import select_bounding_box
from src.utils import region_lookup

region = region_lookup['africa']

base_data_dir = Path("/lustre/soge1/projects/crop_yield/hackathon")

data_dir = base_data_dir / "glofas_africa"
out_file = base_data_dir / "glofas/glofas_africa.nc"

in_files = [f for f in data_dir.glob('*.nc')]

# ds = xr.open_mfdataset(
#     (data_dir / '*.nc').as_posix(), chunks={'time': 1}
# )
# ds.rename({'latitude': 'lat', 'longitude': 'lon'})





select_bounding_box()