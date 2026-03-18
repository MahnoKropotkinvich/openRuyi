# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opentelemetry-api

Name:           python-%{srcname}
Version:        1.40.0
Release:        %autorelease
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/opentelemetry_api-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l opentelemetry

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(importlib-metadata)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
OpenTelemetry Python API provides the interfaces and no-op implementations
for the OpenTelemetry observability framework, enabling distributed tracing,
metrics, and logging in Python applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
