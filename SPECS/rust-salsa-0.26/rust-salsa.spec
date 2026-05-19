# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa
%global full_version 0.26.2
%global pkgname salsa-0.26

Name:           rust-salsa-0.26
Version:        0.26.2
Release:        %autorelease
Summary:        Rust crate "salsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/salsa-rs/salsa
#!RemoteAsset:  sha256:4612ff789805e65c87e9b38cb749a293212a615af065bed8a2001086801498c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(boxcar-0.2/default) >= 0.2.14
Requires:       crate(crossbeam-queue-0.3/default) >= 0.3.12
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.21
Requires:       crate(hashbrown-0.17/default) >= 0.17.0
Requires:       crate(hashlink-0.10/default) >= 0.10.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(intrusive-collections-0.9/default) >= 0.9.7
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(portable-atomic-1/default) >= 1.0.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(salsa-macro-rules-0.26/default) >= 0.26.2
Requires:       crate(salsa-macros-0.26/default) >= 0.26.2
Requires:       crate(smallvec-1/const-new) >= 1.0.0
Requires:       crate(smallvec-1/default) >= 1.0.0
Requires:       crate(thin-vec-0.2/default) >= 0.2.14
Requires:       crate(tracing-0.1/std) >= 0.1.0
Requires:       crate(typeid-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/salsa-unstable) = %{version}

%description
Source code for takopackized Rust crate "salsa"

%package     -n %{name}+accumulator
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "accumulator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(salsa-macro-rules-0.26/accumulator) >= 0.26.2
Provides:       crate(%{pkgname}/accumulator) = %{version}

%description -n %{name}+accumulator
This metapackage enables feature "accumulator" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compact-str
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "compact_str"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compact-str-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/compact-str) = %{version}

%description -n %{name}+compact-str
This metapackage enables feature "compact_str" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/accumulator) = %{version}
Requires:       crate(%{pkgname}/inventory) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/salsa-unstable) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inventory
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "inventory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(inventory-0.3/default) >= 0.3.24
Provides:       crate(%{pkgname}/inventory) = %{version}

%description -n %{name}+inventory
This metapackage enables feature "inventory" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(salsa-macros-0.26/default) >= 0.26.2
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ordermap
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "ordermap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ordermap-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/ordermap) = %{version}

%description -n %{name}+ordermap
This metapackage enables feature "ordermap" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+persistence
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "persistence"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(erased-serde-0.4/default) >= 0.4.6
Requires:       crate(salsa-macros-0.26/persistence) >= 0.26.2
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(thin-vec-0.2/serde) >= 0.2.14
Provides:       crate(%{pkgname}/persistence) = %{version}

%description -n %{name}+persistence
This metapackage enables feature "persistence" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shuttle
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "shuttle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(shuttle-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/shuttle) = %{version}

%description -n %{name}+shuttle
This metapackage enables feature "shuttle" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
