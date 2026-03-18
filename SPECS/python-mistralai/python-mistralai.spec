# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mistralai

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
Summary:        Python Client SDK for the Mistral AI API
License:        Apache-2.0
URL:            https://github.com/mistralai/client-python
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         0001-relax-opentelemetry-semantic-conventions-upper-bound.patch
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  mistralai
BuildOption(check):  -e 'mistralai.gcp*' -e 'mistralai.extra*'

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(eval-type-backport)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(opentelemetry-semantic-conventions)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(typing-inspection)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The official Python client SDK for the Mistral AI API, providing access to
Mistral's language models for chat, embeddings, and other AI capabilities.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
