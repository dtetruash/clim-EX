base_dir='/lustre/soge1/projects/crop_yield/GLOFAS'
base_out_dir=$base_dir/data

mkdir -p $base_out_dir
mkdir -p $base_dir/zip

start_year=1979
end_year=2019
YEARS=`seq $start_year $end_year`

for year in $YEARS; do
    unzip $base_dir/GLOFAS_$year.zip -d $base_out_dir &
    mv $base_dir/GLOFAS_$year.zip $base_dir/zip
done