# Generated by go2rpm 1.16.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/sagernet/ws
%global goihead ws
%global goipath github.com/sagernet/%{goihead}
%global commit          0371dd8da5831608e5c0f7f33c45c3050fb89200

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another package,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%{?!tag:%{?!commit:%global tag v%{oldver}}}
%gometa -L -f

%global common_description %{expand:
Tiny WebSocket library for Go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           golang-github-sagernet-ws
Version:  0
%define oldver 0
Release:        %autorelease -p
Summary:        Tiny WebSocket library for Go

License:        MIT
URL:            %{gourl}
%define stag %{?tag}%{?!tag:%commit}
Source: https://%{goipath}/archive/%{stag}/%{goihead}-%{stag}.tar.gz

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
for cmd in autobahn; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check

%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc example README.md
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should not use globs to avoid installing conflicting
# binaries.
# Write a _bindir line per each of the binaries the package will install.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%{_bindir}/*
%endif

%gopkgfiles

%changelog
%autochangelog
