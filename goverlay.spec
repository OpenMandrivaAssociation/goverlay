%define _empty_manifest_terminate_build 0
Name:           goverlay
Version:        1.7.1
Release:        1
Summary:        Graphical UI to help manage Vulkan/OpenGL overlays
Group:          Graphics/Utilities
License:        GPLv3
URL:            https://github.com/benjamimgois/goverlay
Source0:        https://github.com/benjamimgois/goverlay/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:  lazarus
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
Requires:       mangohud
Requires:       (p7zip or 7zip)
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

sed -i 's/qt5/qt6/' goverlay.lpi

%build
%set_build_flags
%make_build

%install
%make_install prefix=%{_prefix}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1.*
