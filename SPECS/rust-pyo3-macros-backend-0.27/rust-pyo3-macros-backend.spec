# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.27.2
%global pkgname pyo3-macros-backend-0.27

Name:           rust-pyo3-macros-backend-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-macros-backend
#!RemoteAsset:  sha256:03b51720d314836e53327f5871d4c0cfb4fb37cc2c4a11cc71907a86342c40f9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "pyo3-macros-backend".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
