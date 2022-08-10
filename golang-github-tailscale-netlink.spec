# Generated by go2rpm 1.7.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/tailscale/netlink
%global goipath         github.com/tailscale/netlink
Version:                1.1.0
%global commit          cabfb018fe8589d5c1d9d29e805943fb400ee782

%gometa

%global common_description %{expand:
[temporary dev fork] Simple netlink library for go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        [temporary dev fork] Simple netlink library for go

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog