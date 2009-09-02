%define name ccd2iso
%define version 0.3
%define release %mkrel 4

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



