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









 
