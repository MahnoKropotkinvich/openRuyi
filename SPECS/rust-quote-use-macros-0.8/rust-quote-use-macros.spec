# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quote-use-macros
%global full_version 0.8.4
%global pkgname quote-use-macros-0.8

Name:           rust-quote-use-macros-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "quote-use-macros"
License:        MIT
URL:            https://github.com/ModProg/quote-use
#!RemoteAsset:  sha256:82ebfb7faafadc06a7ab141a6f67bcfb24cb8beb158c6fe933f2f035afa99f35
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-utils-0.10/default) >= 0.10.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/clone-impls) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quote-use-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
