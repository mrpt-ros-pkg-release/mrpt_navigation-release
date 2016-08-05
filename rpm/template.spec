Name:           ros-jade-mrpt-tutorials
Version:        0.1.10
Release:        0%{?dist}
Summary:        ROS mrpt_tutorials package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-teleop-twist-keyboard
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin

%description
The mrpt_tutorials package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Aug 05 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.10-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.9-0
- Autogenerated by Bloom

* Wed Jun 29 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.8-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.6-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Markus Bader <markus.bader@tuwien.ac.at> - 0.1.5-0
- Autogenerated by Bloom

