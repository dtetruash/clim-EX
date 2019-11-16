import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset as ncread
import xarray as xr
from cmocean import cm as cmo
import matplotlib.colors as mc
from matplotlib import cm
from glob import glob
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

path = "/Users/milan/git/climax/"

all_river = glob(path+"river/*.nc")
riverfile = all_river[0]

#for i,riverfile in enumerate(all_river[:100]):
#    print(i)
    
## read data
topofile = "topo.nc"
topo = xr.open_dataset(path+topofile)
topo["nlat"]=topo.latitude
topo["nlon"]=topo.longitude
topo = topo.rename({"nlat":"lat","nlon":"lon"})

topo = topo.sel(lat=slice(-35,37),lon=slice(-31,51))

elev = np.array(topo.variables["elevation"])
elevlat = np.array(topo.variables["lat"])
elevlon = np.array(topo.variables["lon"])

river = xr.open_dataset(riverfile)
riveri = river.interp(lat=elevlat,lon=elevlon)
riveri = np.array(riveri.variables["dis24"][0,:,:])

riverm = np.ma.masked_array(riveri,mask=np.isnan(riveri))
riverm = np.flipud(riverm)

## transparent colormap
tempo = cm.get_cmap(cmo.tempo,256)
newcolors = tempo(np.linspace(0, 1, 256))
newcolors[:,3] = np.linspace(0,1,256)
tempot = ListedColormap(newcolors)

##
xx,yy = np.meshgrid(elevlon,elevlat[::-1])

fig,ax = plt.subplots(1,1,figsize=(7.8,8))

ax.scatter(xx[riverm.mask],yy[riverm.mask],np.sqrt(riverm))

ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.savefig(path+"riverplots/river%04d.png" % 0,transparent=True)
plt.close(fig)