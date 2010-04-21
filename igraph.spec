#
# Conditional build:
%bcond_with	shell		# build with shell interface
#
Summary:	Library for creating and manipulating graphs
#Summary(pl.UTF-8):	-
Name:		igraph
Version:	0.5.1
Release:	3
License:	GPL v2+
Group:		Development/Libraries
Source0:	http://cneurocvs.rmki.kfki.hu/igraph/download/%{name}-%{version}.tar.gz
# Source0-md5:	19f9c193fc7c8b88a0e8d98aef9f9bb5
URL:		http://cneurocvs.rmki.kfki.hu/igraph/
BuildRequires:	arpack-devel
BuildRequires:	blas-devel
BuildRequires:	gmp-devel
BuildRequires:	lapack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
igraph is a free software package for creating and manipulating
undirected and directed graphs. It includes implementations for classic
graph theory problems like minimum spanning trees and network flow, and
also implements algorithms for some recent network analysis methods,
like community structure search.

# %description -l pl.UTF-8
# TODO

%package devel
Summary:	Header files for the igraph library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki igraph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the igraph library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki igraph.

%prep
%setup -q

%build
%configure \
	--with-external-arpack \
	--with-external-lapack \
	--with-external-blas   \
	%{?with_shell:--enable-shell}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_libdir}/*.la
%{_pkgconfigdir}/*
%{_includedir}/igraph
