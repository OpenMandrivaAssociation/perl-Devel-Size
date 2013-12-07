%define modname	Devel-Size
%define modver	0.71

Summary:	Find the memory usage of Perl variables
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel

%description
This module figures out the real sizes of Perl variables in bytes. Call
functions with a reference to the variable you want the size of. If the
variable is a plain scalar it returns the size of the scalar. If the variable
is a hash or an array, use a reference when calling.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES SIGNATURE
%{perl_vendorarch}/Devel/*
%{perl_vendorarch}/auto/Devel/*
%{_mandir}/man3/*

