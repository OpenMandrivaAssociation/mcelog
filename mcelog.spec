%define pre_ver pre
%define git 20090623
%define rel_num 2
%if "%{git}" != ""
%define rel 0.%{?pre_ver:%{pre_ver}.}git%{git}.%{rel_num}
%else
%define rel %{?pre_ver:0.%{pre_ver}.}%{rel_num}
%endif

Name:		mcelog
Version:	0.9
Release:	%mkrel %{rel}
Summary:	The kernel machine check logger
License:	GPLv2
Group:		System/Kernel and hardware
Url:		ftp://ftp.x86-64.org/pub/linux/tools/mcelog/
Source:		mcelog-%{version}%{?pre_ver:%{pre_ver}}%{?git:-git%{git}}.tar.lzma
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
mcelog is the user space interface to the in kernel machine check logger
on x86-64. It decodes the binary machine check records into a human
readable format.

%prep
%setup -q -n %{name}-%{version}%{?pre_ver:%{pre_ver}}%{?git:-git%{git}}

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}/%{_sysconfdir}/cron.hourly/

%makeinstall etcprefix=%{buildroot}
cp mcelog.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
cp mcelog.cron %{buildroot}/%{_sysconfdir}/cron.hourly/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/mcelog
%{_mandir}/man8/*
%{_sysconfdir}/cron.hourly/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/mcelog.conf


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-0.pre.git20090623.2mdv2011.0
+ Revision: 620308
- the mass rebuild of 2010.0 packages

* Fri Aug 21 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.9-0.pre.git20090623.1mdv2010.0
+ Revision: 419325
- Updated to git snapshot version (0.9pre-git20090623) compatible with
  kernel 2.6.31
- Updated BuildRoot/License tags.

* Mon Mar 10 2008 Erwan Velu <erwan@mandriva.org> 0.8-0.2mdv2008.1
+ Revision: 183364
- Rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Erwan Velu <erwan@mandriva.org> 0.8-0.1mdv2008.0
+ Revision: 22425
- 0.8pre
- Import mcelog



* Wed May 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdk
- New release 0.7

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdk
- new version
- spec cleanup
- fix optimisations

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 0.5-1mdk
- Initial Release
