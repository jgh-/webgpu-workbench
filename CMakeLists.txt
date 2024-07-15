
cmake_minimum_required(VERSION 3.30)
project(webgpu-workbench)
find_package(CUDAToolkit)
set(CMAKE_CXX_STANDARD 20)
# WIP...
#include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/dawn.cmake")
include("${CMAKE_CURRENT_SOURCE_DIR}/third_party/lib/cmake/Dawn/DawnConfig.cmake")
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/gpudoth.cmake")
add_subdirectory(src)
add_subdirectory(bin)