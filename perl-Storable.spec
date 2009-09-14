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
Version:	2.21
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Storable/%{pnam}-%{version}.tar.gz
# Source0-md5:	9256904c73d8fe393b90b9b5f219f0a6
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
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
pod2man --section=3pm Storable.pm $RPM_BUILD_ROOT%{_mandir}/man3/Storable.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Storable.pm
%dir %{perl_vendorarch}/auto/Storable
%{perl_vendorarch}/auto/Storable/autosplit.ix
%{perl_vendorarch}/auto/Storable/*.al
%{perl_vendorarch}/auto/Storable/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Storable/*.so
%{_mandir}/man3/*
