# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target bumperbot_msgs::bumperbot_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${bumperbot_msgs_TARGETS}.
if(bumperbot_msgs_TARGETS AND NOT TARGET bumperbot_msgs::bumperbot_msgs)
  add_library(bumperbot_msgs::bumperbot_msgs INTERFACE IMPORTED)
  set_target_properties(bumperbot_msgs::bumperbot_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${bumperbot_msgs_TARGETS}")
endif()
