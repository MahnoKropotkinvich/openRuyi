# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonschema-specifications

Name:           python-%{srcname}
Version:        2025.9.1
Release:        %autorelease
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema-specifications
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/jsonschema_specifications-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  jsonschema_specifications

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  pytest
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(referencing)
BuildRequires:  python3dist(hatch-vcs)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The JSON Schema meta-schemas and vocabularies, exposed as a referencing-based
Registry.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING

%changelog
%{?autochangelog}
