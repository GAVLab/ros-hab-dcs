import rospy
import enum
from std_msgs.msg import String
from sensor_msgs.msg import MagneticField,Imu,CameraInfo,CompressedImage,NavSatFix,NavSatStatus,Temperature,FluidPressure
from std_msgs.msg import Float64
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
    
    def bno055_status(self,data):
        if int(data.values[5].value) == 0: # check if system_error = 0
            binary = format(int(data.values[0].value),'008b')
            self.bno_sys_status = status(int(binary[0:2],2))
            self.bno_gyr_status = status(int(binary[2:4],2))
            self.bno_acc_status = status(int(binary[4:6],2))
            self.bno_mag_status = status(int(binary[6:8],2))
            self.bno_imu_status = status(min([int(binary[0:2],2),
                                        int(binary[2:4],2),
                                        int(binary[4:6],2),
                                        int(binary[6:8],2)]))
    def bno055_mag(self,data):
        scale = 1/1000 # nT to uT
        self.bno_mag_data = (data.magnetic_field.x*scale,
                    data.magnetic_field.y*scale,
                    data.magnetic_field.z*scale)  
                    
    def bno055_raw(self,data):
        self.bno_acc_data = (data.linear_acceleration.x,
                    data.linear_acceleration.y,
                    data.linear_acceleration.z)  
                    
        self.bno_gyr_data = (data.angular_velocity.x,
                    data.angular_velocity.y,
                    data.angular_velocity.z)                
                    
    def bno055_orientation(self,data):
        self.bno_q = (data.orientation.x,
                    data.orientation.y,
                    data.orientation.z,
                    data.orientation.w)            
        r = R.from_quat(self.bno_q)                    
        self.bno_euler = tuple(r.as_euler('zyx',degrees=True)) 
        
    def bno055_temp(self,data):
        if not data.temperature == 13:
            self.bno_temp = data.temperature
        
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
     
    def print_output(self):
        print(fmt.CLEAR)
        print(fmt.HEADER+"____BNO055 IMU____"+fmt.ENDC)
        
        if hasattr(self,'bno_imu_status'):
            print("\tCalibrated?: "+self.bno_imu_status)
                        
        print("\tAcceleration: X: % .3f, Y: % .3f, Z: % .3f m/s^2" % (self.bno_acc_data))
        print("\tGyro X: % .3f, Y: % .3f, Z: % .3f rads/s" % (self.bno_gyr_data))
        print("\tMagnetometer X:% .3f, Y: % .3f, Z: % .3f uT" % (self.bno_mag_data))
        print("\tQ: X: % .3f, Y: % .3f, Z: % .3f, W: % .3f m/s^2" % (self.bno_q))
        print("\tEuler: Yaw: % 3.1f, Pitch: % 3.1f, Roll: % 3.1f degrees" % (self.bno_euler))        
        print("\tTemperature: %.1f C" % self.bno_temp)
        
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
        
        print(fmt.HEADER+"____Raspberry Pi____"+fmt.ENDC)
        print("\tTemperature: %.1f C" % self.pi_temp)        
    
def listener():
    output = Display()
    rospy.init_node('listener',anonymous=True)
    
    rospy.Subscriber("bno055_imu/status", DiagnosticStatus, output.bno055_status)
    rospy.Subscriber("bno055_imu/raw", Imu, output.bno055_raw)
    rospy.Subscriber("bno055_imu/mag", MagneticField, output.bno055_mag)
    rospy.Subscriber("bno055_imu/data", Imu, output.bno055_orientation)
    rospy.Subscriber("bno055_imu/temp", Temperature, output.bno055_temp)
    
    rospy.Subscriber("icm20948/raw", Imu, output.icm20948_raw)
    rospy.Subscriber("icm20948/mag", MagneticField, output.icm20948_mag)
    
    rospy.Subscriber("down_cam/camera_info", CameraInfo, output.down_cam)
    
    rospy.Subscriber("mpl3115a2/altitude", Float64, output.mpl3115a2_alt)
    rospy.Subscriber("mpl3115a2/pressure", FluidPressure, output.mpl3115a2_press)
    rospy.Subscriber("mpl3115a2/temperature", Temperature, output.mpl3115a2_temp)
    
    rospy.Subscriber("rpi/cpu_temp", Temperature, output.raspberrypi_temp)
    
    rospy.spin()

if __name__ == '__main__':
	listener()

