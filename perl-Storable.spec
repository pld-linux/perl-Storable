%include	/usr/lib/rpm/macros.perl
Summary:	Storable perl module
Summary(pl):	Modu³ perla Storable
Name:		perl-Storable
Version:	2.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Storable/Storable-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Storable - persistency for perl data structures.

%description -l pl
Storable - modu³ umo¿liwiaj±cy przechowywanie struktur danych perla.

%prep
%setup -q -n Storable-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_archlib}/Storable.pm
%{perl_archlib}/auto/Storable
