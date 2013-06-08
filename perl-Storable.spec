#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Storable
%define		pnam	Storable
Summary:	Storable - persistency for Perl data structures
Summary(pl.UTF-8):	Storable - przechowywanie struktur danych Perla
Name:		perl-Storable
# 2.13 in perl-modules 5.8.7
# 2.15 in perl-modules 5.8.8
# 2.18 in perl-modules 5.10.0
# 2.22 in perl-modules 5.12.0
Version:	2.30
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Storable/AMS/%{pnam}-%{version}.tar.gz
# Source0-md5:	3fb1587d89d1238d4b26f09d3864b9a1
URL:		http://search.cpan.org/dist/Storable/
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# remove the line below if you *really* have newer version than one
# available in perl-modules
#BuildRequires:	this-must-be-newer-version-than-in-perl-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Storable - persistency for Perl data structures.

%description -l pl.UTF-8
Storable - moduł umożliwiający przechowywanie struktur danych Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Storable.pm
%dir %{perl_vendorarch}/auto/Storable
%{perl_vendorarch}/auto/Storable/Storable.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Storable/Storable.so
%{_mandir}/man3/Storable.3pm*
