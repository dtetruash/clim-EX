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
    data_path = Path("/Volumes/Lees_Extend/")
    path = Path("/Users/tommylees/github/climax/turnoff/public/images/borderplot")
elif str(Path.home()) == "/Users/milan":
    path = Path("/Users/milan/git/climax/")

in_path = data_path / 'Africa_SHP/Africa.shp'

## read data
gdf = gpd.read_file(in_path)

## plot
fig, ax = plt.subplots(1, 1, figsize=(7.8, 8))

gdf.plot(
    ax=ax, facecolor='none',
    edgecolor='white', alpha=0.3
)

ax.set_xticks([])
ax.set_yticks([])

# lat=slice(-35, 37), lon=slice(-31, 51)
ax.set_xlim([-31.5, 51.2])
ax.set_ylim([-35, 38])

# lat.max=36.9375
# lat.min=-34.9375
# lon.max=50.9375
# lon.min=-30.9375
# ax.set_xlim([-30.9, 50.9])
# ax.set_ylim([-34.9, 36.9])
plt.axis('off')

ax.set_aspect(1)
plt.tight_layout()

plt.savefig(path / "border.png", transparent=True, pad_inches=0)
plt.close(fig)
