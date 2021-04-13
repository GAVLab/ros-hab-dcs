rosbag record -o ~/bagfiles/calibration --split --duration=60m subset \
/rosout /rousout_agg \
/icm20948/mag /icm20948/raw \
/mpl3115a2/altitude /mpl3115a2/pressure /mpl3115a2/temperature \
/ublox/aideph /ublox/fix /ublox/fix_velocity /ublox/monhw /ublox/navclock /ublox/navpvt /ublox/navsat /ublox/navstatus \
/rpi/cpu_temp

