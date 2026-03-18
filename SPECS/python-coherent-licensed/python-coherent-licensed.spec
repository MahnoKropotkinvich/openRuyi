# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname coherent.licensed

Name:           python-coherent-licensed
Version:        0.5.2
Release:        %autorelease
Summary:        License management tooling for Coherent System and skeleton projects
License:        MIT
URL:            https://github.com/coherent-oss/coherent.licensed
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/coherent_licensed-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  coherent

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)

Provides:       python3-coherent-licensed
%python_provide python3-coherent-licensed

%description
License management tooling for Coherent System and skeleton projects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
