# Generated by go2rpm 1.7.0
%bcond_without check

# https://github.com/pierrec/lz4
%global goipath         github.com/pierrec/lz4
Version:                4.1.14

%gometa

%global goaltipaths     github.com/pierrec/lz4/v4

%global common_description %{expand:
Package lz4 implements reading and writing lz4 compressed data (a frame), as
specified in
http://fastcompression.blogspot.com/2013/04/lz4-streaming-format-final.html.

This package is compatible with the LZ4 frame format although the block level
compression and decompression functions are exposed and are fully compatible
with the LZ4 block format definition, they are low level and should not be
used directly.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        LZ4 compression and decompression in pure Go

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

%build
for cmd in cmd/* ; do
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
%autochangelog
