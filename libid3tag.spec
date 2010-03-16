%define name 	libid3tag
%define version 0.15.1b
%define release %mkrel 10
%define major  	0
%define libname %mklibname id3tag %{major}
%define develname %mklibname -d id3tag

Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
Source1:	id3tag.pc.bz2
Patch0:		libid3tag-0.15.1b-gentoo-CVE-2008-2109_fix_overflow.patch
License:	GPLv2+
Group:		Sound
URL:		http://www.underbit.com/products/mad/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	zlib-devel

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.


%package -n %{libname}
Summary:        Library for reading and writing ID3v1 and ID3v2 tags
Group:          System/Libraries

%description -n %{libname}
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package -n %develname
Summary:        Development tools for programs which will use the %{name} library
Group:          Development/C
Requires:	%{libname} = %{version}
Requires:	zlib-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       id3tag-devel = %{version}-%{release}
Obsoletes:      %mklibname -d id3tag 0

%description -n %develname
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.
 
If you are going to develop programs which will use the %{name} library
you should install this.
 

%prep
%setup -q
%patch0 -p0 -b .cve-2008-2109

%build
%define __libtoolize true
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall
# this is an invalid locale dir
rm -rf %buildroot/%{_datadir}/locale/en
%find_lang %{name}
mkdir -p %buildroot/%_libdir/pkgconfig
bzcat %SOURCE1 | sed -e 's,/lib\>,/%{_lib},;s,0.14.2b,%{version},' >%buildroot/%_libdir/pkgconfig/id3tag.pc

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
 
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libid3tag.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%_libdir/pkgconfig/*
%{_includedir}/*
