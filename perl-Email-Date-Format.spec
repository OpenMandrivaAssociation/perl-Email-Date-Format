%define upstream_name    Email-Date-Format
%define upstream_version 1.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Produce RFC 2822 date strings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source0:    http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a simple means for generating an RFC 2822 compliant
datetime string.  (In case you care, they're not RFC 822 dates, because they
use a four digit year, which is not allowed in RFC 822.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Email
