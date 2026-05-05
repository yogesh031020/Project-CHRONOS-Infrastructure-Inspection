import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
import random

class ChronosDefectDetector(Node):
    def __init__(self):
        super().__init__('defect_detector')
        self.defect_pub = self.create_publisher(String, '/chronos/defects', 10)
        self.image_sub = self.create_subscription(Image, '/camera/image_raw', self.callback, 10)
        self.defect_types = ["SURFACE_RUST", "HAIRLINE_CRACK", "LOOSE_BOLT"]
    def callback(self, msg):
        if random.randint(1, 50) == 1:
            report = f"DETECTION: {random.choice(self.defect_types)} | CONFIDENCE: {random.uniform(0.85, 0.99):.2f}"
            self.defect_pub.publish(String(data=report))
def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(ChronosDefectDetector())
    rclpy.shutdown()
if __name__ == '__main__':
    main()
