%define with_kpilot 1
%{?_with_kpilot: %{expand: %%global with_kpilot 1}}

%define with_kmobiletools 0
%{?_with_kmobiletools: %{expand: %%global with_kmobiletools 1}}

%define with_kitchensync 0
%{?_with_kitchensync: %{expand: %%global with_kitchensync 1}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define dont_strip 1
%endif

%define kderevision svn961800

Name: kdepim4
Summary: K Desktop Environment
Version: 4.2.85
Release: %mkrel 2
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://pim.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.tar.bz2
# Mandriva "customization" patches
Patch0:   kdepim-4.0.83-fix-desktop-files.patch
Patch1:   kdepim-4.0.98-fix-autostart.patch
Patch2:   kdepim-4.2.1-kmail-first-message.patch 
Buildroot:     %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.1.81
BuildRequires: kdepimlibs4-devel >= 2:4.1.81
BuildRequires: gpgme-devel 
BuildRequires: X11-devel 
BuildRequires: flex 
BuildRequires: byacc 
BuildRequires: pam
BuildRequires: libncurses-devel
BuildRequires: readline-devel
BuildRequires: pilot-link-devel
BuildRequires: libgpg-error-devel
BuildRequires: gnokii-devel >= 0.6.18
BuildRequires: libxml2-utils
BuildRequires: gnupg
BuildRequires: bluez-devel 
BuildRequires: libsasl-devel
BuildRequires: pilot-link-devel
BuildRequires: libxslt-proc
BuildRequires: boost-devel
BuildRequires: qca2-devel
BuildRequires: glib2-devel
BuildRequires: libassuan-devel
BuildRequires: mysql-static-devel
BuildRequires: libmal-devel
BuildRequires: soprano-devel
BuildRequires: automoc
%if %{with_kitchensync}
BuildRequires: libopensync-devel >= 0.30
%endif
BuildRequires: akonadi-devel
#FIXME: Remove later
BuildRequires: kdepimlibs4-core
Suggests:      akonadi-common
Suggests:      kleopatra
Suggests:      akregator
%if %{with_kitchensync}
Suggests:      kitchensync
%endif
Suggests: knode
Suggests: kaddressbook
Suggests: kalarm
Suggests: ktimetracker
Suggests: kmail
Suggests: kmailcvt
Suggests: knotes
Suggests: kontact
Suggests: korganizer
Suggests: ksendemail
Suggests: kjots
%if %{with_kmobiletools}
Suggests: kmobiletools
%else
Obsoletes: kmobiletools < %epoch:%version
%endif
%if %{with_kpilot}
Suggests: kpilot
%else
Obsoletes: kpilot < %epoch:%version
%endif
Obsoletes: korn <= 2:4.1.0
Obsoletes: kdepim-korn < 1:3.5.10-2
Obsoletes: kdepim-kandy < 1:3.5.10-2
Obsoletes: ktnef <= 2:4.1.0
Obsoletes: kdepim-ktnef < 1:3.5.10-2
Obsoletes: %{_lib}kdepim2-ktnef < 1:3.5.10-2
Obsoletes: kdepim < 1:3.5.10-2

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kpilot: to sync with your PalmPilot
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer and
           kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- ktimetracker: Time tracker.
%if %{with_kitchensync}
	- kitchensync: Synchronisation framework, still under heavy development.
%endif
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client
	- kmailcvt: converst addressbooks to kmail format

%files

#----------------------------------------------------------------------

%package core
Summary: Core files for kdepim
Group: Graphical desktop/KDE	
Requires: kdelibs4-core
Requires: kdebase4-runtime
Obsoletes: libkdepim42-common < 1:3.93.0-1
Obsoletes: kdepim4-common < 1:3.93.0-1
Obsoletes: kdepim4-plasma-applets < 1:4.1 
Obsoletes: %{_lib}akonadisearchprovider4 < 2:3.94.1-0.729215.1
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim-knotes < 1:3.5.9-10mdv
Conflicts: kdepim-kaddressbook < 1:3.5.9-10mdv
Obsoletes: kdepim-common < 1:3.5.10-2
Obsoletes: %{_lib}kdepim2-common < 1:3.5.10-2

%description core
Core files from kdepim.

%files core
%defattr(-,root,root,-)
%_kde_libdir/strigi/*
%_kde_iconsdir/*/*/*/*
%dir %_kde_datadir/kde4/services/kontact

%exclude %_kde_iconsdir/oxygen/16x16/status/meeting-organizer.png

#-----------------------------------------------------------------------------

%define libgwsoap %mklibname gwsoap 4

%package -n %libgwsoap
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}gwsoap0 < 1:3.5.10-2

%description -n %libgwsoap
KDE 4 library.

%files -n %libgwsoap
%defattr(-,root,root)
%_kde_libdir/libgwsoap.so.*

#-----------------------------------------------------------------------------

%define libakonadi_kabccommon %mklibname akonadi-kabccommon 4

%package -n %libakonadi_kabccommon
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libakonadi_kabccommon
KDE 4 library.

%files -n %libakonadi_kabccommon
%defattr(-,root,root)
%_kde_libdir/libakonadi-kabccommon.so.*

#-----------------------------------------------------------------------------

%define libakonadi_kcal %mklibname akonadi-kcal 4

%package -n %libakonadi_kcal
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libakonadi_kcal
KDE 4 library.

%files -n %libakonadi_kcal
%defattr(-,root,root)
%_kde_libdir/libakonadi-kcal.so.*

#-----------------------------------------------------------------------------

%define libkaddressbookprivate %mklibname kaddressbookprivate 4

%package -n %libkaddressbookprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim2-kaddressbook < 1:3.5.10-2

%description -n %libkaddressbookprivate
KDE 4 library.

%files -n %libkaddressbookprivate
%defattr(-,root,root)
%_kde_libdir/libkaddressbookprivate.so.*

#-----------------------------------------------------------------------------

%define libkontactprivate %mklibname kontactprivate 4

%package -n %libkontactprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim2-kontact < 1:3.5.10-2

%description -n %libkontactprivate
KDE 4 library.

%files -n %libkontactprivate
%defattr(-,root,root)
%_kde_libdir/libkontactprivate.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_core %mklibname korganizer_core 4

%package -n %libkorganizer_core
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorganizer_core
KDE 4 library.

%files -n %libkorganizer_core
%defattr(-,root,root)
%_kde_libdir/libkorganizer_core.so.*

#-----------------------------------------------------------------------------

%define libmbox %mklibname mbox 4

%package -n %libmbox
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmbox
KDE 4 library.

%files -n %libmbox
%defattr(-,root,root)
%_kde_libdir/libmbox.so.*

#-----------------------------------------------------------------------------

%package akonadi
Summary: KDE PIM storage framework
Group: Graphical desktop/KDE
URL: http://pim.kde.org/akonadi/
Requires: %name-core = %epoch:%version
Obsoletes: %name-akonadi < 1:3.93.0-1
Obsoletes: kde4-akonadi < 2:4.0.68
Provides: kde4-akonadi = %epoch:%version

%description akonadi
KDE PIM storage framework.

%files akonadi
%defattr(-,root,root)
%_kde_bindir/akonadi_*
%_kde_bindir/akonadiconsole
%_kde_bindir/akonaditray
%_kde_bindir/akonadi2xml
%_kde_bindir/kres-migrator
%_kde_appsdir/akonadi
%_kde_datadir/akonadi
%_kde_appsdir/akonadiconsole
%_kde_datadir/kde4/services/kresources/kcal/blog.desktop
%_kde_datadir/applications/kde4/akonadiconsole.desktop
%_kde_datadir/applications/kde4/akonaditray.desktop
%_kde_datadir/kde4/services/akonadi.protocol
%_kde_libdir/kde4/kio_akonadi.so
%_kde_libdir/kde4/kabc_akonadi.so
%_kde_libdir/kde4/akonadi_*
%_kde_libdir/kde4/kcm_akonadi.so
%_kde_libdir/kde4/kcm_akonadi_*
%_kde_datadir/kde4/services/kcm_akonadi_resources.desktop
%_kde_datadir/kde4/services/kresources/kabc/akonadi.desktop
%_kde_datadir/kde4/services/kresources/kcal/akonadi.desktop
%_kde_datadir/kde4/services/kcm_akonadi.desktop
%_kde_datadir/kde4/services/kcm_akonadi_server.desktop
%_kde_datadir/config/kres-migratorrc
%_kde_appsdir/nepomuk/ontologies/*

#-----------------------------------------------------------------------------

%define libkdepim %mklibname kdepim 4

%package -n %libkdepim
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim42-index < 1:3.93.0-1
Conflicts: kdepim-common < 1:3.5.9-10mdv

%description -n %libkdepim
KDE 4 library.

%files -n %libkdepim
%defattr(-,root,root)
%_kde_libdir/libkdepim.so.*
%_kde_appsdir/kdepimwidgets
%_kde_appsdir/libkdepim
%_kde_libdir/kde4/kpartsdesignerplugin.so
%_kde_libdir/kde4/plugins/designer/kdepimwidgets.so

#-----------------------------------------------------------------------------

%define libkpgp %mklibname kpgp 4

%package -n %libkpgp
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkpgp
KDE 4 library.

%files -n %libkpgp
%defattr(-,root,root)
%_kde_libdir/libkpgp.so.*
%_kde_appsdir/kconf_update/kpgp-3.1-upgrade-address-data.pl
%_kde_appsdir/kconf_update/kpgp.upd

#-----------------------------------------------------------------------------

%define libkleopatraclientgui %mklibname kleopatraclientgui 4

%package -n %libkleopatraclientgui
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkleopatraclientgui
KDE 4 library.

%files -n %libkleopatraclientgui
%defattr(-,root,root)
%_kde_libdir/libkleopatraclientgui.so.*

#-----------------------------------------------------------------------------

%define libkleopatraclientcore %mklibname kleopatraclientcore 4

%package -n %libkleopatraclientcore
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkleopatraclientcore
KDE 4 library.

%files -n %libkleopatraclientcore
%defattr(-,root,root)
%_kde_libdir/libkleopatraclientcore.so.*

#-----------------------------------------------------------------------------

%package -n kleopatra
Summary: KDE Certificate Manager
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kleopatra < 1:3.93.0-1
Obsoletes: kde4-kleopatra < 2:4.0.68
Provides: kde4-kleopatra = %epoch:%version
Conflicts:  %{_lib}kleo4 < 4.0.80-3

%description -n kleopatra
KDE Certificate Manager

%files -n kleopatra
%defattr(-,root,root)
%_kde_bindir/kleopatra
%_kde_bindir/kgpgconf
%_kde_bindir/kwatchgnupg
%_kde_configdir/libkleopatrarc
%_kde_datadir/applications/kde4/kleopatra_import.desktop
%_kde_appsdir/kleopatra
%_kde_appsdir/libkleopatra
%_kde_appsdir/kwatchgnupg
%_kde_datadir/kde4/services/kleopatra_*
%_kde_libdir/kde4/kcm_kleopatra.so
%doc %_kde_docdir/*/*/kleopatra

#-----------------------------------------------------------------------------

%define libksieve %mklibname ksieve 4

%package -n %libksieve
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libksieve
KDE 4 library.

%files -n %libksieve
%defattr(-,root,root)
%_kde_libdir/libksieve.so.*

#-----------------------------------------------------------------------------

%define libmimelib %mklibname mimelib 4

%package -n %libmimelib
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libmimelib
KDE 4 library.

%files -n %libmimelib
%defattr(-,root,root)
%_kde_libdir/libmimelib.so.*

#-----------------------------------------------------------------------------

%define libakregatorinterfaces %mklibname akregatorinterfaces 4

%package -n %libakregatorinterfaces
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kpinterfaces4 < 2:4.0.80-1

%description -n %libakregatorinterfaces
KDE 4 library.

%files -n %libakregatorinterfaces
%defattr(-,root,root)
%_kde_libdir/libakregatorinterfaces.so.*

#-----------------------------------------------------------------------------

%define libakregatorprivate %mklibname akregatorprivate 4

%package -n %libakregatorprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libakregatorprivate
KDE 4 library.

%files -n %libakregatorprivate
%defattr(-,root,root)
%_kde_libdir/libakregatorprivate.so.*

#-----------------------------------------------------------------------------

%package -n akregator
Summary: A Feed Reader for KDE
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

Obsoletes: %name-akregator < 1:3.93.0-1
Obsoletes: kde4-akregator < 2:4.0.68
Obsoletes: kdepim-akregator < 1:3.5.10-2

Conflicts: kontact < 2:4.0.83
Provides: kde4-akregator = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n akregator
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%files -n akregator
%defattr(-,root,root)
%_kde_bindir/akregator
%_kde_bindir/akregatorstorageexporter
%_kde_datadir/applications/kde4/akregator.desktop
%_kde_appsdir/akregator
%_kde_appsdir/akonadi_knut_resource
%_kde_datadir/kde4/services/kontact/akregatorplugin.desktop
%_kde_datadir/config.kcfg/akregator.kcfg
%_kde_datadir/kde4/services/akregator_*
%_kde_datadir/kde4/services/feed.protocol
%_kde_datadir/kde4/servicetypes/akregator_plugin.desktop
%_kde_libdir/kde4/akregator*
%_kde_libdir/kde4/kontact_akregatorplugin.so
%_kde_appsdir/akregator_onlinesync_plugin
%doc %_kde_docdir/HTML/en/akregator

#-----------------------------------------------------------------------------

%define libakonadi_xml %mklibname akonadi-xml 4

%package -n %libakonadi_xml
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_xml
KDE 4 library.

%files -n %libakonadi_xml
%defattr(-,root,root)
%_kde_libdir/libakonadi-xml.so.*

#-----------------------------------------------------------------------------

%if %{with_kitchensync}

%define libkitchensyncprivate %mklibname kitchensyncprivate 4.2.0

%package -n %libkitchensyncprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim2-kitchensync < 1:3.5.10-2

%description -n %libkitchensyncprivate
KDE 4 library.

%files -n %libkitchensyncprivate
%defattr(-,root,root)
%_kde_libdir/libkitchensyncprivate.so.*

#-----------------------------------------------------------------------------

%define libqopensync %mklibname qopensync 4.2.0

%package -n %libqopensync
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim2-qopensync < 1:3.5.10-2

%description -n %libqopensync
KDE 4 library.

%files -n %libqopensync
%defattr(-,root,root)
%_kde_libdir/libqopensync.so.*

#-----------------------------------------------------------------------------

%package -n kitchensync
Summary: KDE KitchenSync
Group: Graphical desktop/KDE
URL: http://kontact.kde.org/kitchensync/index.php
Requires: %name-core = %epoch:%version

Obsoletes: %name-kitchensync < 1:3.93.0-1
Obsoletes: kde4-kitchensync < 2:4.0.68
Obsoletes: kdepim-kitchensync < 1:3.5.10-2

Provides: kde4-kitchensync = %epoch:%version

%description -n kitchensync
The KDE Synchronization Tool

%files -n kitchensync
%defattr(-,root,root)
%_kde_bindir/kitchensync
%_kde_datadir/applications/kde4/kitchensync.desktop
%_kde_appsdir/kitchensync
%_kde_libdir/kde4/kitchensyncpart.so
%endif

#-----------------------------------------------------------------------------

%define libknodecommon %mklibname knodecommon 4

%package -n %libknodecommon
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim42-knode < 1:3.93.0-1

%description -n %libknodecommon
KDE 4 library.

%files -n %libknodecommon
%defattr(-,root,root)
%_kde_libdir/libknodecommon.so.*

#-----------------------------------------------------------------------------

%package -n knode
Summary: A newsreader for the K Desktop Environment
Group: Graphical desktop/KDE
URL: http://kontact.kde.org/knode/
Requires: %name-core = %epoch:%version
Requires: kdepimlibs4-core
Obsoletes: %name-knode < 1:3.93.0-1
Obsoletes: kde4-knode < 2:4.0.68
Obsoletes: kdepim-knode < 1:3.5.10-2
Provides:  kde4-knode = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n knode
KNode is a newsreader for the K Desktop Environment.

It is GNKSA compliant (unfortunally a review is still pending), and has
support for MIME and multiple servers.

It is a online-reader, but in combination with a local newsserver like
leafnode also usable with dial-up connections.

%files -n knode
%defattr(-,root,root)
%_kde_bindir/knode
%_kde_datadir/applications/kde4/KNode.desktop
%_kde_appsdir/knode
%_kde_datadir/kde4/services/kontact/knodeplugin.desktop
%_kde_datadir/kde4/services/knewsservice.protocol
%_kde_datadir/kde4/services/knode_config_accounts.desktop
%_kde_datadir/kde4/services/knode_config_appearance.desktop
%_kde_datadir/kde4/services/knode_config_cleanup.desktop
%_kde_datadir/kde4/services/knode_config_identity.desktop
%_kde_datadir/kde4/services/knode_config_post_news.desktop
%_kde_datadir/kde4/services/knode_config_privacy.desktop
%_kde_datadir/kde4/services/knode_config_read_news.desktop
%_kde_libdir/kde4/kcm_knode.so
%_kde_libdir/kde4/knodepart.so
%_kde_libdir/kde4/kontact_knodeplugin.so
%_kde_docdir/HTML/en/knode

#-----------------------------------------------------------------------------

%define libkabinterfaces %mklibname kabinterfaces 4

%package -n %libkabinterfaces
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabinterfaces
KDE 4 library.

%files -n %libkabinterfaces
%defattr(-,root,root)
%_kde_libdir/libkabinterfaces.so.*

#-----------------------------------------------------------------------------

%package -n kaddressbook
Summary: The KDE addressbook application
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kaddressbook < 1:3.93.0-1
Obsoletes: kde4-kaddressbook < 2:4.0.68
Obsoletes: kdepim-kaddressbook < 1:3.5.10-2
Obsoletes: kdeaddons-kaddressbook-plugins < 1:3.5.10-2
Provides: kde4-kaddressbook = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdeaddons-kaddressbook-plugins < 1:3.5.9-2mdv
Conflicts: kdepim4-core < 2:4.1.81-1

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%defattr(-,root,root)
%_kde_bindir/kaddressbook
%_kde_bindir/kabcdistlistupdater
%_kde_datadir/applications/kde4/kaddressbook.desktop
%_kde_appsdir/kaddressbook
%_kde_datadir/kde4/services/kontact/kaddressbookplugin.desktop
%_kde_datadir/kde4/services/kabconfig.desktop
%_kde_datadir/kde4/services/kabcustomfields.desktop
%_kde_datadir/kde4/services/kabldapconfig.desktop
%_kde_datadir/kde4/services/kaddressbook
%_kde_datadir/kde4/services/kaddressbookpart.desktop
%_kde_datadir/kde4/services/ldifvcardthumbnail.desktop
%_kde_datadir/kde4/servicetypes/dbusaddressbook.desktop
%_kde_datadir/kde4/servicetypes/kaddressbook*
%_kde_datadir/config.kcfg/contactssettings.kcfg
%_kde_libdir/kde4/kcm_kabconfig.so
%_kde_libdir/kde4/kcm_kabcustomfields.so
%_kde_libdir/kde4/kcm_kabldapconfig.so
%_kde_libdir/kde4/ldifvcardthumbnail.so
%_kde_libdir/kde4/kaddrbk_*
%_kde_libdir/kde4/kaddressbookpart.so
%_kde_docdir/HTML/en/kaddressbook
%_kde_libdir/kde4/kontact_kaddressbookplugin.so
%_kde_datadir/autostart/kabcdistlistupdater.desktop

# Does it make sense to split it on its own package ?
%_kde_bindir/kabc2mutt
%_kde_bindir/kabcclient

#-----------------------------------------------------------------------------

%define libkalarm_resources %mklibname kalarm_resources 4

%package -n %libkalarm_resources
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkalarm_resources
KDE 4 library.

%files -n %libkalarm_resources
%defattr(-,root,root)
%_kde_libdir/libkalarm_resources.so.*

#-----------------------------------------------------------------------------

%package -n kalarm
Summary: A personal alarm message, command and email scheduler
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kalarm < 1:3.93.0-1
Obsoletes: kde4-kalarm < 2:4.0.68
Provides: kde4-kalarm = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n kalarm
KAlarm is a personal alarm message, command and email scheduler. It lets you
set up personal alarm messages which pop up on the screen at the chosen time,
or you can schedule commands to be executed or emails to be sent.

%files -n kalarm
%defattr(-,root,root)
%_kde_bindir/kalarm
%_kde_bindir/kalarmautostart
%_kde_appsdir/kconf_update/kalarm-2.1.5-general.pl
%_kde_datadir/applications/kde4/kalarm.desktop
%_kde_datadir/autostart/kalarm.autostart.desktop
%_kde_appsdir/kalarm/kalarmui.rc
%_kde_appsdir/kconf_update/kalarm-1.2.1-general.pl
%_kde_appsdir/kconf_update/kalarm-1.9.5-defaults.pl
%_kde_appsdir/kconf_update/kalarm-version.pl
%_kde_appsdir/kconf_update/kalarm.upd
%_kde_datadir/config.kcfg/kalarmconfig.kcfg
%_kde_datadir/kde4/services/kresources/alarms/local.desktop
%_kde_datadir/kde4/services/kresources/alarms/localdir.desktop
%_kde_datadir/kde4/services/kresources/alarms/remote.desktop
%_kde_datadir/kde4/services/kresources/kalarm_manager.desktop
%_kde_libdir/kde4/kalarm_local.so
%_kde_libdir/kde4/kalarm_localdir.so
%_kde_libdir/kde4/kalarm_remote.so
%_kde_appsdir/kconf_update/kalarm-2.0.2-general.pl
%_kde_docdir/HTML/en/kalarm

#-----------------------------------------------------------------------------

%package -n ktimetracker
Summary: Tracks time spent on various tasks
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-ktimetracker < 1:3.93.0-1
Obsoletes: kde4-ktimetracker < 2:4.0.68
Obsoletes: kdepim-karm < 1:3.5.10-2
Provides: kde4-ktimetracker = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n ktimetracker
KTimeTracker tracks time spent on various tasks. It is useful for tracking
hours to be billed to different clients or just to find out what percentage
of your day is spent playing Doom or reading Slashdot.

%files -n ktimetracker
%defattr(-,root,root)
%_kde_bindir/karm
%_kde_bindir/ktimetracker
%_kde_appsdir/ktimetracker
%_kde_datadir/applications/kde4/ktimetracker.desktop
%_kde_datadir/kde4/services/kcmplanner.desktop
%_kde_datadir/kde4/services/kontact/plannerplugin.desktop
%_kde_datadir/kde4/services/ktimetrackerpart.desktop
%_kde_datadir/kde4/services/ktimetracker_config_behavior.desktop
%_kde_datadir/kde4/services/ktimetracker_config_display.desktop
%_kde_datadir/kde4/services/ktimetracker_config_storage.desktop
%_kde_libdir/kde4/ktimetrackerpart.so
%_kde_libdir/kde4/kcm_planner.so
%_kde_libdir/kde4/kcm_ktimetracker.so
%_kde_libdir/kde4/kontact_plannerplugin.so
%_kde_docdir/HTML/en/ktimetracker

#-----------------------------------------------------------------------------

%define libkmailprivate %mklibname kmailprivate 4

%package -n %libkmailprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkmailprivate
KDE 4 library.

%files -n %libkmailprivate
%defattr(-,root,root)
%_kde_libdir/libkmailprivate.so.*

#-----------------------------------------------------------------------------

%package -n kmail
Summary: KDE Email Client
Group: Graphical desktop/KDE
URL: http://kontact.kde.org/kmail/
Requires: %name-core = %epoch:%version
Requires: kdepimlibs4-core
Requires:  sasl-plug-plain

Obsoletes: kde4-kmail < 2:4.0.68
Obsoletes: kdepim4-plugins <= 2:4.0.83
Obsoletes: %name-kmail < 1:3.93.0-1
Obsoletes: kdepim-kmail < 1:3.5.10-2
Obsoletes: %{_lib}kdepim2-index < 1:3.5.10-2

Conflicts: kontact < 2:4.0.83-2
Provides: kde4-kmail = %epoch:%version

%description -n kmail
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -n kmail
%defattr(-,root,root)
%_kde_bindir/kmail
%_kde_bindir/kmail_antivir.sh
%_kde_bindir/kmail_clamav.sh
%_kde_bindir/kmail_fprot.sh
%_kde_bindir/kmail_sav.sh
%_kde_appsdir/kmail
%_kde_datadir/kde4/services/kontact/kmailplugin.desktop
%_kde_datadir/applications/kde4/KMail.desktop
%_kde_datadir/applications/kde4/kmail_view.desktop
%_kde_appsdir/kconf_update/kmail*
%_kde_appsdir/kconf_update/upgrade-signature.pl
%_kde_appsdir/kconf_update/upgrade-transport.pl
%_kde_datadir/config.kcfg/custommimeheader.kcfg
%_kde_datadir/config.kcfg/customtemplates_kfg.kcfg
%_kde_datadir/config.kcfg/kmail.kcfg
%_kde_datadir/config.kcfg/replyphrases.kcfg
%_kde_datadir/config.kcfg/templatesconfiguration_kfg.kcfg
%_kde_datadir/config/kmail.antispamrc
%_kde_datadir/config/kmail.antivirusrc
%_kde_datadir/kde4/services/kmail_config_accounts.desktop
%_kde_datadir/kde4/services/kmail_config_appearance.desktop
%_kde_datadir/kde4/services/kmail_config_composer.desktop
%_kde_datadir/kde4/services/kmail_config_identity.desktop
%_kde_datadir/kde4/services/kmail_config_misc.desktop
%_kde_datadir/kde4/services/kmail_config_security.desktop
%_kde_datadir/kde4/servicetypes/dbusimap.desktop
%_kde_datadir/kde4/servicetypes/dbusmail.desktop
%_kde_libdir/kde4/kcm_kmail.so
%_kde_libdir/kde4/kmailpart.so
%_kde_libdir/kde4/kmail_bodypartformatter_*
%_kde_libdir/kde4/kcm_kmailsummary.so
%_kde_libdir/kde4/kontact_kmailplugin.so
%_kde_libdir/kde4/ktexteditorkabcbridge.so
%_kde_datadir/kde4/services/kcmkmailsummary.desktop
%_kde_docdir/HTML/en/kmail

#-----------------------------------------------------------------------------

%package -n kmailcvt
Summary: KDE Mail Import tool
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kmailcvt < 1:3.93.0-1
Obsoletes: kde4-kmailcvt < 2:4.0.68
Provides: kde4-kmailcvt = %epoch:%version

%description -n kmailcvt
KDE Mail Import tool

%files -n kmailcvt
%defattr(-,root,root)
%_kde_bindir/kmailcvt
%_kde_appsdir/kmailcvt/pics/step1.png

#-----------------------------------------------------------------------------

%package -n knotes
Summary: Notes for the K Desktop Environment
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Requires: %name-kresources

Obsoletes: kde4-knotes < 2:4.0.68
Obsoletes: %name-knotes < 1:3.93.0-1
Obsoletes: kdepim-knotes < 1:3.5.10-2

Provides: kde4-knotes = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%defattr(-,root,root)
%_kde_bindir/knotes
%_kde_datadir/applications/kde4/knotes.desktop
%_kde_datadir/kde4/services/kontact/knotesplugin.desktop
%_kde_datadir/config.kcfg/knoteconfig.kcfg
%_kde_datadir/config.kcfg/knotesglobalconfig.kcfg
%_kde_appsdir/knotes
%_kde_datadir/kde4/services/kresources/knotes/local.desktop
%_kde_datadir/kde4/services/kresources/knotes_manager.desktop
%_kde_datadir/kde4/services/knote_config_action.desktop
%_kde_datadir/kde4/services/knote_config_display.desktop
%_kde_datadir/kde4/services/knote_config_editor.desktop
%_kde_datadir/kde4/services/knote_config_network.desktop
%_kde_datadir/kde4/services/knote_config_style.desktop
%_kde_libdir/kde4/knotes_local.so
%_kde_libdir/kde4/knotes_scalix.so
%_kde_libdir/kde4/kcm_knote.so
%_kde_docdir/HTML/en/knotes
%_kde_libdir/kde4/kontact_knotesplugin.so

#-----------------------------------------------------------------------------

%package -n kontact
Summary: Kontact Container
Group: Graphical desktop/KDE
URL: http://kontact.kde.org/
Requires: %name-core = %epoch:%version
Obsoletes: %name-kontact < 1:3.93.0-1
Obsoletes: kde4-kontact < 2:4.0.68
Obsoletes: kdepim-kontact  kdepim-kpilot < 1:3.5.10-2
Provides: kde4-kontact = %epoch:%version

Suggests: akregator
Suggests: kmail
Suggests: knotes
Suggests: ktimetracker
Suggests: knode
Suggests: kalarm
Suggests: kaddressbook

%description -n kontact
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -n kontact
%defattr(-,root,root)
%_kde_bindir/kontact
%_kde_appsdir/kontact
%_kde_appsdir/kontactsummary
%_kde_datadir/config.kcfg/kontact.kcfg
%_kde_datadir/kde4/services/kontactconfig.desktop
%_kde_datadir/kde4/services/kcmapptsummary.desktop
%_kde_datadir/kde4/services/kcmkontactsummary.desktop
%_kde_datadir/kde4/services/kcmsdsummary.desktop
%_kde_datadir/kde4/services/kontact/summaryplugin.desktop
%_kde_datadir/kde4/services/kontact/specialdatesplugin.desktop
%_kde_datadir/kde4/servicetypes/kontactplugin.desktop
%_kde_libdir/kde4/kcm_apptsummary.so
%_kde_libdir/kde4/kcm_kontact.so
%_kde_libdir/kde4/kcm_kontactsummary.so
%_kde_libdir/kde4/kontact_journalplugin.so
%_kde_libdir/kde4/kcm_sdsummary.so
%_kde_libdir/kde4/kontact_specialdatesplugin.so
%_kde_libdir/kde4/kontact_summaryplugin.so
%_kde_docdir/HTML/en/kontact
%_kde_datadir/applications/kde4/Kontact.desktop

#-----------------------------------------------------------------------------

%define libkorg_stdprinting %mklibname korg_stdprinting 4

%package -n %libkorg_stdprinting
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkorg_stdprinting
KDE 4 library.

%files -n %libkorg_stdprinting
%defattr(-,root,root)
%_kde_libdir/libkorg_stdprinting.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_calendar %mklibname korganizer_calendar 4

%package -n %libkorganizer_calendar
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkorganizer_calendar
KDE 4 library.

%files -n %libkorganizer_calendar
%defattr(-,root,root)
%_kde_libdir/libkorganizer_calendar.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_eventviewer %mklibname korganizer_eventviewer 4

%package -n %libkorganizer_eventviewer
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkorganizer_eventviewer
KDE 4 library.

%files -n %libkorganizer_eventviewer
%defattr(-,root,root)
%_kde_libdir/libkorganizer_eventviewer.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_interfaces %mklibname korganizer_interfaces 4

%package -n %libkorganizer_interfaces
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim2-korganizer < 1:3.93.0-1
%description -n %libkorganizer_interfaces
KDE 4 library.

%files -n %libkorganizer_interfaces
%defattr(-,root,root)
%_kde_libdir/libkorganizer_interfaces.so.*

#-----------------------------------------------------------------------------

%package -n korganizer
Summary: Calendar and scheduling component
Group: Graphical desktop/KDE
URL: http://kontact.kde.org/korganizer/
Requires:  %name-core = %epoch:%version
Requires:  %name-kresources
Obsoletes: kde4-korganizer < 2:4.0.68
Obsoletes: %name-korganizer < 1:3.93.0-1
Obsoletes: kdepim-korganizer < 1:3.5.10-2
Provides:  kde4-korganizer = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim4-core < 2:4.1.81-1

%description -n korganizer
KOrganizer provides management of events and tasks, alarm notification,
web export, network transparent handling of data, group scheduling,
import and export of calendar files and more. It is able to work together
with a wide variety of groupware servers, for example Kolab, Open-Xchange,
Citadel or OpenGroupware.org.

%files -n korganizer
%defattr(-,root,root)
%_kde_bindir/ical2vcal
%_kde_bindir/korgac
%_kde_bindir/korganizer
%_kde_datadir/kde4/services/kontact/korganizerplugin.desktop
%_kde_datadir/applications/kde4/korganizer-import.desktop
%_kde_datadir/applications/kde4/korganizer.desktop
%_kde_appsdir/kconf_update/korganizer.upd
%_kde_appsdir/korgac
%_kde_appsdir/korganizer
%_kde_datadir/kde4/services/kontact/todoplugin.desktop
%_kde_datadir/kde4/services/kcmtodosummary.desktop
%_kde_datadir/kde4/services/kontact/journalplugin.desktop
%_kde_libdir/kde4/kcm_todosummary.so
%_kde_libdir/kde4/kontact_todoplugin.so
%_kde_datadir/autostart/korgac.desktop
%_kde_datadir/config.kcfg/korganizer.kcfg
%_kde_datadir/config.kcfg/todosettings.kcfg
%_kde_datadir/config.kcfg/calendarsettings.kcfg
%_kde_datadir/config/korganizer.knsrc
%_kde_datadir/kde4/services/korganizer*
%_kde_datadir/kde4/services/webcal.protocol
%_kde_datadir/kde4/servicetypes/calendardecoration.desktop
%_kde_datadir/kde4/servicetypes/calendarplugin.desktop
%_kde_datadir/kde4/servicetypes/dbuscalendar.desktop
%_kde_datadir/kde4/servicetypes/korganizerpart.desktop
%_kde_datadir/kde4/servicetypes/korgprintplugin.desktop
%_kde_libdir/kde4/kcm_korganizer.so
%_kde_libdir/kde4/korg_*
%_kde_libdir/kde4/korganizerpart.so
%_kde_libdir/kde4/kontact_korganizerplugin.so
%doc %_kde_docdir/*/*/korganizer

%_kde_bindir/konsolekalendar
%_kde_datadir/applications/kde4/konsolekalendar.desktop

#-----------------------------------------------------------------------------

%define libkorganizerprivate %mklibname korganizerprivate 4

%package -n %libkorganizerprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}korganizer4 < 1:3.97.1-0.752060.1
Obsoletes: %{_lib}kdepim42-korganizer < 1:3.93.0-

