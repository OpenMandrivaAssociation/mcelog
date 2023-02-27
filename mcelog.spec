Name:		mcelog
Version:	191
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
%autosetup -p1
%if "%{_bindir}" == "%{_sbindir}"
sed -i -e 's,/sbin,/bin,g' Makefile
%endif

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
%{_sysconfdir}/mcelog/page-error-counter-replacement-trigger
%{_sysconfdir}/mcelog/page-error-post-sync-soft-trigger
%{_sysconfdir}/mcelog/page-error-pre-sync-soft-trigger
%{_sysconfdir}/mcelog/unknown-error-trigger
%{_sysconfdir}/mcelog/socket-memory-error-trigger
%{_unitdir}/%{name}.service
