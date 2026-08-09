# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name insta-cmd
%global full_version 0.6.0
%global pkgname insta-cmd-0.6

Name:           rust-insta-cmd-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "insta-cmd"
License:        Apache-2.0
URL:            https://insta.rs/
#!RemoteAsset:  sha256:ffeeefa927925cced49ccb01bf3e57c9d4cd132df21e576eb9415baeab2d3de6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(insta-1/default) >= 1.29.0
Requires:       crate(insta-1/serde) >= 1.29.0
Requires:       crate(serde-1/default) >= 1.0.139
Requires:       crate(serde-1/derive) >= 1.0.139
Requires:       crate(serde-json-1/default) >= 1.0.82
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "insta-cmd"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
