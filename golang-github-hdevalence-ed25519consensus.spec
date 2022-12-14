# Generated by go2rpm 1.7.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/hdevalence/ed25519consensus
%global goipath         github.com/hdevalence/ed25519consensus
%global commit          c00d1f31bab3e2c79c55705ad930e04e241d3451

%gometa

%global common_description %{expand:
Go Ed25519 suitable for use in consensus-critical contexts.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Go Ed25519 suitable for use in consensus-critical contexts

License:        BSD-3-Clause
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
