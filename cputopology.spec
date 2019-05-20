Summary: CPU Topology Configuration Tool

Name: cputopology
Version: 1.0
Release: 0%{?dist}
License: GPL
Source0: cputopology.tar.bz2
Requires: bash, util-linux, systemd-units

%description
The CPU Topology Configuration Tool is a command-line utility that allows users
to configure their cpu topology at boot time via systemd and kernel parameters
or run time on the command line.

%global debug_package %{nil}
%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/%{_sbindir}/
mkdir -p %{buildroot}/%{_unitdir}/
install -m 755 cputopology %{buildroot}/%{_sbindir}/cputopology
install -m 644 cputopology.service %{buildroot}/%{_unitdir}/cputopology.service

%files
%defattr(-,root,root)
%{_sbindir}/cputopology
%{_unitdir}/cputopology.service

%post
%systemd_post cputopology.service

%preun
%systemd_preun cputopology.service

%postun
%systemd_postun_with_restart cputopology.service

%changelog
* Tue Feb 19 2019 Prarit Bhargava <prarit@redhat.com> 1.0.0
- Initial version
