%define name ermixer
%define version 0.8
%define release %mkrel 4

Name:		%{name}
Summary:	A full featured OSS mixer
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://ermixer.sourceforge.net
Source:		http://erevan.cuore.org/files/ermixer/%{name}-%{version}.tar.bz2
BuildRequires:	libncurses-devel

%description
This is a very sophisticated OSS mixer with a lot of useful 
features like handling of multiple profile files, it offers 
a complete interface to the mixer capatibilities. You can
use it with a nice curses interface or with a command line 
interface (useful for use it in scripts).

%prep

%setup -q 

%build
rm -rf $RPM_BUILD_ROOT

%configure

make
mkdir -p $RPM_BUILD_ROOT/%{_menudir}/
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/ermixer
?package(ermixer):command="/usr/bin/ermixer" icon="sound_section.png" needs="text" section="Multimedia/Sound" title="Ermixer" longtitle="A full featured OSS mixer" 
EOF

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc INSTALL COPYING
%{_bindir}/ermixer
%{_mandir}/man1/ermixer.1*
%{_menudir}/ermixer

