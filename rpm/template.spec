Name:           ros-melodic-mrpt-rawlog
Version:        0.1.26
Release:        1%{?dist}
Summary:        ROS mrpt_rawlog package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/mrpt_rawlog
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-marker-msgs
Requires:       ros-melodic-mrpt-bridge
Requires:       ros-melodic-mrpt-msgs
Requires:       ros-melodic-mrpt1
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-marker-msgs
BuildRequires:  ros-melodic-mrpt-bridge
BuildRequires:  ros-melodic-mrpt-msgs
BuildRequires:  ros-melodic-mrpt1
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf

%description
This package enables you to record a rawlog from a ROS drive robot. At the
moment the package is able to deal with odometry and 2d laser scans.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Sun Oct 06 2019 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.26-1
- Autogenerated by Bloom

* Fri Apr 12 2019 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.24-0
- Autogenerated by Bloom

* Tue May 22 2018 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.22-0
- Autogenerated by Bloom

* Mon May 21 2018 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.21-1
- Autogenerated by Bloom

* Mon May 21 2018 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.21-0
- Autogenerated by Bloom

