%define 	module	TwistedNames
%define		major	0.3
%define		minor	0

Summary:	Domain name server and a client resolver library
Summary(pl):	Serwer nazw oraz biblioteka kliencka rozwi�zuj�ca nazwy
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Names/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	5aa672d0e26718466351351e7bfcf22a
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

%description -l pl
Twisted Names to serwer nazw (DNS) oraz biblioteka kliencka
rozwi�zuj�ca nazwy (resolver). Twisted Names "z pude�ka" zawiera
serwer nazw potrafi�cy czyta� wi�kszo�� plik�w stref w sk�adni BIND-a,
a tak�e prostym formacie opartym o Pythona. Twisted Names mo�e dzia�a�
jako serwer autorytatywny, wykonywa� transfery stref z serwera
g��wnego aby dzia�a� jako serwer zapasowy, dzia�a� jako serwer
buforuj�cy (cache) lub w dowolnej kombinacji tych funkcji. Biblioteka
kliencka Twisted Names udost�pnia funkcje do odpytywania serwera o
wszystkie powszechnie u�ywane rodzaje rekord�w, a tak�e zamiennik
blokujacej funkcji gethostbyname() udost�pnianej przez modu�
biblioteki standardowej Pythona socket.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
