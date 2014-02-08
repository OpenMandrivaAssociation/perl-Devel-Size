%define upstream_name	 Devel-Size
%define upstream_version 0.71

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:	Find the memory usage of Perl variables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel

%description
This module figures out the real sizes of Perl variables in bytes. Call
functions with a reference to the variable you want the size of. If the
variable is a plain scalar it returns the size of the scalar. If the variable
is a hash or an array, use a reference when calling.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc CHANGES SIGNATURE
%{perl_vendorarch}/Devel/*
%{perl_vendorarch}/auto/Devel/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.710.0-5mdv2012.0
+ Revision: 765174
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.710.0-4
+ Revision: 763698
- rebuilt for perl-5.14.x

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.710.0-3
+ Revision: 681404
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-2mdv2011.0
+ Revision: 555240
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.0
+ Revision: 406981
- rebuild using %%perl_convert_version

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-1mdv2009.0
+ Revision: 277948
- update to new version 0.71

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.69-4mdv2009.0
+ Revision: 256659
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.69-2mdv2008.1
+ Revision: 151431
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-1mdv2008.0
+ Revision: 63954
- update to new version 0.69

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2008.0
+ Revision: 46621
- update to new version 0.68


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.66-1mdv2007.0
+ Revision: 131642
- 0.66

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Devel-Size

* Wed Jan 11 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.64-1mdk
- 0.64

* Sun Jul 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.63-1mdk
- 0.63

* Wed Jun 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.62-1mdk
- Initial Mandriva release.

