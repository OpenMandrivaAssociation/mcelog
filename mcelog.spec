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
