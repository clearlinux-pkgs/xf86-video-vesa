#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5B8A2D50A0ECD0D3 (ajax@nwnk.net)
#
Name     : xf86-video-vesa
Version  : 2.4.0
Release  : 22
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-2.4.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-2.4.0.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vesa-2.4.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-vesa-lib = %{version}-%{release}
Requires: xf86-video-vesa-license = %{version}-%{release}
Requires: xf86-video-vesa-man = %{version}-%{release}
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-vesa - Generic VESA video driver for the Xorg X server
Please submit bugs & patches to the Xorg bugzilla:

%package lib
Summary: lib components for the xf86-video-vesa package.
Group: Libraries
Requires: xf86-video-vesa-license = %{version}-%{release}

%description lib
lib components for the xf86-video-vesa package.


%package license
Summary: license components for the xf86-video-vesa package.
Group: Default

%description license
license components for the xf86-video-vesa package.


%package man
Summary: man components for the xf86-video-vesa package.
Group: Default

%description man
man components for the xf86-video-vesa package.


%prep
%setup -q -n xf86-video-vesa-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542076828
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542076828
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-vesa
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-video-vesa/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/vesa_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-vesa/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/vesa.4
