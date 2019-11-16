from pathlib import Path
import shutil

from src.preprocess import NDVIPreprocessor

data_dir = Path('/soge-home/projects/crop_yield/ml_drought/data/')
out_dir = Path('/soge-home/projects/crop_yield/hackathon/ndvi')

if not out_dir.exists():
    out_dir.mkdir(exist_ok=True, parents=True)

processor = NDVIPreprocessor(data_dir)
processor.preprocess(
    subset_str='africa',
    regrid=None,
    resample_time=None,
    upsampling=False,
    parallel_processes=1,
    years_to_process=None,
    ignore_timesteps=['2018-05-28', '2016-08-26'],
    drop_invalid=False,
    nan_subset_str='indian_ocean',
    cleanup=False
)

assert (data_dir / 'interim' / 'ndvi_preprocessed' / 'data_africa.nc').exists()

shutil.copy(
    str(data_dir / 'interim' / 'ndvi_preprocessed' / 'data_africa.nc'),
    str(out_dir / 'ndvi' / 'data_africa.nc')
)