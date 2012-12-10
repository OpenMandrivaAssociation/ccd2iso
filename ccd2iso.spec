%define name ccd2iso
%define version 0.3
%define release %mkrel 5

Summary: CloneCD image to ISO image file converter
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group: Archiving/Cd burning
# Not yet real page
Url: http://sourceforge.net/projects/ccd2iso/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
CloneCD is an image to ISO image file converter.

%prep
%setup -q

%build
aclocal-1.9
automake-1.9
autoheader
autoconf
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README INSTALL AUTHORS
%_bindir/ccd2iso





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-5mdv2011.0
+ Revision: 616942
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2010.0
+ Revision: 424749
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3-3mdv2009.0
+ Revision: 243440
- rebuild
- fix description

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2008.1
+ Revision: 136287
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3-1mdv2007.0
+ Revision: 131388
- 0.3

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org> 0.2-4mdv2007.0
+ Revision: 52998
- rebuild
- Import ccd2iso

* Sat May 20 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.2-3mdk
- build with automake1.8

* Sat Oct 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-2mdk
- Fix BuildRequires

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-1mdk
- 0.2
- %%mkrel 
- Make rpmbuildable

* Fri Jun 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.1-1mdk
- First mdk build

