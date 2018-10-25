#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5B8A2D50A0ECD0D3 (ajax@nwnk.net)
#
Name     : xf86-video-vesa
Version  : 2.3.4
Release  : 21
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-2.3.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-2.3.4.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-2.3.4.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-vesa-lib
Requires: xf86-video-vesa-doc
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-vesa - Generic VESA video driver for the Xorg X server
Please submit bugs & patches to the Xorg bugzilla:

%package doc
Summary: doc components for the xf86-video-vesa package.
Group: Documentation

%description doc
doc components for the xf86-video-vesa package.


%package lib
Summary: lib components for the xf86-video-vesa package.
Group: Libraries

%description lib
lib components for the xf86-video-vesa package.


%prep
%setup -q -n xf86-video-vesa-2.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507172035
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507172035
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/vesa_drv.so
