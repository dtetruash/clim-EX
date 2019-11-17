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

rainfile = "precip_2018.nc"
maskfile = "mask_africa.nc"
topofile = "topo.nc"

## read data

maskxr = xr.open_dataset(path+maskfile)

rain = xr.open_dataset(path+rainfile)

topo = xr.open_dataset(path+topofile)
topo["nlat"]=topo.latitude
topo["nlon"]=topo.longitude
topo = topo.rename({"nlat":"lat","nlon":"lon"})

topo = topo.sel(lat=slice(-35,37),lon=slice(-31,51))

elev = np.array(topo.variables["elevation"])
elevlat = np.array(topo.variables["lat"])
elevlon = np.array(topo.variables["lon"])

elev = np.flipud(elev)

for i in range(1,181):
    
    print(i)
    
    raini = rain.isel(time=i-1).interp(lat=elevlat,lon=elevlon)
    raini = np.array(raini.variables["tp"])
    raini = np.flipud(raini)
    
    maski = maskxr.interp(lat=elevlat,lon=elevlon)
    maski = np.array(maski.variables["t2m"])
    maski = np.flipud(maski)
    
    mask = np.isnan(maski)
    maska = np.ma.masked_array(np.ones_like(mask),mask=~mask)
    
    rainm = np.ma.masked_array(raini,mask=mask+(raini<0.01))
    
    ## transparent colormap 
    tempo = cm.get_cmap(cmo.tempo,256)
    newcolors = tempo(np.linspace(0, 1, 256))
    newcolors[:,3] = np.linspace(0,1,256)
    tempot = ListedColormap(newcolors)
    
    ##
    xx,yy = np.meshgrid(np.arange(len(elevlon)),np.arange(len(elevlat))[::-1])
    
    fig,ax = plt.subplots(1,1,figsize=(7.8,8))
    
    ax.scatter(xx,yy,s=~rainm.mask,c="#549cf9",marker=(2,0,45),alpha=0.5)

    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.set_xlim(-0.5,655.5)
    ax.set_ylim(-0.5,575.5)
    ax.set_aspect(1)
    ax.axis("off")
    
    plt.tight_layout()
    plt.savefig(path+"rainplots/rain%04d.png" % i,transparent=True)
    plt.close(fig)