%include	/usr/lib/rpm/macros.perl
%define		pdir	Storable
%define		pnam	Storable
Summary:	Storable Perl module
Summary(cs):	Modul Storable pro Perl
Summary(da):	Perlmodul Storable
Summary(de):	Storable Perl Modul
Summary(es):	Módulo de Perl Storable
Summary(fr):	Module Perl Storable
Summary(it):	Modulo di Perl Storable
Summary(ja):	Storable Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Storable ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Storable
Summary(pl):	Modu³ Perla Storable
Summary(pt):	Módulo de Perl Storable
Summary(pt_BR):	Módulo Perl Storable
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Storable
Summary(sv):	Storable Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Storable
Summary(zh_CN):	Storable Perl Ä£¿é
Name:		perl-Storable
Version:	2.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Storable - persistency for Perl data structures.

%description -l pl
Storable - modu³ umo¿liwiaj±cy przechowywanie struktur danych Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
%{perl_archlib}/Storable.pm
%dir %{perl_archlib}/auto/Storable
%{perl_archlib}/auto/Storable/autosplit.ix
%{perl_archlib}/auto/Storable/*.al
%{perl_archlib}/auto/Storable/*.bs
%attr(755,root,root) %{perl_archlib}/auto/Storable/*.so
%{_mandir}/man3/*
