%define		module sexy-python
Summary:	Python bindings to libsexy
Summary(pl.UTF-8):	Dowiązania do biblioteki libsexy dla Pythona
Name:		python-sexy
Version:	0.1.9
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://releases.chipx86.com/libsexy/sexy-python/sexy-python-%{version}.tar.gz
# Source0-md5:	313f11e98555b0e9eea28219564e5063
URL:		http://www.chipx86.com/wiki/Libsexy
BuildRequires:	libsexy-devel >= 0.1.10
BuildRequires:	libxml2-devel
BuildRequires:	python-devel >= 2
BuildRequires:	python-pygtk-devel >= 2.8.0
Requires:	libsexy >= 0.1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
sexy-python is a set of Python bindings around libsexy.

%description -l pl.UTF-8
sexy-python to zbiór dowiązań Pythona wokół biblioteki libsexy.

%prep
%setup -q -n  %{module}-%{version}

%build
%configure \
	--enable-docs \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{py_sitedir}/gtk-2.0/sexy.so
%{_datadir}/pygtk/2.0/defs/sexy.defs
