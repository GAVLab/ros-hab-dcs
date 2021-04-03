echo "Waiting for sensors to initialize before recording..."
sleep 15
read -p "Start recording? (y/n)" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
echo "Recording...."
rosbag record -o ~/bagfiles/flight --split --duration=5m subset \
/rosout /rousout_agg \
/down_cam/camera_info /down_cam/image/compressed /down_cam/parameter_descriptions \
/icm20948/mag /icm20948/raw \
/mpl3115a2/altitude /mpl3115a2/pressure /mpl3115a2/temperature \
/ublox/aideph /ublox/fix /ublox/fix_velocity /ublox/monhw /ublox/navclock /ublox/navpvt /ublox/navsat /ublox/navstatus \
/rpi/cpu_temp \
/ina219/current /ina219/voltage
fi
