#!/usr/bin/env python3


import rospy

import tf2_ros

from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry


def callback(data):
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "odom"
    t.child_frame_id = "base_link"
    t.transform.translation.x = data.pose.pose.position.x
    t.transform.translation.y = data.pose.pose.position.y
    t.transform.translation.z = data.pose.pose.position.z

    t.transform.rotation.x = data.pose.pose.orientation.x
    t.transform.rotation.y = data.pose.pose.orientation.y
    t.transform.rotation.z = data.pose.pose.orientation.z
    t.transform.rotation.w = data.pose.pose.orientation.w

    br.sendTransform(t)

def main():

    # initialize a node by the name 'listener'.
    # you may choose to name it however you like,
    # since you don't have to use it ahead
    rospy.init_node('fake_tf', anonymous=True)
    rospy.Subscriber("/ground_truth/state", Odometry, callback)

    # spin() simply keeps python from
    # exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    # you could name this function
    try:
        main()
    except rospy.ROSInterruptException:
        pass