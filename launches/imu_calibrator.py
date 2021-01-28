import rospy
import enum
from std_msgs.msg import String
from diagnostic_msgs.msg import DiagnosticStatus

def status(value):
    if value == 3:
        return "True"
    elif value == 2:
        return "Almost"
    elif value == 1:
        return "Some"
    else:
        return "False"

def callback(data):
    if int(data.values[5].value) == 0: # check if system_error = 0
        binary = format(int(data.values[0].value),'008b')
        sys_status = status(int(binary[0:2],2))
        gyr_status = status(int(binary[2:4],2))
        acc_status = status(int(binary[4:6],2))
        mag_status = status(int(binary[6:8],2))
        imu_status = status(min([int(binary[0:2],2),int(binary[2:4],2),int(binary[4:6],2),int(binary[6:8],2)]))
        rospy.loginfo("Calibrated?: Full IMU("+imu_status+") Sys("+sys_status+") Gyr ("+gyr_status+") Acc("+acc_status+") Mag("+mag_status+")")

def listener():
	rospy.init_node('listener',anonymous=True)
	rospy.Subscriber("bno055_imu/status", DiagnosticStatus, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

