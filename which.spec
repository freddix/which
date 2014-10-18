# based on PLD Linux spec git://git.pld-linux.org/packages/which.git
Summary:	Displays where a particular program in your path is located
Name:		which
Version:	2.20
Release:	15
License:	GPL v3+
Group:		Applications/File
Source0:	http://www.xs4all.nl/~carlo17/which/%{name}-%{version}.tar.gz
# Source0-md5:	95be0501a466e515422cde4af46b2744
URL:		http://www.xs4all.nl/~carlo17/which/
Requires:	setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS EXAMPLES NEWS README*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/which.info*

