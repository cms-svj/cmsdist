### RPM external CICADA 1.2.2
%define tag 2baca92cc3f6041e98d43c7391b9e7eba6ed249a
Source: git+https://github.com/cms-hls4ml/%{n}.git?obj=%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz
Requires: hls4mlEmulatorExtras hls
BuildRequires: gmake

%prep
%setup -n %{n}-%{realversion}

%build
make %{makeprocesses} EMULATOR_EXTRAS=${HLS4MLEMULATOREXTRAS_ROOT} HLS_ROOT=${HLS_ROOT}

%install
make PREFIX=%{i} install

