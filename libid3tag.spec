%define name 	libid3tag
%define version 0.15.1b
%define release %mkrel 6
%define major  	0
%define lib_name %mklibname id3tag %{major}

Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
Source1:	id3tag.pc.bz2
License:	GPL
Group:		Sound
URL:		http://www.underbit.com/products/mad/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	zlib-devel

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.


%package -n %{lib_name}
Summary:        Library for reading and writing ID3v1 and ID3v2 tags
Group:          System/Libraries

%description -n %{lib_name}
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package -n %{lib_name}-devel
Summary:        Development tools for programs which will use the %{name} library
Group:          Development/C
Requires:	%{lib_name} = %{version}
Requires:	zlib-devel
Requires:	pkgconfig
Provides:       %{name}-devel = %{version}-%{release}
Provides:       id3tag-devel = %{version}-%{release}

%description -n %{lib_name}-devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs using the %{name} library.
 
If you are going to develop programs which will use the %{name} library
you should install %{name}-devel.  You'll also need to have the %name
package installed.
 

%prep
%setup -q

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

%post -n %{lib_name} -p /sbin/ldconfig
 
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%_libdir/pkgconfig/*
%{_includedir}/*
