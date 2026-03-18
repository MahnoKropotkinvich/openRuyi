# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rpds-py
%global pypi_name rpds_py

Name:           python-%{srcname}
Version:        0.30.0
Release:        %autorelease
Summary:        Python bindings to Rust's persistent data structures (rpds)
License:        MIT
URL:            https://github.com/crate-py/rpds
#!RemoteAsset:  sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  rpds

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  python3dist(maturin)
# Rust crate dependencies
BuildRequires:  crate(rpds-1.0/default)
BuildRequires:  crate(archery-1.0/default)
BuildRequires:  crate(triomphe-0.1/default)
BuildRequires:  crate(pyo3-0.27/default)
BuildRequires:  crate(pyo3-0.27/extension-module)
BuildRequires:  crate(pyo3-0.27/generate-import-lib)
BuildRequires:  crate(pyo3-build-config-0.27/default)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%prep -a
rm -f Cargo.lock
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

%description
Python bindings to the Rust rpds crate, which provides persistent (immutable)
data structures including hash tries, red-black trees, and lists.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
