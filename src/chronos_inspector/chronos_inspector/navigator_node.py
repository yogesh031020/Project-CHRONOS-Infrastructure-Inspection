import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import String, Float32
from nav_msgs.msg import Odometry
import time

class ChronosNavigator(Node):
    def __init__(self):
        super().__init__('navigator_node')
        self.gps_sub = self.create_subscription(NavSatFix, '/gps/data', self.gps_callback, 10)
        self.state_pub = self.create_publisher(String, '/chronos/nav_state', 10)
        self.gps_health = 100.0
        self.current_state = "GPS_NAVIGATION"
        self.timer = self.create_timer(1.0, self.monitor_nav_health)

    def gps_callback(self, msg):
        if msg.position_covariance[0] > 1.0:
            self.gps_health = 0.0
        else:
            self.gps_health = 100.0

    def monitor_nav_health(self):
        msg = String()
        if self.gps_health < 20.0:
            self.current_state = "SLAM_FALLBACK"
            msg.data = "NAV_ALERT: GPS SIGNAL LOST | SWITCHING TO SLAM"
        else:
            self.current_state = "GPS_NAVIGATION"
            msg.data = f"STATUS: {self.current_state} | GPS: {self.gps_health}%"
        self.state_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ChronosNavigator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
