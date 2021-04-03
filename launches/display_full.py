import rospy
import enum
import time
from std_msgs.msg import String
from sensor_msgs.msg import MagneticField,Imu,CameraInfo,CompressedImage,NavSatFix,NavSatStatus,Temperature,FluidPressure
from std_msgs.msg import Float32, Float64
from diagnostic_msgs.msg import DiagnosticStatus
from scipy.spatial.transform import Rotation as R

class fmt:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033c'

def status(value):
    if value == 3:
        return fmt.OKGREEN+"True"+fmt.ENDC
    elif value == 2:
        return fmt.WARNING+"Almost"+fmt.ENDC
    elif value == 1:
        return fmt.WARNING+"Some"+fmt.ENDC
    else:
        return fmt.FAIL+"False"+fmt.ENDC
    
class Display:            
    def icm20948_mag(self,data):
        scale = 1000 # T to uT
        self.icm_mag_data = (data.magnetic_field.x*scale,
                    data.magnetic_field.y*scale,
                    data.magnetic_field.z*scale)  
                    
    def icm20948_raw(self,data):
        self.icm_acc_data = (data.linear_acceleration.x,
                    data.linear_acceleration.y,
                    data.linear_acceleration.z)  
                    
        self.icm_gyr_data = (data.angular_velocity.x,
                    data.angular_velocity.y,
                    data.angular_velocity.z)    
        self.print_output()         
        
    def ublox_fix(self,data):
        self.ublox_lat = data.latitude
        self.ublox_lon = data.longitude
        self.ublox_alt = data.altitude    
        
    def down_cam(self,data):
        self.down_cam_secs = data.header.stamp.secs
        self.down_cam_nsecs = data.header.stamp.nsecs                           
                                    
    def mpl3115a2_alt(self,data):
        self.mpl_alt = data.data        
        
    def mpl3115a2_temp(self,data):
        self.mpl_temp = data.temperature
          
    def mpl3115a2_press(self,data):
        self.mpl_press = data.fluid_pressure
        
    def raspberrypi_temp(self,data):
        self.pi_temp = data.temperature
     
    def ina219_voltage(self,data):
        self.battery_voltage = data.data
         
    def ina219_current(self,data):
        self.battery_current = data.data
        
    def print_output(self):
        print(fmt.CLEAR)

        print(fmt.HEADER+"____ICM20948 IMU____"+fmt.ENDC)        
        print("\tAcceleration: X: % .3f, Y: % .3f, Z: % .3f m/s^2" % (self.icm_acc_data))
        print("\tGyro X: % .3f, Y: % .3f, Z: % .3f rads/s" % (self.icm_gyr_data))
        print("\tMagnetometer X:% .3f, Y: % .3f, Z: % .3f uT" % (self.icm_mag_data))

        print(fmt.HEADER+"____Down Cam____"+fmt.ENDC)
        print("\tTime Stamp: %d.%d" % (self.down_cam_secs,self.down_cam_nsecs))
        
        print(fmt.HEADER+"____MPL3115A2 Altimeter____"+fmt.ENDC)
        print("\tAltitude: %.2f m" % self.mpl_alt)
        print("\tTemperature: %.1f C" % self.mpl_temp)
        print("\tPressure: %.1f Pa" % self.mpl_press)
        
        print(fmt.HEADER+"____UBLOX GPS____"+fmt.ENDC)
        print("\tLatitude: %.5f degrees" % self.ublox_lat)
        print("\tLongitude: %.5f degrees" % self.ublox_lon)
        print("\tAltitude: %.2f m" % self.ublox_alt)
        
        print(fmt.HEADER+"____Raspberry Pi____"+fmt.ENDC)
        print("\tTemperature: %.1f C" % self.pi_temp)
        
        print(fmt.HEADER+"____INA219 Battery Monitor____"+fmt.ENDC)
        print("\tVoltage: %.4f V" % self.battery_voltage)
        print("\tCurrent: %.4f A" % self.battery_current)
        
def listener():
    output = Display()
    rospy.init_node('listener',anonymous=True)

    rospy.Subscriber("icm20948/raw", Imu, output.icm20948_raw)
    rospy.Subscriber("icm20948/mag", MagneticField, output.icm20948_mag)

    rospy.Subscriber("down_cam/camera_info", CameraInfo, output.down_cam)

    rospy.Subscriber("mpl3115a2/altitude", Float64, output.mpl3115a2_alt)
    rospy.Subscriber("mpl3115a2/pressure", FluidPressure, output.mpl3115a2_press)
    rospy.Subscriber("mpl3115a2/temperature", Temperature, output.mpl3115a2_temp)

    rospy.Subscriber("ublox/fix", NavSatFix, output.ublox_fix)

    rospy.Subscriber("rpi/cpu_temp", Temperature, output.raspberrypi_temp)
    
    rospy.Subscriber("/ina219/voltage", Float32, output.ina219_voltage)
    rospy.Subscriber("/ina219/current", Float32, output.ina219_current)
    
    rospy.spin()
    
if __name__ == '__main__':
    print("Initializing Sensors...")
    time.sleep(10)
    listener()
	
