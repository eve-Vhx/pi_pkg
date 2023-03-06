#!/usr/bin/env python3
import rospy
from msg_pkg.srv import masterConnect

class PiConnect:

    def __init__(self):
        rospy.init_node("pi_connect_node")
        print("Ready to connect to the server")
        result = self.connect_to_server()
        print(result)
    
    def connect_to_server(self):
        rospy.wait_for_service('nest_pi_connect_master')
        try:
            pi_connect_client = rospy.ServiceProxy('nest_pi_connect_master', masterConnect)
            pi_connect_res = pi_connect_client('NEST11014')
            return pi_connect_res.verified
        except rospy.ServiceException as e:
            print("Connection to server failed")
            return False


if __name__ == '__main__':
    PiConnect()
    rospy.spin()