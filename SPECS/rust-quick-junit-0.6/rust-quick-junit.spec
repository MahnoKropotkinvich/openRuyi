# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quick-junit
%global full_version 0.6.0
%global pkgname quick-junit-0.6

Name:           rust-quick-junit-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "quick-junit"
License:        Apache-2.0 OR MIT
URL:            https://github.com/nextest-rs/quick-junit
#!RemoteAsset:  sha256:e3e64c58c4c88fc1045e8fe98a1b7cec3643187e3dd678f9bbcdd8f12a6933d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chrono-0.4/std) >= 0.4.44
Requires:       crate(indexmap-2/default) >= 2.11.4
Requires:       crate(newtype-uuid-1/default) >= 1.3.2
Requires:       crate(quick-xml-0.38/default) >= 0.38.4
Requires:       crate(strip-ansi-escapes-0.2/default) >= 0.2.1
Requires:       crate(thiserror-2/default) >= 2.0.17
Requires:       crate(uuid-1/default) >= 1.17.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quick-junit"

%package     -n %{name}+internal-testing
Summary:        Data model, serializer, and deserializer for JUnit/XUnit XML - feature "internal-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proptest) = %{version}
Requires:       crate(xxhash-rust-0.8/default) >= 0.8.15
Requires:       crate(xxhash-rust-0.8/xxh3) >= 0.8.15
Provides:       crate(%{pkgname}/internal-testing) = %{version}

%description -n %{name}+internal-testing
This metapackage enables feature "internal-testing" for the Rust quick-junit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Data model, serializer, and deserializer for JUnit/XUnit XML - feature "proptest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(newtype-uuid-1/proptest1) >= 1.3.2
Requires:       crate(proptest-1/default) >= 1.7.0
Requires:       crate(test-strategy-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/proptest) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust quick-junit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
