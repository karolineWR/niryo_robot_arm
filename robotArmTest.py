#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
import time
rospy.init_node('niryo_one_example_python_api')

n = NiryoOne()

try:
    n.calibrate_auto()
    print "Calibration finished"
    n.activate_learning_mode(False)
    n.change_tool(TOOL_GRIPPER_1_ID)
    n.close_gripper(TOOL_GRIPPER_1_ID, 100)
    time.sleep(2)
    n.open_gripper(TOOL_GRIPPER_1_ID, 100)


except NiryoOneException as e:
    print e
    # Handle errors here
