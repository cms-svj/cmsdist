### RPM external pythia8 240

%define tag bc4d696a8ac4e69943db8954dca3b16323ee577a
%define branch cms/%{realversion}
%define github_user cms-externals
Source: git+https://github.com/%github_user/%{n}.git?obj=%{branch}/%{tag}&export=%{n}%{realversion}&output=/%{n}-%{realversion}.tgz
Patch0: slhainterface

Requires: hepmc lhapdf

%prep
%setup -q -n %{n}%{realversion}
%patch0 -p1

./configure --prefix=%i --enable-shared --with-hepmc2=${HEPMC_ROOT} --with-lhapdf6=${LHAPDF_ROOT}

%build
make %makeprocesses

%install
make install
test -f %i/lib/libpythia8lhapdf6.so || exit 1
