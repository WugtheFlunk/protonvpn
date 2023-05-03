%define unmangled_name protonvpn-cli
%define version 3.13.0
%define release 2

Prefix: %{_prefix}

Name: protonvpn-cli
Version: %{version}
Release: %{release}
Summary: Official ProtonVPN CLI

Group: Proton VPN
License: GPLv3
Url: https://github.com/ProtonVPN
Vendor: Proton Technologies AG <opensource@proton.me>
Source0: %{unmangled_name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{unmangled_name}-%{version}-%{release}-buildroot

BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-protonvpn-nm-lib
Requires: python3-dialog

%{?python_disable_dependency_generator}

%description
Official Proton VPN CLI.


%prep
%setup -n %{unmangled_name}-%{version} -n %{unmangled_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%{python3_sitelib}/protonvpn_cli/
%{python3_sitelib}/protonvpn_cli-%{version}*.egg-info/
%defattr(-,root,root)

%changelog
* Thu Sep 22 2022 Proton Technologies AG <opensource@proton.me> 3.13.0-2
- Drop F34-35 and add F37

* Thu Sep 01 2022 Proton Technologies AG <opensource@proton.me> 3.13.0-1
- Fix: If session is invalid, inform the user about it.

* Thu May 19 2022 Proton Technologies AG <opensource@proton.me> 3.12.0-1
- Introducing Proton's refreshed look. As we continue to make privacy accessible to everyone, we've updated our apps to provide you with an even better experience with our services. Proton - Privacy by default

* Thu Dez 16 2021 Proton Technologies AG <opensource@proton.me> 3.11.1-4
- Bugfix: Display message when incorrectly formatted servername is provided
- Feature: Moderate NAT, Non Standard Ports

* Thu Nov 12 2021 Proton Technologies AG <opensource@proton.me> 3.11.0-7
- Improve: Handle accounting use cases

* Fri Sep 24 2021 Proton Technologies AG <opensource@proton.me> 3.10.1-1
- Improve: Exception handling

* Fri Sep 24 2021 Proton Technologies AG <opensource@proton.me> 3.10.0-1
- Handle human verification

* Thu Sep 30 2021 Proton Technologies AG <opensource@proton.me> 3.9.1-1
- Fix: VPN Accelerator setting (unable to either disable or enable it)

* Mon Aug 09 2021 Proton Technologies AG <opensource@proton.me> 3.9.0-1
- Feature: Add alternative routing option

* Fri Jun 16 2021 Proton Technologies AG <opensource@proton.me> 3.8.0-2
- Fix: When adding custom DNS IP it will no longer automatically set "automatic DNS"
- Fix: Add VPN Accelerator setting 
- Feature: Add alternative routing option

* Mon Jun 28 2021 Proton Technologies AG <opensource@proton.me> 3.7.2-2
- Fix: Update README.md and create USAGE.md

* Tue Jun 22 2021 Proton Technologies AG <opensource@proton.me> 3.7.1-1
- Hotfix: Display force disable connectivity check message in case of failure

* Fri Jun 18 2021 Proton Technologies AG <opensource@proton.me> 3.7.0-3
- Feature: Generate and provide easy access to logs

* Fri May 21 2021 Proton Technologies AG <opensource@proton.me> 3.6.0-5
- Update to latest library version (3.2.0 =< and < 3.3.0)

* Thu May 20 2021 Proton Technologies AG <opensource@proton.me> 3.5.3-2
- Bugfix: fixed crash when trying to display netshield help

* Wed May 19 2021 Proton Technologies AG <opensource@proton.me> 3.5.2-2
- Bugfix: fixed crash when trying to display netshield status

* Fri Apr 30 2021 Proton Technologies AG <opensource@proton.me> 3.5.1-1
- Update dependency (protonvpn-nm-lib) version

* Tue Mar 30 2021 Proton Technologies AG <opensource@proton.me> 3.5.0-2
- Handle servers with multiple features
- Fix server feature issue when displaying connection status

* Tue Mar 30 2021 Proton Technologies AG <opensource@proton.me> 3.4.1-4
- Fix dialog crash
- Remove "-" when displaying DNS servers after being added
- Add "config --list" to help message
- User CLI logger instead of lib logger
- Catch unexpected exceptions upon setting up reconnect and upon connect()
- Adopt new library exceptions for improved error handling
- Add confirmation upon logout if VPN is active
- Replace always-on for permanent

* Fri Feb 26 2021 Proton Technologies AG <opensource@proton.me> 3.4.0-3
- Add support for protonvpn-nm-lib 0.5.0
- Replace os.system for custom subprocess wrapper

* Thu Feb 25 2021 Proton Technologies AG <opensource@proton.me> 3.3.1-1
- Update change for protonvpn-nm-lib 0.4.2

* Tue Feb 02 2021 Proton Technologies AG <opensource@proton.me> 3.3.0-1
- Apply server label if it exists

* Wed Jan 27 2021 Proton Technologies AG <opensource@proton.me> 3.2.1-2
- Update .spec file for public release
