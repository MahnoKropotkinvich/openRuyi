# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-ffi
%global full_version 0.27.2
%global pkgname pyo3-ffi-0.27

Name:           rust-pyo3-ffi-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3-ffi"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pyo3-ffi
#!RemoteAsset:  sha256:1c85c9cbfaddf651b1221594209aed57e9e5cff63c4d11d1feead529b872a089
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "pyo3-ffi".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
