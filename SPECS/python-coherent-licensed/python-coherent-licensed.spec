# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname coherent-licensed
%global pypi_name coherent_licensed

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        License management tooling for Coherent System and skeleton projects
License:        MIT
URL:            https://github.com/coherent-oss/coherent.licensed
#!RemoteAsset:  sha256:d8071403ce742d3ac3592ddc4fb7057a46caffb415b928b4d52802e5f208416d
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  coherent

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
License management tooling for Coherent System and skeleton projects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
