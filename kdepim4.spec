%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 680510

%if %unstable
%define dont_strip 1
%endif

Name: kdepim4
Summary: K Desktop Environment
Version: 3.90.2
Release: %mkrel 0.%revision
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.%revision.tar.bz2
%else
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.tar.bz2
%endif
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: gpgme-devel 
BuildRequires: X11-devel 
BuildRequires: flex 
BuildRequires: byacc 
BuildRequires: pam
BuildRequires: libmal-devel >= 0.31
BuildRequires: libncurses-devel
BuildRequires: readline-devel
BuildRequires: pilot-link-devel
BuildRequires: libgpg-error-devel
BuildRequires: gnokii-devel
BuildRequires: libxml2-utils
BuildRequires: gnupg
BuildRequires: bluez-devel 
BuildRequires: libsasl-devel
BuildRequires: pilot-link-devel
BuildRequires: libxslt-proc
BuildRequires: boost-devel
BuildRequires: opensync-devel
Requires: %name-core
Requires: kde4-kode
Requires: kde4-akonadi
Requires: kde4-kleopatra
Requires: kde4-akregator
Requires: kde4-kitchensync
Requires: kde4-knode
Requires: kde4-kaddressbook
Requires: kde4-kalarm
Requires: kde4-ktimetracker
Requires: kde4-kmail
Requires: kde4-kmailcvt
Requires: kde4-knotes
Requires: kde4-kontact
Requires: kde4-korganizer
Requires: kde4-kmobiletools
Requires: kde4-korn
Requires: kde4-kpilot
Requires: kde4-ktnef

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kpilot: to sync with your PalmPilot
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer and
           kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- karm: Time tracker.
	- kitchensync: Synchronisation framework, still under heavy development.
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

%description core
Core files fro kdepim.

