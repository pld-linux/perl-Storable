%include	/usr/lib/rpm/macros.perl
Summary:	Storable perl module
Summary(pl):	Modu� perla Storable
Name:		perl-Storable
Version:	0.6.7
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module//Storable-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-13
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Storable - persistency for perl data structures. 

%description -l pl
Storable - modu� umo�liwiaj�cy przechowywanie struktur danych perla.

%prep
%setup -q -n Storable-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Storable/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Storable
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitearch}/Storable.pm

%dir %{perl_sitearch}/auto/Storable
%{perl_sitearch}/auto/Storable/.packlist
%{perl_sitearch}/auto/Storable/*.al
%{perl_sitearch}/auto/Storable/autosplit.ix
%{perl_sitearch}/auto/Storable/Storable.bs
%attr(755,root,root) %{perl_sitearch}/auto/Storable/Storable.so

%{_mandir}/man3/*
