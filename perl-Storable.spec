%include	/usr/lib/rpm/macros.perl
Summary:	Storable perl module
Summary(pl):	Modu³ perla Storable
Name:		perl-Storable
Version:	1.0.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Storable/Storable-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Storable - persistency for perl data structures.

%description -l pl
Storable - modu³ umo¿liwiaj±cy przechowywanie struktur danych perla.

%prep
%setup -q -n Storable-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitearch}/Storable.pm

%dir %{perl_sitearch}/auto/Storable
%{perl_sitearch}/auto/Storable/*.al
%{perl_sitearch}/auto/Storable/autosplit.ix
%{perl_sitearch}/auto/Storable/Storable.bs
%attr(755,root,root) %{perl_sitearch}/auto/Storable/Storable.so

%{_mandir}/man3/*
