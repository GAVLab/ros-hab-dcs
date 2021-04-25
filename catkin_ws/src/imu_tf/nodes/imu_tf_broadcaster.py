#!/usr/bin/env python3
import roslib
import rospy
from sensor_msgs.msg import Imu
import tf

xoffset = 0.0
yoffset = 0.0
zoffset = 0.0

def handle_imu_pose(msg, imuname):
    br = tf.TransformBroadcaster()
    br.sendTransform((xoffset,yoffset,zoffset),
                    (msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w),
                     rospy.Time.now(),
                     imuname,
                     "map")

if __name__ == '__main__':
    rospy.init_node('imu_tf_broadcaster')
    imuname = rospy.get_param('~imu')
    xoffset = rospy.get_param('~xoffset')
    yoffset = rospy.get_param('~yoffset')
    zoffset = rospy.get_param('~zoffset')
    rospy.Subscriber('/%s/data' % imuname,
                     Imu,
                     handle_imu_pose,
                     imuname)
    rospy.spin()
