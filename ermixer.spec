%define name ermixer
%define version 0.8
%define release 10

Name:		%{name}
Summary:	A full featured OSS mixer
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		https://ermixer.sourceforge.net
Source:		http://erevan.cuore.org/files/ermixer/%{name}-%{version}.tar.bz2
Patch0:		ermixer-0.8-fix-link.patch
BuildRequires:	ncurses-devel

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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-8mdv2011.0
+ Revision: 610383
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.8-7mdv2010.1
+ Revision: 508319
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.8-4mdv2008.1
+ Revision: 130454
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- fix hardcoded man page extension
- import ermixer


* Thu Jan 05 2006 Lenny Cartier <lenny@mandriva.com> 0.8-4mdk
- rebuild

* Thu Jul 22 2004 Michael Scherer <misc@mandrake.org> 0.8-3mdk 
- rebuild for new gcc

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8-2mdk
- rebuild

* Mon Mar 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.8-1mdk
- 0.8

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.7-2mdk
- rebuild

* Thu May 16 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.7-1mdk
- added by Michele Balistreri <brain@email.it>

