# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonschema-specifications
%global pypi_name jsonschema_specifications

Name:           python-%{srcname}
Version:        2025.9.1
Release:        %autorelease
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema-specifications
#!RemoteAsset:  sha256:b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  jsonschema_specifications

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(referencing)
BuildRequires:  python3dist(hatch-vcs)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The JSON Schema meta-schemas and vocabularies, exposed as a referencing-based
Registry.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING

%changelog
%autochangelog
