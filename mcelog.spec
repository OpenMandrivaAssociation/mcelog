Name:		mcelog
Version:	168
Release:	1
Summary:	The kernel machine check logger
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.mcelog.org
Source0:	https://github.com/andikleen/mcelog/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:	mcelog.service

%description
mcelog is the user space interface to the in kernel machine check logger
on x86-64. It decodes the binary machine check records into a human
readable format.

%prep
%setup -q

%build
%make_build \
	CFLAGS="%{optflags}" \
	LDFLAGS="%{ldflags}"

%install
%make_install

install -Dpm644 mcelog.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

# Don't install as we prefer systemd service
#install -Dpm755 mcelog.cron %{buildroot}/%{_sysconfdir}/cron.hourly/%{name}

#systemd
install -Dpm644 %{_sourcedir}/mcelog.service %{buildroot}%{_unitdir}/%{name}.service

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%doc README.md README.releases CHANGES
%{_sbindir}/mcelog
%{_mandir}/man8/mcelog.8.*
%{_mandir}/man5/mcelog.conf.5.*
%{_mandir}/man5/mcelog.triggers.5.*
#%{_sysconfdir}/cron.hourly/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/mcelog/mcelog.conf
%{_sysconfdir}/mcelog/bus-error-trigger
%{_sysconfdir}/mcelog/cache-error-trigger
%{_sysconfdir}/mcelog/dimm-error-trigger
%{_sysconfdir}/mcelog/iomca-error-trigger
%{_sysconfdir}/mcelog/page-error-trigger
%{_sysconfdir}/mcelog/page-error-post-sync-soft-trigger
%{_sysconfdir}/mcelog/page-error-pre-sync-soft-trigger
%{_sysconfdir}/mcelog/unknown-error-trigger
%{_sysconfdir}/mcelog/socket-memory-error-trigger
%{_unitdir}/%{name}.service

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
