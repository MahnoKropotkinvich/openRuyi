# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros
%global full_version 0.27.2
%global pkgname pyo3-macros-0.27

Name:           rust-pyo3-macros-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3-macros"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-macros
#!RemoteAsset:  sha256:0a5b10c9bf9888125d917fb4d2ca2d25c8df94c7ab5a52e13313a07e050a3b02
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
