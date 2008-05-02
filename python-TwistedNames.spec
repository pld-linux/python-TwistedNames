%define 	module	TwistedNames
%define		major	8.0
%define		minor	0

Summary:	Domain name server and a client resolver library
Summary(pl.UTF-8):	Serwer nazw oraz biblioteka kliencka rozwiązująca nazwy
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Names/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	09533501b9e1ae02c8a969a289df2d80
URL:		http://twistedmatrix.com/projects/web/
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 2.4.0
BuildRequires:	python-devel >= 2.2
Requires:	python-TwistedCore >= 2.4.0
BuildArch:	noarch
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--install-purelib=%{py_sitescriptdir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/twisted/names
%{py_sitescriptdir}/twisted/plugins/*
