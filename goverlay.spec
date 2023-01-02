Name:           goverlay
Version:        0.9.1
Release:        %mkrel 1
Summary:        Graphical UI to help manage Vulkan/OpenGL overlays
Group:          Graphics/Utilities
License:        GPLv3
URL:            https://github.com/benjamimgois/goverlay
Source0:        https://github.com/benjamimgois/goverlay/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         goverlay-enable-debuginfo-generation.patch

BuildRequires:  lazarus
Requires:       mangohud

Recommends:     git
Recommends:     mesa-demos
Recommends:     vkbasalt
Recommends:     vulkan-tools

%description
GOverlay is an opensource project that aims to create a graphical UI to
help manage Vulkan/OpenGL overlays. Currently supported:

- MangoHUD
- vkBasalt

%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install prefix=%{_prefix}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/metainfo/%{rdnsname}.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1.*