%description -n %libkorganizerprivate
KDE 4 library.

%files -n %libkorganizerprivate
%defattr(-,root,root)
%_kde_libdir/libkorganizerprivate.so.*

#-----------------------------------------------------------------------------

%if %{with_kmobiletools}

%define libkmobiletoolsengineui %mklibname kmobiletoolsengineui 4

%package -n %libkmobiletoolsengineui
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkmobiletoolsengineui
KDE 4 library.

%files -n %libkmobiletoolsengineui
%defattr(-,root,root)
%_kde_libdir/libkmobiletoolsengineui.so.*

#-----------------------------------------------------------------------------

%define libkmobiletoolslib %mklibname kmobiletoolslib 4

%package -n %libkmobiletoolslib
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kmobiletools4 < 1:3.94.1-0.730680.1

%description -n %libkmobiletoolslib
KDE 4 library.

%files -n %libkmobiletoolslib
%defattr(-,root,root)
%_kde_libdir/libkmobiletoolslib.so.*

#-----------------------------------------------------------------------------

%package -n kmobiletools
Summary: A KDE application that allows you to control your mobile phone
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kmobiletools < 1:3.93.0-1
Obsoletes: kde4-kmobiletools < 2:4.0.68
Provides: kde4-kmobiletools = %epoch:%version

