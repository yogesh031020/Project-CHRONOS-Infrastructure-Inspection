import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
from cv_bridge import CvBridge

class ChronosCameraSim(Node):
    def __init__(self):
        super().__init__('camera_simulator')
        self.pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.timer = self.create_timer(0.1, self.publish)
        self.bridge = CvBridge()
    def publish(self):
        image = np.full((480, 640, 3), 128, dtype=np.uint8)
        msg = self.bridge.cv2_to_imgmsg(image, encoding="bgr8")
        self.pub.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(ChronosCameraSim())
    rclpy.shutdown()
if __name__ == '__main__':
    main()
