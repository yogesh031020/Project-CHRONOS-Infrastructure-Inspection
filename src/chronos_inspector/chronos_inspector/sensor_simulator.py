import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import random

class ChronosSensorSim(Node):
    def __init__(self):
        super().__init__('sensor_simulator')
        self.pub = self.create_publisher(LaserScan, '/scan', 10)
        self.timer = self.create_timer(0.1, self.publish)
    def publish(self):
        scan = LaserScan()
        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = 'base_link'
        scan.angle_min = 0.0
        scan.angle_max = 2 * math.pi
        scan.angle_increment = math.pi / 180.0
        scan.ranges = [2.0 + random.uniform(-0.05, 0.05) for _ in range(360)]
        self.pub.publish(scan)
def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(ChronosSensorSim())
    rclpy.shutdown()
if __name__ == '__main__':
    main()
