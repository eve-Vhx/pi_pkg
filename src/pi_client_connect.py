#!/usr/bin/env python
import rospy
from msg_pkg.srv import masterConnect

class PiConnect():

    def __init__(self,name):
        print("Ready to connect to the server")
        result = self.connect_to_server()
        print(result)
    
    def connect_to_server():
        rospy.wait_for_service('pi_connect_master')
        try:
            pi_connect_client = rospy.ServiceProxy('pi_connect_master', masterConnect)
            pi_connect_res = pi_connect_client(1)
            return pi_connect_res.verified





if __name__ == '__main__':
    rospy.init_node("pi_connect_node")
    PiConnect(rospy.get_name())