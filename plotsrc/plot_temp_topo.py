import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset as ncread
import xarray as xr
from cmocean import cm
import matplotlib.colors as mc
from glob import glob

path = "/Users/milan/git/climax/"

tempfile = "temp_doy.nc"
topofile = "topo.nc"
maskfile = "mask_africa.nc"

## read data

maskxr = xr.open_dataset(path+maskfile)

t2m = xr.open_dataset(path+tempfile)

topo = xr.open_dataset(path+topofile)
topo["nlat"]=topo.latitude
topo["nlon"]=topo.longitude
topo = topo.rename({"nlat":"lat","nlon":"lon"})

topo = topo.sel(lat=slice(-35,37),lon=slice(-31,51))

elev = np.array(topo.variables["elevation"])
elevlat = np.array(topo.variables["lat"])
elevlon = np.array(topo.variables["lon"])

elev = np.flipud(elev)

t2mi = t2m.interp(dayofyear=1,lat=elevlat,lon=elevlon)
t2mi = np.array(t2mi.variables["t2m"])-273.15
t2mi = np.flipud(t2mi)

maski = maskxr.interp(lat=elevlat,lon=elevlon)
maski = np.array(maski.variables["t2m"])
maski = np.flipud(maski)

mask = np.isnan(maski)
maska = np.ma.masked_array(np.ones_like(mask),mask=~mask)

t2mi[mask] = 0.0
elev[mask] = -2000.0

## plot
fig,ax = plt.subplots(1,1,figsize=(7.8,8))

#norm = mc.Normalize(10,32)
#lsource = mc.LightSource(90,45,hsv_max_sat=0.6)
#rgb = lsource.shade_rgb(cm.thermal(norm(t2mi)),0.0001*elev)

hand = ax.imshow(t2mi,interpolation="bilinear",vmin=10,vmax=32,cmap=cm.gray_r)

ax.set_xticks([])
ax.set_yticks([])


plt.tight_layout()
plt.show()