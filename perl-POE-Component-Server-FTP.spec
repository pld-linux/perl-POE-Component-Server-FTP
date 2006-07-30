#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Server-FTP
Summary:	perl(POE::Component::Server::FTP) - Event based FTP server on a virtual filesystem
Name:		perl-POE-Component-Server-FTP
Version:	1.06
Release:	0.2
# no license anywhere described..
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4cddf0b0793b6c82ca92a479da15628
#URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
URL:		poe.perl.org
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-POE
%if %{with tests}
# dont fail for now without, but its required anyway
BuildRequires:	perl-Filesys-Virtual
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description 
POE::Component::Server::FTP is an event driven FTP server backed by a virtual
filesystem interface as implemented by Filesys::Virtual.

%prep
%setup -q -n %{pdir}-%{pnam}-0.06

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
	
%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__install} examples/*pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Server/FTP.pm
%dir %{perl_vendorlib}/POE/Component/Server/FTP
%{perl_vendorlib}/POE/Component/Server/FTP/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
