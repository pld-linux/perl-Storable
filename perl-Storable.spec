#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Storable
%define	pnam	Storable
Summary:	Storable - persistency for Perl data structures
Summary(pl):	Storable - przechowywanie struktur danych Perla
Name:		perl-Storable
Version:	2.06
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5: 28251cdd6aa2e39f1e36c02472ca5e34
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Storable - persistency for Perl data structures.

%description -l pl
Storable - modu³ umo¿liwiaj±cy przechowywanie struktur danych Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
