%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kdegraphics-mobipocket
Summary:	KDE graphics mobipocket
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7ef350c644ffeafe7f52710f30c6bbce
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-tools
BuildRequires:	kf5-kio-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to support mobipocket ebooks.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libqmobipocket.so.2
%attr(755,root,root) %{_libdir}/libqmobipocket.so.2.0.0
%attr(755,root,root) %{_libdir}/qt5/plugins/mobithumbnail.so
%{_datadir}/kservices5/mobithumbnail.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/qmobipocket
%{_libdir}/cmake/QMobipocket
%attr(755,root,root) %{_libdir}/libqmobipocket.so
