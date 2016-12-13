Name:           ros-kinetic-mrpt-tutorials
Version:        0.1.16
Release:        0%{?dist}
Summary:        ROS mrpt_tutorials package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-teleop-twist-keyboard
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin

%description
The mrpt_tutorials package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Dec 13 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.16-0
- Autogenerated by Bloom

* Sun Nov 06 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.15-0
- Autogenerated by Bloom

* Mon Sep 12 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.14-0
- Autogenerated by Bloom

* Sat Sep 03 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.13-0
- Autogenerated by Bloom

* Sun Aug 21 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.11-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.10-0
- Autogenerated by Bloom

* Wed Jun 29 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.8-0
- Autogenerated by Bloom

* Mon Jun 20 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.7-0
- Autogenerated by Bloom

