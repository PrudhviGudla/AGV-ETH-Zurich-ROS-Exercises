# ETH-Zurich-Exercises

## Exercise 1
1) I first downloaded the zip file given for the exercise 1 from the official website: https://rsl.ethz.ch/education-students/lectures/ros.html
2) I then extracted the zip file: smb_common into the git folder i made.
3) I followed this github repository for reference and teleop file. I needed this repo because there were may errors while I ran the launch file of the simulation as I had to install some plugins and the readme files given in the downloaded zip files were not good.
![Screenshot (614)](https://user-images.githubusercontent.com/106007058/185797804-efcc508d-8172-4d73-bbf3-dc70ad7a471f.png)


4) Then I created a workspace ' zurich ' with catkin build.
``` bash
sudo apt-get install python3-catkin-tools
mkdir -p zurich/src
cd ~/zurich
catkin build
```

5) Then I downloaded the required plugins/ dependencies
``` bash
sudo apt install -y ros-<distro>-hector-gazebo-plugins \
                    ros-<distro>-velodyne \
                    ros-<distro>-velodyne-description \
                    ros-<distro>-velodyne-gazebo-plugins \
                    ros-<distro>-pointcloud-to-laserscan \
                    ros-<distro>-twist-mux
```
where `<distro>` can be either melodic or noetic.

6) 
``` bash
catkin build
```
7) then I used symlink to link packages in my git folder to my workspace and built the package.

``` bash
ln -s ~/git/smb_common/smb_gazebo/ ~/zurich/src/
catkin build smb_gazebo
```
similarly for other 2 packages
![image](https://user-images.githubusercontent.com/106007058/185797139-fb71766b-0c56-4bd7-8c29-ea3da9a58a13.png)
![image](https://user-images.githubusercontent.com/106007058/185797184-160c7756-1b34-4ee3-9a46-81d8542732f2.png)

8) Then I created another package ' exer1 ' and built it
9) Then I made a folder scripts and made a file : 'teleop_twist_keyboard.py' and copied the code from the repo I mentioned. Then, I made it executable using
```bash
chmod +x teleop_twist_keyboard.py
```
Then, I added these lines in the CMake file of the package
```bash
catkin_install_python(PROGRAMS scripts/teleop_twist_keyboard.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

10) I launched the simulation with 
```bash
roslaunch smb_gazebo smb_gazebo.launch
```
11) I ran the teleop node with
```bash
rosrun exer1 teleop_twist_keyboard.py
```
![Screenshot (616)](https://user-images.githubusercontent.com/106007058/185797607-63b61223-7e58-440b-84ab-f3ae2f44648b.png)
![Screenshot (619)](https://user-images.githubusercontent.com/106007058/185797648-0f0c27bd-d605-4d1a-bad4-29a4b2360088.png)
![Screenshot (618)](https://user-images.githubusercontent.com/106007058/185797628-84a263e9-5488-48a5-b874-8d01c6861f2b.png)

## errors you may face

when u run the teleop file, you will have to make changes in it based on the name of the package in which u created it.
![image](https://user-images.githubusercontent.com/106007058/185798185-d1128b2d-8784-4a18-ae19-4642ce52cf6a.png)

12) Now. I changed the world file in launch file code.
![Screenshot (620)](https://user-images.githubusercontent.com/106007058/185801334-9bfd43f2-5286-417f-b790-9988e34c4bba.png)
![Screenshot (617)](https://user-images.githubusercontent.com/106007058/185801349-ffa64c3d-04b7-4fa1-b473-bcd0f27b6774.png)

13) I used rqt graph to generate this
![Screenshot (615)](https://user-images.githubusercontent.com/106007058/185801450-50475eca-ca65-4a8c-8848-14de24caca85.png)

## Exercise 2

1) download the zip file and move the package into the same workspace. Make scipts, config, launch folders in the smb_highlevel_controller package
2) check the topic info /scan, based on that write a node to subscribe to scan topic, its sensor_msgs/LaserScan, so import it accordingly
![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/c8e465fb-c1c0-4f01-902e-f27cff9535ca)

![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/9fc44349-9d48-40b0-aeac-1fed582cda7c)


4) create a launch file to launch the above subscriber node
5) then make a config.yaml file with the topic name and queue size in config folder

![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/699f8da2-dcf5-4ba0-bd98-b8751cb20709)

6) load the parameter server using the launch file

![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/a2024192-398e-4c01-9c05-ef6f4205b41a)

7) access the params using rospy.get_param()

![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/69f63ff6-d123-4c7a-aa0f-224528128e1a)

8) check the msg type of laserscan and access the ranges and find min value accordingly
![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/9a848627-35f3-4040-a88f-471c906809a3)

9) in rviz, using add option add the following with these params
  in Global Options, Fixed Frame : odom
  in PointCloud2, Topic: /rslidar_points, Size: 0.05
  in LaserScan, Topic: /scan, Size: 0.05
  add TF and RobotModel too

10) save the rviz configuration as default.rviz in a rviz folder inside the package
11) add the rviz launching command in the launch file
![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/764addad-bb72-4315-9c2a-119fc908256b)

12) Now you can visualize the point clouds and the laser scan in rviz like this:
RVIZ
![Screenshot from 2023-09-04 22-50-35](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/0b254c48-7c9d-4ab3-92a8-f33afa8ded6f)
Gazebo
![Screenshot from 2023-09-04 22-51-28](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/f307801b-a9b6-4660-a0da-efb86dc587ad)

13) Now you can write a subscriber node which subscribes to the rslidar_points and prints the number of points and can launch it through another launch file

![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/18811518-9f1a-44a0-8fc3-12a6cbc93e6e)

14) You can launch a launch file from another launch file and pass arguments to it using the below code.(useful for big projects)
![image](https://github.com/PrudhviGudla/AGV-ETH-Zurich-ROS-Exercises/assets/106007058/6dc12eb3-0249-4c14-8d72-1acc77c99c42)


### Some resources:

reading laserscan data
https://www.theconstructsim.com/read-laserscan-data/

yaml fromat for rosparam
https://roboticsbackend.com/ros-param-yaml-format/

saving a rviz configurationa and launching it through launch file
https://www.theconstructsim.com/gazebo-in-5-minutes-010-how-to-launch-rviz-using-a-configuration-file/

showing laser data on rviz
https://www.theconstructsim.com/ros-qa-122-how-to-show-laser-data-on-rviz/

launching a launch file from a launch file
https://www.theconstructsim.com/ros-5-mins-017-include-launch-file-inside-launch-file/
https://answers.ros.org/question/199152/run-launch-file-with-arg-from-launch-file/
https://wiki.ros.org/roslaunch/XML/include












 
