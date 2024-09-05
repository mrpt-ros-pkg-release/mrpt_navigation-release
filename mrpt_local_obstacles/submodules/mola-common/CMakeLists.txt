# ------------------------------------------------------------------------------
#        A Modular Optimization framework for Localization and mApping
#                               (MOLA)
#
# Copyright (C) 2018-2021, Jose Luis Blanco-Claraco, contributors (AUTHORS.md)
# All rights reserved.
# Released under GNU GPL v3. See LICENSE file
# ------------------------------------------------------------------------------

# Minimum CMake vesion: limited by CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS
cmake_minimum_required(VERSION 3.4)

project(mola-common)

# Instrumental lib:
add_library(${PROJECT_NAME} INTERFACE)

# Project version:
include(mola-version.cmake)

# Generate: mola-common-version.cmake
include(CMakePackageConfigHelpers)

if(NOT ${CMAKE_VERSION} VERSION_LESS "3.14.0")
	set(ARCH_INDEP_FLAG "ARCH_INDEPENDENT")
endif()

write_basic_package_version_file(
	# generate to the topmost root binary dir:
	${CMAKE_BINARY_DIR}/mola-common-version.cmake
  	VERSION ${MOLA_VERSION_NUMBER_MAJOR}.${MOLA_VERSION_NUMBER_MINOR}.${MOLA_VERSION_NUMBER_PATCH}
  	COMPATIBILITY AnyNewerVersion
  	${ARCH_INDEP_FLAG}
)

# Generate: mola-common.cmake
configure_file(
	# Input:
	mola-common-config.cmake.in
	# Output: generate to the topmost root binary dir:
	${CMAKE_BINARY_DIR}/mola-common-config.cmake
	# Parse: "@var_names@" only
	@ONLY
)

# Allow build-time finding of this package:
set(mola-common_DIR ${CMAKE_CURRENT_SOURCE_DIR} CACHE PATH "Path to mola-common")

# Install files:
# TODO

# Provide make uninstall:
if (NOT TARGET uninstall)
  configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake_uninstall.cmake.in"
    "${CMAKE_BINARY_DIR}/cmake_uninstall.cmake"
    IMMEDIATE @ONLY)
  add_custom_target(uninstall
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_BINARY_DIR}/cmake_uninstall.cmake)
endif()
