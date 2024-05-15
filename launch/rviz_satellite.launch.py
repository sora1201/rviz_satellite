import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import LogInfo
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    share_dir = get_package_share_directory('rviz_satellite')

    ld = LaunchDescription()

    rviz_satellite_node = Node(
        package='rviz_satellite',
        executable='publish_demo_data',
        # arguments=['51.424', '5.4943']
        arguments=['34.64788622485221', '135.75892322235143'] # 奈良高専の緯度経度
    )

    tf2_ros_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        # arguments=['--frame-id', 'map', '--child-frame-id', 'gps_sensor']
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'gps_sensor']
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(share_dir, 'rviz', 'demo.rviz')],
        output='screen'
    )

    ld.add_action(rviz_satellite_node)
    ld.add_action(tf2_ros_node)
    ld.add_action(rviz2_node)
    
    return ld