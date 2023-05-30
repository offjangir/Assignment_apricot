#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *


global marker_array
marker_array = []
def odom_callback(data):
    # rospy.sleep(1)
    pose = data.pose.pose
    marker_pub = rospy.Publisher('path_markers', Marker, queue_size=10)

    marker = Marker()
    marker.header.frame_id = 'map'
    marker.type = Marker.CUBE_LIST
    marker.action = Marker.ADD
    marker.pose.orientation.w = pose.orientation.w
    marker.scale.x = 0.81
    marker.scale.y = 0.51
    marker.scale.z = 0.05
    marker.color.a = 0.8
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    # Add points to the marker message
    point = Point()
    point.x = pose.position.x
    point.y = pose.position.y
    
    marker_array.append(point)
    
    marker.points = marker_array
    # Publish the marker
    marker_pub.publish(marker)




if __name__ == '__main__':
    # Retrieve the list of waypoints from the previous task
    
    rospy.init_node('path_marker_publisher')
    # Publish the path markers
    
    rospy.Subscriber("odom", Odometry, odom_callback)
    rospy.spin()