# https://docs.google.com/document/d/1I4NJlFwT7iH9Zw-qKS_HBG5cqmMj3UpzS65GQ2tCwNs/edit?tab=t.0

Name:           qtengine
Version:        0.2.2
Release:        1%{?dist}
Summary:        QT Platform Theme made easy.

License:        MIT
URL:            https://github.com/kosslan/qtengine
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules

# Qt5
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kiconthemes-devel

# Qt6
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kiconthemes-devel
Requires:       bash

%description
%{summary}

%prep
%autosetup

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install
# Upstream hardcodes /usr/lib/qt{5,6}/plugins; Fedora's Qt only searches
# /usr/lib64/qt{5,6}/plugins, so move the plugins there.
for qt in qt5 qt6; do
    if [ -d %{buildroot}%{_prefix}/lib/$qt ]; then
        mkdir -p %{buildroot}%{_libdir}
        mv %{buildroot}%{_prefix}/lib/$qt %{buildroot}%{_libdir}/$qt
    fi
done

%files
%{_prefix}/lib/qt6/plugins/platformthemes/libqt6engine-plugin.so
%{_prefix}/lib/qt6/plugins/styles/libqt6engine-style.so
%{_libdir}/libqt6engine-common.so
%{_prefix}/lib/qt5/plugins/platformthemes/libqt5engine-plugin.so
%{_prefix}/lib/qt5/plugins/styles/libqt5engine-style.so
%{_libdir}/libqt5engine-common.so
%license LICENSE
