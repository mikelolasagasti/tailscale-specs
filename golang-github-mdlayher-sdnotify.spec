# Generated by go2rpm 1.7.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/mdlayher/sdnotify
%global goipath         github.com/mdlayher/sdnotify
Version:                1.0.0

%gometa

%global common_description %{expand:
Package sdnotify implements systemd readiness notifications as described in
https://www.freedesktop.org/software/systemd/man/sd_notify.html. MIT Licensed.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        sdnotify implements systemd readiness notifications

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

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