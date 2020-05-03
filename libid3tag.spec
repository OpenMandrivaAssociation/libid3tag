%define major 0
%define libname %mklibname id3tag %{major}
%define devname %mklibname id3tag -d

Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Name:		libid3tag
Version:	0.15.1b
Release:	22
License:	GPLv2+
Group:		Sound
Url:		http://www.underbit.com/products/mad/
Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
Source1:	id3tag.pc.bz2
Patch0:         libid3tag-0.15.1b-fix_overflow.patch
Patch1:         libid3tag-0.15.1b-id3v1-zero-padding.patch
Patch2:         libid3tag-0.15.1b-handle-unknown-encoding.patch
Patch3:         libid3tag-0.15.1b-id3v2-endless-loop.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=869598
Patch4:         libid3tag-0.15.1b-gperf-size_t.patch
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gperf

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Group:		System/Libraries

%description -n %{libname}
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%files -n %{libname}
%doc COPYING
%{_libdir}/libid3tag.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(zlib)
Provides:	%{name}-devel = %{EVRD}
Provides:	id3tag-devel = %{EVRD}

%description -n %{devname}
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.

If you are going to develop programs which will use the %{name} library
you should install this.

%files -n %{devname}
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .CVE-2008-2109
%patch1 -p1 -b .zero-padding
%patch2 -p1 -b .unknown-encoding
%patch3 -p0 -b .endless-loop
%patch4 -p1 -b .gperf

# Force these files to be regenerated from the .gperf sources.
rm compat.c frametype.c

%build
%configure --disable-static
%make_build

%install
%make_install
# this is an invalid locale dir
rm -rf %{buildroot}/%{_datadir}/locale/en

mkdir -p %{buildroot}%{_libdir}/pkgconfig
bzcat %{SOURCE1} | sed -e 's,/lib\>,/%{_lib},;s,0.14.2b,%{version},' >%{buildroot}%{_libdir}/pkgconfig/id3tag.pc
