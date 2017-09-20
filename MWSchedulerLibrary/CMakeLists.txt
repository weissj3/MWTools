project(MWSchedulerLibrary)

cmake_minimum_required(VERSION 2.6)

set(MWSCHEDLIB_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/include" CACHE INTERNAL "libmwschedlib headers")
include_directories(${MWSCHEDLIB_INCLUDE_DIR})


set(MWSchedLib_INCLUDES   include/RunInstance.h
                          include/Scheduler.h
                          include/Util.h)

set(MWSchedLib_SRC        src/RunInstance.cpp
                          src/Scheduler.cpp
                          src/Util.cpp)

add_library(${PROJECT_NAME} STATIC ${MWSchedLib_INCLUDES} ${MWSchedLib_SRC})

