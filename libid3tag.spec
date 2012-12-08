%define major 0
%define libname %mklibname id3tag %{major}
%define develname %mklibname -d id3tag

Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Name:		libid3tag
Version:	0.15.1b
Release:	15
License:	GPLv2+
Group:		Sound
URL:		http://www.underbit.com/products/mad/
Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
Source1:	id3tag.pc.bz2
Patch0:		libid3tag-0.15.1b-gentoo-CVE-2008-2109_fix_overflow.patch
BuildRequires:	zlib-devel

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package -n %{libname}
Summary:	Library for reading and writing ID3v1 and ID3v2 tags
Group:		System/Libraries

%description -n %{libname}
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package -n %{develname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	zlib-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	id3tag-devel = %{version}-%{release}

%description -n %{develname}
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.

If you are going to develop programs which will use the %{name} library
you should install this.

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

%files -n %{develname}
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-12mdv2011.0
+ Revision: 661473
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-11mdv2011.0
+ Revision: 602558
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-10mdv2010.1
+ Revision: 520868
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.15.1b-9mdv2010.0
+ Revision: 425566
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.15.1b-8mdv2009.0
+ Revision: 264821
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1b-7mdv2009.0
+ Revision: 209308
- P0: security fix for CVE-2008-2109

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1b-6mdv2008.1
+ Revision: 101761
- new devel name
- update license tag

* Wed Sep 19 2007 Antoine Ginies <aginies@mandriva.com> 0.15.1b-6mdv2008.0
+ Revision: 90593
- increase release to rebuild/submit and fix lost in space package...

* Sun Jul 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1b-5mdv2008.0
+ Revision: 46430
- Import libid3tag



* Tue Jun 27 2006 Götz Waschk <waschk@mandriva.org> 0.15.1b-5mdv2007.0
- Rebuild

* Sun Jun 26 2005 Austin Acton <austin@mandriva.org> 0.15.1b-4mdk
- fix provides

* Fri Oct  1 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.15.1b-3mdk
- lib64 fixes to pkgconfig files

* Tue Jun 03 2004 Laurent Montel <waschk@mandrakesoft.com> 0.15.1b-2mdk
- Rebuild

* Mon May 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.15.1b-1mdk
- spec fix
- don't libtoolize
- fix source URL
- New release 0.15.1b

* Wed Jul  9 2003 Götz Waschk <waschk@linux-mandrake.com> 0.15.0b-4mdk
- rebuild for new rpm

* Thu Jun 26 2003 Götz Waschk <waschk@linux-mandrake.com> 0.15.0b-2mdk
- update doc section
- fix pkgconfig file
- update URL

* Thu Jun 26 2003 Götz Waschk <waschk@linux-mandrake.com> 0.15.0b-1mdk
- autoconf2.5 macro
- new version
- split out from the main mad package

* Wed May 21 2003 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-6mdk
- rebuild for provides

* Sun May  4 2003 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-5mdk
- devel package requires zlib-devel
- devel package requires pkgconfig
- mklibname macro

* Mon Oct 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-4mdk
- arrgh, also add mad.pc

* Mon Oct 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-3mdk
- add id3tag.pc from debian package (required by xmms-mad)

* Thu Jul 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.14.2b-2mdk
- add .la files

* Sat Jan 26 2002 Yves Duret <yduret@mandrakesoft.com> 0.14.2b-1mdk
- spec mandrakificazion: macros, standard libificazion, macros

* Sat Nov 10 2001 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-0.1mdk
- 0.14.2b

* Wed Nov  7 2001 Götz Waschk <waschk@linux-mandrake.com> 0.14.1b-0.1mdk
- 0.14.1b
- build shared library

* Fri Oct 19 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.14.0b-0.1mdk
- 0.14.0b

* Mon Sep 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.13.0-0.b1mdk
- added by Götz Waschk <waschk@linux-mandrake.com> :
        - initial package

#EOF
