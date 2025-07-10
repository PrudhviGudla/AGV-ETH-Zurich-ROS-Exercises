# ETH-Zurich-Exercises

A step-by-step tutorial for setting up and running the ETH Zurich ROS exercises, including troubleshooting and visualization tips.

## Exercise 1: Setting Up the Simulation

### 1. Download and Extract Exercise Files

- Download the zip file for Exercise 1 from the [official website](https://rsl.ethz.ch/education-students/lectures/ros.html).
- Extract the `smb_common` directory into your Git folder.

### 2. Reference Repository for Teleop

- Use a reference GitHub repository for the teleop file and troubleshooting. The provided README files in the zip may be insufficient, and you may encounter errors running the simulation launch file due to missing plugins.

  
    
  

### 3. Create a Catkin Workspace

```bash
sudo apt-get install python3-catkin-tools
mkdir -p zurich/src
cd ~/zurich
catkin build
```

### 4. Install Required Plugins and Dependencies

Replace `` with your ROS distribution (e.g., `melodic` or `noetic`):

```bash
sudo apt install -y ros--hector-gazebo-plugins \
                    ros--velodyne \
                    ros--velodyne-description \
                    ros--velodyne-gazebo-plugins \
                    ros--pointcloud-to-laserscan \
                    ros--twist-mux
```

### 5. Build the Workspace

```bash
catkin build
```

### 6. Link and Build Packages

- Use symbolic links to add packages from your Git folder to the workspace, then build:

```bash
ln -s ~/git/smb_common/smb_gazebo/ ~/zurich/src/
catkin build smb_gazebo
```

- Repeat for the other two packages as needed.

  
    
    
  

### 7. Create and Build a New Package

- Create a package named `exer1` and build it.

### 8. Add Teleop Script

- Create a `scripts` folder in `exer1` and add `teleop_twist_keyboard.py` (copy code from the reference repo).
- Make it executable:

```bash
chmod +x teleop_twist_keyboard.py
```

- In your `CMakeLists.txt`, add:

```cmake
catkin_install_python(PROGRAMS scripts/teleop_twist_keyboard.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

### 9. Launch the Simulation

```bash
roslaunch smb_gazebo smb_gazebo.launch
```

### 10. Run the Teleop Node

```bash
rosrun exer1 teleop_twist_keyboard.py
```

  
    
    
    
  

### Common Errors

- When running the teleop file, ensure you update the script to match the package name where it's placed.

  
    
  

### 11. Modify the World File

- Change the world file in your launch file as needed.

  
    
    
  

### 12. Visualize Node Graph

- Use `rqt_graph` to visualize the node connections.

  
    
  

## Exercise 2: Working with Sensors and Visualization

### 1. Prepare the Package

- Download the zip file and move the package into the same workspace.
- Create `scripts`, `config`, and `launch` folders in the `smb_highlevel_controller` package.

### 2. Subscribe to LaserScan Topic

- Check `/scan` topic info and write a node subscribing to it (`sensor_msgs/LaserScan`).

  
    
    
  

### 3. Create Launch and Config Files

- Create a launch file to start the subscriber node.
- Make a `config.yaml` file with the topic name and queue size in the `config` folder.

  
    
  

### 4. Load Parameters and Access in Code

- Load the parameter server using the launch file.

  
    
  

- Access parameters using `rospy.get_param()`:

  
    
  

### 5. Process LaserScan Data

- Check the message type of LaserScan, access the `ranges`, and find the minimum value.

  
    
  

### 6. Visualize in RViz

- In RViz, add the following:
  - **Global Options:** Fixed Frame: `odom`
  - **PointCloud2:** Topic: `/rslidar_points`, Size: 0.05
  - **LaserScan:** Topic: `/scan`, Size: 0.05
  - Add **TF** and **RobotModel** as well.

- Save the RViz configuration as `default.rviz` inside an `rviz` folder in your package.
- Add the RViz launch command to your launch file.

  
    
  

- Example results:

  
    
    
  

### 7. Advanced: PointCloud Subscriber

- Write a subscriber node for `rslidar_points` to print the number of points, and launch it via another launch file.

  
    
  

### 8. Launch File Chaining

- You can launch one launch file from another and pass arguments—useful for large projects.

  
    
  

## Helpful Resources

- [Reading LaserScan Data](https://www.theconstructsim.com/read-laserscan-data/)
- [YAML Format for rosparam](https://roboticsbackend.com/ros-param-yaml-format/)
- [Saving & Launching RViz Config](https://www.theconstructsim.com/gazebo-in-5-minutes-010-how-to-launch-rviz-using-a-configuration-file/)
- [Showing Laser Data on RViz](https://www.theconstructsim.com/ros-qa-122-how-to-show-laser-data-on-rviz/)
- [Launching a Launch File from Another](https://www.theconstructsim.com/ros-5-mins-017-include-launch-file-inside-launch-file/)
- [roslaunch/XML/include](https://wiki.ros.org/roslaunch/XML/include)

This guide provides a clear, professional, and image-rich walkthrough for the ETH Zurich ROS exercises, ensuring all steps and troubleshooting tips are easy to follow.

[1] https://rsl.ethz.ch/education-students/lectures/ros.html
