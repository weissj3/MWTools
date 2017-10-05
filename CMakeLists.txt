project(MWTools)

cmake_minimum_required(VERSION 2.6)
SET(CMAKE_BUILD_TYPE RelWithDebInfo)

set(MWTOOLS_ROOT ${PROJECT_BINARY_DIR})
list(INSERT CMAKE_PREFIX_PATH 0 ${MWTOOLS_ROOT})


# Set output to be in this root
set(EXECUTABLE_OUTPUT_PATH ${MWTOOLS_ROOT}/bin)
set(LIBRARY_OUTPUT_PATH ${MWTOOLS_ROOT}/lib)
set(PROJECT_INCLUDE_DIR ${MWTOOLS_ROOT}/include)

include_directories(${PROJECT_INCLUDE_DIR})
link_directories(${LIBRARY_OUTPUT_PATH})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x -g")

add_subdirectory(MWSchedulerLibrary)
add_subdirectory(SweepProgram)
add_subdirectory(HessianCode)
