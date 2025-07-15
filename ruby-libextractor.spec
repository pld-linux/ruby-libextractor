# NOTE: slightly newer version available at:
# http://ftp.gnu.org/gnu/libextractor/libextractor-ruby-0.1.gem
# but still doesn't build with libextractor 1+
%define pkgname libextractor
Summary:	Ruby binding for libextractor
Summary(pl.UTF-8):	Wiązanie języka Ruby dla biblioteki libextractor
Name:		ruby-%{pkgname}
Version:	0.9
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://gnunet.org/libextractor/download/%{pkgname}-ruby-%{version}.tar.gz
# Source0-md5:	442f131710cad3dec22465698e25db1f
Patch0:		%{name}-ruby1.9.patch
URL:		http://gnunet.org/libextractor/
BuildRequires:	libextractor-devel
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding for libextractor.

%description -l pl.UTF-8
Wiązanie języka Ruby dla biblioteki libextractor.

%prep
%setup -q -n libextractor-ruby-%{version}
%patch -P0 -p1

%build
%{__ruby} extconf.rb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/extractor.so
