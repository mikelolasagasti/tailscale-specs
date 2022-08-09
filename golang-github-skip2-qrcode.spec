# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/skip2/go-qrcode
%global goipath         github.com/skip2/go-qrcode
%global commit          da1b6568686e89143e94f980a98bc2dbd5537f13

%gometa

%global common_description %{expand:
QR Code encoder (Go).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        QR Code encoder (Go)

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0001:      https://patch-diff.githubusercontent.com/raw/skip2/go-qrcode/pull/53.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0001 -p1

%build
for cmd in qrcode; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Nov 28 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0-0.1.20211128gitda1b656
- Initial package
