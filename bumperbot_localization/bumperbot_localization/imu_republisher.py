#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time
from sensor_msgs.msg import Imu

imu_pub = None

def imuCallback(imu):
    global imu_pub
    imu.header.frame_id = "base_footprint_ekf"
    imu_pub.publish(imu)

def main():
    global imu_pub

    rclpy.init()
    node = Node("imu_republisher")
    time.sleep(1)

    imu_pub = node.create_publisher(Imu, "imu_ekf", 10)
    imu_sub = node.create_subscription(imu, "imu/out", imuCallback, 10)

    rclpy.spin(Node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()