%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kdegraphics-mobipocket
Summary:	KDE graphics mobipocket
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ad21b72ee1b9622cc3d2cd03b466b8a7
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-tools
BuildRequires:	kf5-kio-devel
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
