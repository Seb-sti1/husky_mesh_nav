# Husky Mesh navigation

This package is a working simulation of [mesh navigation](https://github.com/uos/mesh_navigation) which uses [move_base_flex](https://github.com/magazino/move_base_flex) for husky.

## Map and files in this repo

The map is from the [repo of the pluto robot](https://github.com/uos/pluto_robot) and most of the files in this repo are from one of those four repos :

- [pluto robot](https://github.com/uos/pluto_robot) : the maps and the mesh_navigation yaml config
- [mesh navigation](https://github.com/uos/mesh_navigation)
- [move_base_flex](https://github.com/magazino/move_base_flex)
- [turtlebot3_mbf](https://github.com/Rayman/turtlebot3_mbf) : the idea and the launch file for the simulation

## Installation

git-lfs: `sudo apt install git-lfs`

Husky simulation: `git clone https://github.com/husky/husky noetic-devel`
`git clone https://github.com/husky/husky_robot noetic-devel` **or any modified version of the husky packages**

move_base_flex: `sudo apt install ros-noetic-move-base-flex`

mesh_navigation: `sudo apt install ros-noetic-mesh-navigation ros-noetic-rviz-map-plugin`

It uses git lfs to store binary files.

## Simulation

Start simulation: `roslaunch husky_mesh_nav sim.launch`

Start mesh nav server: `roslaunch husky_mesh_nav move_base_flex.launch`

To start the navigation you should publish on topic `/move_base_flex/move_base/goal` _(for some reason the topic used on the pluto robot repo is `/move_base_flex/get_path/goal` which only generates the global path but doesn't actually transfer the result to the local planner. Please read the [move_base_action.cpp of move_base_flex](https://github.com/magazino/move_base_flex/blob/master/mbf_abstract_nav/src/move_base_action.cpp) to understand how the informations are transfered in the navigation stack)_

Also, you can simply do: `roslaunch husky_mesh_nav start_experiment.launch`.

## Graph

```mermaid
graph TD
    A[move_base_simple/goal] --> B(move_base_flex/move_base)
    C(move_base) <--> B
    style A fill:#f5f
    style C fill:#f5f


    F([make_plan])<-->D
    B --> D(move_base_flex/get_path)
    D --> E(move_base_flex/exe_path)
```

Square : topic, rounded corner square : action server, rounded side square : service server

In purple the action/service/topic created by move_base_legacy_relay (pkg mbf_costmap_nav: script/move_base_legacy_relay.py). Others created by mbf_abstract_nav.

<br/>
<br/>
<br/>

Assembled by Sébastien K. for CoHoMa 2023 - U2IS Team.