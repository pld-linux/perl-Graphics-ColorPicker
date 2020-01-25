#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Graphics
%define		pnam	ColorPicker
Summary:	Graphics::ColorPicker - allows web applications selection of hex color numbers
Summary(pl.UTF-8):	Graphics::ColorPicker - wybór szesnastkowych kodów kolorów dla aplikacji WWW
Name:		perl-Graphics-ColorPicker
Version:	0.12
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22130749d48845a8dcb13fdc7a6a5a70
URL:		http://search.cpan.org/dist/Graphics-ColorPicker/
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

%description -l pl.UTF-8
Ten moduł generuje zbiór palet do wyboru szesnastkowego lub
dziesiętnego numeru koloru przez przeglądarkę WWW. make_page() może
być wywołane z poziomu JavaScriptu na stronie i ustawi wartość
szesnastkową w zmiennej w wywoływanej stronie. Strona wyboru koloru
może być utworzona dla 24 milionów kolorów lub tylko 216 kolorów
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
cp -p images/* $RPM_BUILD_ROOT%{imgdir}

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
