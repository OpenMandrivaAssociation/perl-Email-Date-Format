%define modname	Email-Date-Format

Summary:	Produce RFC 2822 date strings
Name:		perl-%{modname}
Version:	1.008
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Email/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl-devel
# Ease version scheme switching without an Epoch
Obsoletes:	%{name} = 1.5.0-1

%description
This module provides a simple means for generating an RFC 2822 compliant
datetime string.  (In case you care, they're not RFC 822 dates, because they
use a four digit year, which is not allowed in RFC 822.)

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Email
%{_mandir}/man3/*
