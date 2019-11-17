import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset as ncread
import xarray as xr
from cmocean import cm as cmo
import matplotlib.colors as mc
from glob import glob
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
from pathlib import Path

# set the paths
if str(Path.home()) == "/Users/tommylees":
    path = Path("/Volumes/Lees_Extend/")
elif str(Path.home()) == "/Users/milan":
    path = Path("/Users/milan/git/climax/")

topofile = "topo.nc"
maskfile = "mask_africa.nc"

## read data
maskxr = xr.open_dataset(path / maskfile)
topo = xr.open_dataset(path / topofile)

# reset lat/lon coordinates
topo["nlat"] = topo.latitude
topo["nlon"] = topo.longitude
topo = topo.rename({"nlat": "lat", "nlon": "lon"})

# chop east africa

topo = topo.sel(lat=slice(-35, 37), lon=slice(-31, 51))

elev = np.array(topo.variables["elevation"])
elevlat = np.array(topo.variables["lat"])
elevlon = np.array(topo.variables["lon"])

elev = np.flipud(elev)

maski = maskxr.interp(lat=elevlat, lon=elevlon)
maski = np.array(maski.variables["t2m"])
maski = np.flipud(maski)

mask = np.isnan(maski)
maska = np.ma.masked_array(np.ones_like(mask), mask=~mask)

# elev[mask] = -2000.0

dz = np.gradient(elev, 1)[0]

dz = dz - dz.min()
dz = dz / dz.max()

dz = 1 - dz

## colormap
gray = cm.get_cmap(cmo.gray, 256)
newcolors = gray(np.linspace(0, 1, 256))
newcolors[:, 3] = np.hstack(
    (np.linspace(1, 0, 128) ** (1 / 4), np.linspace(0, 1, 128) ** (1 / 4))
)
grayt = ListedColormap(newcolors)

## plot
fig, ax = plt.subplots(1, 1, figsize=(7.8, 8))

hand = ax.imshow(dz, interpolation="bilinear", vmin=0, vmax=1, cmap=grayt)

ax.set_xticks([])
ax.set_yticks([])


plt.tight_layout()
plt.savefig(path + "figs/topo_only_4.png", transparent=True)
plt.close(fig)
