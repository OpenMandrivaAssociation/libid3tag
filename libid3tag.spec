%define major	0
%define libname %mklibname id3tag %{major}
%define devname %mklibname -d id3tag

%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Name:		libid3tag
Version:	0.15.1b
Release:	29
License:	GPLv2+
Group:		Sound
Url:		http://www.underbit.com/products/mad/
Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
Source1:	id3tag.pc.bz2
Patch0:		libid3tag-0.15.1b-gentoo-CVE-2008-2109_fix_overflow.patch
BuildRequires:	pkgconfig(zlib)

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package -n %{libname}
Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Group:		System/Libraries

%description -n %{libname}
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package -n %{devname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	id3tag-devel = %{version}-%{release}

%description -n %{devname}
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.

%prep
%setup -q
%patch0 -p0 -b .cve-2008-2109

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
# this is an invalid locale dir
rm -rf %{buildroot}/%{_datadir}/locale/en

mkdir -p %{buildroot}%{_libdir}/pkgconfig
bzcat %{SOURCE1} | sed -e 's,/lib\>,/%{_lib},;s,0.14.2b,%{version},' >%{buildroot}%{_libdir}/pkgconfig/id3tag.pc

%files -n %{libname}
%doc COPYING
%{_libdir}/libid3tag.so.%{major}*

%files -n %{devname}
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

