#
# Conditional build:
%bcond_without	gnome		# build without GNOME integration
#
Summary:	Gobby network editor
Summary(pl.UTF-8):	Edytor sieciowy Gobby
Name:		gobby
Version:	0.4.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://releases.0x539.de/gobby/%{name}-%{version}.tar.gz
# Source0-md5:	e5501d37f4199938dfe97d30fdf14e9a
URL:		http://gobby.0x539.de/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9
BuildRequires:	gtkmm-devel >= 2.6.0
BuildRequires:	gtksourceview-devel >= 1.0.0
BuildRequires:	libxml++-devel >= 2.6.0
BuildRequires:	obby-devel >= 0.4.3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gobby network editor.

%description -l pl.UTF-8
Edytor sieciowy Gobby.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{?with_gnome: --with-gnome}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/gobby.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
