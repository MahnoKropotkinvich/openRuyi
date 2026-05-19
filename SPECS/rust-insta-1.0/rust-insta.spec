# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name insta
%global full_version 1.47.2
%global pkgname insta-1.0

Name:           rust-insta-1
Version:        1.47.2
Release:        %autorelease
Summary:        Rust crate "insta"
License:        Apache-2.0
URL:            https://insta.rs/
#!RemoteAsset:  sha256:7b4a6248eb93a4401ed2f37dfe8ea592d3cf05b7cf4f8efa867b6895af7e094e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.20.2
Requires:       crate(similar-2/default) >= 2.1.0
Requires:       crate(similar-2/inline) >= 2.1.0
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "insta"

%package     -n %{name}+clap
Summary:        Snapshot testing library for Rust - feature "clap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.1.0
Requires:       crate(clap-4/derive) >= 4.1.0
Requires:       crate(clap-4/env) >= 4.1.0
Provides:       crate(%{pkgname}/cargo-insta-internal) = %{version}
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "_cargo_insta_internal" feature.

%package     -n %{name}+console
Summary:        Snapshot testing library for Rust - feature "console" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(console-0.16/std) >= 0.16.0
Provides:       crate(%{pkgname}/colors) = %{version}
Provides:       crate(%{pkgname}/console) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+console
This metapackage enables feature "console" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "colors", and "default" features.

%package     -n %{name}+csv
Summary:        Snapshot testing library for Rust - feature "csv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(csv-1/default) >= 1.1.6
Provides:       crate(%{pkgname}/csv) = %{version}

%description -n %{name}+csv
This metapackage enables feature "csv" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glob
Summary:        Snapshot testing library for Rust - feature "glob"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/globset) = %{version}
Requires:       crate(%{pkgname}/walkdir) = %{version}
Provides:       crate(%{pkgname}/glob) = %{version}

%description -n %{name}+glob
This metapackage enables feature "glob" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+globset
Summary:        Snapshot testing library for Rust - feature "globset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(globset-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/globset) = %{version}

%description -n %{name}+globset
This metapackage enables feature "globset" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pest
Summary:        Snapshot testing library for Rust - feature "pest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-2/default) >= 2.1.3
Provides:       crate(%{pkgname}/pest) = %{version}

%description -n %{name}+pest
This metapackage enables feature "pest" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pest-derive
Summary:        Snapshot testing library for Rust - feature "pest_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-derive-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/pest-derive) = %{version}

%description -n %{name}+pest-derive
This metapackage enables feature "pest_derive" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+redactions
Summary:        Snapshot testing library for Rust - feature "redactions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pest) = %{version}
Requires:       crate(%{pkgname}/pest-derive) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/redactions) = %{version}

%description -n %{name}+redactions
This metapackage enables feature "redactions" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Snapshot testing library for Rust - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/std) >= 1.6.0
Requires:       crate(regex-1/unicode) >= 1.6.0
Provides:       crate(%{pkgname}/filters) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "filters" feature.

%package     -n %{name}+ron
Summary:        Snapshot testing library for Rust - feature "ron"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(ron-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/ron) = %{version}

%description -n %{name}+ron
This metapackage enables feature "ron" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Snapshot testing library for Rust - feature "serde" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.117
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/yaml) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json", and "yaml" features.

%package     -n %{name}+toml
Summary:        Snapshot testing library for Rust - feature "toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(toml-edit-0.25/default) >= 0.25.0
Requires:       crate(toml-edit-0.25/display) >= 0.25.0
Requires:       crate(toml-edit-0.25/parse) >= 0.25.0
Requires:       crate(toml-edit-0.25/serde) >= 0.25.0
Requires:       crate(toml-writer-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/toml) = %{version}

%description -n %{name}+toml
This metapackage enables feature "toml" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Snapshot testing library for Rust - feature "walkdir"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(walkdir-2/default) >= 2.3.1
Provides:       crate(%{pkgname}/walkdir) = %{version}

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
