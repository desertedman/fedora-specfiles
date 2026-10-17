%global commit      8a6fe8961749887d677700b6508e0c9249968b7e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate    20261016

Name:           m3shapes-git
Version:        0^%{snapdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        A QT port of the androidx shape library

License:        MIT
URL:            https://github.com/soramanew/m3shapes
Source0:        %{url}/archive/%{commit}/m3shapes-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
Requires:       bash

%description
%{summary}

%prep
%autosetup -n m3shapes-%{commit}

%build
%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libm3shapes.so
%{_libdir}/qt6/qml/M3Shapes/
%{_includedir}/m3shapes/
%{_libdir}/cmake/M3Shapes/
%license LICENSE
%doc README.md
