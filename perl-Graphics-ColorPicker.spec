#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Graphics
%define		pnam	ColorPicker
Summary:	Graphics::ColorPicker - allows web applications selection of hex color numbers
Summary(pl):	Graphics::ColorPicker - wyb�r szesnastkowych kod�w kolor�w dla aplikacji WWW
Name:		perl-Graphics-ColorPicker
Version:	0.09
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e2996ecb76cbb31c2fbd477abb9c15cd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cgidir	/home/services/httpd/cgi-bin
%define		imgreldir	/ColorPicker
%define		imgdir	/home/services/httpd/html%{imgreldir}

%description
This module generates a set of palettes to select a HEX or DECIMAL
color number via a web browser. make_page() can be called by
javascript from your web page and will set the HEX value in a variable
in the calling page and scope. The selector page can be created for 24
million or 216 web safe colors only.

%description -l pl
Ten modu� generuje zbi�r palet do wyboru szesnastkowego lub
dziesi�tnego numeru koloru przez przegl�dark� WWW. make_page() mo�e
by� wywo�ane z poziomu JavaScriptu na stronie i ustawi warto��
szesnastkow� w zmiennej w wywo�ywanej stronie. Strona wyboru koloru
mo�e by� utworzona dla 24 milion�w kolor�w lub tylko 216 kolor�w
"bezpiecznych dla WWW".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{cgidir},%{imgdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -e "/^use lib/d;s@'./'@'%{imgreldir}/'@" scripts/p_gen.cgi \
	> $RPM_BUILD_ROOT%{cgidir}/p_gen.cgi
install images/* $RPM_BUILD_ROOT%{imgdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README examples/demo.html
%{perl_vendorlib}/Graphics/ColorPicker.pm
%dir %{perl_vendorlib}/auto/Graphics
%{perl_vendorlib}/auto/Graphics/ColorPicker
%{_mandir}/man3/*

%attr(755,root,root) %{cgidir}/p_gen.cgi
%{imgdir}
