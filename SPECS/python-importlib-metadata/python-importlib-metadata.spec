# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname importlib-metadata

Name:           python-%{srcname}
Version:        8.7.1
Release:        %autorelease
Summary:        Read metadata from Python packages
License:        Apache-2.0
URL:            https://github.com/python/importlib_metadata
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/importlib_metadata-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  importlib_metadata

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(coherent-licensed)
BuildRequires:  python3dist(zipp)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A library to access the metadata for a Python package, providing a backport
of importlib.metadata from the standard library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
