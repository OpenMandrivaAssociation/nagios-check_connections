%define up_name check_connections

Name:		nagios-%{up_name}
Version:	2.1.0
Release:	%mkrel 1
Summary:	A Nagios plugin to check the number of TCP connections
License:	GPL
Group:		Networking/Other
URL:		https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_connections
Source:     %{up_name}-%{version}.tar.gz
Requires:	nagios-plugins
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
check_connections is a Nagios plugin to check the number of TCP connections 

%prep
%setup -q -n %{up_name}-%{version}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/nagios/plugins
install -m 755 check_connections %{buildroot}%{_datadir}/nagios/plugins/check_connections

perl -pi -e 's|^#!perl|#!%{_bindir}/perl|' \
    %{buildroot}%{_datadir}/nagios/plugins/check_connections

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_connections.cfg <<'EOF'
define command {
	command_name    check_connections
	command_line    %{_datadir}/nagios/plugins/check_connections
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes NAME NEWS README
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_connections.cfg
%{_datadir}/nagios/plugins/check_connections



%changelog
* Sun Dec 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.0-1mdv2009.1
+ Revision: 317110
- import nagios-check_connections


* Sun Dec 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.0-1mdv2009.1
- first mdv release 
