# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zipp

Name:           python-%{srcname}
Version:        3.23.0
Release:        %autorelease
Summary:        Backport of pathlib-compatible object wrapper for zip files
License:        MIT
URL:            https://github.com/jaraco/zipp
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  zipp

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(coherent-licensed)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A pathlib-compatible Zipfile object wrapper. A backport of the Path object
from zipimport in Python 3.8.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
