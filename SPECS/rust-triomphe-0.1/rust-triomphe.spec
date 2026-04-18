# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name triomphe
%global full_version 0.1.15
%global pkgname triomphe-0.1

Name:           rust-triomphe-0.1
Version:        0.1.15
Release:        %autorelease
Summary:        Rust crate "triomphe"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/triomphe
#!RemoteAsset:  sha256:dd69c5aa8f924c7519d6372789a74eac5b94fb0f8fcf0d4a97eb0bfc3e785f39
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "triomphe".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
