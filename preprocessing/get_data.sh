era5_dir='/soge-home/data/analysis/era5/0.28125x0.28125/daily/'
base_our_dir='/soge-home/projects/crop_yield/hackathon/'

# AFRICA bounding box
lonmin=-31.6
lonmax=51.8
latmin=-35.8
latmax=37.2

# declare -a vars=("t2m" "tp" "u_component_of_wind" "v_component_of_wind")
# for var in "${vars[@]}"; do

for var in t2m tp u_component_of_wind v_component_of_wind; do
    in_dir=$era5_dir/$var/nc/
    out_dir=$base_our_dir/$var

    # make directory
    mkdir -p $out_dir

    for in_file in $in_dir/*.nc; do
        out_file=$out_dir/$(basename $in_file)
        # echo $in_file
        echo $out_file
        cdo sellonlatbox,$lonmin,$lonmax,$latmin,$latmax $in_file $out_file &
    done

    wait
    echo "Done for variable $var"

done
