# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname referencing

Name:           python-%{srcname}
Version:        0.37.0
Release:        %autorelease
Summary:        Cross-specification JSON referencing
License:        MIT
URL:            https://github.com/python-jsonschema/referencing
#!RemoteAsset:  sha256:44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  referencing
# test_referencing_suite requires a full git checkout of the suite; skip it
BuildOption(check):  -e referencing.tests*

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(rpds-py)
BuildRequires:  python3dist(hatch-vcs)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An implementation-agnostic Python library for resolving JSON references
across JSON Schema specifications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING

%changelog
%autochangelog
