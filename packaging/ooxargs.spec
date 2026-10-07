Name:           ooxargs
Version:        0.1.0
Release:        1%{?dist}
Summary:        Bounded argument builder and parallel execution dispatcher with backpressure limits.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooxargs
Source0:        ooxargs-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooxargs is a sovereign, capability-bounded STREAM DISPATCHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooxargs
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooxargs-uninstall

%files
/usr/bin/ooxargs
/usr/bin/ooxargs-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
