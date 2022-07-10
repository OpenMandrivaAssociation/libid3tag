%define major 0
%define libname %mklibname id3tag %{major}
%define devname %mklibname id3tag -d

Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Name:		libid3tag
Version:	0.16.2
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://github.com/tenacityteam/libid3tag
Source0:	https://github.com/tenacityteam/libid3tag/archive/refs/tags/%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(zlib)

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
%dir %{_libdir}/cmake/id3tag
%{_libdir}/cmake/id3tag/*.cmake

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install -C build
