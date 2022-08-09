# Generated by go2rpm 1.7.0
%bcond_without check

# https://github.com/WireGuard/wireguard-go
%global goipath         golang.zx2c4.com/wireguard
%global forgeurl        https://github.com/WireGuard/wireguard-go
Version:                0.0.20220316
%global tag             0.0.20220316

%gometa

%global common_description %{expand:
Mirror only. Official repository is at https://git.zx2c4.com/wireguard-go.}

%global golicenses      LICENSE
%global godocs          README.md examples

Name:           %{goname}
Release:        %autorelease
Summary:        Mirror only. Official repository is at https://git.zx2c4.com/wireguard-go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/wireguard-go %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
rm format_test.go
%gocheck
%endif

%files
%license LICENSE
%doc README.md examples
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
