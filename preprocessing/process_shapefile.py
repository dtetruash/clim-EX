"""NOTE: https://github.com/esowc/ml_drought for the `src` code"""
import xarray as xr
from src.preprocess.admin_boundaries import OCHAAdminBoundariesPreprocesser
from src.preprocess.utils import SHPtoXarray
from pathlib import Path

data_dir = Path('/Volumes/Lees_Extend/data/ecmwf_sowc/data')
shp_filepath = Path('/Users/tommylees/Downloads/Africa_SHP')
reference_nc_filepath = Path('/Volumes/Lees_Extend/temp_doy.nc/')
reference_nc_filepath = Path('/Volumes/Lees_Extend/data/ecmwf_sowc/data/interim/temp_doy.nc')
var_name = 't2m'
lookup_colname = 'COUNTRY'

processor = OCHAAdminBoundariesPreprocesser(
    data_dir,
)
processor.country = 'africa'

processor._preprocess_single(
    shp_filepath=shp_filepath,
    reference_nc_filepath=reference_nc_filepath,
    var_name=var_name,
    lookup_colname=lookup_colname,
)