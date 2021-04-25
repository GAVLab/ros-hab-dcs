import rospy
import enum
import time
import math

from std_msgs.msg import String
from sensor_msgs.msg import MagneticField,Imu,CameraInfo,CompressedImage,NavSatFix,NavSatStatus,Temperature,FluidPressure,RelativeHumidity
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
    def bno080_data(self,data):
        self.bno_q = (data.orientation.x,
                    data.orientation.y,
                    data.orientation.z,
                    data.orientation.w)  
        r = R.from_quat(self.bno_q)
        self.bno_euler = tuple(r.as_euler('zyx',degrees=True))         
        self.print_output() 
                    
    def icm20948_data(self,data):
        self.icm_q = (data.orientation.x,
                    data.orientation.y,
                    data.orientation.z,
                    data.orientation.w) 
        r = R.from_quat(self.icm_q)
        self.icm_euler = tuple(r.as_euler('zyx',degrees=True))
        
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
        
    def lps22hb_press(self,data):
        self.lps_press = data.fluid_pressure    
        
    def hts221_temp(self,data):
        self.hts_temp = data.temperature
        
    def hts221_humidity(self,data):
        self.hts_humidity = data.relative_humidity
        
    def raspberrypi_temp(self,data):
        self.pi_temp = data.temperature
     
    def ina219_voltage(self,data):
        self.battery_voltage = data.data
         
    def ina219_current(self,data):
        self.battery_current = data.data
        
    def print_output(self):
        print(fmt.CLEAR)

        print(fmt.HEADER+"____ICM20948 IMU____"+fmt.ENDC)        
        print("\tEuler: Yaw: %3.1f, Pitch: %3.1f, Roll: %3.1f degrees" % (self.icm_euler))
        
        print(fmt.HEADER+"____BNO080 IMU____"+fmt.ENDC)        
        print("\tEuler: Yaw: %3.1f, Pitch: %3.1f, Roll: %3.1f degrees" % (self.bno_euler))

        print(fmt.HEADER+"____Down Cam____"+fmt.ENDC)
        print("\tTime Stamp: %d.%d" % (self.down_cam_secs,self.down_cam_nsecs))
        
        print(fmt.HEADER+"____MPL3115A2 Altimeter____"+fmt.ENDC)
        print("\tAltitude: %.2f m" % self.mpl_alt)
        print("\tTemperature: %.1f C" % self.mpl_temp)
        print("\tPressure: %.1f Pa" % self.mpl_press)        
        
        print(fmt.HEADER+"____LPS22HB Barometer____"+fmt.ENDC)
        print("\tPressure: %.1f Pa" % self.lps_press)   
        
        print(fmt.HEADER+"____HTS221 Humidity Temperature____"+fmt.ENDC)
        print("\tTemperature: %.1f C" % self.hts_temp)
        print("\tHumidity: %.1f%%" % (self.hts_humidity*100))   
        
        print(fmt.HEADER+"____Raspberry Pi____"+fmt.ENDC)
        print("\tTemperature: %.1f C" % self.pi_temp)
        
        print(fmt.HEADER+"____INA219 Battery Monitor____"+fmt.ENDC)
        print("\tVoltage: %.4f V" % self.battery_voltage)
        print("\tCurrent: %.4f A" % self.battery_current)
        
        print(fmt.HEADER+"____UBLOX GPS____"+fmt.ENDC)
        print("\tLatitude: %.5f degrees" % self.ublox_lat)
        print("\tLongitude: %.5f degrees" % self.ublox_lon)
        print("\tAltitude: %.2f m" % self.ublox_alt)
        
        
def listener():
    output = Display()
    rospy.init_node('listener',anonymous=True)

    rospy.Subscriber("icm20948/data", Imu, output.icm20948_data)
    rospy.Subscriber("bno080/data", Imu, output.bno080_data)

    rospy.Subscriber("down_cam/camera_info", CameraInfo, output.down_cam)

    rospy.Subscriber("mpl3115a2/altitude", Float64, output.mpl3115a2_alt)
    rospy.Subscriber("mpl3115a2/pressure", FluidPressure, output.mpl3115a2_press)
    rospy.Subscriber("mpl3115a2/temperature", Temperature, output.mpl3115a2_temp)

    rospy.Subscriber("lps22hb/pressure", FluidPressure, output.lps22hb_press)
    
    rospy.Subscriber("hts221/temperature", Temperature, output.hts221_temp)
    rospy.Subscriber("hts221/humidity", RelativeHumidity, output.hts221_humidity)
    
    rospy.Subscriber("ublox/fix", NavSatFix, output.ublox_fix)

    rospy.Subscriber("rpi/cpu_temp", Temperature, output.raspberrypi_temp)
    
    rospy.Subscriber("/ina219/voltage", Float32, output.ina219_voltage)
    rospy.Subscriber("/ina219/current", Float32, output.ina219_current)
    
    rospy.spin()
    
if __name__ == '__main__':
    print("Initializing Sensors...")
    time.sleep(2)
    listener()
	
