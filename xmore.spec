Name:		xmore
Version:	1.0.1
Release:	%mkrel 6
Summary:	Plain text display program for the X Window System
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	libxprintutil-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xmore is a plain text display program for the X Window System.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xmore
%{_datadir}/X11/app-defaults/XMore
%{_mandir}/man1/xmore.1*

