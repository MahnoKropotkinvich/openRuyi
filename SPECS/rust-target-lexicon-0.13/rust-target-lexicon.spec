# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name target-lexicon
%global full_version 0.13.4
%global pkgname target-lexicon-0.13

Name:           rust-target-lexicon-0.13
Version:        0.13.4
Release:        %autorelease
Summary:        Rust crate "target-lexicon"
License:        Apache-2.0 WITH LLVM-exception
URL:            https://crates.io/crates/target-lexicon
#!RemoteAsset
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for Rust crate "target-lexicon".

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
