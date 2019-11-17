<p align="center">
  <img src="https://github.com/davzzar/clim-AX/raw/master/turnoff/public/images/logos/readme-banner.png" alt="Clim-AX Logo Banner" width="738">
</p>

Clim-AX (Climate Animation eXperience) is a tool for visualising and viewing past meteorological data which will help solve African droughts. This tool bridges the gap between the layman and scientific meteorological experts making the viewing of this data enjoyable and aesthetically pleasing.

### Features

Clim-AX is capable of displaying temperature and temperature anomaly, topography, precipitation, the flow of water and rivers across the surface. Each layer can be toggled according to the user's intent and wish.

Clim-AX can dynamically scroll through the temporal axis, enabling the user to glimpse the past and

Clim-AX uses ERA5 Reanalysis Product data taken from the [Copernicus Data Store](https://cds.climate.copernicus.eu/).

### Under the hood

- Pre-generates image plots via MatPlotLib for each time step and each data layer from the NetCDF data
- Send the data to the React frontend
- Stacks the layers via the SVG format to achieve hacky data layer blending
- Auto interpolated between images for a smooth and pleasing viewing experience

### Screenshots

#### TODO

### Team

- [David Simon Tetruashvli](https://github.com/davzzar)
- [Sijmen Huizenga](https://github.com/SijmenHuizenga)
- [Milan Kloewer](https://github.com/milankl)
- [Tommy Lees](https://github.com/tommylees112)

