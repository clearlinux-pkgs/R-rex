#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rex
Version  : 1.2.0
Release  : 13
URL      : https://cran.r-project.org/src/contrib/rex_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rex_1.2.0.tar.gz
Summary  : Friendly Regular Expressions
Group    : Development/Tools
License  : MIT
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-lazyeval
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-lazyeval
BuildRequires : buildreq-R

%description
# Rex
<!-- badges: start -->
[![Build Status](https://travis-ci.org/kevinushey/rex.png?branch=master)](https://travis-ci.org/kevinushey/rex)
[![codecov.io](https://codecov.io/github/kevinushey/rex/coverage.svg?branch=master)](https://codecov.io/github/kevinushey/rex?branch=master)
[![Lifecycle: stable](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://www.tidyverse.org/lifecycle/#stable)
<!-- badges: end -->

%prep
%setup -q -c -n rex
cd %{_builddir}/rex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589775631

%install
export SOURCE_DATE_EPOCH=1589775631
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rex
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rex || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rex/DESCRIPTION
/usr/lib64/R/library/rex/INDEX
/usr/lib64/R/library/rex/LICENSE
/usr/lib64/R/library/rex/Meta/Rd.rds
/usr/lib64/R/library/rex/Meta/features.rds
/usr/lib64/R/library/rex/Meta/hsearch.rds
/usr/lib64/R/library/rex/Meta/links.rds
/usr/lib64/R/library/rex/Meta/nsInfo.rds
/usr/lib64/R/library/rex/Meta/package.rds
/usr/lib64/R/library/rex/Meta/vignette.rds
/usr/lib64/R/library/rex/NAMESPACE
/usr/lib64/R/library/rex/NEWS.md
/usr/lib64/R/library/rex/R/rex
/usr/lib64/R/library/rex/R/rex.rdb
/usr/lib64/R/library/rex/R/rex.rdx
/usr/lib64/R/library/rex/doc/index.html
/usr/lib64/R/library/rex/doc/log_parsing.R
/usr/lib64/R/library/rex/doc/log_parsing.Rmd
/usr/lib64/R/library/rex/doc/log_parsing.html
/usr/lib64/R/library/rex/doc/url_parsing.R
/usr/lib64/R/library/rex/doc/url_parsing.Rmd
/usr/lib64/R/library/rex/doc/url_parsing.html
/usr/lib64/R/library/rex/help/AnIndex
/usr/lib64/R/library/rex/help/aliases.rds
/usr/lib64/R/library/rex/help/paths.rds
/usr/lib64/R/library/rex/help/rex.rdb
/usr/lib64/R/library/rex/help/rex.rdx
/usr/lib64/R/library/rex/html/00Index.html
/usr/lib64/R/library/rex/html/R.css
/usr/lib64/R/library/rex/tests/testthat.R
/usr/lib64/R/library/rex/tests/testthat/test-aaa.R
/usr/lib64/R/library/rex/tests/testthat/test-capture.R
/usr/lib64/R/library/rex/tests/testthat/test-character_class.R
/usr/lib64/R/library/rex/tests/testthat/test-common.R
/usr/lib64/R/library/rex/tests/testthat/test-counts.R
/usr/lib64/R/library/rex/tests/testthat/test-escape.R
/usr/lib64/R/library/rex/tests/testthat/test-lookarounds.R
/usr/lib64/R/library/rex/tests/testthat/test-match.R
/usr/lib64/R/library/rex/tests/testthat/test-or.R
/usr/lib64/R/library/rex/tests/testthat/test-print.R
/usr/lib64/R/library/rex/tests/testthat/test-rex_mode.R
/usr/lib64/R/library/rex/tests/testthat/test-shortcuts.R
/usr/lib64/R/library/rex/tests/testthat/test-wildcards.R
