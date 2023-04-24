
from ament_index_python import get_package_share_directory
from ament_index_python.packages import get_package_share_path
import launch
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
import os
from launch.launch_description_sources import PythonLaunchDescriptionSource
def generate_launch_description():
    return launch.LaunchDescription([
        DeclareLaunchArgument('manipulator_type', default_value='True'),
        IncludeLaunchDescription(
            str(get_package_share_path('urdf_joint') / 'launch/cartesian.launch.py'),
            condition=IfCondition(LaunchConfiguration('manipulator_type')),
        ),
        IncludeLaunchDescription(
            str(get_package_share_path('urdf_joint') / 'launch/3r_manipulator.launch.py'),
            condition=UnlessCondition(LaunchConfiguration('manipulator_type')),
        ),
    ])

   