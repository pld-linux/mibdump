Summary:	mibdump - dump management agent data based on MIBs
Summary(pl):	mibdump - zrzucanie danych agenta zarz±dzaj±cego w oparciu o MIB-y
Name:		mibdump
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/%{name}-%{version}.tar.gz
# Source0-md5:	724bf7632d649087439f5cb0f5b39c19
Patch0:		%{name}-netsnmp.patch
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsmi-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mibdump program is used to dump the agent data of a single MIB
module to stdout in a selectable output format.

%description -l pl
Program mibdump s³u¿y do zrzucania danych agenta pojedynczego modu³u
MIB na standardowe wyj¶cie w wybranym formacie wyj¶ciowym.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/mibdump
%{_mandir}/man1/mibdump.1*
