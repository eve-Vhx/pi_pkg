#!/usr/bin/env python3
import rospy
from msg_pkg.srv import masterConnect
from msg_pkg.msg import uiMasterList

class PiConnectNest:

    def __init__(self):
        rospy.init_node("pi_connect_nest_node")
        self.id = 'NEST11014'
        self.master_list = []
        rospy.Subscriber('nest_master_list', uiMasterList, self.master_list_cb)
        self.run_routine()

    def master_list_cb(self,msg):
        self.master_list = msg.ui_master_list

    def run_routine(self):
        while (not rospy.is_shutdown()):
            exists = False
            for id_ in self.master_list:
                if (id_ == self.id):
                    exists = True

            if not exists:
                self.connect_to_server()

            rospy.sleep(5)
    
    def connect_to_server(self):
        rospy.wait_for_service('nest_pi_connect_master', timeout=rospy.Duration(3))
        try:
            pi_connect_client = rospy.ServiceProxy('nest_pi_connect_master', masterConnect)
            pi_connect_res = pi_connect_client(self.id)
            return pi_connect_res.verified
        except rospy.ServiceException as e:
            print("Connection to server failed")
            return False


if __name__ == '__main__':
    PiConnectNest()
    rospy.spin()