import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os

class ChronosReportGenerator(Node):
    def __init__(self):
        super().__init__('report_generator')
        self.sub = self.create_subscription(String, '/chronos/defects', self.callback, 10)
        self.findings = []
    def callback(self, msg):
        if msg.data not in self.findings:
            self.findings.append(msg.data)
            self.get_logger().info(f'RECORDED: {msg.data}')
def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(ChronosReportGenerator())
    rclpy.shutdown()
if __name__ == '__main__':
    main()
