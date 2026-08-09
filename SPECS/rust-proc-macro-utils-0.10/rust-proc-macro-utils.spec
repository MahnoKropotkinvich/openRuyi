# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-utils
%global full_version 0.10.0
%global pkgname proc-macro-utils-0.10

Name:           rust-proc-macro-utils-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-utils"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/proc-macro-utils
#!RemoteAsset:  sha256:eeaf08a13de400bc215877b5bdc088f241b12eb42f0a548d3390dc1c56bb7071
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-utils"

%package     -n %{name}+default
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parser) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Requires:       crate(%{pkgname}/proc-macro2) = %{version}
Requires:       crate(%{pkgname}/quote) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parser
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "parser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proc-macro2) = %{version}
Requires:       crate(%{pkgname}/smallvec) = %{version}
Provides:       crate(%{pkgname}/parser) = %{version}

%description -n %{name}+parser
This metapackage enables feature "parser" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro2
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "proc-macro2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/proc-macro2) = %{version}

%description -n %{name}+proc-macro2
This metapackage enables feature "proc-macro2" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "quote"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quote-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/quote) = %{version}

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/const-generics) >= 1.5.0
Requires:       crate(smallvec-1/default) >= 1.5.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
