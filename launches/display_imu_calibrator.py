import rospy
import enum
from std_msgs.msg import String
from sensor_msgs.msg import MagneticField,Imu
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
                                    
    def print_output(self):
        print(fmt.CLEAR)
        print(fmt.HEADER+"____BNO055 IMU____"+fmt.ENDC)
        
        if hasattr(self,'bno_imu_status'):
            print("Calibrated?:")
            print("\tFull IMU: "+self.bno_imu_status+
                "\n\tSys: "+self.bno_sys_status+
                "\n\tGyr: "+self.bno_gyr_status+
                "\n\tAcc: "+self.bno_acc_status+
                "\n\tMag: "+self.bno_mag_status)
                        
        print("Raw Data:")
        print("\tAcceleration: X: % .3f, Y: % .3f, Z: % .3f m/s^2" % (self.bno_acc_data))
        print("\tGyro X: % .3f, Y: % .3f, Z: % .3f rads/s" % (self.bno_gyr_data))
        print("\tMagnetometer X:% .3f, Y: % .3f, Z: % .3f uT" % (self.bno_mag_data))
        
        print("Orientation:")
        print("\tQ: X: % .3f, Y: % .3f, Z: % .3f, W: % .3f m/s^2" % (self.bno_q))
        print("\tEuler: Yaw: % 3.1f, Pitch: % 3.1f, Roll: % 3.1f degrees" % (self.bno_euler))
        
        print(fmt.HEADER+"____ICM20948 IMU____"+fmt.ENDC)
        
        print("Raw Data:")
        print("\tAcceleration: X: % .3f, Y: % .3f, Z: % .3f m/s^2" % (self.icm_acc_data))
        print("\tGyro X: % .3f, Y: % .3f, Z: % .3f rads/s" % (self.icm_gyr_data))
        print("\tMagnetometer X:% .3f, Y: % .3f, Z: % .3f uT" % (self.icm_mag_data))


    
    
def listener():
    output = Display()
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber("bno055_imu/status", DiagnosticStatus, output.bno055_status)
    rospy.Subscriber("bno055_imu/raw", Imu, output.bno055_raw)
    rospy.Subscriber("bno055_imu/mag", MagneticField, output.bno055_mag)
    rospy.Subscriber("bno055_imu/data", Imu, output.bno055_orientation)
    rospy.Subscriber("icm20948/raw", Imu, output.icm20948_raw)
    rospy.Subscriber("icm20948/mag", MagneticField, output.icm20948_mag)
    
    
    
    rospy.spin()

if __name__ == '__main__':
	listener()

