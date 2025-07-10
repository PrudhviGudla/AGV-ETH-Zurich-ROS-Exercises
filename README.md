# ETH-Zurich-Exercises

A step-by-step tutorial for setting up and running the ETH Zurich ROS exercises, including troubleshooting and visualization tips.

## Exercise 1: Setting Up the Simulation

### 1. Download and Extract Exercise Files

- Download the zip file for Exercise 1 from the [official website](https://rsl.ethz.ch/education-students/lectures/ros.html).
- Extract the `smb_common` directory into your Git folder.

### 2. Reference Repository for Teleop

- Use a reference GitHub repository for the teleop file and troubleshooting. The provided README files in the zip may be insufficient, and you may encounter errors running the simulation launch file due to missing plugins.

<div align="center">
  <img src="https://user-images.githubusercontent.com/106007058/185797804-efcc508d-8172-4d73-bbf3-dc70ad7a471f.png" width="600"/>
</div>

### 3. Create a Catkin Workspace
```
sudo apt-get install python3-catkin-tools
mkdir -p zurich/src
cd ~/zurich
catkin build
```

### 4. Install Required Plugins and Dependencies

Replace `<distro>` with your ROS distribution (e.g., `melodic` or `noetic`):
```
sudo apt install -y ros-<distro>-hector-gazebo-plugins
ros-<distro>-velodyne
ros-<distro>-velodyne-description
ros-<distro>-velodyne-gazebo-plugins
ros-<distro>-pointcloud-to-laserscan
ros-<distro>-twist-mux
```

### 5. Build the Workspace
```
catkin build
```

### 6. Link and Build Packages

- Use symbolic links to add packages from your Git folder to the workspace, then build:
```
ln -s ~/git/smb_common/smb_gazebo/ ~/zurich/src/
catkin build smb_gazebo
```

- Repeat for the other two packages as needed.

<div align="center">
  <img src="https://user-images.githubusercontent.com/106007058/185797139-fb71766b-0c56-4bd7-8c29-ea3da9a58a13.png" width="350"/>
  <img src="https://user-images.githubusercontent.com/106007058/185797184-160c7756-1b34-4ee3-9a46-81d8542732f2.png" width="350"/>
</div>

### 7. Create and Build a New Package

- Create a package named `exer1` and build it.

### 8. Add Teleop Script

- Create a `scripts` folder in `exer1` and add `teleop_twist_keyboard.py` (copy code from the reference repo).
- Make it executable:

```
chmod +x teleop_twist_keyboard.py
```

- In your `CMakeLists.txt`, add:

```
catkin_install_python(PROGRAMS scripts/teleop_twist_keyboard.py
DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

### 9. Launch the Simulation

```
roslaunch smb_gazebo smb_gazebo.launch
```

### 10. Run the Teleop Node
```
rosrun exer1 teleop_twist_keyboard.py
```

<div align="center">
  <img src="https://user-images.githubusercontent.com/106007058/185797607-63b61223-7e58-440b-84ab-f3ae2f44648b.png" width="350"/>
  <img src="https://user-images.githubusercontent.com/106007058/185797648-0f0c27bd-d605-4d1a-bad4-29a4b2360088.png" width="350"/>
  <img src="https://user-images.githubusercontent.com/106007058/185797628-84a263e9-5488-48a5-b874-8d01c6861f2b.png" width="350"/>
</div>

### Common Errors

- When running the teleop file, ensure you update the script to match the package name where it's placed.

<div align="center">
  <img src="https://user-images.githubusercontent.com/106007058/185798185-d1128b2d-8784-4a18-ae19-4642ce52cf6a.png" width="500"/>
</div>

### 11. Modify the World File

- Change the world file in your launch file as needed.

<div align="center">
  <img src="https://user-images.githubusercontent.com/106007058/185801334-9bfd43f2-5286-417f-b790-9988e34c4bba.png" width="350"/>
  <img src="https://user-images.githubusercontent.com/106007058/185801349-ffa64c3d-04b7-4fa1-b473-bcd0f27b6774.png" width="350"/>
</div>

### 12. Visualize Node Graph

- Use `rqt_graph` to visualize the node connections.

<div align="center">
  <img src="https://user-images.githubusercontent.com/106007058/185801450-50475eca-ca65-4a8c-8848-14de24caca85.png" width="600"/>
</div>

---

## Exercise 2: Working with Sensors and Visualization

### 1. Prepare the Package

- Download the zip file and move the package into the same workspace.
- Create `scripts`, `config`, and `launch` folders in the `smb_highlevel_controller` package.

### 2. Subscribe to LaserScan Topic

- Check `/scan` topic info and write a node subscribing to it (`sensor_msgs/LaserScan`).

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/c8e465fb-c1c0-4f01-902e-f27cff9535ca" width="350"/>
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/9fc44349-9d48-40b0-aeac-1fed582cda7c" width="350"/>
</div>

### 3. Create Launch and Config Files

- Create a launch file to start the subscriber node.
- Make a `config.yaml` file with the topic name and queue size in the `config` folder.

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/699f8da2-dcf5-4ba0-bd98-b8751cb20709" width="350"/>
</div>

### 4. Load Parameters and Access in Code

- Load the parameter server using the launch file.

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/a2024192-398e-4c01-9c05-ef6f4205b41a" width="350"/>
</div>

- Access parameters using `rospy.get_param()`:

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/69f63ff6-d123-4c7a-aa0f-224528128e1a" width="350"/>
</div>

### 5. Process LaserScan Data

- Check the message type of LaserScan, access the `ranges`, and find the minimum value.

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/9a848627-35f3-4040-a88f-471c906809a3" width="350"/>
</div>

### 6. Visualize in RViz

- In RViz, add the following:
  - **Global Options:** Fixed Frame: `odom`
  - **PointCloud2:** Topic: `/rslidar_points`, Size: 0.05
  - **LaserScan:** Topic: `/scan`, Size: 0.05
  - Add **TF** and **RobotModel** as well.

- Save the RViz configuration as `default.rviz` inside an `rviz` folder in your package.
- Add the RViz launch command to your launch file.

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/764addad-bb72-4315-9c2a-119fc908256b" width="350"/>
</div>

- Example results:

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/0b254c48-7c9d-4ab3-92a8-f33afa8ded6f" width="350"/>
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/f307801b-a9b6-4660-a0da-efb86dc587ad" width="350"/>
</div>

### 7. Advanced: PointCloud Subscriber

- Write a subscriber node for `rslidar_points` to print the number of points, and launch it via another launch file.

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/18811518-9f1a-44a0-8fc3-12a6cbc93e6e" width="350"/>
</div>

### 8. Launch File Chaining

- You can launch one launch file from another and pass arguments—useful for large projects.

<div align="center">
  <img src="https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/6dc12eb3-0249-4c14-8d72-1acc77c99c42" width="350"/>
</div>

---

## Helpful Resources

- [Reading LaserScan Data](https://www.theconstructsim.com/read-laserscan-data/)
- [YAML Format for rosparam](https://roboticsbackend.com/ros-param-yaml-format/)
- [Saving & Launching RViz Config](https://www.theconstructsim.com/gazebo-in-5-minutes-010-how-to-launch-rviz-using-a-configuration-file/)
- [Showing Laser Data on RViz](https://www.theconstructsim.com/ros-qa-122-how-to-show-laser-data-on-rviz/)
- [Launching a Launch File from Another](https://www.theconstructsim.com/ros-5-mins-017-include-launch-file-inside-launch-file/)
- [roslaunch/XML/include](https://wiki.ros.org/roslaunch/XML/include)
