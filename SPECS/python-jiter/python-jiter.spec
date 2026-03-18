# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jiter

Name:           python-%{srcname}
Version:        0.13.0
Release:        %autorelease
Summary:        Fast iterable JSON parser
License:        MIT
URL:            https://github.com/pydantic/jiter
#!RemoteAsset:  sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  jiter

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  python3dist(maturin)
# Rust crate dependencies
BuildRequires:  crate(pyo3-0.28/default)
BuildRequires:  crate(num-bigint-0.4/default)
BuildRequires:  crate(num-traits-0.2/default)
BuildRequires:  crate(ahash-0.8/default)
BuildRequires:  crate(smallvec-1.0/default)
BuildRequires:  crate(lexical-parse-float-1.0/default)
BuildRequires:  crate(bitvec-1.0/default)
BuildRequires:  crate(pyo3-build-config-0.28/default)
BuildRequires:  crate(python3-dll-a-0.2/default) >= 0.2.12
# Rust dev-dependencies required by cargo metadata during buildrequire generation
BuildRequires:  crate(codspeed-criterion-compat-2.0/default)
BuildRequires:  crate(paste-1.0/default)
BuildRequires:  crate(pyo3-0.28/auto-initialize)
BuildRequires:  crate(serde-1.0/default)
BuildRequires:  crate(serde-json-1.0/arbitrary-precision)
BuildRequires:  crate(serde-json-1.0/default)
BuildRequires:  crate(serde-json-1.0/float-roundtrip)
BuildRequires:  crate(serde-json-1.0/preserve-order)

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
A fast iterable JSON parser written in Rust, used as the JSON parsing backend
for pydantic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
