out_dir=/soge-home/projects/crop_yield/hackathon/africa/v_component_of_wind_hourly/
v_wind_dir=/soge-home/data/analysis/era5/0.28125x0.28125/hourly/v_component_of_wind/nc

mkdir -p out_dir

# AFRICA bounding box
lonmin=-31.6
lonmax=51.8
latmin=-35.8
latmax=37.2

for in_file in $v_wind_dir/*.nc; do
    # get the filename '{time_variable}.nc'
    out_file=$out_dir/$(basename $in_file)
    # echo $in_file
    # echo $out_file

    cdo sellonlatbox,$lonmin,$lonmax,$latmin,$latmax $in_file $out_file &
done
