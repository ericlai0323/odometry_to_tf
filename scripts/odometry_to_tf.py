#!/usr/bin/env python3

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

def odometry_callback(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z),
                     (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w),
                     rospy.Time.now(),
                     "base_link",
                     "odom")

def listener():
    rospy.init_node('odometry_to_tf', anonymous=True)

    # Get topic parameter, default to "/vins_estimator/odometry" if not specified
    topic = rospy.get_param('~topic', '/vins_estimator/odometry')
    rospy.Subscriber(topic, Odometry, odometry_callback)
    rospy.loginfo(f"Subscribing to topic: {topic}")

    rospy.spin()

if __name__ == '__main__':
    listener()
