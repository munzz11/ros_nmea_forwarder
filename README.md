# ROS_NMEA_Forwarder

## Overview

This NMEA forwarding node is a ROS 1 node that reads either raw NMEA data or NavSatFix msgs from a specified ROS topic and forwards it to a specified IP address and port via UDP. 
## Dependencies

This node requires the following dependencies:

- ROS 1
- Python 3

## Building and Running

To build and run follow these steps:

1. Clone the `ros_nmea_forwarder` package to your ROS workspace:

```
cd ~/catkin_ws/src
git clone https://github.com/munzz11/ros_nmea_forwarder.git
```

2. Build the package using `catkin_make`:

```
cd ~/catkin_ws
catkin_make
```

3. Launch the node in raw NMEA mode using the example ROS launch file. For example:

```
roslaunch ros_nmea_forwarder example.launch
```

This launch file will launch the GPS NMEA Forwarder Node and set the IP address to `localhost`, the port to `27002`, and the ROS topic to ``/pos/gps_driver/raw_nmea. You can modify these parameters to suit your specific use case.

## Parameters

The following parameters can be set:

- `ip_address` (default: `localhost`): The IP address to forward NMEA data to
- `port` (default: `27002`): The port number to use for the UDP connection
- `topic_name` (default: `/gps/nmea_data`): The name of the ROS topic to read NMEA data from

## Troubleshooting

If you encounter any issues:

- Check that the IP address and port number are correct and reachable from the target device or application.
- Ensure that the NMEA data is being published to the specified ROS topic.
- Check that the UDP port is not being blocked by a firewall or other measures.