%description -n kmobiletools
KMobileTools is a KDE application that allows you to control your mobile
phone from your GNU/Linux workstation.

%files -n kmobiletools
%defattr(-,root,root)
%_kde_bindir/kmobiletools
%_kde_datadir/applications/kde4/kmobiletools.desktop
%_kde_appsdir/akonadi/plugins/serializer/akonadi_serializer_sms.desktop
%_kde_appsdir/kmobiletools
%_kde_datadir/config.kcfg/kmobiletools_devices.kcfg
%_kde_datadir/kde4/services/kmobiletools_mainpart.desktop
%_kde_datadir/kde4/services/fake_engine.desktop
%_kde_datadir/kde4/servicetypes/kmobile*
%_kde_libdir/kde4/kmobiletools*
%_kde_docdir/HTML/en/kmobiletools
%endif # with_kmobiletools

#-----------------------------------------------------------------------------

%if %{with_kpilot}

%define libkpilot %mklibname kpilot 5

%package -n %libkpilot
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1
Obsoletes: %{_lib}kdepim42-kpilot < 1:3.93.0-1
Obsoletes: %{_lib}kdepim2-kpilot < 1:3.93.0-1

%description -n %libkpilot
KDE 4 library.

%files -n %libkpilot
%defattr(-,root,root)
%_kde_libdir/libkpilot.so.*

