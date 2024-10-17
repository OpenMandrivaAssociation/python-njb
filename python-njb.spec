%define module	njb
%define r_version 2.2.1

Name:           python-%{module}
Version:        0.1.0
Release:        %mkrel 4
Summary:        Python module for nomad jukebox
Group:          Development/Python
License:        GPL
URL:            https://lsongs.com/?page=downloads
Source0:        http://software.linspire.com/pool-src/p/pynjb/py%{module}_%{version}-0.0.0.50.linspire0.6.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  python-devel python-sip

%description
Python module for nomad jukebox

%prep
%setup -n marlin_build_pynjb-0.1 -q


%build
%{__python} configure.py 

make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pyver}/site-packages/
cp -f pynjb.so $RPM_BUILD_ROOT%{_libdir}/python%{pyver}/site-packages/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/python%{pyver}/site-packages/*
%doc LICENSE.GPL README 


