#
# Conditional build:
%bcond_with	gtk3		# GTK+ 3.x instead of 2.x [seems an early adoption]
#
Summary:	Gobby network editor
Summary(pl.UTF-8):	Edytor sieciowy Gobby
Name:		gobby
Version:	0.5.0
Release:	4
License:	ISC
Group:		X11/Applications/Editors
Source0:	http://releases.0x539.de/gobby/%{name}-%{version}.tar.gz
# Source0-md5:	80b30bb4205b623f8e065150cbfb21e6
URL:		http://gobby.0x539.de/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.18.0
BuildRequires:	gnome-doc-utils >= 0.9.0
BuildRequires:	gsasl-devel >= 0.2.21
%{!?with_gtk3:BuildRequires:	gtkmm-devel >= 2.6.0}
%{?with_gtk3:BuildRequires:	gtkmm3-devel >= 3.0}
%{!?with_gtk3:BuildRequires:	gtksourceview2-devel >= 2.4}
%{?with_gtk3:BuildRequires:	gtksourceview3-devel >= 3.0}
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libinfinity-devel >= 0.6
%{!?with_gtk3:BuildRequires:	libinfinity-gtk-devel >= 0.6}
%{?with_gtk3:BuildRequires:	libinfinity-gtk3-devel >= 0.6}
BuildRequires:	libstdc++-devel >= 6:4.3
%{!?with_gtk3:BuildRequires:	libunique-devel >= 1.1.2}
%{?with_gtk3:BuildRequires:	libunique3-devel >= 3}
BuildRequires:	libxml++2-devel >= 2.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%configure \
	%{?with_gtk3:--with-gtk3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{el_GR,el}

# gobby05.mo, gnome/help/gobby
%find_lang %{name} --all-name --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/gobby-0.5
%{_datadir}/gobby-0.5
%{_datadir}/appdata/gobby-0.5.appdata.xml
%{_mandir}/man1/gobby-0.5.1*
%{_desktopdir}/gobby-0.5.desktop
%{_iconsdir}/hicolor/48x48/apps/gobby-0.5.png
%{_iconsdir}/hicolor/scalable/apps/gobby-0.5.svg
# which themes???
#%{_iconsdir}/HighContrastLargePrint/48x48/apps/gobby-0.5.png
#%{_iconsdir}/HighContrastLargePrint/scalable/apps/gobby-0.5.svg
#%{_iconsdir}/HighContrastLargePrintInverse/48x48/apps/gobby-0.5.png
#%{_iconsdir}/HighContrastLargePrintInverse/scalable/apps/gobby-0.5.svg
