# http://github.com/gonum/blas
%global provider_prefix github.com/gonum/blas
%global gobaseipath     %{provider_prefix}
%global commit          80dca99229cccca259b550ae3f755cf79c65a224
%global commitdate      20150711

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.10.%{commitdate}git%{shortcommit}%{?dist}
Summary:        A blas implementation for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

Patch0:         add-license.patch
Patch1:         internal-to-inteernal.patch
Patch2:         0001-use-system-library.patch
Patch3:         0001-change-C.int-to-C.blastint.patch

%description
%{summary}

%package devel
Summary:       %{summary}

BuildRequires: openblas-devel
Requires:      openblas-devel
BuildRequires: golang(github.com/gonum/floats)
BuildRequires: golang(github.com/gonum/inteernal/asm)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%install
%goinstall

%check
%gochecks %{gobaseipath}/{cgo,native/inteernal/math32}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150711git80dca99
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git80dca99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git80dca99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git80dca99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git80dca99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git80dca99
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jul 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.4.git80dca99
- Fix Exclusive arches for golang/openblas

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git80dca99
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git80dca99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git80dca99
- First package for Fedora
  resolves: #1269877
