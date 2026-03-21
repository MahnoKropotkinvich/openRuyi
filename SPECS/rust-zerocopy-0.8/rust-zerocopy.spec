# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy
%global full_version 0.8.37
%global pkgname zerocopy-0.8

Name:           rust-zerocopy-0.8
Version:        0.8.37
Release:        %autorelease
Summary:        Rust crate "zerocopy"
License:        BSD-2-Clause OR MIT OR Apache-2.0
URL:            https://crates.io/crates/zerocopy
#!RemoteAsset:  sha256:7456cf00f0685ad319c5b1693f291a650eaf345e941d082fc4e03df8a03996ac
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "zerocopy".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
