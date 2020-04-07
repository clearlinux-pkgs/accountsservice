#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : accountsservice
Version  : 0.6.55
Release  : 20
URL      : https://www.freedesktop.org/software/accountsservice/accountsservice-0.6.55.tar.xz
Source0  : https://www.freedesktop.org/software/accountsservice/accountsservice-0.6.55.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: accountsservice-data = %{version}-%{release}
Requires: accountsservice-lib = %{version}-%{release}
Requires: accountsservice-libexec = %{version}-%{release}
Requires: accountsservice-license = %{version}-%{release}
Requires: accountsservice-locales = %{version}-%{release}
Requires: accountsservice-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : intltool-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : polkit-dev
Patch1: 0001-Use-stateless-dbus-1-system.d-directory.patch
Patch2: 0002-daemon-Support-stateless-operating-systems-with-spli.patch
Patch3: 0003-Add-support-for-default-group-policy-within-Clear-Li.patch
Patch4: 0004-fix-stateless-autologin.patch

%description
[![Build Status](https://gitlab.freedesktop.org/accountsservice/accountsservice/badges/master/build.svg)](https://gitlab.freedesktop.org/accountsservice/accountsservice/pipelines)

%package data
Summary: data components for the accountsservice package.
Group: Data

%description data
data components for the accountsservice package.


%package dev
Summary: dev components for the accountsservice package.
Group: Development
Requires: accountsservice-lib = %{version}-%{release}
Requires: accountsservice-data = %{version}-%{release}
Provides: accountsservice-devel = %{version}-%{release}
Requires: accountsservice = %{version}-%{release}

%description dev
dev components for the accountsservice package.


%package doc
Summary: doc components for the accountsservice package.
Group: Documentation

%description doc
doc components for the accountsservice package.


%package lib
Summary: lib components for the accountsservice package.
Group: Libraries
Requires: accountsservice-data = %{version}-%{release}
Requires: accountsservice-libexec = %{version}-%{release}
Requires: accountsservice-license = %{version}-%{release}

%description lib
lib components for the accountsservice package.


%package libexec
Summary: libexec components for the accountsservice package.
Group: Default
Requires: accountsservice-license = %{version}-%{release}

%description libexec
libexec components for the accountsservice package.


%package license
Summary: license components for the accountsservice package.
Group: Default

%description license
license components for the accountsservice package.


%package locales
Summary: locales components for the accountsservice package.
Group: Default

%description locales
locales components for the accountsservice package.


%package services
Summary: services components for the accountsservice package.
Group: Systemd services

%description services
services components for the accountsservice package.


%prep
%setup -q -n accountsservice-0.6.55
cd %{_builddir}/accountsservice-0.6.55
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586221367
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsystemd=true \
-Dsystemdsystemunitdir=/usr/lib/systemd/system \
-Dgtk_doc=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/accountsservice
cp %{_builddir}/accountsservice-0.6.55/COPYING %{buildroot}/usr/share/package-licenses/accountsservice/8624bcdae55baeef00cd11d5dfcfa60f68710a02
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang accounts-service

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/AccountsService-1.0.typelib
/usr/share/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Accounts.xml
/usr/share/dbus-1/system-services/org.freedesktop.Accounts.service
/usr/share/dbus-1/system.d/org.freedesktop.Accounts.conf
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.accounts.policy

%files dev
%defattr(-,root,root,-)
/usr/include/accountsservice-1.0/act/act-user-enum-types.h
/usr/include/accountsservice-1.0/act/act-user-manager.h
/usr/include/accountsservice-1.0/act/act-user.h
/usr/include/accountsservice-1.0/act/act.h
/usr/lib64/libaccountsservice.so
/usr/lib64/pkgconfig/accountsservice.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libaccountsservice/ActUser.html
/usr/share/gtk-doc/html/libaccountsservice/ActUserManager.html
/usr/share/gtk-doc/html/libaccountsservice/annotation-glossary.html
/usr/share/gtk-doc/html/libaccountsservice/api-index-0-6-27.html
/usr/share/gtk-doc/html/libaccountsservice/api-index-0-6-39.html
/usr/share/gtk-doc/html/libaccountsservice/api-index-full.html
/usr/share/gtk-doc/html/libaccountsservice/ch01.html
/usr/share/gtk-doc/html/libaccountsservice/home.png
/usr/share/gtk-doc/html/libaccountsservice/index.html
/usr/share/gtk-doc/html/libaccountsservice/left-insensitive.png
/usr/share/gtk-doc/html/libaccountsservice/left.png
/usr/share/gtk-doc/html/libaccountsservice/libaccountsservice.devhelp2
/usr/share/gtk-doc/html/libaccountsservice/right-insensitive.png
/usr/share/gtk-doc/html/libaccountsservice/right.png
/usr/share/gtk-doc/html/libaccountsservice/style.css
/usr/share/gtk-doc/html/libaccountsservice/up-insensitive.png
/usr/share/gtk-doc/html/libaccountsservice/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaccountsservice.so.0
/usr/lib64/libaccountsservice.so.0.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/accounts-daemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/accountsservice/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/accounts-daemon.service

%files locales -f accounts-service.lang
%defattr(-,root,root,-)

