# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3
%global full_version 0.27.2
%global pkgname pyo3-0.27

Name:           rust-pyo3-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3
#!RemoteAsset:  sha256:ab53c047fcd1a1d2a8820fe84f05d6be69e9526be40cb03b73f86b6b03e6d87d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "pyo3".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
