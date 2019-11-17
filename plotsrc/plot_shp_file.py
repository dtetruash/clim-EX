import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

from cmocean import cm as cmo
import matplotlib.colors as mc
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
from pathlib import Path

## set the paths
if str(Path.home()) == "/Users/tommylees":
    path = Path("/Volumes/Lees_Extend/")
elif str(Path.home()) == "/Users/milan":
    path = Path("/Users/milan/git/climax/")

in_path = path / 'Africa_SHP/Africa.shp'

## read data
gdf = gpd.read_file(in_path)

## plot
fig, ax = plt.subplots(1, 1, figsize=(7.8, 8))

gdf.plot(ax=ax, facecolor='none', edgecolor='gray', alpha=1)

ax.set_xticks([])
ax.set_yticks([])

# lat=slice(-35, 37), lon=slice(-31, 51)
ax.set_xlim([-31, 51.2])
ax.set_ylim([-35, 40])
plt.axis('off')

ax.set_aspect(1)
plt.tight_layout()

plt.savefig(path / "border_plots/border.png", transparent=True, pad_inches=0)
plt.close(fig)
