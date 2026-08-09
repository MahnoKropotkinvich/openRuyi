# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minicov
%global full_version 0.3.7
%global pkgname minicov-0.3

Name:           rust-minicov-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "minicov"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/minicov
#!RemoteAsset:  sha256:f27fe9f1cc3c22e1687f9446c2083c4c5fc7f0bcf1c7a86bdbded14985895b4b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.77
Requires:       crate(walkdir-2) >= 2.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "minicov"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
