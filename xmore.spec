Name:		xmore
Version:	1.0.4
Release:	1
Summary:	Plain text display program for the X Window System
Group:		Development/X11
Url:		https://gitlab.freedesktop.org/xorg/app/xmore
Source:		https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xaw7)
#BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
Xmore is a plain text display program for the X Window System.

%prep
%autosetup -p1

%build
%configure	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xmore
%{_datadir}/X11/app-defaults/XMore
%{_mandir}/man1/xmore.1*
