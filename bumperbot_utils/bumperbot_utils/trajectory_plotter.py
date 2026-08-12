import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from nav_msgs.msg import Path



class TrajectoryPlotter(Node):
    def __init__(self):
        super().__init__("trajectory_plotter")

        self.odom_sub_ = self.create_subscription(Odometry, "bumperbot_controller/odom", self.odomCallback, 10)
        self.path_pub_ = self.create_publisher(Path, "bumperbot_controller/trajectory", 10)

        self.path_msg_ = Path()

    def odomCallback(self, msg):
        self.path_msg_.header = msg.header

        pose_stamped = PoseStamped()
        pose_stamped.header = msg.header
        pose_stamped.pose = msg.pose.pose

        self.path_msg_.poses.append(pose_stamped)

        self.path_pub_.publish(self.path_msg_)


def main():
    rclpy.init()
    draw_trajectory = TrajectoryPlotter()
    rclpy.spin(draw_trajectory)
    draw_trajectory.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()