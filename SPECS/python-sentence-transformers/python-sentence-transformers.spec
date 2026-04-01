# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sentence-transformers

Name:           python-%{srcname}
Version:        5.3.0
Release:        %autorelease
Summary:        Embeddings, Retrieval, and Reranking
License:        Apache-2.0
URL:            https://www.sbert.net
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/sentence_transformers-%{version}.tar.gz
# check_package_availability() raises KeyError/TypeError when a package's
# metadata lacks the "Home-page" field (e.g. importlib_metadata backend).
Patch0:         0001-fix-check_package_availability-KeyError-on-missing-Home-page.patch
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  sentence_transformers

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(huggingface-hub)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Sentence Transformers is a Python library for state-of-the-art sentence, text,
and image embeddings. It can be used to compute embeddings for sentences and
paragraphs, and to find semantically similar sentences using cosine similarity.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
