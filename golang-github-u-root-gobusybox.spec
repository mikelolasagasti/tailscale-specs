# Generated by go2rpm 1.7.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/u-root/gobusybox
%global goipath         github.com/u-root/gobusybox
Version:                0.1.0
%global commit          85dc1fd1bc759b58405db41b84c381aeab70ff08

%gometa

%global common_description %{expand:
Tools for compiling many Go commands into one binary to save space. Builds are
supported in vendor-based Go, module-based Go, and bazel with Starlark.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Tools for compiling many Go commands into one binary to save space. Builds are supported in vendor-based Go, module-based Go, and bazel with Starlark

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
