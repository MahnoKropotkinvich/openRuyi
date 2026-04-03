# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-traits
%global full_version 0.2.19
%global pkgname num-traits-0.2

Name:           rust-num-traits-0.2
Version:        0.2.19
Release:        %autorelease
Summary:        Rust crate "num-traits"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-traits
#!RemoteAsset:  sha256:071dfc062690e90b734c0b2273ce72ad0ffa95f0c74596bc250dcfd960262841
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "num-traits".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
