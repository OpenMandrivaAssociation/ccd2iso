Summary: CloneCD image to ISO image file converter
Name:    ccd2iso
Version: 0.3
Release: 7
Source0: http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group:   Archiving/Cd burning
Url:     https://sourceforge.net/projects/ccd2iso/

%description
CloneCD is an image to ISO image file converter.

%prep
%setup -q

%build
aclocal-1.9
automake-1.9 --add-missing
autoheader
autoconf
%configure
%make

%install
%makeinstall_std

%files
%doc README INSTALL AUTHORS
%{_bindir}/ccd2iso
