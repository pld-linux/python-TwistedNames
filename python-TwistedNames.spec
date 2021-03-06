%define 	module	TwistedNames
%define		major	13.0
%define		minor	0

Summary:	Domain name server and a client resolver library
Summary(pl.UTF-8):	Serwer nazw oraz biblioteka kliencka rozwiązująca nazwy
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	http://twistedmatrix.com/Releases/Names/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	9264b6f9fc85e1f7ed31d5fd13eeb48a
URL:		http://twistedmatrix.com/trac/wiki/TwistedNames
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 2.4.0
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
Requires:	python-TwistedCore >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Names is both a domain name server as well as a client
resolver library. Twisted Names comes with an "out of the box"
nameserver which can read most BIND-syntax zone files as well as a
simple Python-based configuration format. Twisted Names can act as an
authoritative server, perform zone transfers from a master to act as a
secondary, act as a caching nameserver, or any combination of these.
Twisted Names' client resolver library provides functions to query for
all commonly used record types as well as a replacement for the
blocking gethostbyname() function provided by the Python stdlib socket
module.

%description -l pl.UTF-8
Twisted Names to serwer nazw (DNS) oraz biblioteka kliencka
rozwiązująca nazwy (resolver). Twisted Names "z pudełka" zawiera
serwer nazw potrafiący czytać większość plików stref w składni BIND-a,
a także prostym formacie opartym o Pythona. Twisted Names może działać
jako serwer autorytatywny, wykonywać transfery stref z serwera
głównego aby działać jako serwer zapasowy, działać jako serwer
buforujący (cache) lub w dowolnej kombinacji tych funkcji. Biblioteka
kliencka Twisted Names udostępnia funkcje do odpytywania serwera o
wszystkie powszechnie używane rodzaje rekordów, a także zamiennik
blokujacej funkcji gethostbyname() udostępnianej przez moduł
biblioteki standardowej Pythona socket.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitedir}/*.egg-info
%{py_sitedir}/twisted/names
%{py_sitedir}/twisted/plugins/*
