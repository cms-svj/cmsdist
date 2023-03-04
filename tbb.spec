### RPM external tbb v2021.8.0

%define tag %{realversion}
%define branch onetbb_2021
%define github_user oneapi-src
%define github_repo oneTBB
Source: git+https://github.com/%{github_user}/%{github_repo}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{branch}-%{tag}.tgz
Source3: tbb_modulemap
Patch0: tbb-782
Requires: hwloc
BuildRequires: cmake

%prep
%setup -n %{n}-%{realversion}
%patch0 -p1

%build
rm -rf %{_builddir}/build
mkdir %{_builddir}/build

cd %{_builddir}/build
cmake ../%{n}-%{realversion} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_STANDARD=17 \
  -DCMAKE_INSTALL_PREFIX=%{i} \
  -DCMAKE_INSTALL_LIBDIR=lib \
  -DCMAKE_HWLOC_2_5_INCLUDE_PATH=$HWLOC_ROOT/include \
  -DCMAKE_HWLOC_2_5_LIBRARY_PATH=$HWLOC_ROOT/lib/libhwloc.so \
  -DTBB_CPF=ON

make %{makeprocesses}

%install
cd %{_builddir}/build
make install
ls
ls %{i}

cp %{_sourcedir}/tbb_modulemap  %{i}/include/module.modulemap
ls ../%{n}-%{realversion}/include/tbb
