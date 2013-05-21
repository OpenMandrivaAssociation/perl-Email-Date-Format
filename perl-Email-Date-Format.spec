%define upstream_name    Email-Date-Format
%define upstream_version 1.002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Produce RFC 2822 date strings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl-devel

BuildArch:		noarch

%description
This module provides a simple means for generating an RFC 2822 compliant
datetime string.  (In case you care, they're not RFC 822 dates, because they
use a four digit year, which is not allowed in RFC 822.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Email


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdv2012.0
+ Revision: 765195
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3
+ Revision: 763711
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2
+ Revision: 667126
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 405856
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.00.2-2mdv2009.0
+ Revision: 223664
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary's case

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00.2-1mdv2008.1
+ Revision: 114717
- import perl-Email-Date-Format


* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00.2-1mdv2008.1
- first mdv release
