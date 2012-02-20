%global packname  RBGL
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.30.1
Release:          1
Summary:          An interface to the BOOST graph library
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-graph R-methods 
Requires:         R-methods 
Requires:         R-Rgraphviz 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graph R-methods
BuildRequires:    R-methods 
BuildRequires:    R-Rgraphviz 
BuildRequires:    blas-devel
BuildRequires:    boost-devel
BuildRequires:    graphviz-devel
BuildRequires:    lapack-devel

%description
A fairly extensive and comprehensive interface to the graph algorithms
contained in the BOOST library.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/XML
%{rlibdir}/%{packname}/boostExamples
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demos
%{rlibdir}/%{packname}/dot
%{rlibdir}/%{packname}/dtd
%{rlibdir}/%{packname}/fdep.ps
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
