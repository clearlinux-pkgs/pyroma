#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroma
Version  : 2.6
Release  : 10
URL      : https://files.pythonhosted.org/packages/3e/2e/6a4e59afc16a56677d6e828f32a98c953f04b62f904acf2488e16c836612/pyroma-2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/2e/6a4e59afc16a56677d6e828f32a98c953f04b62f904acf2488e16c836612/pyroma-2.6.tar.gz
Summary  : Test your project's packaging friendliness
Group    : Development/Tools
License  : MIT
Requires: pyroma-bin = %{version}-%{release}
Requires: pyroma-license = %{version}-%{release}
Requires: pyroma-python = %{version}-%{release}
Requires: pyroma-python3 = %{version}-%{release}
Requires: Pygments
Requires: docutils
Requires: setuptools
Requires: zope.event
BuildRequires : Pygments
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : setuptools
BuildRequires : util-linux
BuildRequires : zope.event

%description
======
        
        Pyroma rhymes with aroma, and is a product aimed at giving a rating of how well
        a Python project complies with the best practices of the Python packaging
        ecosystem, primarily PyPI, pip, Distribute etc, as well as a list of issues that
        could be improved.
        
        The aim of this is both to help people make a project that is nice and usable,
        but also to improve the quality of Python third-party software, making it easier
        and more enjoyable to use the vast array of available modules for Python.
        
        It's written so that there are a library with methods to call from Python, as
        well as a script, also called pyroma.

%package bin
Summary: bin components for the pyroma package.
Group: Binaries
Requires: pyroma-license = %{version}-%{release}

%description bin
bin components for the pyroma package.


%package license
Summary: license components for the pyroma package.
Group: Default

%description license
license components for the pyroma package.


%package python
Summary: python components for the pyroma package.
Group: Default
Requires: pyroma-python3 = %{version}-%{release}

%description python
python components for the pyroma package.


%package python3
Summary: python3 components for the pyroma package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyroma package.


%prep
%setup -q -n pyroma-2.6
cd %{_builddir}/pyroma-2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576014069
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyroma
cp %{_builddir}/pyroma-2.6/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyroma/b0fc0d8365766fe5b3c0ed32016393c8441272d7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyroma

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyroma/b0fc0d8365766fe5b3c0ed32016393c8441272d7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
