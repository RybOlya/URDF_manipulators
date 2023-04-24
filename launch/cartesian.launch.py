from launch import LaunchDescription
from launch_ros.actions import Node
import xacro
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

def generate_launch_description():
    # Load xacro file for manipulator 2
    pkg_name = 'urdf_joint' # Replace with your actual package name
    file_subpath = 'description/cartesian.urdf.xacro' # Replace with the file path of your custom xacro file for manipulator 2

    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Configure the node for manipulator 2
    cartesian = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}] # Pass the processed xacro content as a parameter
    )

    return LaunchDescription([cartesian])