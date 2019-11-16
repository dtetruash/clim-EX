base_data_dir=/lustre/soge1/projects/crop_yield/hackathon

data_dir=$base_data_dir/glofas_africa
out_file=$base_data_dir/glofas/glofas_africa.nc

# cdo mergetime $data_dir/*.nc $out_file
# cdo cat $data_dir/*198*.nc $base_data_dir/glofas/1980.nc
# cdo cat $data_dir/*199*.nc $base_data_dir/glofas/1990.nc
# cdo cat $data_dir/*200*.nc $base_data_dir/glofas/2000.nc
# cdo cat $data_dir/*201*.nc $base_data_dir/glofas/2010.nc