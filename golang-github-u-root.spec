# Generated by go2rpm 1.7.0
%bcond_with bootstrap
%if %{with bootstrap}
# Do not run %%check when bootstrapping.
%bcond_with check
%else
%bcond_without check
%endif

# https://github.com/u-root/u-root
%global goipath         github.com/u-root/u-root
Version:                0.9.0

%gometa

%global goipaths0       github.com/u-root/u-root
%global goipathsex0     github.com/u-root/u-root/pkg/strace github.com/u-root/u-root/pkg/ulog

%if %{without bootstrap}
%global goipaths1       github.com/u-root/u-root/pkg/strace github.com/u-root/u-root/pkg/ulog
%endif


%global common_description %{expand:
A fully Go userland with Linux bootloaders! u-root can create a one-binary root
file system (initramfs) containing a busybox-like set of tools written in Go.}

%global golicenses      LICENSE
%global godocs          examples docs AUTHORS

Name:           %{goname}
Release:        %autorelease
Summary:        A fully Go userland with Linux bootloaders! u-root can create a one-binary root file system (initramfs) containing a busybox-like set of tools written in Go

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  golang(github.com/beevik/ntp)
BuildRequires:  golang(github.com/c-bata/go-prompt)
BuildRequires:  golang(github.com/c-bata/go-prompt/completer)
BuildRequires:  golang(github.com/cenkalti/backoff/v4)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/gliderlabs/ssh)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-tpm/tpm)
BuildRequires:  golang(github.com/google/go-tpm/tpm2)
BuildRequires:  golang(github.com/google/go-tpm/tpmutil)
BuildRequires:  golang(github.com/google/goexpect)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/insomniacslk/dhcp/dhcpv4)
BuildRequires:  golang(github.com/insomniacslk/dhcp/dhcpv4/nclient4)
BuildRequires:  golang(github.com/insomniacslk/dhcp/dhcpv4/server4)
BuildRequires:  golang(github.com/insomniacslk/dhcp/dhcpv6)
BuildRequires:  golang(github.com/insomniacslk/dhcp/dhcpv6/nclient6)
BuildRequires:  golang(github.com/insomniacslk/dhcp/dhcpv6/server6)
BuildRequires:  golang(github.com/insomniacslk/dhcp/iana)
BuildRequires:  golang(github.com/insomniacslk/dhcp/interfaces)
BuildRequires:  golang(github.com/insomniacslk/dhcp/netboot)
BuildRequires:  golang(github.com/intel-go/cpuid)
BuildRequires:  golang(github.com/kevinburke/ssh_config)
BuildRequires:  golang(github.com/klauspost/pgzip)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/pborman/getopt/v2)
BuildRequires:  golang(github.com/pierrec/lz4/v4)
BuildRequires:  golang(github.com/rck/unit)
BuildRequires:  golang(github.com/rekby/gpt)
BuildRequires:  golang(github.com/safchain/ethtool)
BuildRequires:  golang(github.com/spf13/pflag)
%if %{without bootstrap}
BuildRequires:  golang(github.com/u-root/gobusybox/src/pkg/bb)
BuildRequires:  golang(github.com/u-root/gobusybox/src/pkg/golang)
%endif
BuildRequires:  golang(github.com/u-root/iscsinl)
BuildRequires:  golang(github.com/ulikunitz/xz)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(github.com/vtolstov/go-ioctl)
BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/openpgp/errors)
BuildRequires:  golang(golang.org/x/crypto/openpgp/packet)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/text/message)
BuildRequires:  golang(golang.org/x/text/transform)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/imports)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(mvdan.cc/sh/v3/interp)
BuildRequires:  golang(mvdan.cc/sh/v3/syntax)
BuildRequires:  golang(pack.ag/tftp)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/creack/pty)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf cmds
rm -rf pkg/namespace pkg/fb


%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
