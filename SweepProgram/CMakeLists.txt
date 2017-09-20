project(SweepProgram)

cmake_minimum_required(VERSION 2.6)

include_directories(${MWSCHEDLIB_INCLUDE_DIR})
set(SWEEPPROGRAM_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/include" CACHE INTERNAL "SweepProgram includes")
include_directories(${SWEEPPROGRAM_INCLUDE_DIR})

set(SWEEPPROGRAM_INCLUDES   include/Sweep.h)

set(SWEEPPROGRAM_SRC        src/main.cpp
                            src/Sweep.cpp)


add_executable(${PROJECT_NAME} ${SWEEPPROGRAM_SRC})

target_link_libraries(${PROJECT_NAME} MWSchedulerLibrary)
