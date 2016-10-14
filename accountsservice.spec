#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : accountsservice
Version  : 0.6.43
Release  : 1
URL      : https://www.freedesktop.org/software/accountsservice/accountsservice-0.6.43.tar.xz
Source0  : https://www.freedesktop.org/software/accountsservice/accountsservice-0.6.43.tar.xz
Summary  : Client Library for communicating with accounts service
Group    : Development/Tools
License  : GPL-3.0
Requires: accountsservice-config
Requires: accountsservice-lib
Requires: accountsservice-bin
Requires: accountsservice-data
Requires: accountsservice-doc
Requires: accountsservice-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : xmlto

%description
Overview
========
The AccountsService project provides
o  A set of D-Bus interfaces for querying and manipulating
user account information.

%package bin
Summary: bin components for the accountsservice package.
Group: Binaries
Requires: accountsservice-data
Requires: accountsservice-config

%description bin
bin components for the accountsservice package.


%package config
Summary: config components for the accountsservice package.
Group: Default

%description config
config components for the accountsservice package.


%package data
Summary: data components for the accountsservice package.
Group: Data

%description data
data components for the accountsservice package.


%package dev
Summary: dev components for the accountsservice package.
Group: Development
Requires: accountsservice-lib
Requires: accountsservice-bin
Requires: accountsservice-data
Provides: accountsservice-devel

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
Requires: accountsservice-data
Requires: accountsservice-config

%description lib
lib components for the accountsservice package.


%package locales
Summary: locales components for the accountsservice package.
Group: Default

%description locales
locales components for the accountsservice package.


%prep
%setup -q -n accountsservice-0.6.43

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang accounts-service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/accounts-daemon

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/accounts-daemon.service

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Accounts.xml
/usr/share/dbus-1/system-services/org.freedesktop.Accounts.service
/usr/share/polkit-1/actions/org.freedesktop.accounts.policy

%files dev
%defattr(-,root,root,-)
/usr/include/accountsservice-1.0/act/act-user-enum-types.h
/usr/include/accountsservice-1.0/act/act-user-manager.h
/usr/include/accountsservice-1.0/act/act-user.h
/usr/include/accountsservice-1.0/act/act.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/AccountsService-1.0.typelib
/usr/lib64/pkgconfig/*.pc
/usr/share/gir-1.0/*.gir

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libaccountsservice/ActUser.html
/usr/share/gtk-doc/html/libaccountsservice/ActUserManager.html
/usr/share/gtk-doc/html/libaccountsservice/annotation-glossary.html
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
/usr/lib64/*.so.*

%files locales -f accounts-service.lang 
%defattr(-,root,root,-)

