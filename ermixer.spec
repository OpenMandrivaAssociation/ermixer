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
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/ermixer
Icon=sound_section
Categories=AudioVideo;Player;Audio;
Name=Ermixer
Comment=A full featured OSS mixer
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
%{_datadir}/applications/mandriva-ermixer.desktop

