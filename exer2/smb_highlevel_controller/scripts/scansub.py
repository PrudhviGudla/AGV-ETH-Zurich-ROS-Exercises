#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print(f"min of vector ranges: {min(list(msg.ranges))}")

rospy.init_node('scan_values')
topic = rospy.get_param('/scan_values/topic')
qs = rospy.get_param('/scan_values/queue_size')
sub = rospy.Subscriber(topic, LaserScan, callback, queue_size = qs )
rospy.spin()
