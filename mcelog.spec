%define name	mcelog
%define version 0.8
%define release %mkrel 0.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The kernel machine check logger
License:	GPL 
Group:		System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		ftp://ftp.suse.com/pub/people/ak/mcelog
Source:		ftp://ftp.suse.com/pub/people/ak/mcelog/%{name}-%{version}pre.tar.gz

%description
mcelog is the user space interface to the in kernel machine check logger
on x86-64. It decodes the binary machine check records into a human
readable format.

%prep
%setup -q -n %{name}-%{version}pre

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}/%{_sysconfdir}/cron.hourly/

%makeinstall
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
