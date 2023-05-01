#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
import socket

# Getting IP address and port from the parameter server
ip_address = rospy.get_param('~ip_address')
port = rospy.get_param('~port')


def send_nmea(position):
    # Create NMEA string from position information
    lat = position.latitude
    lat_deg = int(lat)
    lat_min = (lat - lat_deg) * 60
    lat_dir = 'N' if lat > 0 else 'S'
    lon = position.longitude
    lon_deg = int(lon)
    lon_min = (lon - lon_deg) * 60
    lon_dir = 'E' if lon > 0 else 'W'
    nmea_str = f'$GPGGA,{lat_deg:02d}{lat_min:.4f},{lat_dir},{lon_deg:03d}{lon_min:.4f},{lon_dir},1,08,1.0,{position.altitude:.2f},M,,M,,*'

    # Send NMEA string over UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(nmea_str.encode(), (ip_address, port))

def navsatfix_callback(msg):
    # Send NMEA string with position information
    send_nmea(msg)

if __name__ == '__main__':
    rospy.init_node('nmea_publisher')
    rospy.Subscriber('/fix', NavSatFix, navsatfix_callback)
    rospy.spin()

