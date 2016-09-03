Name:           ros-indigo-mrpt-navigation
Version:        0.1.13
Release:        0%{?dist}
Summary:        ROS mrpt_navigation package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/mrpt_navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-mrpt-bridge
Requires:       ros-indigo-mrpt-local-obstacles
Requires:       ros-indigo-mrpt-localization
Requires:       ros-indigo-mrpt-map
Requires:       ros-indigo-mrpt-msgs
Requires:       ros-indigo-mrpt-rawlog
Requires:       ros-indigo-mrpt-reactivenav2d
Requires:       ros-indigo-mrpt-tutorials
BuildRequires:  ros-indigo-catkin

%description
Tools related to the Mobile Robot Programming Toolkit (MRPT). Refer to
http://wiki.ros.org/mrpt_navigation for further documentation.

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

