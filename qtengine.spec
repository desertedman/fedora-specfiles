Name:           qtengine
Version:        0.2.2
Release:        1%{?dist}
Summary:        QT Platform Theme made easy.

License:        MIT
URL:            https://github.com/kosslan/qtengine
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kiconthemes-devel
Requires:       bash

%description
%{summary}

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install

%files
%{_prefix}/lib/qt6/plugins/platformthemes/libqt6engine-plugin.so
%{_prefix}/lib/qt6/plugins/styles/libqt6engine-style.so
%{_libdir}/libqt6engine-common.so
%{_prefix}/lib/qt5/plugins/platformthemes/libqt5engine-plugin.so
%{_prefix}/lib/qt5/plugins/styles/libqt5engine-style.so
%{_libdir}/libqt5engine-common.so
%license LICENSE
