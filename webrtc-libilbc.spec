# NOTE: it's (almost?) API- (but not ABI-) compatible with RFC 3591 libilbc,
#       but it uses single header file; thus only Obsoletes, not Provides
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	iLBC speech codec from the WebRTC project
Summary(pl.UTF-8):	Kodek mowy iLBC z projektu WebRTC
Name:		webrtc-libilbc
Version:	1.1.1
%define	snap	20120913
Release:	0.%{snap}.2
License:	BSD
Group:		Libraries
# git clone git://github.com/dekkers/libilbc.git
Source0:	libilbc.tar.xz
# Source0-md5:	69c52eaa5157921f87fe68ffd7197392
URL:		https://github.com/dekkers/libilbc
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libilbc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the iLBC codec from the WebRTC project. It can
be used as drop-in replacement for the non-free code from RFC 3591.

%description -l pl.UTF-8
Ten pakiet zawiera kodek iLBC z projektu WebRTC. Może być używany jako
zamiennik kodu z RFC 3591, który jest na bardziej restrykcyjnej
licencji.

%package devel
Summary:	Header files for iLBC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki iLBC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libilbc-devel

%description devel
Header files for iLBC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki iLBC.

%package static
Summary:	Static iLBC library
Summary(pl.UTF-8):	Statyczna biblioteka iLBC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libilbc-static

%description static
Static iLBC library.

%description static -l pl.UTF-8
Statyczna biblioteka iLBC.

%prep
%setup -q -n libilbc

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libilbc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libilbc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libilbc.so
%{_libdir}/libilbc.la
%{_includedir}/ilbc.h
%{_pkgconfigdir}/libilbc.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libilbc.a
%endif
