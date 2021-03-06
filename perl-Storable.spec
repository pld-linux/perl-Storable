#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Storable
%define		pnam	Storable
Summary:	Storable - persistency for Perl data structures
Summary(pl.UTF-8):	Storable - przechowywanie struktur danych Perla
Name:		perl-Storable
# 2.13 in perl-modules 5.8.7
# 2.15 in perl-modules 5.8.8
# 2.18 in perl-modules 5.10.0
# 2.22 in perl-modules 5.12.0
# 2.41 in perl-modules 5.18.0
# 2.49 in perl-modules 5.20.1
# 3.08 in perl-modules 5.28.0
# 3.15 in perl-modules 5.30.0
Version:	3.15
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Storable/%{pnam}-%{version}.tar.gz
# Source0-md5:	7890d8e32c03f9584a1cc65068a7a154
URL:		https://metacpan.org/release/Storable
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if "%{version}" <= "%(rpm -q --provides perl-modules | grep ^perl-Storable | awk '{ print $3 }')"
BuildRequires:	this-must-be-newer-version-than-in-perl-modules
%endif
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
%attr(755,root,root) %{perl_vendorarch}/auto/Storable/Storable.so
%{_mandir}/man3/Storable*.3pm*
