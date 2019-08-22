from niryo_one_python_api.niryo_one_api import *
import rospy
import time
rospy.init_node('niryo_one_example_python_api')

n = NiryoOne()

try:
    n.calibrate_auto()
    print "Calibration finished"
    n.activate_learning_mode(False)
    print "Stirring coffee"
    n.move_pose(0.1, 0.15, 0.23, 0.25, 1.551, 0)
    n.change_tool(TOOL_GRIPPER_1_ID)
    n.open_gripper(TOOL_GRIPPER_1_ID, 100)
    n.close_gripper(TOOL_GRIPPER_1_ID, 100)
    for i in range 2:
        n.move_pose(0.13, 0.15, 0.23, 0.25, 1.551, 0)
        n.move_pose(0.13, 0.18, 0.23, 0.25, 1.551, 0)
        n.move_pose(0.1, 0.18, 0.23, 0.25, 1.551, 0)
        n.move_pose(0.1, 0.15, 0.23, 0.25, 1.551, 0)

    n.move_pose(0.1, 0.15, 0.33, 0.25, 1.551, 0)
    n.move_pose(0.1, 0.23, 0.33, 0.25, 1.551, 0)
    n.open_gripper(TOOL_GRIPPER_1_ID, 100)

except NiryoOneException as e:
    print e
    # Handle errors here
