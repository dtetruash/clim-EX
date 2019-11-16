in_dir=/lustre/soge1/projects/crop_yield/GLOFAS/data
out_dir=/lustre/soge1/projects/crop_yield/hackathon/glofas_africa

mkdir -p $out_dir

# AFRICA bounding box
lonmin=-31.6
lonmax=51.8
latmin=-35.8
latmax=37.2

for in_file in $in_dir/*.nc; do
    # get the filename '{time_variable}.nc'
    out_file=$out_dir/$(basename $in_file)
    # echo $in_file
    # echo $out_file

    cdo sellonlatbox,$lonmin,$lonmax,$latmin,$latmax $in_file $out_file &
done
