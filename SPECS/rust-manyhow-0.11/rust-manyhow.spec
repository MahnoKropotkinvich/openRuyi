# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name manyhow
%global full_version 0.11.4
%global pkgname manyhow-0.11

Name:           rust-manyhow-0.11
Version:        0.11.4
Release:        %autorelease
Summary:        Rust crate "manyhow"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/manyhow
#!RemoteAsset:  sha256:b33efb3ca6d3b07393750d4030418d594ab1139cee518f0dc88db70fec873587
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.60
Requires:       crate(quote-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "manyhow"

%package     -n %{name}+darling-core
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "darling_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(darling-core-0.20/default) >= 0.20.1
Provides:       crate(%{pkgname}/darling) = %{version}
Provides:       crate(%{pkgname}/darling-core) = %{version}

%description -n %{name}+darling-core
This metapackage enables feature "darling_core" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "darling" feature.

%package     -n %{name}+default
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/syn) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(manyhow-macros-0.11/default) >= 0.11.4
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syn1
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "syn1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-1/printing) >= 1.0.0
Provides:       crate(%{pkgname}/syn1) = %{version}

%description -n %{name}+syn1
This metapackage enables feature "syn1" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syn2
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "syn2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Provides:       crate(%{pkgname}/syn) = %{version}
Provides:       crate(%{pkgname}/syn2) = %{version}

%description -n %{name}+syn2
This metapackage enables feature "syn2" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "syn" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
