#!/usr/bin/env python

import rospy
import socket
from std_msgs.msg import String

def nmea_forwarder():
    rospy.init_node('nmea_forwarder', anonymous=True)

    # UDP socket initialization
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Getting IP address and port from the parameter server
    ip_address = rospy.get_param('~ip_address')
    port = rospy.get_param('~port')

    # Setting up the subscriber to the NMEA topic
    topic_name = rospy.get_param('~topic_name')
    rospy.Subscriber(topic_name, String, lambda msg: udp_sock.sendto(msg.data.encode(), (ip_address, port)))
    rospy.spin()

if __name__ == '__main__':
    try:
        nmea_forwarder()
    except rospy.ROSInterruptException:
        pass

