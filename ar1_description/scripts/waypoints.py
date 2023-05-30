#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

def send(waypoints):
    # Initialize the ROS node
    rospy.init_node('navigation_client')

    # Create the action client for the move_base action
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    for waypoint in waypoints:
        # Create a goal message
        goal = MoveBaseGoal()

        # Set the pose for the goal
        goal.target_pose.pose = Pose(Point(waypoint[0], waypoint[1], 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()

        # Send the goal
        rospy.loginfo("Sending goal: {}".format(waypoint))
        client.send_goal(goal)

        # Wait for the result
        client.wait_for_result()

    rospy.loginfo("Navigation complete!")
    rospy.signal_shutdown("Navigation complete")

if __name__ == '__main__':

    waypoints = []
    num_waypoints = int(input("Enter the number of waypoints: "))

    for i in range(num_waypoints):
        x = float(input("Enter x-coordinate for waypoint {}: ".format(i+1)))
        y = float(input("Enter y-coordinate for waypoint {}: ".format(i+1)))
        waypoints.append((x, y))

    send(waypoints)
