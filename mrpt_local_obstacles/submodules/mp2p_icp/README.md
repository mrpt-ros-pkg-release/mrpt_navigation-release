[![CircleCI](https://img.shields.io/circleci/build/gh/MOLAorg/mp2p_icp/master.svg)](https://circleci.com/gh/MOLAorg/mp2p_icp) [![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.mola-slam.org/latest/module-mp2p-icp.html)


# `mp2p_icp`
A repertory of multi primitive-to-primitive (MP2P) ICP algorithms in C++. 

License: New BSD 3-Clause

Docs:
- [Main library documentation](https://docs.mola-slam.org/latest/module-mp2p-icp.html)
- [C++ API reference](https://docs.mola-slam.org/latest/group_mp2p_icp_grp.html)

The OLAE-ICP method is described in [this technical report](https://arxiv.org/abs/1906.10783):

```
Jose-Luis Blanco-Claraco. "OLAE-ICP: Robust and fast alignment of geometric
features with the optimal linear attitude estimator", Arxiv 2019.
```

![mp2p_pairings](docs/mp2p_pairings.png)

## Introduction

This library provides:
 * [`mp2p_icp::pointcloud_t`](https://docs.mola-slam.org/latest/): A generic
   data type to store raw or processed point clouds, e.g. segmented, discrete
   extracted features. Note that filtering point clouds is intentionally left
   outside of the scope of this library.
   See [MOLA](https://github.com/MOLAorg/mola) for possible implementations.
 * [`mp2p_icp::ICP_Base`](https://docs.mola-slam.org/latest/): A uniform API
   for matching those generic point clouds.
 * Implementations/wrappers of different ICP algorithms under such uniform API.
 * The library exposes both, complete iterative ICP algorithms, and the
 underlying optimal transformation estimators which are run at each ICP iteration.

## Implemented Optimal Transformation methods
 * `optimal_tf_olae()`: A novel algorithm that can recover the optimal attitude from a set
    of point-to-point, line-to-line, and plane-to-plane pairings.
 * `optimal_tf_horn()`: Classic Horn's closed-form optimal quaternion solution.
    Relies on the implementation in [`<mrpt/tfest/se3.h>`](http://mrpt.ual.es/reference/devel/group__mrpt__tfest__grp.html).
 * `optimal_gauss_newton()`: Simple non-linear optimizer to find the SE(3)
    optimal transformation for these pairings: point-to-point, point-to-plane.

## Implemented ICP methods

 * `ICP_OLAE`: ICP for point clouds, planes, and lines. Uses `optimal_tf_olae()`.
 * `ICP_Horn_MultiCloud`: Align point clouds layers, using classic Horn's
    closed-form optimal quaternion solution.

## Building

### Requisites
 * A C++17 compiler. Tested with gcc-7, MSVC 2017.
 * Eigen3
 * CMake >= 3.4
 * MRPT >=2.4.0

Install all the dependencies in Ubuntu with:

```
# MRPT >=2.4.0, for now from this PPA (or build from sources if preferred):
sudo add-apt-repository ppa:joseluisblancoc/mrpt
sudo apt update
sudo apt install libmrpt-dev

# Rest of dependencies:
sudo apt install build-essential cmake libeigen3-dev
```

### Build

```
cmake -H. -Bbuild
cd build
cmake --build .   # or make
```

### Run the tests

```
make test
```

### Run the demos

```bash
# 2D icp with point-to-point pairings only:
build/bin/mp2p-icp-run \
  --input-local demos/local_001.mm \
  --input-global demos/global_001.mm \
  -c demos/icp-settings-2d-lidar-example-point2point.yaml \
  --generate-debug-log

# Inspect the debug log:
build/bin/mp2p-icp-log-viewer
```

```bash
# 2D icp with point-to-line pairings:
build/bin/mp2p-icp-run \
  --input-local demos/local_001.mm \
  --input-global demos/global_001.mm \
  -c demos/icp-settings-2d-lidar-example-point2line.yaml \
  --generate-debug-log

# Inspect the debug log:
build/bin/mp2p-icp-log-viewer
```


```bash
# 3D icp with external library wrapper
build/bin/mp2p-icp-run \
  --input-local demos/local_001.mm \
  --input-global demos/global_001.mm \
  -c demos/icp-settings-example-libpointmatcher.yaml \
  --generate-debug-log

# Inspect the debug log:
build/bin/mp2p-icp-log-viewer
```

