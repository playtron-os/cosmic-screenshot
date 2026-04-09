%global app_name cosmic-screenshot
%global debug_package %{nil}

Name:           %{app_name}
Epoch:          1
Version: 1.0.1
Release:        1%{?dist}
Summary:        Screenshot Utility (Playtron fork)

License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-screenshot
Source0:        %{name}-%{_arch}.tar.gz

# No BuildRequires - binary is pre-built

# Disable automatic dependency detection for Rust binaries
AutoReqProv:    no

# Override the upstream cosmic-screenshot
Provides:       cosmic-screenshot = %{epoch}:%{version}-%{release}
Obsoletes:      cosmic-screenshot < %{epoch}:%{version}

%description
Screenshot utility for the COSMIC desktop environment.

%prep
%autosetup -n %{name} -p1

%build

%install
install -Dm0755 "usr/bin/cosmic-screenshot" "%{buildroot}%{_bindir}/cosmic-screenshot"
install -Dm0644 "usr/share/applications/com.system76.CosmicScreenshot.desktop" "%{buildroot}%{_datadir}/applications/com.system76.CosmicScreenshot.desktop"
install -Dm0644 "usr/share/licenses/cosmic-screenshot/LICENSE" "%{buildroot}%{_datadir}/licenses/cosmic-screenshot/LICENSE"

# Install icons
install -Dm0644 "usr/share/icons/hicolor/16x16/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicScreenshot.svg"
install -Dm0644 "usr/share/icons/hicolor/24x24/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicScreenshot.svg"
install -Dm0644 "usr/share/icons/hicolor/32x32/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicScreenshot.svg"
install -Dm0644 "usr/share/icons/hicolor/48x48/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicScreenshot.svg"
install -Dm0644 "usr/share/icons/hicolor/64x64/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicScreenshot.svg"
install -Dm0644 "usr/share/icons/hicolor/128x128/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicScreenshot.svg"
install -Dm0644 "usr/share/icons/hicolor/256x256/apps/com.system76.CosmicScreenshot.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicScreenshot.svg"

%files
%license %{_datadir}/licenses/cosmic-screenshot/LICENSE
%{_bindir}/cosmic-screenshot
%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicScreenshot.svg

%changelog
* Thu Mar 27 2026 Playtron <dev@playtron.one> - 0.1.0-1
- Initial RPM package for Playtron fork
