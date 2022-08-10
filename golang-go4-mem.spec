# Generated by go2rpm 1.7.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/go4org/mem
%global goipath         go4.org/mem
%global forgeurl        https://github.com/go4org/mem
%global commit          4f986261bf13b31d92d3cee582c1b30e8b0eeaf0

%gometa

%global common_description %{expand:
Cheap Go type to hold & operate on either a read-only []byte or string.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Cheap Go type to hold & operate on either a read-only []byte or string

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