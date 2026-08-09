# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa-macros
%global full_version 0.26.2
%global pkgname salsa-macros-0.26

Name:           rust-salsa-macros-0.26
Version:        0.26.2
Release:        %autorelease
Summary:        Rust crate "salsa-macros"
License:        Apache-2.0 OR MIT
URL:            https://github.com/salsa-rs/salsa
#!RemoteAsset:  sha256:3067861075c2b80608f84ad49fb88f2c7610b94cdf8b4201e79ddee87f8980c8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.104
Requires:       crate(syn-2/full) >= 2.0.104
Requires:       crate(syn-2/visit-mut) >= 2.0.104
Requires:       crate(synstructure-0.13/default) >= 0.13.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/persistence) = %{version}

%description
Source code for takopackized Rust crate "salsa-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