%files core
%defattr(-,root,root,-)
%_datadir/dbus-1/interfaces/org.kde.pim.IdentityManager.xml
%_kde_bindir/kabc2mutt
%_kde_bindir/kabcclient
%_kde_bindir/konsolekalendar
%_kde_datadir/applications/kde4/konsolekalendar.desktop
%_kde_datadir/icons/*/*/*/konsolekalendar*
%_kde_docdir/HTML/en/konsolekalendar
%_kde_libdir/strigi/*
%_kde_datadir/icons/*/*/*/playsound*

#-----------------------------------------------------------------------------

%define libkode %mklibname kode 5

%package -n %libkode
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkode
KDE 4 library.

%post -n %libkode -p /sbin/ldconfig
%postun -n %libkode -p /sbin/ldconfig

%files -n %libkode
%defattr(-,root,root)
%_kde_libdir/libkode.so.*

#-----------------------------------------------------------------------------

%define libkschema %mklibname kschema 5

%package -n %libkschema
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkschema
KDE 4 library.

%post -n %libkschema -p /sbin/ldconfig
%postun -n %libkschema -p /sbin/ldconfig

%files -n %libkschema
%defattr(-,root,root)
%_kde_libdir/libkschema.so.*

#-----------------------------------------------------------------------------

%define libkschemawidgets %mklibname kschemawidgets 5

%package -n %libkschemawidgets
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkschemawidgets
KDE 4 library.

%post -n %libkschemawidgets -p /sbin/ldconfig
%postun -n %libkschemawidgets -p /sbin/ldconfig

%files -n %libkschemawidgets
%defattr(-,root,root)
%_kde_libdir/libkschemawidgets.so.*

#-----------------------------------------------------------------------------

%define libkxmlcommon %mklibname kxmlcommon 5

%package -n %libkxmlcommon
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkxmlcommon
KDE 4 library.

%post -n %libkxmlcommon -p /sbin/ldconfig
%postun -n %libkxmlcommon -p /sbin/ldconfig

%files -n %libkxmlcommon
%defattr(-,root,root)
%_kde_libdir/libkxmlcommon.so.*

#-----------------------------------------------------------------------------

%define libschema %mklibname schema 5

%package -n %libschema
Summary: KDE 4 library
Group: System/Libraries

%description -n %libschema
KDE 4 library.

%post -n %libschema -p /sbin/ldconfig
%postun -n %libschema -p /sbin/ldconfig

%files -n %libschema
%defattr(-,root,root)
%_kde_libdir/libschema.so.*

#-----------------------------------------------------------------------------

%define libwscl %mklibname wscl 5

%package -n %libwscl
Summary: KDE 4 library
Group: System/Libraries

%description -n %libwscl
KDE 4 library.

%post -n %libwscl -p /sbin/ldconfig
%postun -n %libwscl -p /sbin/ldconfig

%files -n %libwscl
%defattr(-,root,root)
%_kde_libdir/libwscl.so.*

#-----------------------------------------------------------------------------

%define libwsdl %mklibname wsdl 5

%package -n %libwsdl
Summary: KDE 4 library
Group: System/Libraries

%description -n %libwsdl
KDE 4 library.

%post -n %libwsdl -p /sbin/ldconfig
%postun -n %libwsdl -p /sbin/ldconfig

%files -n %libwsdl
%defattr(-,root,root)
%_kde_libdir/libwsdl.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kode
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kode

%description -n kde4-kode
Dialog KDE base widgets

%files -n kde4-kode
%defattr(-,root,root)
%_kde_bindir/kode
%_kde_bindir/kung
%_kde_bindir/kwsdl_compiler
%_kde_bindir/kxforms
%_kde_bindir/kxml_compiler
%_kde_bindir/schematest
%_kde_datadir/applications/kde4/kwsdl_compiler.desktop
%_kde_appsdir/kxforms/kxformsui.rc
%_kde_datadir/config.kcfg/kxforms.kcfg

#-----------------------------------------------------------------------------

%define libakonadi %mklibname akonadi 5

%package -n %libakonadi
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi
KDE 4 library.

%post -n %libakonadi -p /sbin/ldconfig
%postun -n %libakonadi -p /sbin/ldconfig

%files -n %libakonadi
%defattr(-,root,root)
%_kde_libdir/libakonadi.so.*

#-----------------------------------------------------------------------------

%define libakonadicomponents %mklibname akonadicomponents 5

%package -n %libakonadicomponents
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadicomponents
KDE 4 library.

%post -n %libakonadicomponents -p /sbin/ldconfig
%postun -n %libakonadicomponents -p /sbin/ldconfig

%files -n %libakonadicomponents
%defattr(-,root,root)
%_kde_libdir/libakonadicomponents.so.*

#-----------------------------------------------------------------------------

%define libakonadiprivate %mklibname akonadiprivate 5

%package -n %libakonadiprivate
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadiprivate
KDE 4 library.

%post -n %libakonadiprivate -p /sbin/ldconfig
%postun -n %libakonadiprivate -p /sbin/ldconfig

%files -n %libakonadiprivate
%defattr(-,root,root)
%_kde_libdir/libakonadiprivate.so.*

#-----------------------------------------------------------------------------

%define libakonadisearchprovider %mklibname akonadisearchprovider 5

%package -n %libakonadisearchprovider
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadisearchprovider
KDE 4 library.

%post -n %libakonadisearchprovider -p /sbin/ldconfig
%postun -n %libakonadisearchprovider -p /sbin/ldconfig

%files -n %libakonadisearchprovider
%defattr(-,root,root)
%_kde_libdir/libakonadisearchprovider.so.*

#-----------------------------------------------------------------------------

%define libkabcakonadi %mklibname kabcakonadi 5

%package -n %libkabcakonadi
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabcakonadi
KDE 4 library.

%post -n %libkabcakonadi -p /sbin/ldconfig
%postun -n %libkabcakonadi -p /sbin/ldconfig

%files -n %libkabcakonadi
%defattr(-,root,root)
%_kde_libdir/libkabcakonadi.so.*

#-----------------------------------------------------------------------------

%define libkcal_resourcefeatureplan %mklibname kcal_resourcefeatureplan 5

%package -n %libkcal_resourcefeatureplan
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcal_resourcefeatureplan
KDE 4 library.

%post -n %libkcal_resourcefeatureplan -p /sbin/ldconfig
%postun -n %libkcal_resourcefeatureplan -p /sbin/ldconfig

%files -n %libkcal_resourcefeatureplan
%defattr(-,root,root)
%_kde_libdir/kcal_resourcefeatureplan.so.*

#-----------------------------------------------------------------------------

%define libkmimeakonadi %mklibname kmimeakonadi 5

%package -n %libkmimeakonadi
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmimeakonadi
KDE 4 library.

%post -n %libkmimeakonadi -p /sbin/ldconfig
%postun -n %libkmimeakonadi -p /sbin/ldconfig

%files -n %libkmimeakonadi
%defattr(-,root,root)
%_kde_libdir/libkmimeakonadi.so.*

#-----------------------------------------------------------------------------

%package -n kde4-akonadi
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-akonadi

%description -n kde4-akonadi
Dialog KDE base widgets

%files -n kde4-akonadi
%defattr(-,root,root)
%_kde_bindir/akonadi
%_kde_bindir/akonadi_control
%_kde_bindir/akonadi_ical_resource
%_kde_bindir/akonadi_knut_resource
%_kde_bindir/akonadi_maildir_resource
%_kde_bindir/akonadi_mailthreader_agent
%_kde_bindir/akonadi_message_searchprovider
%_kde_bindir/akonadi_nntp_resource
%_kde_bindir/akonadi_strigi_searchprovider
%_kde_bindir/akonadi_vcard_resource
%_kde_bindir/akonadiconsole
%_kde_bindir/akonadiserver
%_kde_bindir/kabceditor
%_kde_bindir/kabcviewer
%_kde_bindir/kagenda
%_kde_appsdir/akonadi
%_kde_datadir/dbus-1/services/org.kde.Akonadi.Control.service
%_kde_datadir/kde4/services/akonadi.protocol
%_datadir/dbus-1/interfaces/org.kde.Akonadi.AgentManager.xml
%_datadir/dbus-1/interfaces/org.kde.Akonadi.CachePolicyManager.xml
%_datadir/dbus-1/interfaces/org.kde.Akonadi.NotificationManager.xml
%_datadir/dbus-1/interfaces/org.kde.Akonadi.ProfileManager.xml
%_datadir/dbus-1/interfaces/org.kde.Akonadi.SearchProviderManager.xml
%_datadir/dbus-1/interfaces/org.kde.Akonadi.Tracer.xml
%_datadir/dbus-1/interfaces/org.kde.Akonadi.TracerNotification.xml
%_kde_libdir/kde4/kio_akonadi.so
%_kde_libdir/kde4/libakonadi_serializer_addressee.so
%_kde_libdir/kde4/libakonadi_serializer_kcal.so
%_kde_libdir/kde4/libakonadi_serializer_mail.so

#-----------------------------------------------------------------------------

%define libkdepim %mklibname kdepim 5

%package -n %libkdepim
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdepim
KDE 4 library.

%post -n %libkdepim -p /sbin/ldconfig
%postun -n %libkdepim -p /sbin/ldconfig

%files -n %libkdepim
%defattr(-,root,root)
%_kde_libdir/libkdepim.so.*
%_kde_appsdir/kdepimwidgets
%_kde_appsdir/libkdepim
%_kde_datadir/icons/oxygen/22x22/actions/button_fewer.png
%_kde_datadir/icons/oxygen/22x22/actions/button_more.png
%_datadir/dbus-1/interfaces/org.kde.addressbook.service.xml
%_datadir/dbus-1/interfaces/org.kde.mailtransport.service.xml
%_kde_libdir/kde4/kpartsdesignerplugin.so
%_kde_libdir/kde4/plugins/designer/kdepimwidgets.so

#-----------------------------------------------------------------------------

%define libkholidays %mklibname kholidays 5

%package -n %libkholidays
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkholidays
KDE 4 library.

%post -n %libkholidays -p /sbin/ldconfig
%postun -n %libkholidays -p /sbin/ldconfig

%files -n %libkholidays
%defattr(-,root,root)
%_kde_libdir/libkholidays.so.*
%_kde_appsdir/libkholidays

#-----------------------------------------------------------------------------

%define libkleopatra %mklibname kleopatra 5

%package -n %libkleopatra
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkleopatra
KDE 4 library.

%post -n %libkleopatra -p /sbin/ldconfig
%postun -n %libkleopatra -p /sbin/ldconfig

%files -n %libkleopatra
%defattr(-,root,root)
%_kde_libdir/libkleopatra.so.*
%_kde_appsdir/libkleopatra
%_kde_datadir/icons/*/*/*/gpg*

#-----------------------------------------------------------------------------

%define libkpgp %mklibname kpgp 5

%package -n %libkpgp
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkpgp
KDE 4 library.

%post -n %libkpgp -p /sbin/ldconfig
%postun -n %libkpgp -p /sbin/ldconfig

%files -n %libkpgp
%defattr(-,root,root)
%_kde_libdir/libkpgp.so.*
%_kde_appsdir/kconf_update/kpgp-3.1-upgrade-address-data.pl
%_kde_appsdir/kconf_update/kpgp.upd

#-----------------------------------------------------------------------------

%package -n kde4-kleopatra
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kleopatra

%description -n kde4-kleopatra
Dialog KDE base widgets

%files -n kde4-kleopatra
%defattr(-,root,root)
%_kde_bindir/kleopatra
%_kde_bindir/kwatchgnupg
%_kde_datadir/applications/kde4/kleopatra_import.desktop
%_kde_appsdir/kleopatra/kleopatraui.rc
%_kde_appsdir/kwatchgnupg/kwatchgnupgui.rc
%_kde_appsdir/kwatchgnupg/pics/kwatchgnupg.png
%_kde_appsdir/kwatchgnupg/pics/kwatchgnupg2.png
%_kde_datadir/kde4/services/kleopatra_config_appear.desktop
%_kde_datadir/kde4/services/kleopatra_config_dirserv.desktop
%_kde_datadir/kde4/services/kleopatra_config_dnorder.desktop
%_kde_libdir/kde4/kcm_kleopatra.so

#-----------------------------------------------------------------------------

%define libkpimidentities %mklibname kpimidentities 5

%package -n %libkpimidentities
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkpimidentities
KDE 4 library.

%post -n %libkpimidentities -p /sbin/ldconfig
%postun -n %libkpimidentities -p /sbin/ldconfig

%files -n %libkpimidentities
%defattr(-,root,root)
%_kde_libdir/libkpimidentities.so.*

#-----------------------------------------------------------------------------

%define libksieve %mklibname ksieve 5

%package -n %libksieve
Summary: KDE 4 library
Group: System/Libraries

%description -n %libksieve
KDE 4 library.

%post -n %libksieve -p /sbin/ldconfig
%postun -n %libksieve -p /sbin/ldconfig

%files -n %libksieve
%defattr(-,root,root)
%_kde_libdir/libksieve.so.*

#-----------------------------------------------------------------------------

%define libmimelib %mklibname mimelib 5

%package -n %libmimelib
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmimelib
KDE 4 library.

%post -n %libmimelib -p /sbin/ldconfig
%postun -n %libmimelib -p /sbin/ldconfig

%files -n %libmimelib
%defattr(-,root,root)
%_kde_libdir/libmimelib.so.*

#-----------------------------------------------------------------------------

%define libakregatorinterfaces %mklibname akregatorinterfaces 5

%package -n %libakregatorinterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakregatorinterfaces
KDE 4 library.

%post -n %libakregatorinterfaces -p /sbin/ldconfig
%postun -n %libakregatorinterfaces -p /sbin/ldconfig

%files -n %libakregatorinterfaces
%defattr(-,root,root)
%_kde_libdir/libakregatorinterfaces.so.*

#-----------------------------------------------------------------------------

%define libakregatorprivate %mklibname akregatorprivate 5

%package -n %libakregatorprivate
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakregatorprivate
KDE 4 library.

%post -n %libakregatorprivate -p /sbin/ldconfig
%postun -n %libakregatorprivate -p /sbin/ldconfig

%files -n %libakregatorprivate
%defattr(-,root,root)
%_kde_libdir/libakregatorprivate.so.*

#-----------------------------------------------------------------------------

%package -n kde4-akregator
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-akregator

%description -n kde4-akregator
Dialog KDE base widgets

%files -n kde4-akregator
%defattr(-,root,root)
%_kde_bindir/akregator
%_kde_datadir/applications/kde4/akregator.desktop
%_kde_appsdir/akregator
%_kde_datadir/config.kcfg/akregator.kcfg
%_kde_datadir/icons/*/*/*/akregator*
%_kde_datadir/icons/*/*/*/rss*
%_kde_datadir/kde4/services/akregator_mk4storage_plugin.desktop
%_kde_datadir/kde4/services/akregator_part.desktop
%_kde_datadir/kde4/services/feed.protocol
%_kde_datadir/kde4/servicetypes/akregator_plugin.desktop
%_datadir/dbus-1/interfaces/org.kde.akregator.part.xml
%_kde_libdir/kde4/libakregator_mk4storage_plugin.so
%_kde_libdir/kde4/libakregatorpart.so
%_kde_docdir/HTML/en/akregator

#-----------------------------------------------------------------------------

%define libgpgmepp %mklibname gpgmepp 5

%package -n %libgpgmepp
Summary: KDE 4 library
Group: System/Libraries

%description -n %libgpgmepp
KDE 4 library.

%post -n %libgpgmepp -p /sbin/ldconfig
%postun -n %libgpgmepp -p /sbin/ldconfig

%files -n %libgpgmepp
%defattr(-,root,root)
%_kde_libdir/libgpgmepp.so.*

#-----------------------------------------------------------------------------

%define libkitchensyncprivate %mklibname kitchensyncprivate 4.2.0

%package -n %libkitchensyncprivate
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkitchensyncprivate
KDE 4 library.

%post -n %libkitchensyncprivate -p /sbin/ldconfig
%postun -n %libkitchensyncprivate -p /sbin/ldconfig

%files -n %libkitchensyncprivate
%defattr(-,root,root)
%_kde_libdir/libkitchensyncprivate.so.*

#-----------------------------------------------------------------------------

%define libqopensync %mklibname qopensync 4.2.0

%package -n %libqopensync
Summary: KDE 4 library
Group: System/Libraries

%description -n %libqopensync
KDE 4 library.

%post -n %libqopensync -p /sbin/ldconfig
%postun -n %libqopensync -p /sbin/ldconfig

%files -n %libqopensync
%defattr(-,root,root)
%_kde_libdir/libqopensync.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kitchensync
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kitchensync

%description -n kde4-kitchensync
Dialog KDE base widgets

%files -n kde4-kitchensync
%defattr(-,root,root)
%_kde_bindir/kitchensync
%_kde_datadir/applications/kde4/kitchensync.desktop
%_kde_appsdir/kitchensync
%_kde_datadir/icons/*/*/*/kitchensync*
%_kde_datadir/icons/*/*/*/mobile_*
%_kde_datadir/icons/*/*/*/hotsync*
%_kde_libdir/kde4/libkitchensyncpart.so

#-----------------------------------------------------------------------------

%define libknodecommon %mklibname knodecommon 5

%package -n %libknodecommon
Summary: KDE 4 library
Group: System/Libraries

%description -n %libknodecommon
KDE 4 library.

%post -n %libknodecommon -p /sbin/ldconfig
%postun -n %libknodecommon -p /sbin/ldconfig

%files -n %libknodecommon
%defattr(-,root,root)
%_kde_libdir/libknodecommon.so.*

#-----------------------------------------------------------------------------

%package -n kde4-knode
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-knode

%description -n kde4-knode
Dialog KDE base widgets

%files -n kde4-knode
%defattr(-,root,root)
%_kde_bindir/knode
%_kde_datadir/applications/kde4/KNode.desktop
%_kde_appsdir/knode
%_kde_datadir/icons/*/*/*/knode*
%_kde_datadir/kde4/services/knewsservice.protocol
%_kde_datadir/kde4/services/knode_config_accounts.desktop
%_kde_datadir/kde4/services/knode_config_appearance.desktop
%_kde_datadir/kde4/services/knode_config_cleanup.desktop
%_kde_datadir/kde4/services/knode_config_identity.desktop
%_kde_datadir/kde4/services/knode_config_post_news.desktop
%_kde_datadir/kde4/services/knode_config_privacy.desktop
%_kde_datadir/kde4/services/knode_config_read_news.desktop
%_datadir/dbus-1/interfaces/org.kde.knode.xml
%_kde_libdir/kde4/kcm_knode.so
%_kde_libdir/kde4/libknodepart.so
%_kde_docdir/HTML/en/knode

#-----------------------------------------------------------------------------

%define libkabinterfaces %mklibname kabinterfaces 5

%package -n %libkabinterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabinterfaces
KDE 4 library.

%post -n %libkabinterfaces -p /sbin/ldconfig
%postun -n %libkabinterfaces -p /sbin/ldconfig

%files -n %libkabinterfaces
%defattr(-,root,root)
%_kde_libdir/libkabinterfaces.so.*

#-----------------------------------------------------------------------------

%define libkaddressbook %mklibname kaddressbook 5

%package -n %libkaddressbook
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkaddressbook
KDE 4 library.

%post -n %libkaddressbook -p /sbin/ldconfig
%postun -n %libkaddressbook -p /sbin/ldconfig

%files -n %libkaddressbook
%defattr(-,root,root)
%_kde_libdir/libkaddressbook.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kaddressbook
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kaddressbook

%description -n kde4-kaddressbook
Dialog KDE base widgets

%files -n kde4-kaddressbook
%defattr(-,root,root)
%_kde_bindir/kaddressbook
%_kde_datadir/applications/kde4/kaddressbook.desktop
%_kde_appsdir/kaddressbook
%_kde_datadir/icons/*/*/*/kaddressbook*
%_kde_datadir/kde4/services/kabconfig.desktop
%_kde_datadir/kde4/services/kabcustomfields.desktop
%_kde_datadir/kde4/services/kabldapconfig.desktop
%_kde_datadir/kde4/services/kaddressbook
%_kde_datadir/kde4/services/ldifvcardthumbnail.desktop
%_kde_datadir/kde4/servicetypes/dbusaddressbook.desktop
%_kde_datadir/kde4/servicetypes/kaddressbook*
%_datadir/dbus-1/interfaces/org.kde.KAddressbook.Core.xml
%_kde_libdir/kde4/kcm_kabconfig.so
%_kde_libdir/kde4/kcm_kabcustomfields.so
%_kde_libdir/kde4/kcm_kabldapconfig.so
%_kde_libdir/kde4/ldifvcardthumbnail.so
%_kde_libdir/kde4/libkaddrbk_*
%_kde_libdir/kde4/libkaddressbookpart.so
%_kde_docdir/HTML/en/kaddressbook

#-----------------------------------------------------------------------------

%define libkalarm_resources %mklibname kalarm_resources 5

%package -n %libkalarm_resources
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkalarm_resources
KDE 4 library.

%post -n %libkalarm_resources -p /sbin/ldconfig
%postun -n %libkalarm_resources -p /sbin/ldconfig

%files -n %libkalarm_resources
%defattr(-,root,root)
%_kde_libdir/libkalarm_resources.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kalarm
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kalarm

%description -n kde4-kalarm
Dialog KDE base widgets

%files -n kde4-kalarm
%defattr(-,root,root)
%_kde_bindir/kalarm
%_kde_bindir/kalarmd
%_kde_datadir/applications/kde4/kalarm.desktop
%_kde_datadir/applications/kde4/kalarmd.desktop
%_kde_appsdir/kalarm/kalarmui.rc
%_kde_appsdir/kconf_update/kalarm-1.2.1-general.pl
%_kde_appsdir/kconf_update/kalarm-1.9.5-defaults.pl
%_kde_appsdir/kconf_update/kalarm-version.pl
%_kde_appsdir/kconf_update/kalarm.upd
%_kde_datadir/autostart/kalarm.tray.desktop
%_kde_datadir/autostart/kalarmd.autostart.desktop
%_kde_datadir/config.kcfg/kalarmconfig.kcfg
%_kde_datadir/icons/*/*/*/kalarm*
%_kde_datadir/icons/*/*/*/new_*
%_kde_datadir/kde4/services/kresources/alarms/local.desktop
%_kde_datadir/kde4/services/kresources/alarms/localdir.desktop
%_kde_datadir/kde4/services/kresources/alarms/remote.desktop
%_kde_datadir/kde4/services/kresources/kalarm_manager.desktop
%_datadir/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%_datadir/dbus-1/interfaces/org.kde.kalarm.kalarmd.Daemon.xml
%_datadir/dbus-1/interfaces/org.kde.kalarm.notify.xml
%_kde_libdir/kde4/kalarm_local.so
%_kde_libdir/kde4/kalarm_localdir.so
%_kde_libdir/kde4/kalarm_remote.so
%_kde_docdir/HTML/en/kalarm

#-----------------------------------------------------------------------------

%package -n kde4-ktimetracker
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-ktimetracker

%description -n kde4-ktimetracker
Dialog KDE base widgets

%files -n kde4-ktimetracker
%defattr(-,root,root)
%_kde_bindir/karm
%_kde_bindir/ktimetracker
%_kde_datadir/applications/kde4/karm.desktop
%_kde_appsdir/karm
%_kde_appsdir/karmpart
%_kde_datadir/icons/*/*/*/karm*
%_kde_datadir/kde4/services/karm_part.desktop
%_datadir/dbus-1/interfaces/org.kde.karm.Karm.xml
%_kde_libdir/kde4/libkarmpart.so
%_kde_docdir/HTML/en/ktimetracker/

#-----------------------------------------------------------------------------

%package ioslaves
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version

%description ioslaves
Dialog KDE base widgets

%files ioslaves
%defattr(-,root,root)
%_kde_datadir/kde4/services/imap4.protocol
%_kde_datadir/kde4/services/imaps.protocol
%_kde_datadir/kde4/services/mbox.protocol
%_kde_datadir/kde4/services/sieve.protocol
%_kde_libdir/kde4/kio_imap4.so
%_kde_libdir/kde4/kio_mbox.so
%_kde_libdir/kde4/kio_sieve.so

#-----------------------------------------------------------------------------

%define libkmailprivate %mklibname kmailprivate 5

%package -n %libkmailprivate
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmailprivate
KDE 4 library.

%post -n %libkmailprivate -p /sbin/ldconfig
%postun -n %libkmailprivate -p /sbin/ldconfig

%files -n %libkmailprivate
%defattr(-,root,root)
%_kde_libdir/libkmailprivate.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kmail
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kmail
Requires: %name-ioslaves
Requires: %name-plugins

%description -n kde4-kmail
Dialog KDE base widgets

%files -n kde4-kmail
%defattr(-,root,root)
%_kde_bindir/kmail
%_kde_bindir/kmail_antivir.sh
%_kde_bindir/kmail_clamav.sh
%_kde_bindir/kmail_fprot.sh
%_kde_bindir/kmail_sav.sh
%_kde_datadir/applications/kde4/KMail.desktop
%_kde_datadir/applications/kde4/kmail_view.desktop
%_kde_appsdir/kconf_update/kmail*
%_kde_appsdir/kconf_update/upgrade-signature.pl
%_kde_appsdir/kconf_update/upgrade-transport.pl
%_kde_appsdir/kmail
%_kde_datadir/config.kcfg/custommimeheader.kcfg
%_kde_datadir/config.kcfg/customtemplates_kfg.kcfg
%_kde_datadir/config.kcfg/kmail.kcfg
%_kde_datadir/config.kcfg/replyphrases.kcfg
%_kde_datadir/config.kcfg/templatesconfiguration_kfg.kcfg
%_kde_datadir/config/kmail.antispamrc
%_kde_datadir/config/kmail.antivirusrc
%_kde_datadir/icons/*/*/*/kmail.*
%_kde_datadir/icons/*/*/*/kmaillight.*
%_kde_datadir/kde4/services/kmail_config_accounts.desktop
%_kde_datadir/kde4/services/kmail_config_appearance.desktop
%_kde_datadir/kde4/services/kmail_config_composer.desktop
%_kde_datadir/kde4/services/kmail_config_identity.desktop
%_kde_datadir/kde4/services/kmail_config_misc.desktop
%_kde_datadir/kde4/services/kmail_config_security.desktop
%_kde_datadir/kde4/servicetypes/dbusimap.desktop
%_kde_datadir/kde4/servicetypes/dbusmail.desktop
%_datadir/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
%_datadir/dbus-1/interfaces/org.kde.kmail.mailcomposer.xml
%_kde_libdir/kde4/kcm_kmail.so
%_kde_libdir/kde4/libkmail_bodypartformatter_application_octetstream.so
%_kde_libdir/kde4/libkmailpart.so
%_kde_docdir/HTML/en/kmail

#-----------------------------------------------------------------------------

%package -n kde4-kmailcvt
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kmailcvt

%description -n kde4-kmailcvt
Dialog KDE base widgets

%files -n kde4-kmailcvt
%defattr(-,root,root)
%_kde_bindir/kmailcvt
%_kde_appsdir/kmailcvt/pics/step1.png
%_kde_datadir/icons/*/*/*/kmailcvt*

#-----------------------------------------------------------------------------

%package -n kde4-knotes
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-knotes
Requires: %name-kresources

%description -n kde4-knotes
Dialog KDE base widgets

%files -n kde4-knotes
%defattr(-,root,root)
%_kde_bindir/knotes
%_kde_datadir/applications/kde4/knotes.desktop
%_kde_datadir/config.kcfg/knoteconfig.kcfg
%_kde_datadir/config.kcfg/knotesglobalconfig.kcfg
%_kde_datadir/icons/*/*/*/knotes*
%_kde_appsdir/knotes
%_kde_datadir/kde4/services/kresources/knotes/local.desktop
%_kde_datadir/kde4/services/kresources/knotes_manager.desktop
%_datadir/dbus-1/interfaces/org.kde.KNotes.xml
%_kde_libdir/kde4/knotes_local.so
%_kde_docdir/HTML/en/knotes

#-----------------------------------------------------------------------------

%define libkontact %mklibname kontact 5

%package -n %libkontact
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkontact
KDE 4 library.

%post -n %libkontact -p /sbin/ldconfig
%postun -n %libkontact -p /sbin/ldconfig

%files -n %libkontact
%defattr(-,root,root)
%_kde_libdir/libkontact.so.*

#-----------------------------------------------------------------------------

%define libkpinterfaces %mklibname kpinterfaces 5

%package -n %libkpinterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkpinterfaces
KDE 4 library.

%post -n %libkpinterfaces -p /sbin/ldconfig
%postun -n %libkpinterfaces -p /sbin/ldconfig

%files -n %libkpinterfaces
%defattr(-,root,root)
%_kde_libdir/libkpinterfaces.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kontact
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kontact

%description -n kde4-kontact
Dialog KDE base widgets

%files -n kde4-kontact
%defattr(-,root,root)
%_kde_bindir/kontact
%_kde_datadir/applications/kde4/Kontact.desktop
%_kde_appsdir/knotes/knotes_part.rc
%_kde_appsdir/kontact/about/kontact.css
%_kde_appsdir/kontact/about/main.html
%_kde_appsdir/kontact/about/top-right-kontact.png
%_kde_appsdir/kontact/kontact.setdlg
%_kde_appsdir/kontact/kontactui.rc
%_kde_appsdir/kontactsummary/kontactsummary_part.rc
%_kde_datadir/config.kcfg/kontact.kcfg
%_kde_datadir/icons/*/*/*/kontact*
%_kde_datadir/kde4/services/kontactconfig.desktop
%_kde_datadir/kde4/services/kcmapptsummary.desktop
%_kde_datadir/kde4/services/kcmkmailsummary.desktop
%_kde_datadir/kde4/services/kcmkontactsummary.desktop
%_kde_datadir/kde4/services/kcmsdsummary.desktop
%_kde_datadir/kde4/services/kcmtodosummary.desktop
%_kde_datadir/kde4/services/kontact
%_kde_datadir/kde4/servicetypes/kontactplugin.desktop
%_datadir/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%_kde_libdir/kde4/kcm_apptsummary.so
%_kde_libdir/kde4/kcm_kmailsummary.so
%_kde_libdir/kde4/kcm_kontact.so
%_kde_libdir/kde4/kcm_kontactsummary.so
%_kde_libdir/kde4/kcm_sdsummary.so
%_kde_libdir/kde4/kcm_todosummary.so
%_kde_libdir/kde4/libkontact_*
%_kde_docdir/HTML/en/kontact

#-----------------------------------------------------------------------------

%define libkocorehelper %mklibname kocorehelper 5

%package -n %libkocorehelper
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkocorehelper
KDE 4 library.

%post -n %libkocorehelper -p /sbin/ldconfig
%postun -n %libkocorehelper -p /sbin/ldconfig

%files -n %libkocorehelper
%defattr(-,root,root)
%_kde_libdir/libkocorehelper.so.*

#-----------------------------------------------------------------------------

%define libkorg_stdprinting %mklibname korg_stdprinting 5

%package -n %libkorg_stdprinting
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorg_stdprinting
KDE 4 library.

%post -n %libkorg_stdprinting -p /sbin/ldconfig
%postun -n %libkorg_stdprinting -p /sbin/ldconfig

%files -n %libkorg_stdprinting
%defattr(-,root,root)
%_kde_libdir/libkorg_stdprinting.so.*

#-----------------------------------------------------------------------------

%define libkorganizer %mklibname korganizer 5

%package -n %libkorganizer
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorganizer
KDE 4 library.

%post -n %libkorganizer -p /sbin/ldconfig
%postun -n %libkorganizer -p /sbin/ldconfig

%files -n %libkorganizer
%defattr(-,root,root)
%_kde_libdir/libkorganizer.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_calendar %mklibname korganizer_calendar 5

%package -n %libkorganizer_calendar
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorganizer_calendar
KDE 4 library.

%post -n %libkorganizer_calendar -p /sbin/ldconfig
%postun -n %libkorganizer_calendar -p /sbin/ldconfig

%files -n %libkorganizer_calendar
%defattr(-,root,root)
%_kde_libdir/libkorganizer_calendar.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_eventviewer %mklibname korganizer_eventviewer 5

%package -n %libkorganizer_eventviewer
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorganizer_eventviewer
KDE 4 library.

%post -n %libkorganizer_eventviewer -p /sbin/ldconfig
%postun -n %libkorganizer_eventviewer -p /sbin/ldconfig

%files -n %libkorganizer_eventviewer
%defattr(-,root,root)
%_kde_libdir/libkorganizer_eventviewer.so.*

#-----------------------------------------------------------------------------

%define libkorganizer_interfaces %mklibname korganizer_interfaces 5

%package -n %libkorganizer_interfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorganizer_interfaces
KDE 4 library.

%post -n %libkorganizer_interfaces -p /sbin/ldconfig
%postun -n %libkorganizer_interfaces -p /sbin/ldconfig

%files -n %libkorganizer_interfaces
%defattr(-,root,root)
%_kde_libdir/libkorganizer_interfaces.so.*

#-----------------------------------------------------------------------------

%package -n kde4-korganizer
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-korganizer
Requires: %name-kresources

%description -n kde4-korganizer
Dialog KDE base widgets

%files -n kde4-korganizer
%defattr(-,root,root)
%_kde_bindir/ical2vcal
%_kde_bindir/korgac
%_kde_bindir/korganizer
%_kde_datadir/applications/kde4/korganizer-import.desktop
%_kde_datadir/applications/kde4/korganizer.desktop
%_kde_appsdir/kconf_update/korganizer.upd
%_kde_appsdir/korgac/icons/oxygen/22x22/actions/korgac.png
%_kde_appsdir/korgac/icons/oxygen/22x22/actions/korgac_disabled.png
%_kde_appsdir/korganizer
%_kde_datadir/autostart/korgac.desktop
%_kde_datadir/config.kcfg/korganizer.kcfg
%_kde_datadir/config/korganizer.knsrc
%_kde_datadir/icons/*/*/*/korganizer*
%_kde_datadir/kde4/services/korganizer*
%_kde_datadir/kde4/services/webcal.protocol
%_kde_datadir/kde4/servicetypes/calendardecoration.desktop
%_kde_datadir/kde4/servicetypes/calendarplugin.desktop
%_kde_datadir/kde4/servicetypes/dbuscalendar.desktop
%_kde_datadir/kde4/servicetypes/korganizerpart.desktop
%_kde_datadir/kde4/servicetypes/korgprintplugin.desktop
%_kde_datadir/kde4/servicetypes/oldcalendardecoration.desktop
%_datadir/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%_datadir/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%_datadir/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%_kde_libdir/kde4/kcm_korganizer.so
%_kde_libdir/kde4/libkorg_*
%_kde_libdir/kde4/libkorganizerpart.so

#-----------------------------------------------------------------------------

%define libkmobiletools %mklibname kmobiletools 5

%package -n %libkmobiletools
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmobiletools
KDE 4 library.

%post -n %libkmobiletools -p /sbin/ldconfig
%postun -n %libkmobiletools -p /sbin/ldconfig

%files -n %libkmobiletools
%defattr(-,root,root)
%_kde_libdir/libkmobiletools.so.*

#-----------------------------------------------------------------------------

%define libkmobiletools_at %mklibname kmobiletools_at 5

%package -n %libkmobiletools_at
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmobiletools_at
KDE 4 library.

%post -n %libkmobiletools_at -p /sbin/ldconfig
%postun -n %libkmobiletools_at -p /sbin/ldconfig

%files -n %libkmobiletools_at
%defattr(-,root,root)
%_kde_libdir/libkmobiletools_at.so.*

#-----------------------------------------------------------------------------

%define libkmobiletoolsengineui %mklibname kmobiletoolsengineui 5

%package -n %libkmobiletoolsengineui
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmobiletoolsengineui
KDE 4 library.

%post -n %libkmobiletoolsengineui -p /sbin/ldconfig
%postun -n %libkmobiletoolsengineui -p /sbin/ldconfig

%files -n %libkmobiletoolsengineui
%defattr(-,root,root)
%_kde_libdir/libkmobiletoolsengineui.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kmobiletools
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kmobiletools

%description -n kde4-kmobiletools
Dialog KDE base widgets

%files -n kde4-kmobiletools
%defattr(-,root,root)
%_kde_bindir/kmobiletools
%_kde_datadir/applications/kde4/kmobiletools.desktop
%_kde_appsdir/akonadi/plugins/serializer/akonadi_serializer_sms.desktop
%_kde_appsdir/kmobiletools
%_kde_datadir/config.kcfg/atengineconfig.kcfg
%_kde_datadir/config.kcfg/kmobiletools_devices.kcfg
%_kde_datadir/kde4/services/at_engine.desktop
%_kde_datadir/kde4/services/kmobiletools_mainpart.desktop
%_kde_datadir/kde4/servicetypes/kmobiletoolsengine.desktop
%_kde_libdir/kde4/libakonadi_serializer_sms.so
%_kde_libdir/kde4/libkmobiletoolsmainpart.so
%_kde_docdir/HTML/en/kmobiletools

#-----------------------------------------------------------------------------

%package -n kde4-korn
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-korn

%description -n kde4-korn
Dialog KDE base widgets

%files -n kde4-korn
%defattr(-,root,root)
%_kde_bindir/korn
%_kde_datadir/applications/kde4/KOrn.desktop
%_kde_appsdir/kconf_update/korn*
%_kde_datadir/icons/*/*/*/korn*
%_datadir/dbus-1/interfaces/org.kde.korn.BoxContainerItem.xml
%_datadir/dbus-1/interfaces/org.kde.korn.MailDrop.xml
%_kde_docdir/HTML/en/korn

#-----------------------------------------------------------------------------

%define libkpilot %mklibname kpilot 5

%package -n %libkpilot
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkpilot
KDE 4 library.

%post -n %libkpilot -p /sbin/ldconfig
%postun -n %libkpilot -p /sbin/ldconfig

%files -n %libkpilot
%defattr(-,root,root)
%_kde_libdir/libkpilot.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kpilot
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kpilot

%description -n kde4-kpilot
Dialog KDE base widgets

%files -n kde4-kpilot
%defattr(-,root,root)
%_kde_bindir/kpalmdoc
%_kde_bindir/kpilot
%_kde_bindir/kpilotDaemon
%_kde_datadir/applications/kde4/kpalmdoc.desktop
%_kde_datadir/applications/kde4/kpilot.desktop
%_kde_datadir/applications/kde4/kpilotdaemon.desktop
%_kde_appsdir/kconf_update/kpalmdoc.upd
%_kde_appsdir/kconf_update/kpilot.upd
%_kde_appsdir/kpilot/kpilotui.rc
%_kde_appsdir/kpilot/sysinfoconduit/Template.html
%_kde_appsdir/kpilot/sysinfoconduit/Template.txt
%_kde_datadir/config.kcfg/docconduit.kcfg
%_kde_datadir/config.kcfg/kpalmdoc.kcfg
%_kde_datadir/config.kcfg/kpilot.kcfg
%_kde_datadir/config.kcfg/kpilotlib.kcfg
%_kde_datadir/config.kcfg/memofileconduit.kcfg
%_kde_datadir/config.kcfg/popmail.kcfg
%_kde_datadir/config.kcfg/sysinfoconduit.kcfg
%_kde_datadir/config.kcfg/timeconduit.kcfg
%_kde_datadir/config.kcfg/vcalconduitbase.kcfg
%_kde_datadir/icons/*/*/*/kpalm*
%_kde_datadir/icons/*/*/*/kpilot*
%_kde_datadir/kde4/services/doc_conduit.desktop
%_kde_datadir/kde4/services/kpilot_config.desktop
%_kde_datadir/kde4/services/memofile-conduit.desktop
%_kde_datadir/kde4/services/notepad-conduit.desktop
%_kde_datadir/kde4/services/null-conduit.desktop
%_kde_datadir/kde4/services/popmail-conduit.desktop
%_kde_datadir/kde4/services/sysinfo_conduit.desktop
%_kde_datadir/kde4/services/time_conduit.desktop
%_kde_datadir/kde4/services/todo-conduit.desktop
%_kde_datadir/kde4/services/vcal-conduit.desktop
%_kde_datadir/kde4/servicetypes/kpilotconduit.desktop
%_kde_libdir/kde4/kcm_kpilot.so
%_kde_libdir/kde4/libconduit_doc.so
%_kde_libdir/kde4/libconduit_memofile.so
%_kde_libdir/kde4/libconduit_notepad.so
%_kde_libdir/kde4/libconduit_null.so
%_kde_libdir/kde4/libconduit_popmail.so
%_kde_libdir/kde4/libconduit_sysinfo.so
%_kde_libdir/kde4/libconduit_time.so
%_kde_libdir/kde4/libconduit_todo.so
%_kde_libdir/kde4/libconduit_vcal.so

#-----------------------------------------------------------------------------

%define libkabc_groupdav %mklibname kabc_groupdav 5

%package -n %libkabc_groupdav
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabc_groupdav
KDE 4 library.

%post -n %libkabc_groupdav -p /sbin/ldconfig
%postun -n %libkabc_groupdav -p /sbin/ldconfig

%files -n %libkabc_groupdav
%defattr(-,root,root)
%_kde_libdir/libkabc_groupdav.so.*

#-----------------------------------------------------------------------------

%define libkabc_slox %mklibname kabc_slox 5

%package -n %libkabc_slox
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabc_slox
KDE 4 library.

%post -n %libkabc_slox -p /sbin/ldconfig
%postun -n %libkabc_slox -p /sbin/ldconfig

%files -n %libkabc_slox
%defattr(-,root,root)
%_kde_libdir/libkabc_slox.so.*

#-----------------------------------------------------------------------------

%define libkabc_xmlrpc %mklibname kabc_xmlrpc 5

%package -n %libkabc_xmlrpc
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabc_xmlrpc
KDE 4 library.

%post -n %libkabc_xmlrpc -p /sbin/ldconfig
%postun -n %libkabc_xmlrpc -p /sbin/ldconfig

%files -n %libkabc_xmlrpc
%defattr(-,root,root)
%_kde_libdir/libkabc_xmlrpc.so.*

#-----------------------------------------------------------------------------

%define libkabckolab %mklibname kabckolab 5

%package -n %libkabckolab
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabckolab
KDE 4 library.

%post -n %libkabckolab -p /sbin/ldconfig
%postun -n %libkabckolab -p /sbin/ldconfig

%files -n %libkabckolab
%defattr(-,root,root)
%_kde_libdir/libkabckolab.so.*

#-----------------------------------------------------------------------------

%define libkcal_groupdav %mklibname kcal_groupdav 5

%package -n %libkcal_groupdav
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcal_groupdav
KDE 4 library.

%post -n %libkcal_groupdav -p /sbin/ldconfig
%postun -n %libkcal_groupdav -p /sbin/ldconfig

%files -n %libkcal_groupdav
%defattr(-,root,root)
%_kde_libdir/libkcal_groupdav.so.*

#-----------------------------------------------------------------------------

%define libkcal_resourceblog %mklibname kcal_resourceblog 5

%package -n %libkcal_resourceblog
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcal_resourceblog
KDE 4 library.

%post -n %libkcal_resourceblog -p /sbin/ldconfig
%postun -n %libkcal_resourceblog -p /sbin/ldconfig

%files -n %libkcal_resourceblog
%defattr(-,root,root)
%_kde_libdir/libkcal_resourceblog.so.*

#-----------------------------------------------------------------------------

%define libkcal_resourceremote %mklibname kcal_resourceremote 5

%package -n %libkcal_resourceremote
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcal_resourceremote
KDE 4 library.

%post -n %libkcal_resourceremote -p /sbin/ldconfig
%postun -n %libkcal_resourceremote -p /sbin/ldconfig

%files -n %libkcal_resourceremote
%defattr(-,root,root)
%_kde_libdir/libkcal_resourceremote.so.*

#-----------------------------------------------------------------------------

%define libkcal_slox %mklibname kcal_slox 5

%package -n %libkcal_slox
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcal_slox
KDE 4 library.

%post -n %libkcal_slox -p /sbin/ldconfig
%postun -n %libkcal_slox -p /sbin/ldconfig

%files -n %libkcal_slox
%defattr(-,root,root)
%_kde_libdir/libkcal_slox.so.*

#-----------------------------------------------------------------------------

%define libkcal_xmlrpc %mklibname kcal_xmlrpc 5

%package -n %libkcal_xmlrpc
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcal_xmlrpc
KDE 4 library.

%post -n %libkcal_xmlrpc -p /sbin/ldconfig
%postun -n %libkcal_xmlrpc -p /sbin/ldconfig

%files -n %libkcal_xmlrpc
%defattr(-,root,root)
%_kde_libdir/libkcal_xmlrpc.so.*

#-----------------------------------------------------------------------------

%define libkcalkolab %mklibname kcalkolab 5

%package -n %libkcalkolab
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcalkolab
KDE 4 library.

%post -n %libkcalkolab -p /sbin/ldconfig
%postun -n %libkcalkolab -p /sbin/ldconfig

%files -n %libkcalkolab
%defattr(-,root,root)
%_kde_libdir/libkcalkolab.so.*

#-----------------------------------------------------------------------------

%define libkgroupwarebase %mklibname kgroupwarebase 5

%package -n %libkgroupwarebase
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkgroupwarebase
KDE 4 library.

%post -n %libkgroupwarebase -p /sbin/ldconfig
%postun -n %libkgroupwarebase -p /sbin/ldconfig

%files -n %libkgroupwarebase
%defattr(-,root,root)
%_kde_libdir/libkgroupwarebase.so.*

#-----------------------------------------------------------------------------

%define libkgroupwaredav %mklibname kgroupwaredav 5

%package -n %libkgroupwaredav
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkgroupwaredav
KDE 4 library.

%post -n %libkgroupwaredav -p /sbin/ldconfig
%postun -n %libkgroupwaredav -p /sbin/ldconfig

%files -n %libkgroupwaredav
%defattr(-,root,root)
%_kde_libdir/libkgroupwaredav.so.*

#-----------------------------------------------------------------------------

%define libknotes_xmlrpc %mklibname knotes_xmlrpc 5

%package -n %libknotes_xmlrpc
Summary: KDE 4 library
Group: System/Libraries

%description -n %libknotes_xmlrpc
KDE 4 library.

%post -n %libknotes_xmlrpc -p /sbin/ldconfig
%postun -n %libknotes_xmlrpc -p /sbin/ldconfig

%files -n %libknotes_xmlrpc
%defattr(-,root,root)
%_kde_libdir/libknotes_xmlrpc.so.*

#-----------------------------------------------------------------------------

%define libknoteskolab %mklibname knoteskolab 5

%package -n %libknoteskolab
Summary: KDE 4 library
Group: System/Libraries

%description -n %libknoteskolab
KDE 4 library.

%post -n %libknoteskolab -p /sbin/ldconfig
%postun -n %libknoteskolab -p /sbin/ldconfig

%files -n %libknoteskolab
%defattr(-,root,root)
%_kde_libdir/libknoteskolab.so.*

#-----------------------------------------------------------------------------

%define libkslox %mklibname kslox 5

%package -n %libkslox
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkslox
KDE 4 library.

%post -n %libkslox -p /sbin/ldconfig
%postun -n %libkslox -p /sbin/ldconfig

%files -n %libkslox
%defattr(-,root,root)
%_kde_libdir/libkslox.so.*

#-----------------------------------------------------------------------------

%package kresources
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kresources

%description kresources
Dialog KDE base widgets

%files kresources
%defattr(-,root,root)
%_kde_datadir/kde4/services/kresources/kabc/kabc_groupdav.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_opengroupware.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_ox.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_slox.desktop
%_kde_datadir/kde4/services/kresources/kabc/kabc_xmlrpc.desktop
%_kde_datadir/kde4/services/kresources/kabc/kolab.desktop
%_kde_datadir/kde4/services/kresources/kcal/blog.desktop
%_kde_datadir/kde4/services/kresources/kcal/kabc.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_groupdav.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_opengroupware.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_ox.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_resourcefeatureplan.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_slox.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_xmlrpc.desktop
%_kde_datadir/kde4/services/kresources/kcal/kolab.desktop
%_kde_datadir/kde4/services/kresources/kcal/remote.desktop
%_kde_datadir/kde4/services/kresources/knotes/knotes_xmlrpc.desktop
%_kde_datadir/kde4/services/kresources/knotes/kolabresource.desktop
%_kde_libdir/kde4/kabc_groupdav.so
%_kde_libdir/kde4/kabc_kolab.so
%_kde_libdir/kde4/kabc_slox.so
%_kde_libdir/kde4/kabc_xmlrpc.so
%_kde_libdir/kde4/kcal_blog.so
%_kde_libdir/kde4/kcal_groupdav.so
%_kde_libdir/kde4/kcal_kabc.so
%_kde_libdir/kde4/kcal_kolab.so
%_kde_libdir/kde4/kcal_remote.so
%_kde_libdir/kde4/kcal_resourcefeatureplan.*
%_kde_libdir/kde4/kcal_slox.so
%_kde_libdir/kde4/kcal_xmlrpc.so
%_kde_libdir/kde4/knotes_kolab.so
%_kde_libdir/kde4/knotes_xmlrpc.so

#-----------------------------------------------------------------------------

%package -n kde4-ktnef
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-ktnef

%description -n kde4-ktnef
Dialog KDE base widgets

%files -n kde4-ktnef
%defattr(-,root,root)
%_kde_bindir/ktnef
%_kde_datadir/applications/kde4/ktnef.desktop
%_kde_appsdir/ktnef
%_kde_datadir/icons/*/*/*/ktnef*

#-----------------------------------------------------------------------------

%package plugins
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-plugins

%description plugins
Dialog KDE base widgets

%files plugins
%defattr(-,root,root)
%_kde_appsdir/kmail/plugins/bodypartformatter/text_calendar.desktop
%_kde_appsdir/kmail/plugins/bodypartformatter/text_vcard.desktop
%_kde_appsdir/kmail/plugins/bodypartformatter/text_xdiff.desktop
%_kde_libdir/kde4/ktexteditorkabcbridge.so
%_kde_libdir/kde4/libkmail_bodypartformatter_text_calendar.so
%_kde_libdir/kde4/libkmail_bodypartformatter_text_vcard.so
%_kde_libdir/kde4/libkmail_bodypartformatter_text_xdiff.so

#-----------------------------------------------------------------------------

%define libqgpgme %mklibname qgpgme 5

%package -n %libqgpgme
Summary: KDE 4 library
Group: System/Libraries

%description -n %libqgpgme
KDE 4 library.

%post -n %libqgpgme -p /sbin/ldconfig
%postun -n %libqgpgme -p /sbin/ldconfig

%files -n %libqgpgme
%defattr(-,root,root)
%_kde_libdir/libqgpgme.so.*

#-----------------------------------------------------------------------------

%package wizards
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-wizards

%description wizards
Dialog KDE base widgets

%files wizards
%defattr(-,root,root)
%_kde_bindir/egroupwarewizard
%_kde_bindir/groupwarewizard
%_kde_bindir/kolabwizard
%_kde_bindir/sloxwizard
%_kde_datadir/applications/kde4/groupwarewizard.desktop
%_kde_datadir/config.kcfg/egroupware.kcfg
%_kde_datadir/config.kcfg/groupwise.kcfg
%_kde_datadir/config.kcfg/kolab.kcfg
%_kde_datadir/config.kcfg/slox.kcfg

#-----------------------------------------------------------------------------

%define libmaildir %mklibname maildir 5

%package -n %libmaildir
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmaildir
KDE 4 library.

%post -n %libmaildir -p /sbin/ldconfig
%postun -n %libmaildir -p /sbin/ldconfig

%files -n %libmaildir
%defattr(-,root,root)
%_kde_libdir/libmaildir.so.*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdegraphics
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libkode = %epoch:%version
Requires: %libkschema = %epoch:%version
Requires: %libkschemawidgets = %epoch:%version
Requires: %libkxmlcommon = %epoch:%version
Requires: %libschema = %epoch:%version
Requires: %libwscl = %epoch:%version
Requires: %libwsdl = %epoch:%version
Requires: %libakonadi = %epoch:%version
Requires: %libakonadicomponents = %epoch:%version
Requires: %libakonadiprivate = %epoch:%version
Requires: %libakonadisearchprovider = %epoch:%version
Requires: %libkabcakonadi = %epoch:%version
Requires: %libkmimeakonadi = %epoch:%version
Requires: %libkdepim = %epoch:%version
Requires: %libkholidays = %epoch:%version
Requires: %libkleopatra = %epoch:%version
Requires: %libkpgp = %epoch:%version
Requires: %libkpimidentities = %epoch:%version
Requires: %libksieve = %epoch:%version
Requires: %libmimelib = %epoch:%version
Requires: %libakregatorinterfaces = %epoch:%version
Requires: %libakregatorprivate = %epoch:%version
Requires: %libgpgmepp = %epoch:%version
Requires: %libkitchensyncprivate = %epoch:%version
Requires: %libqopensync = %epoch:%version
Requires: %libknodecommon = %epoch:%version
Requires: %libkabinterfaces = %epoch:%version
Requires: %libkaddressbook = %epoch:%version
Requires: %libkalarm_resources = %epoch:%version
Requires: %libkmailprivate = %epoch:%version
Requires: %libkontact = %epoch:%version
Requires: %libkpinterfaces = %epoch:%version
Requires: %libkocorehelper = %epoch:%version
Requires: %libkorg_stdprinting = %epoch:%version
Requires: %libkorganizer = %epoch:%version
Requires: %libkorganizer_calendar = %epoch:%version
Requires: %libkorganizer_eventviewer = %epoch:%version
Requires: %libkorganizer_interfaces = %epoch:%version
Requires: %libkmobiletools = %epoch:%version
Requires: %libkmobiletools_at = %epoch:%version
Requires: %libkmobiletoolsengineui = %epoch:%version
Requires: %libkpilot = %epoch:%version
Requires: %libkabc_groupdav = %epoch:%version
Requires: %libkabc_slox = %epoch:%version
Requires: %libkabc_xmlrpc = %epoch:%version
Requires: %libkabckolab = %epoch:%version
Requires: %libkcal_groupdav = %epoch:%version
Requires: %libkcal_resourceblog = %epoch:%version
Requires: %libkcal_resourceremote = %epoch:%version
Requires: %libkcal_slox = %epoch:%version
Requires: %libkcal_xmlrpc = %epoch:%version
Requires: %libkcalkolab = %epoch:%version
Requires: %libkgroupwarebase = %epoch:%version
Requires: %libkgroupwaredav = %epoch:%version
Requires: %libknotes_xmlrpc = %epoch:%version
Requires: %libknoteskolab = %epoch:%version
Requires: %libkslox = %epoch:%version
Requires: %libqgpgme = %epoch:%version
Requires: %libmaildir = %epoch:%version
Requires: %libkcal_resourcefeatureplan = %epoch:%version

%description  devel
This package contains header files needed if you wish to build applications based on kdegraphics.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*
%_kde_appsdir/cmake/modules/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%version

%build
%cmake_kde4 \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=debugfull
%endif

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

