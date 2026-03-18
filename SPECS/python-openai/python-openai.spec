# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname openai

Name:           python-%{srcname}
Version:        2.28.0
Release:        %autorelease
Summary:        The official Python library for the OpenAI API
License:        Apache-2.0
URL:            https://github.com/openai/openai-python
#!RemoteAsset:  sha256:bb7fdff384d2a787fa82e8822d1dd3c02e8cf901d60f1df523b7da03cbb6d48d
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Backport to relax hatchling upper bound for the build
Patch2000:      2000-relax-hatchling-version-constraint.patch

BuildOption(install):  openai

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
# For import check: openai.helpers.microphone imports numpy at top level
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(jiter)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(sniffio)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The official Python library for the OpenAI API, providing convenient access
to the OpenAI REST API from Python applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/openai

%changelog
%autochangelog
