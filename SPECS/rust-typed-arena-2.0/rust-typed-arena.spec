# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name typed-arena
%global full_version 2.0.2
%global pkgname typed-arena-2.0

Name:           rust-typed-arena-2
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "typed-arena"
License:        MIT
URL:            https://github.com/SimonSapin/rust-typed-arena
#!RemoteAsset:  sha256:6af6ae20167a9ece4bcb41af5b80f8a1f1df981f6391189ce00fd257af04126a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "typed-arena"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
