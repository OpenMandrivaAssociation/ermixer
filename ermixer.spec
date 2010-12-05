%define name ermixer
%define version 0.8
%define release %mkrel 8

Name:		%{name}
Summary:	A full featured OSS mixer
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://ermixer.sourceforge.net
Source:		http://erevan.cuore.org/files/ermixer/%{name}-%{version}.tar.bz2
Patch0:		ermixer-0.8-fix-link.patch
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
%patch0 -p0 -b .link

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

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

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc INSTALL COPYING
%{_bindir}/ermixer
%{_mandir}/man1/ermixer.1*
%{_datadir}/applications/mandriva-ermixer.desktop

