Name:           ros-indigo-mrpt-bridge
Version:        0.1.14
Release:        0%{?dist}
Summary:        ROS mrpt_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/mrpt_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       mrpt-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-mrpt-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  gtest-devel
BuildRequires:  mrpt-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-mrpt-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

%description
The mrpt_bridge package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Sep 20 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.14-0
- Autogenerated by Bloom

* Sat Sep 03 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.13-0
- Autogenerated by Bloom

* Sun Aug 21 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.11-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.10-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.9-0
- Autogenerated by Bloom

* Wed Jun 29 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.8-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.6-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.5-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.4-0
- Autogenerated by Bloom

* Thu Dec 18 2014 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.3-0
- Autogenerated by Bloom

* Thu Dec 18 2014 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.2-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.1.1-0
- Autogenerated by Bloom