#-----------------------------------------------------------------------------

%package -n kpilot
Summary: Sync PalmOS based handhelds with a machine
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kpilot < 1:3.93.0-1
Obsoletes: kde4-kpilot < 2:4.0.68
Obsoletes: kdepim-kpilot < 1:3.5.10-2
Conflicts: %name-devel < 2:4.1.71-2
Provides: kde4-kpilot = %epoch:%version

%description -n kpilot
KPilot is software for syncing PalmOS based handhelds such as the 3Com Palm
Pilot with a machine running some flavor of UNIX.

%files -n kpilot
%defattr(-,root,root)
%_kde_bindir/kpilot
%_kde_bindir/kpilotDaemon
%_kde_datadir/applications/kde4/kpilot.desktop
%_kde_datadir/applications/kde4/kpilotdaemon.desktop
%_kde_appsdir/kconf_update/kpilot.upd
%_kde_appsdir/kpilot
%_kde_datadir/config.kcfg/kpilot.kcfg
%_kde_datadir/config.kcfg/kpilotlib.kcfg
%_kde_datadir/config.kcfg/memofileconduit.kcfg
#%_kde_datadir/config.kcfg/popmail.kcfg
%_kde_datadir/config.kcfg/timeconduit.kcfg
#%_kde_datadir/config.kcfg/vcalconduitbase.kcfg
#%_kde_datadir/config.kcfg/keyringconduit.kcfg
%_kde_datadir/kde4/services/kpilot_config.desktop
%_kde_datadir/kde4/services/*-conduit* 
%_kde_datadir/kde4/services/time_conduit.desktop
%_kde_datadir/kde4/servicetypes/kpilotconduit.desktop
%_kde_libdir/kde4/kcm_kpilot.so
%_kde_libdir/kde4/kpilot_*
%_kde_libdir/libkpilot_conduit_base.so
%_kde_libdir/libkpilot_akonadibase.so
%_kde_docdir/HTML/en/kpilot
%endif # with_kpilot

#-----------------------------------------------------------------------------

%define libkabc_groupdav %mklibname kabc_groupdav 4

%package -n %libkabc_groupdav
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabc_groupdav
KDE 4 library.

%files -n %libkabc_groupdav
%defattr(-,root,root)
%_kde_libdir/libkabc_groupdav.so.*

#-----------------------------------------------------------------------------

%define libkabc_slox %mklibname kabc_slox 4

%package -n %libkabc_slox
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabc_slox
KDE 4 library.

%files -n %libkabc_slox
%defattr(-,root,root)
%_kde_libdir/libkabc_slox.so.*

#-----------------------------------------------------------------------------

%define libkabc_xmlrpc %mklibname kabc_xmlrpc 4

%package -n %libkabc_xmlrpc
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabc_xmlrpc
KDE 4 library.

%files -n %libkabc_xmlrpc
%defattr(-,root,root)
%_kde_libdir/libkabc_xmlrpc.so.*

#-----------------------------------------------------------------------------

%define libkabckolab %mklibname kabckolab 4

%package -n %libkabckolab
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabckolab
KDE 4 library.

%files -n %libkabckolab
%defattr(-,root,root)
%_kde_libdir/libkabckolab.so.*

#-----------------------------------------------------------------------------

%define libkcal_groupdav %mklibname kcal_groupdav 4

%package -n %libkcal_groupdav
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcal_groupdav
KDE 4 library.

%files -n %libkcal_groupdav
%defattr(-,root,root)
%_kde_libdir/libkcal_groupdav.so.*

#-----------------------------------------------------------------------------

%define libkcal_resourceblog %mklibname kcal_resourceblog 4

%package -n %libkcal_resourceblog
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcal_resourceblog
KDE 4 library.

%files -n %libkcal_resourceblog
%defattr(-,root,root)
%_kde_libdir/libkcal_resourceblog.so.*

#-----------------------------------------------------------------------------

%define libkcal_resourceremote %mklibname kcal_resourceremote 4

%package -n %libkcal_resourceremote
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcal_resourceremote
KDE 4 library.

%files -n %libkcal_resourceremote
%defattr(-,root,root)
%_kde_libdir/libkcal_resourceremote.so.*

#-----------------------------------------------------------------------------

%define libkcal_slox %mklibname kcal_slox 4

%package -n %libkcal_slox
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcal_slox
KDE 4 library.

%files -n %libkcal_slox
%defattr(-,root,root)
%_kde_libdir/libkcal_slox.so.*

#-----------------------------------------------------------------------------

%define libkcal_xmlrpc %mklibname kcal_xmlrpc 4

%package -n %libkcal_xmlrpc
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcal_xmlrpc
KDE 4 library.

%files -n %libkcal_xmlrpc
%defattr(-,root,root)
%_kde_libdir/libkcal_xmlrpc.so.*

#-----------------------------------------------------------------------------

%define libkcalkolab %mklibname kcalkolab 4

%package -n %libkcalkolab
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcalkolab
KDE 4 library.

%files -n %libkcalkolab
%defattr(-,root,root)
%_kde_libdir/libkcalkolab.so.*

#-----------------------------------------------------------------------------

%define libkgroupwarebase %mklibname kgroupwarebase 4

%package -n %libkgroupwarebase
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkgroupwarebase
KDE 4 library.

%files -n %libkgroupwarebase
%defattr(-,root,root)
%_kde_libdir/libkgroupwarebase.so.*

#-----------------------------------------------------------------------------

%define libkgroupwaredav %mklibname kgroupwaredav 4

%package -n %libkgroupwaredav
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkgroupwaredav
KDE 4 library.

%files -n %libkgroupwaredav
%defattr(-,root,root)
%_kde_libdir/libkgroupwaredav.so.*

#-----------------------------------------------------------------------------

%define libknotes_xmlrpc %mklibname knotes_xmlrpc 4

%package -n %libknotes_xmlrpc
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libknotes_xmlrpc
KDE 4 library.

%files -n %libknotes_xmlrpc
%defattr(-,root,root)
%_kde_libdir/libknotes_xmlrpc.so.*

#-----------------------------------------------------------------------------

%define libknoteskolab %mklibname knoteskolab 4

%package -n %libknoteskolab
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libknoteskolab
KDE 4 library.

%files -n %libknoteskolab
%defattr(-,root,root)
%_kde_libdir/libknoteskolab.so.*

#-----------------------------------------------------------------------------

%define libkslox %mklibname kslox 4

%package -n %libkslox
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkslox
KDE 4 library.

%files -n %libkslox
%defattr(-,root,root)
%_kde_libdir/libkslox.so.*

#-----------------------------------------------------------------------------

%define libkabcommon %mklibname kabcommon 4

%package -n %libkabcommon
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabcommon
KDE 4 library.

%files -n %libkabcommon
%defattr(-,root,root)
%_kde_libdir/libkabcommon.so.*

#-----------------------------------------------------------------------------

%define libkleo %mklibname kleo 4

%package -n %libkleo
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkleo
KDE 4 library.

%files -n %libkleo
%defattr(-,root,root)
%_kde_libdir/libkleo.so.*

#-----------------------------------------------------------------------------

%package kresources
Summary: KDE pim resource plugins
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kresources < 1:3.93.0-1
Conflicts: %{_lib}kcal_resourcefeatureplan4 < 3.93.0-0.726734.2

%description kresources
This package includes several plugins needed to interface with groupware
servers. It also includes plugins for features such as blogging and
tracking feature plans.

%files kresources
%defattr(-,root,root)
%_kde_datadir/kde4/services/kresources/kabc/kabc_groupdav.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_opengroupware.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_ox.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_slox.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_xmlrpc.desktop
%_kde_datadir/kde4/services/kresources/kabc/kolab.desktop
%_kde_datadir/kde4/services/kresources/kcal/kabc.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_groupdav.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_opengroupware.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_ox.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_slox.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_xmlrpc.desktop
%_kde_datadir/kde4/services/kresources/kcal/kolab.desktop
%_kde_datadir/kde4/services/kresources/kcal/remote.desktop
%_kde_datadir/kde4/services/kresources/kcal/scalix.desktop
%_kde_datadir/kde4/services/kresources/knotes/knotes_xmlrpc.desktop
%_kde_datadir/kde4/services/kresources/kabc/scalix.desktop
%_kde_datadir/kde4/services/kresources/knotes/scalix.desktop
%_kde_datadir/kde4/services/kresources/knotes/kolabresource.desktop
%_kde_appsdir/kconf_update/kolab-resource.upd
%_kde_appsdir/kconf_update/upgrade-resourcetype.pl
%_kde_libdir/kde4/kabc_groupdav.so
%_kde_libdir/kde4/kabc_kolab.so
%_kde_libdir/kde4/kabc_slox.so
%_kde_libdir/kde4/kabc_xmlrpc.so
%_kde_libdir/kde4/kabc_scalix.so
%_kde_libdir/kde4/kcal_*
%_kde_libdir/kde4/knotes_kolab.so
%_kde_libdir/kde4/knotes_xmlrpc.so

#-----------------------------------------------------------------------------

%package wizards
Summary: KDE Groupware Wizard
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-wizards < 1:3.93.0-1
Obsoletes: kdepim-wizards < 1:3.5.10-2

%description wizards
KDE Groupware Wizard

%files wizards
%defattr(-,root,root)
%_kde_bindir/egroupwarewizard
%_kde_bindir/groupwarewizard
%_kde_bindir/kolabwizard
%_kde_bindir/sloxwizard
%_kde_bindir/scalixwizard
%_kde_bindir/scalixadmin
%_kde_bindir/groupwisewizard
%_kde_libdir/kde4/kio_scalix.so
%_kde_libdir/kde4/kio_groupwise.so
%_kde_libdir/kde4/kabc_groupwise.so
%_kde_datadir/applications/kde4/groupwarewizard.desktop
%_kde_datadir/config.kcfg/egroupware.kcfg
%_kde_datadir/config.kcfg/groupwise.kcfg
%_kde_datadir/config.kcfg/kolab.kcfg
%_kde_datadir/config.kcfg/slox.kcfg
%_kde_datadir/config.kcfg/scalix.kcfg
%_kde_datadir/kde4/services/scalix.protocol
%_kde_datadir/kde4/services/scalixs.protocol
%_kde_datadir/kde4/services/groupwise.protocol
%_kde_datadir/kde4/services/groupwises.protocol
%_kde_datadir/kde4/services/kresources/kabc/kabc_groupwise.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_groupwise.desktop

#-----------------------------------------------------------------------------

%define libmaildir %mklibname maildir 4

%package -n %libmaildir
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libmaildir
KDE 4 library.

%files -n %libmaildir
%defattr(-,root,root)
%_kde_libdir/libmaildir.so.*

#-----------------------------------------------------------------------------

%define libkabcscalix %mklibname kabcscalix 4

%package -n %libkabcscalix
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkabcscalix
KDE 4 library.

%files -n %libkabcscalix
%defattr(-,root,root)
%_kde_libdir/libkabcscalix.so.*


#-----------------------------------------------------------------------------

%define libkcalscalix %mklibname kcalscalix 4

%package -n %libkcalscalix
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libkcalscalix
KDE 4 library.

%files -n %libkcalscalix
%defattr(-,root,root)
%_kde_libdir/libkcalscalix.so.*

#-----------------------------------------------------------------------------

%define libknotesscalix %mklibname knotesscalix 4

%package -n %libknotesscalix
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libknotesscalix
KDE 4 library.

%files -n %libknotesscalix
%defattr(-,root,root)
%_kde_libdir/libknotesscalix.so.*

#-----------------------------------------------------------------------------

%define libkabcgroupwise %mklibname kabc_groupwise 4

%package -n %libkabcgroupwise
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabcgroupwise
KDE 4 library.

%files -n %libkabcgroupwise
%defattr(-,root,root)
%_kde_libdir/libkabcgroupwise.so.*

#-----------------------------------------------------------------------------

%define libkcalgroupwise %mklibname kcal_groupwise 4

%package -n %libkcalgroupwise
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcalgroupwise
KDE 4 library.

%files -n %libkcalgroupwise
%defattr(-,root,root)
%_kde_libdir/libkcalgroupwise.so.*

#-----------------------------------------------------------------------------

%define libkontactinterfaces %mklibname kontactinterfaces 4

%package -n %libkontactinterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkontactinterfaces
KDE 4 library.

%files -n %libkontactinterfaces
%defattr(-,root,root)
%_kde_libdir/libkontactinterfaces.so.*

#-----------------------------------------------------------------------------

%define libakonadi_next %mklibname akonadi_next 4

%package -n %libakonadi_next
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_next
KDE 4 library.

%files -n %libakonadi_next
%defattr(-,root,root)
%_kde_libdir/libakonadi_next.so.*

#-----------------------------------------------------------------------------

%package -n kjots
Summary: %{name} kjots
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kjots < 3.93.0-0.714053.1
Obsoletes: kde4-kjots < 4.0.68
Provides: kde4-kjots = %version
Conflicts: kontact < 2:4.0.83-2

%description -n kjots
%{name} kjots.

%files -n kjots
%defattr(-,root,root)
%_kde_bindir/kjots
%_kde_appsdir/kjots
%_kde_datadir/kde4/services/kontact/kjots_plugin.desktop
%_kde_libdir/kde4/kjotspart.so
%_kde_libdir/kde4/kcm_kjots.so
%_kde_datadir/applications/kde4/Kjots.desktop
%_kde_datadir/kde4/services/kjotspart.desktop
%_kde_datadir/kde4/services/kjots_config_misc.desktop
%_kde_datadir/config.kcfg/kjots.kcfg
%_kde_docdir/HTML/*/kjots
%_kde_libdir/kde4/kontact_kjotsplugin.so

