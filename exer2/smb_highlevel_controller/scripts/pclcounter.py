#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2

def counter(msg):
    print(f"number of points in the point cloud {len(msg.data)}")
    
    
def pclcounter():
    rospy.init_node('pclcounter', anonymous=True)
    rospy.Subscriber("rslidar_points", PointCloud2, counter)
    rospy.spin()

if __name__ == '__main__':
    pclcounter()
