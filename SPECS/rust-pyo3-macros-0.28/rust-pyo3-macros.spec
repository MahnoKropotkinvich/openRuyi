# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros
%global full_version 0.28.0
%global pkgname pyo3-macros-0.28

Name:           rust-pyo3-macros-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "pyo3-macros"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-macros
#!RemoteAsset:  sha256:11ce9cc8d81b3c4969748807604d92b4eef363c5bb82b1a1bdb34ec6f1093a18
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "pyo3-macros".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
