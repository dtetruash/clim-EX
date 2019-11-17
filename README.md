# Clim-AX
## Making climate data sexy again.

Clim-AX (Climate Aminamtion Experience) is a tool for visialising and viewing past metorological data which will help solve african droughts. This tool bridges the gap between the layman and scientieifc meteological experts making the viewing of this data enjoyable and aesthetically pleasing. 

### Features

Clim-AX is capable of displaying temprature and temperature anomoly, topography, precipitation, the flow of watrer and rivers across the surface. Each are individual layers and can be toggled according to the user's intent and wish.

Clim-AX is able to dynamically scroll through the temporal axis, enabling the user to glimpse the past and 

Clim-AX uses ERA5 Reanalysis Product data taken from the [Copernicus Data Store](https://cds.climate.copernicus.eu)

### Under the hood
- Pregenerates image plots via MatPlotLib for each time step and each data layer from the NetCDF data
- Send the data to the React Frontend
- Stacks the layers via the SVG format to achieve hacky data layer blending
- Auto interpolated between images for a smooth and pleaseing viewign experience

### Screenshots

#### TODO

### Team

- [David Simon Tetruashvli](https://github.com/davzzar)
- [Sijmen Huizenga](https://github.com/SijmenHuizenga)
- [Milan Koewer](https://github.com/milankl)
- [Tommy Lees](https://github.com/tommylees112)

