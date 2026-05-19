# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name interpolator
%global full_version 0.5.0
%global pkgname interpolator-0.5

Name:           rust-interpolator-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "interpolator"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/interpolator
#!RemoteAsset:  sha256:71dd52191aae121e8611f1e8dc3e324dd0dd1dee1e6dd91d10ee07a3cfb4d9d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/iter) = %{version}
Provides:       crate(%{pkgname}/number) = %{version}
Provides:       crate(%{pkgname}/pointer) = %{version}

%description
Source code for takopackized Rust crate "interpolator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
