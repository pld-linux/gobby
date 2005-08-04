Summary:	Gobby network editor
Summary(pl):	Edytor sieciowy Gobby
Name:		gobby
Version:	0.2.0
Release:	1
License:	BSD
Group:		Applications/Editors
Source0:	http://releases.0x539.de/gobby/%{name}-%{version}.tar.gz
# Source0-md5:	96840791c38db6a36d4fb16aefbedad2
URL:		http://gobby.0x539.de/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	obby-devel >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gobby network editor.

%description -l pl
Edytor sieciowy Gobby.

%prep
%setup -q

%build
%configure
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
