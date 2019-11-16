import numpy as np
from pathlib import Path

data_dir = Path('/run/media/davzzar/USB DISK')
assert data_dir.exists(), 'Expecting the data_dir path to exist!'

jan_1 = np.load(data_dir / 'jan_1_temp.npy')