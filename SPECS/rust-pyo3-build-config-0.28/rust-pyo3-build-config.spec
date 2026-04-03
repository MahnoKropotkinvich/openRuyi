# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.28.0
%global pkgname pyo3-build-config-0.28

Name:           rust-pyo3-build-config-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-build-config
#!RemoteAsset:  sha256:972720a441c91fd9c49f212a1d2d74c6e3803b231ebc8d66c51efbd7ccab11c8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "pyo3-build-config".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
