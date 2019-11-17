import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset as ncread
import xarray as xr
from cmocean import cm
import matplotlib.colors as mc
from glob import glob
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

path = "/Users/milan/git/climax/"

tempfile = "temp_doy.nc"
anofile = "temp_2018.nc"
topofile = "topo.nc"
maskfile = "mask_africa.nc"

## read colormaps

cpath = "/Users/milan/python/ScientificColourMaps5/"
davos = LinearSegmentedColormap.from_list("test",np.loadtxt(cpath+"davos/davos.txt"))
lajolla = LinearSegmentedColormap.from_list("test",np.loadtxt(cpath+"lajolla/lajolla.txt"))
batlow = LinearSegmentedColormap.from_list("test",np.loadtxt(cpath+"batlow/batlow.txt"))

## read data

maskxr = xr.open_dataset(path+maskfile)

t2m = xr.open_dataset(path+tempfile)
ano = xr.open_dataset(path+anofile)

topo = xr.open_dataset(path+topofile)
topo["nlat"]=topo.latitude
topo["nlon"]=topo.longitude
topo = topo.rename({"nlat":"lat","nlon":"lon"})

topo = topo.sel(lat=slice(-35,37),lon=slice(-31,51))

elev = np.array(topo.variables["elevation"])
elevlat = np.array(topo.variables["lat"])
elevlon = np.array(topo.variables["lon"])

elev = np.flipud(elev)

for i in range(1,366):

    t2mi = t2m.interp(dayofyear=i,lat=elevlat,lon=elevlon)
    anoi = ano.isel(time=i-1).interp(lat=elevlat,lon=elevlon)
    t2mi = np.array(anoi.variables["t2m"])-np.array(t2mi.variables["t2m"])
    t2mi = np.flipud(t2mi)
    
    maski = maskxr.interp(lat=elevlat,lon=elevlon)
    maski = np.array(maski.variables["t2m"])
    maski = np.flipud(maski)
    
    mask = np.isnan(maski)
    maska = np.ma.masked_array(np.ones_like(mask),mask=~mask)
    
    t2mi = np.ma.masked_array(t2mi,mask=mask)
    
    ## plot
    fig,ax = plt.subplots(1,1,figsize=(7.8,8))
    
    cax = fig.add_axes([0.1,0.1,0.03,0.45])
    
    q = ax.imshow(t2mi,interpolation="bilinear",vmin=-6,vmax=6 ,cmap=cm.balance)
    
    cb = plt.colorbar(q,cax=cax,orientation="vertical",extend="both")
    cb.set_ticks(np.arange(-6,8,2))
    cb.ax.tick_params(labelsize=8,color="w",labelcolor="w")
    cb.outline.set_edgecolor("w")
    cb.set_label("[°C]",color="w",size=8)
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")
    
    plt.tight_layout()
    plt.savefig(path+"anoplots/ano%04d.png" % i,transparent=True)
    plt.close(fig)