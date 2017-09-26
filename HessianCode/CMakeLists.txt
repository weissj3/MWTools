project(HessianErrors)

cmake_minimum_required(VERSION 2.6)

find_package(Armadillo REQUIRED)
include_directories(${ARMADILLO_INCLUDE_DIRS})

include_directories(${MWSCHEDLIB_INCLUDE_DIR})
set(HESSIANERRORS_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/include" CACHE INTERNAL "HessianErrors includes")
include_directories(${HESSIANERRORS_INCLUDE_DIR})

set(HESSIANERRORS_INCLUDES   include/Hessian.h)

set(HESSIANERRORS_SRC        src/main.cpp
                             src/Hessian.cpp)


add_executable(${PROJECT_NAME} ${HESSIANERRORS_SRC})

target_link_libraries(${PROJECT_NAME} MWSchedulerLibrary
                                      ${ARMADILLO_INCLUDE_DIRS})