#-----------------------------------------------------------------------------

%package -n ksendemail
Summary: %{name} ksendemail
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n ksendemail
%{name} ksendemail.

%files -n ksendemail
%defattr(-,root,root)
%_kde_bindir/ksendemail

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdepimlibs4-devel
Requires: %libkdepim = %epoch:%version
Requires: %libkpgp = %epoch:%version
Requires: %libksieve = %epoch:%version
Requires: %libmimelib = %epoch:%version
Requires: %libakregatorinterfaces = %epoch:%version
Requires: %libakregatorprivate = %epoch:%version
%if %{with_kitchensync}
Requires: %libkmobiletoolslib = %epoch:%version
Requires: %libkitchensyncprivate = %epoch:%version
Requires: %libqopensync = %epoch:%version
%endif
Requires: %libknodecommon = %epoch:%version
Requires: %libkabinterfaces = %epoch:%version
Requires: %libkalarm_resources = %epoch:%version
Requires: %libkmailprivate = %epoch:%version
Requires: %libkorg_stdprinting = %epoch:%version
Requires: %libkorganizerprivate = %epoch:%version
Requires: %libkorganizer_calendar = %epoch:%version
Requires: %libkorganizer_eventviewer = %epoch:%version
Requires: %libkorganizer_interfaces = %epoch:%version
%if %{with_kmobiletools}
Requires: %libkmobiletoolsengineui = %epoch:%version
%endif
%if %{with_kpilot}
Requires: %libkpilot = %epoch:%version
%endif
Requires: %libkabc_groupdav = %epoch:%version
Requires: %libkabc_slox = %epoch:%version
Requires: %libkabc_xmlrpc = %epoch:%version
Requires: %libkabckolab = %epoch:%version
Requires: %libkcal_groupdav = %epoch:%version
Requires: %libkcal_resourceremote = %epoch:%version
Requires: %libkcal_slox = %epoch:%version
Requires: %libkcal_xmlrpc = %epoch:%version
Requires: %libkcalkolab = %epoch:%version
Requires: %libkgroupwarebase = %epoch:%version
Requires: %libkgroupwaredav = %epoch:%version
Requires: %libknotes_xmlrpc = %epoch:%version
Requires: %libknoteskolab = %epoch:%version
Requires: %libkslox = %epoch:%version
Requires: %libkabcommon = %epoch:%version
Requires: %libkleo = %epoch:%version
Requires: %libmaildir = %epoch:%version
Requires: %libknotesscalix = %epoch:%version
Requires: %libkabcscalix  = %epoch:%version
Requires: %libkcalscalix  = %epoch:%version
Requires: %libgwsoap = %epoch:%version
Requires: %libkabcgroupwise = %epoch:%version
Requires: %libkcalgroupwise = %epoch:%version
Requires: %libkontactinterfaces = %epoch:%version
Requires: %libakonadi_next = %epoch:%version

Obsoletes: kdepim-devel < 1:3.5.10-2
Obsoletes: kdepim-devel-doc < 1:3.5.10-2

%description  devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%if %{with_kpilot}
%exclude %_kde_libdir/libkpilot_conduit_base.so
%exclude %_kde_libdir/libkpilot_akonadibase.so
%endif
%_kde_prefix/include/*
%_kde_datadir/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%version
#%patch0 -p0
#%patch1 -p0
#%patch2 -p1

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

