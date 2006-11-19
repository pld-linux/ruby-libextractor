Summary:	Ruby binding for libextractor
Summary(pl):	Wi±zanie jêzyka Ruby dla biblioteki libextractor
Name:		ruby-libextractor
Version:	0.9
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://gnunet.org/libextractor/download/libextractor-ruby-%{version}.tar.gz
# Source0-md5:	442f131710cad3dec22465698e25db1f
URL:		http://gnunet.org/libextractor/
BuildRequires:	libextractor-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding for libextractor.

%description -l pl
Wi±zanie jêzyka Ruby dla biblioteki libextractor.

%prep
%setup -q -n libextractor-ruby-%{version}

%build
ruby extconf.rb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/extractor.so
