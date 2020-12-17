rosbag record -o ~/bagfiles/flight --split --duration=1m subset \
/rosout /rousout_agg \
/side_cam/camera_info /side_cam/image_raw/compressed /side_cam/image_raw/compressed/parameter_descriptions \
/down_cam/camera_info /down_cam/image/compressed /down_cam/parameter_descriptions \
/icm20948/mag /icm20948/raw /icm20948/status /icm20948/temp \
/bno055_imu/data /bno055_imu/mag /bno055_imu/raw /bno055_imu/status /bno055_imu/temp \
/mpl3115a2/altitude /mpl3115a2/pressure /mpl3115a2/temperature \
/mt3339/fix /mt3339/heading /mt3339/time_reference /mt3339/vel \
/rpi/cpu_temp

