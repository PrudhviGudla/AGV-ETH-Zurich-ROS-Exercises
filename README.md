# ETH-Zurich-Exercises

## Exercise 1
1) I first downloaded the zip file given for the exercise 1 from the official website: https://rsl.ethz.ch/education-students/lectures/ros.html
2) I then extracted the zip file: smb_common into the git folder i made.
3) I followed this github repository for reference and teleop file. I needed this repo because there were may errors while I ran the launch file of the simulation as I had to install some plugins and the readme files given in the downloaded zip files were not good.

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

6) ``` bash
catkin build
```
7) then I used symlink to link packages in my git folder to my workspace and built the package.

``` bash
ln -s ~/git/smb_common/smb_gazebo/ ~/zurich/src/
catkin build smb_gazebo
```
similarly for other 2 packages



 
