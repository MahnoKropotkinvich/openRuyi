# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name manyhow-macros
%global full_version 0.11.4
%global pkgname manyhow-macros-0.11

Name:           rust-manyhow-macros-0.11
Version:        0.11.4
Release:        %autorelease
Summary:        Rust crate "manyhow-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/manyhow
#!RemoteAsset:  sha256:46fce34d199b78b6e6073abf984c9cf5fd3e9330145a93ee0738a7443e371495
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-utils-0.10/default) >= 0.10.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "manyhow-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
