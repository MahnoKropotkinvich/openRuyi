# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname peft

Name:           python-%{srcname}
Version:        0.18.1
Release:        %autorelease
Summary:        Parameter-Efficient Fine-Tuning of large pretrained models
License:        Apache-2.0
URL:            https://github.com/huggingface/peft
#!RemoteAsset:  sha256:2dd0d6bfce936d1850e48aaddbd250941c5c02fc8ef3237cd8fd5aac35e0bae2
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  peft
# bnb submodules require bitsandbytes which is not packaged
BuildOption(check):  -e 'peft.tuners.*.bnb*'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
# peft.tuners.lora.corda imports attr at top level (from attrs package)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(accelerate)
BuildRequires:  python3dist(safetensors)
BuildRequires:  python3dist(huggingface-hub)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PEFT (Parameter-Efficient Fine-Tuning) provides methods for efficiently
adapting large pretrained models to various downstream applications without
fine-tuning all of a model's parameters.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
