%define with_kitchensync 0
%{?_with_kitchensync: %{expand: %%global with_kitchensync 1}}

%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053190
%endif

Name: kdepim4
Summary: K Desktop Environment
Version: 4.4.2
Release: %mkrel 3
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://pim.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.tar.bz2
%endif
# Mandriva "customization" patches  0 - 99
Patch0:   kdepim-4.2.95-kmail-first-message.patch 
Patch1:   kdepim-4.3.90-fix-desktop-files.patch
# Patches from branch 100 - 199

# Trunk Patches 200 - 299
Patch200:  kdepim-4.4.1-t1088322-kmail-do-not-start-akonadi.patch
Patch201:  kdepim-4.4.1-t1088359-kontact-do-not-start-akonadi.patch
Patch202:  kdepim-4.4.1-t1088354-kaddressbook-do-not-start-akonadi.patch
# Test patches : 300+
Patch300:      kdepim-4.3.2-kmail-nepomuk.patch
#(nl) : (301-302) Patch from Kubuntu
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdelibs4-experimental-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel >= 2:4.2.98
BuildRequires: kdepim4-runtime-devel >= 4.2.98
BuildRequires: gpgme-devel
BuildRequires: X11-devel 
BuildRequires: flex 
BuildRequires: byacc 
BuildRequires: pam
BuildRequires: libncurses-devel
BuildRequires: readline-devel
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
BuildRequires: akonadi-devel
BuildRequires: shared-desktop-ontologies-devel
BuildRequires: nepomuk-scribo-devel
#(nl) Do not enable back w/o kde team agreement
#BuildRequires: libindicate-qt-devel
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
#Suggests: nepomuk-email-feeder
Obsoletes: kpilot < %epoch:%version
Obsoletes: korn <= 2:4.1.0
%if %mdkversion >= 200910
Obsoletes: kdepim-korn < 1:3.5.10-2
Obsoletes: kdepim-kandy < 1:3.5.10-2
Obsoletes: kdepim-ktnef < 1:3.5.10-2
Obsoletes: kdepim < 1:3.5.10-2
%endif
Obsoletes: ktnef

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer and
           kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- ktimetracker: Time tracker.
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client
	- kmailcvt: converst addressbooks to kmail format
%if %{with_kitchensync}
    - kitchensync: Synchronisation framework, still under heavy development.
%endif

%files

#----------------------------------------------------------------------

%package core
Summary: Core files for kdepim
Group: Graphical desktop/KDE	
Requires: kdelibs4-core
Requires: kdebase4-runtime
Requires: akonadi-kde
Obsoletes: libkdepim42-common < 1:3.93.0-1
Obsoletes: kdepim4-common < 1:3.93.0-1
Obsoletes: kdepim4-plasma-applets < 1:4.1 
Obsoletes: %{mklibname akonadisearchprovider 4} < 2:3.94.1-0.729215.1
%if %mdkversion >= 200910
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim-knotes < 1:3.5.9-10mdv
Conflicts: kdepim-kaddressbook < 1:3.5.9-10mdv
Obsoletes: kdepim-common < 1:3.5.10-2
%endif
Obsoletes: kode < 2:4.3
Conflicts: akonadi-kde < 2:4.3.85

%description core
Core files from kdepim.

%files core
%defattr(-,root,root,-)
%_kde_bindir/akonadiconsole
%_kde_datadir/applications/kde4/akonadiconsole.desktop
%_kde_appsdir/akonadiconsole/akonadiconsoleui.rc
%_kde_libdir/strigi/*
%_kde_iconsdir/*/*/*/*
%dir %_kde_datadir/kde4/services/kontact

#-----------------------------------------------------------------------------

%define gwsoap_major 4
%define libgwsoap %mklibname gwsoap %{gwsoap_major}

%package -n %libgwsoap
Summary: KDE 4 library
Group: System/Libraries

%description -n %libgwsoap
KDE 4 library.

%files -n %libgwsoap
%defattr(-,root,root)
%_kde_libdir/libgwsoap.so.%{gwsoap_major}*

#-----------------------------------------------------------------------------

%define kaddressbookprivate_major 4
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %libkaddressbookprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkaddressbookprivate
KDE 4 library.

%files -n %libkaddressbookprivate
%defattr(-,root,root)
%_kde_libdir/libkaddressbookprivate.so.%{kaddressbookprivate_major}*

#-----------------------------------------------------------------------------

%define kontactprivate_major 4
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %libkontactprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkontactprivate
KDE 4 library.

%files -n %libkontactprivate
%defattr(-,root,root)
%_kde_libdir/libkontactprivate.so.%{kontactprivate_major}*

#-----------------------------------------------------------------------------

%define korganizer_core_major 4
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %libkorganizer_core
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkorganizer_core
KDE 4 library.

%files -n %libkorganizer_core
%defattr(-,root,root)
%_kde_libdir/libkorganizer_core.so.%{korganizer_core_major}*

#-----------------------------------------------------------------------------

%define libkdepim %mklibname kdepim 4

%package -n %libkdepim
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1
Obsoletes: %{_lib}kdepim42-index < 1:3.93.0-1
%if %mdkversion >= 200910
Conflicts: kdepim-common < 1:3.5.9-10mdv
%endif

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

%define kpgp_major 4
%define libkpgp %mklibname kpgp %{kpgp_major}

%package -n %libkpgp
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkpgp
KDE 4 library.

%files -n %libkpgp
%defattr(-,root,root)
%_kde_libdir/libkpgp.so.%{kpgp_major}*
#TODO: move away from here
%_kde_appsdir/kconf_update/kpgp-3.1-upgrade-address-data.pl
%_kde_appsdir/kconf_update/kpgp.upd

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
%_kde_datadir/applications/kde4/kleopatra.desktop
%_kde_configdir/libkleopatrarc
%_kde_datadir/applications/kde4/kleopatra_import.desktop
%_kde_appsdir/kleopatra
%_kde_appsdir/libkleopatra
%_kde_appsdir/kwatchgnupg
%_kde_datadir/kde4/services/kleopatra_*
%_kde_libdir/kde4/kcm_kleopatra.so
%doc %_kde_docdir/*/*/kleopatra
%doc %_kde_docdir/*/*/kwatchgnupg

#-----------------------------------------------------------------------------

%define ksieve_major 4
%define libksieve %mklibname ksieve %{ksieve_major}

%package -n %libksieve
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libksieve
KDE 4 library.

%files -n %libksieve
%defattr(-,root,root)
%_kde_libdir/libksieve.so.%{ksieve_major}*

#-----------------------------------------------------------------------------

%define mimelib_major 4
%define libmimelib %mklibname mimelib %{mimelib_major}

%package -n %libmimelib
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libmimelib
KDE 4 library.

%files -n %libmimelib
%defattr(-,root,root)
%_kde_libdir/libmimelib.so.%{mimelib_major}*

#-----------------------------------------------------------------------------

%define akregatorinterfaces_major 4
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %libakregatorinterfaces
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1
Obsoletes: %{_lib}kpinterfaces4 < 2:4.0.80-1

%description -n %libakregatorinterfaces
KDE 4 library.

%files -n %libakregatorinterfaces
%defattr(-,root,root)
%_kde_libdir/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#-----------------------------------------------------------------------------

%define akregatorprivate_major 4
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %libakregatorprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

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
%if %mdkversion >= 200910
Obsoletes: kdepim-akregator < 1:3.5.10-2
%endif
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
%_kde_datadir/kde4/services/kontact/akregatorplugin.desktop
%_kde_datadir/config.kcfg/akregator.kcfg
%_kde_datadir/kde4/services/akregator_*
%_kde_datadir/kde4/services/feed.protocol
%_kde_datadir/kde4/servicetypes/akregator_plugin.desktop
%_kde_libdir/kde4/akregator*
%_kde_libdir/kde4/kontact_akregatorplugin.so
%doc %_kde_docdir/HTML/en/akregator

#-----------------------------------------------------------------------------

%if %{with_kitchensync}

%define kitchensyncprivate_major 4
%define libkitchensyncprivate %mklibname kitchensyncprivate %{kitchensyncprivate_major}

%package -n %libkitchensyncprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkitchensyncprivate
KDE 4 library.

%files -n %libkitchensyncprivate
%defattr(-,root,root)
%_kde_libdir/libkitchensyncprivate.so.%{kitchensyncprivate_major}*

#-----------------------------------------------------------------------------

%define qopensync_major 4
%define libqopensync %mklibname qopensync %{qopensync_major}

%package -n %libqopensync
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libqopensync
KDE 4 library.

%files -n %libqopensync
%defattr(-,root,root)
%_kde_libdir/libqopensync.so.%{qopensync_major}*

#-----------------------------------------------------------------------------

%package -n kitchensync
Summary: KDE KitchenSync
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

Obsoletes: %name-kitchensync < 1:3.93.0-1
Obsoletes: kde4-kitchensync < 2:4.0.68

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

%define knodecommon_major 4
%define libknodecommon %mklibname knodecommon %{knodecommon_major}

%package -n %libknodecommon
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1
Obsoletes: %{_lib}kdepim42-knode < 1:3.93.0-1

%description -n %libknodecommon
KDE 4 library.

%files -n %libknodecommon
%defattr(-,root,root)
%_kde_libdir/libknodecommon.so.%{knodecommon_major}*

#-----------------------------------------------------------------------------

%package -n knode
Summary: A newsreader for the K Desktop Environment
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Requires: kdepimlibs4-core
Obsoletes: %name-knode < 1:3.93.0-1
Obsoletes: kde4-knode < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdepim-knode < 1:3.5.10-2
%endif
Provides:  kde4-knode = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Requires: kio4-nntp

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
%doc %_kde_docdir/HTML/en/knode
%doc %_kde_docdir/HTML/en/kioslave/news

#-----------------------------------------------------------------------------

%package -n kaddressbook
Summary: The KDE addressbook application
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kaddressbook < 1:3.93.0-1
Obsoletes: kde4-kaddressbook < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdepim-kaddressbook < 1:3.5.10-2
Obsoletes: kdeaddons-kaddressbook-plugins < 1:3.5.10-2
Conflicts: kdeaddons-kaddressbook-plugins < 1:3.5.9-2mdv
%endif
Provides: kde4-kaddressbook = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim4-core < 2:4.1.81-1
Requires:  akonadi-common 

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%defattr(-,root,root)
%_kde_bindir/kaddressbook
%_kde_bindir/kabc2mutt                        
%_kde_bindir/kabcclient
%_kde_datadir/applications/kde4/kaddressbook.desktop
%_kde_appsdir/kaddressbook
%_kde_libdir/kde4/kcm_ldap.so
%_kde_libdir/akonadi/contact/editorpageplugins/cryptopageplugin.so
%_kde_libdir/kde4/kaddressbookpart.so
%_kde_libdir/kde4/kontact_kaddressbookplugin.so
%_kde_datadir/kde4/services/kaddressbookpart.desktop
%_kde_datadir/kde4/services/kontact/kaddressbookplugin.desktop
%_kde_datadir/kde4/services/kcmldap.desktop
%_kde_mandir/man1/kabcclient.1.lzma
%doc %_kde_docdir/HTML/en/kabcclient

#-----------------------------------------------------------------------------

%package -n blogilo
Summary: Blogging client for kde
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description -n blogilo
Blogilo is a blogging client for KDE, which supports famous blogging
APIs.

It was known as Bilbo blogger before, But because of a trademark
issue, We (Blogilo developers) decided to choose a new name for it.
More information about the decision can be found at
http://blogilo.gnufolks.org/news/.

Its current features:

* A full featured WYSIWYG editor.
* An HTML editor with syntax highlighting.
* Previewing your post with your blog style! like when you are
visiting it at your blog.
* Support for Blogger1.0, MetaWeblog, MovableType (Wordpress supports
All of these!) and Google GData (used on Blogspot.com blogs) APIs!
* Support for Creating/Modifying/Deleting posts.
* Support for creating drafts and scheduled posts!
* Support for uploading media files to your blog (Just on supported
APIs e.g. MetaWeblog and MovableType)
* Support for uploading to FTP server.
* Support for Fetching your recent blog entries.
* Support for adding Images to post from your system. It will upload
them on Submitting post to blog (Just on supported APIs e.g.
MetaWeblog and MovableType)
* Support for saving local entries before publishing.
* Saving your writing copy to prevent data loss, at configurable
intervals.
* and ...

%files -n blogilo
%defattr(-,root,root)
%{_kde_bindir}/blogilo
%_kde_datadir/applications/kde4/blogilo.desktop
%_kde_datadir/config.kcfg/blogilo.kcfg
%doc %_kde_docdir/HTML/en/blogilo
%_kde_appsdir/blogilo/blogiloui.rc

#-----------------------------------------------------------------------------

%define messagecore_major 4
%define libmessagecore %mklibname messagecore %{messagecore_major}

%package -n %libmessagecore
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmessagecore
KDE 4 library.

%files -n %libmessagecore
%defattr(-,root,root)
%_kde_libdir/libmessagecore.so.%{messagecore_major}*

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
%_kde_libdir/kde4/kalarm_local.so
%_kde_libdir/kde4/kalarm_localdir.so
%_kde_libdir/kde4/kalarm_remote.so
%_kde_datadir/applications/kde4/kalarm.desktop
%_kde_appsdir/kalarm
%_kde_appsdir/kconf_update/kalarm-1.2.1-general.pl
%_kde_appsdir/kconf_update/kalarm-1.9.5-defaults.pl
%_kde_appsdir/kconf_update/kalarm-2.0.2-general.pl
%_kde_appsdir/kconf_update/kalarm-2.1.5-general.pl
%_kde_appsdir/kconf_update/kalarm-version.pl
%_kde_appsdir/kconf_update/kalarm.upd
%_kde_datadir/autostart/kalarm.autostart.desktop
%_kde_datadir/config.kcfg/kalarmconfig.kcfg
%doc %_kde_docdir/HTML/en/kalarm
%_kde_datadir/kde4/services/kresources/alarms/local.desktop
%_kde_datadir/kde4/services/kresources/alarms/localdir.desktop
%_kde_datadir/kde4/services/kresources/alarms/remote.desktop
%_kde_datadir/kde4/services/kresources/kalarm_manager.desktop

#-----------------------------------------------------------------------------

%define kalarm_calendar_major 4 
%define libkalarm_calendar %mklibname kalarm_calendar %{kalarm_calendar_major} 

%package -n %libkalarm_calendar
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkalarm_calendar
KDE 4 library.

%files -n %libkalarm_calendar
%defattr(-,root,root)
%_kde_libdir/libkalarm_calendar.so.%{kalarm_calendar_major}*

#-----------------------------------------------------------------------------

%define kalarm_resources_major 4
%define libkalarm_resources %mklibname kalarm_resources %{kalarm_resources_major}

%package -n %libkalarm_resources
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkalarm_resources
KDE 4 library.

%files -n %libkalarm_resources
%defattr(-,root,root)
%_kde_libdir/libkalarm_resources.so.%{kalarm_resources_major}*

#-----------------------------------------------------------------------------

%package -n ktimetracker
Summary: Tracks time spent on various tasks
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-ktimetracker < 1:3.93.0-1
Obsoletes: kde4-ktimetracker < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdepim-karm < 1:3.5.10-2
%endif
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
%_kde_datadir/kde4/services/kontact/ktimetracker_plugin.desktop
%_kde_libdir/kde4/ktimetrackerpart.so
%_kde_libdir/kde4/kcm_planner.so
%_kde_libdir/kde4/kcm_ktimetracker.so
%_kde_libdir/kde4/kontact_plannerplugin.so
%_kde_libdir/kde4/kontact_ktimetrackerplugin.so
%_kde_docdir/HTML/en/ktimetracker

#-----------------------------------------------------------------------------

%define kmailnepomukprivate_major 4
%define libkmailnepomukprivate %mklibname kmailnepomukprivate %{kmailnepomukprivate_major}

%package -n %libkmailnepomukprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkmailnepomukprivate
KDE 4 library.

%files -n %libkmailnepomukprivate
%defattr(-,root,root)
%_kde_libdir/libkmailnepomukprivate.so.%{kmailnepomukprivate_major}*

#-----------------------------------------------------------------------------

%package -n kmail
Summary: KDE Email Client
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Requires: kdepimlibs4-core
Requires: sasl-plug-plain
Requires: sasl-plug-ntlm
Requires: sasl-plug-login
Requires: sasl-plug-digestmd5
Requires: kio4-pop3
Requires: kio4-smtp
Requires: kio4-mbox
Requires: kio4-imap
Requires: kio4-sieve
Suggests: kmailcvt
Suggests: pinentry-qt4
Suggests: openssh-askpass-qt4
Obsoletes: kde4-kmail < 2:4.0.68
Obsoletes: kdepim4-plugins <= 2:4.0.83
Obsoletes: %name-kmail < 1:3.93.0-1
%if %mdkversion >= 200910
Obsoletes: kdepim-kmail < 1:3.5.10-2
%endif
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
Requires: kio4-nntp
Obsoletes: kde4-knotes < 2:4.0.68
Obsoletes: %name-knotes < 1:3.93.0-1
%if %mdkversion >= 200910
Obsoletes: kdepim-knotes < 1:3.5.10-2
%endif
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
%_kde_libdir/kde4/kcm_knote.so
%_kde_docdir/HTML/en/knotes
%_kde_libdir/kde4/kontact_knotesplugin.so

#-----------------------------------------------------------------------------

%package -n kontact
Summary: Kontact Container
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kontact < 1:3.93.0-1
Obsoletes: kde4-kontact < 2:4.0.68
Requires: kio4-ldap
%if %mdkversion >= 200910
Obsoletes: kdepim-kontact  kdepim-kpilot < 1:3.5.10-2
%endif
Provides: kde4-kontact = %epoch:%version
Suggests: akregator
Suggests: kmail
Suggests: knotes
Suggests: ktimetracker
Suggests: knode
Suggests: kalarm
Suggests: kaddressbook
Suggests: korganizer

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
%_kde_libdir/kde4/kcm_apptsummary.so
%_kde_libdir/kde4/kcm_kontact.so
%_kde_libdir/kde4/kcm_kontactsummary.so
%_kde_libdir/kde4/kontact_journalplugin.so
%_kde_libdir/kde4/kcm_sdsummary.so
%_kde_libdir/kde4/kontact_specialdatesplugin.so
%_kde_libdir/kde4/kontact_summaryplugin.so
%_kde_datadir/applications/kde4/Kontact.desktop
%_kde_datadir/applications/kde4/kontact-admin.desktop

%_kde_docdir/HTML/en/kontact
%_kde_docdir/HTML/en/kontact-admin

#-----------------------------------------------------------------------------

%define korg_stdprinting_major 4
%define libkorg_stdprinting %mklibname korg_stdprinting %{korg_stdprinting_major}

%package -n %libkorg_stdprinting
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkorg_stdprinting
KDE 4 library.

%files -n %libkorg_stdprinting
%defattr(-,root,root)
%_kde_libdir/libkorg_stdprinting.so.%{korg_stdprinting_major}*

#-----------------------------------------------------------------------------

%define korganizer_calendar_major 4
%define libkorganizer_calendar %mklibname korganizer_calendar %{korganizer_calendar_major}

%package -n %libkorganizer_calendar
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkorganizer_calendar
KDE 4 library.

%files -n %libkorganizer_calendar
%defattr(-,root,root)
%_kde_libdir/libkorganizer_calendar.so.%{korganizer_calendar_major}*

#-----------------------------------------------------------------------------

%define korganizer_eventviewer_major 4
%define libkorganizer_eventviewer %mklibname korganizer_eventviewer %{korganizer_eventviewer_major}

%package -n %libkorganizer_eventviewer
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkorganizer_eventviewer
KDE 4 library.

%files -n %libkorganizer_eventviewer
%defattr(-,root,root)
%_kde_libdir/libkorganizer_eventviewer.so.%{korganizer_eventviewer_major}*

#-----------------------------------------------------------------------------

%define korganizer_interfaces_major 4
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %libkorganizer_interfaces
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkorganizer_interfaces
KDE 4 library.

%files -n %libkorganizer_interfaces
%defattr(-,root,root)
%_kde_libdir/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#-----------------------------------------------------------------------------

%package -n korganizer
Summary: Calendar and scheduling component
Group: Graphical desktop/KDE
Requires:  %name-core = %epoch:%version
Requires:  %name-kresources
Obsoletes: kde4-korganizer < 2:4.0.68
Obsoletes: %name-korganizer < 1:3.93.0-1
Requires: kio4-ldap
%if %mdkversion >= 200910
Obsoletes: kdepim-korganizer < 1:3.5.10-2
%endif
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
%_kde_appsdir/konsolekalendar
%doc %_kde_docdir/HTML/en/konsolekalendar

#-----------------------------------------------------------------------------

%define korganizerprivate_major 4
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %libkorganizerprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}korganizer4 < 1:3.97.1-0.752060.1
Obsoletes: %{_lib}kdepim42-korganizer < 1:3.93.0-

%description -n %libkorganizerprivate
KDE 4 library.

%files -n %libkorganizerprivate
%defattr(-,root,root)
%_kde_libdir/libkorganizerprivate.so.%{korganizerprivate_major}*

#-----------------------------------------------------------------------------

%define kabc_groupdav_major 4
%define libkabc_groupdav %mklibname kabc_groupdav %{kabc_groupdav_major}

%package -n %libkabc_groupdav
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkabc_groupdav
KDE 4 library.

%files -n %libkabc_groupdav
%defattr(-,root,root)
%_kde_libdir/libkabc_groupdav.so.%{kabc_groupdav_major}*

#-----------------------------------------------------------------------------

%define kabc_slox_major 4
%define libkabc_slox %mklibname kabc_slox %{kabc_slox_major}

%package -n %libkabc_slox
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkabc_slox
KDE 4 library.

%files -n %libkabc_slox
%defattr(-,root,root)
%_kde_libdir/libkabc_slox.so.%{kabc_slox_major}*

#-----------------------------------------------------------------------------

%define messagelist_major 4
%define libmessagelist %mklibname messagelist %{messagelist_major}

%package -n %libmessagelist
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmessagelist
KDE 4 library.

%files -n %libmessagelist
%defattr(-,root,root)
%_kde_libdir/libmessagelist.so.%{messagelist_major}*

#-----------------------------------------------------------------------------

%define kabckolab_major 4
%define libkabckolab %mklibname kabckolab %{kabckolab_major}

%package -n %libkabckolab
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkabckolab
KDE 4 library.

%files -n %libkabckolab
%defattr(-,root,root)
%_kde_libdir/libkabckolab.so.%{kabckolab_major}*

#-----------------------------------------------------------------------------

%define kcal_groupdav_major 4
%define libkcal_groupdav %mklibname kcal_groupdav %{kcal_groupdav_major}

%package -n %libkcal_groupdav
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkcal_groupdav
KDE 4 library.

%files -n %libkcal_groupdav
%defattr(-,root,root)
%_kde_libdir/libkcal_groupdav.so.%{kcal_groupdav_major}*

#-----------------------------------------------------------------------------

%define kcal_resourceblog 4
%define libkcal_resourceblog %mklibname kcal_resourceblog %{kcal_resourceblog}

%package -n %libkcal_resourceblog
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkcal_resourceblog
KDE 4 library.

%files -n %libkcal_resourceblog
%defattr(-,root,root)
%_kde_libdir/libkcal_resourceblog.so.%{kcal_resourceblog}*

#-----------------------------------------------------------------------------

%define kcal_resourceremote_major 4
%define libkcal_resourceremote %mklibname kcal_resourceremote %{kcal_resourceremote_major}

%package -n %libkcal_resourceremote
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkcal_resourceremote
KDE 4 library.

%files -n %libkcal_resourceremote
%defattr(-,root,root)
%_kde_libdir/libkcal_resourceremote.so.%{kcal_resourceremote_major}*

#-----------------------------------------------------------------------------

%define kcal_slox_major 4
%define libkcal_slox %mklibname kcal_slox %{kcal_slox_major}

%package -n %libkcal_slox
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkcal_slox
KDE 4 library.

%files -n %libkcal_slox
%defattr(-,root,root)
%_kde_libdir/libkcal_slox.so.%{kcal_slox_major}*

#-----------------------------------------------------------------------------

%define kcalkolab_major 4
%define libkcalkolab %mklibname kcalkolab %{kcalkolab_major}

%package -n %libkcalkolab
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkcalkolab
KDE 4 library.

%files -n %libkcalkolab
%defattr(-,root,root)
%_kde_libdir/libkcalkolab.so.%{kcalkolab_major}*

#-----------------------------------------------------------------------------

%define kgroupwarebase_major 4
%define libkgroupwarebase %mklibname kgroupwarebase %{kgroupwarebase_major}

%package -n %libkgroupwarebase
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkgroupwarebase
KDE 4 library.

%files -n %libkgroupwarebase
%defattr(-,root,root)
%_kde_libdir/libkgroupwarebase.so.%{kgroupwarebase_major}*

#-----------------------------------------------------------------------------

%define kgroupwaredav_major 4
%define libkgroupwaredav %mklibname kgroupwaredav %{kgroupwaredav_major}

%package -n %libkgroupwaredav
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkgroupwaredav
KDE 4 library.

%files -n %libkgroupwaredav
%defattr(-,root,root)
%_kde_libdir/libkgroupwaredav.so.%{kgroupwaredav_major}*

#-----------------------------------------------------------------------------

%define knoteskolab_major 4
%define libknoteskolab %mklibname knoteskolab %{knoteskolab_major}

%package -n %libknoteskolab
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libknoteskolab
KDE 4 library.

%files -n %libknoteskolab
%defattr(-,root,root)
%_kde_libdir/libknoteskolab.so.%{knoteskolab_major}*
#-----------------------------------------------------------------------------

%define kslox_major 4
%define libkslox %mklibname kslox %{kslox_major}

%package -n %libkslox
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkslox
KDE 4 library.

%files -n %libkslox
%defattr(-,root,root)
%_kde_libdir/libkslox.so.%{kslox_major}*

#-----------------------------------------------------------------------------

%define kleo_major 4
%define libkleo %mklibname kleo %{kleo_major}

%package -n %libkleo
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkleo
KDE 4 library.

%files -n %libkleo
%defattr(-,root,root)
%_kde_libdir/libkleo.so.%{kleo_major}*

#-----------------------------------------------------------------------------

%package kresources
Summary: KDE pim resource plugins
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kresources < 1:3.93.0-1
Conflicts: %{_lib}kcal_resourcefeatureplan4 < 3.93.0-0.726734.2
Conflicts: kdepim4-akonadi < 2:4.3.0

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
%_kde_datadir/kde4/services/kresources/kabc/kolab.desktop
%_kde_datadir/kde4/services/kresources/kcal/kabc.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_groupdav.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_opengroupware.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_ox.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_slox.desktop
%_kde_datadir/kde4/services/kresources/kcal/kolab.desktop
%_kde_datadir/kde4/services/kresources/kcal/remote.desktop
%_kde_datadir/kde4/services/kresources/kcal/blog.desktop
%_kde_datadir/kde4/services/kresources/knotes/kolabresource.desktop
%_kde_appsdir/kconf_update/kolab-resource.upd
%_kde_appsdir/kconf_update/upgrade-resourcetype.pl
%_kde_libdir/kde4/kabc_groupdav.so
%_kde_libdir/kde4/kabc_kolab.so
%_kde_libdir/kde4/kabc_slox.so
%_kde_libdir/kde4/kcal_*
%_kde_libdir/kde4/knotes_kolab.so

#-----------------------------------------------------------------------------

%package wizards
Summary: KDE Groupware Wizard
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-wizards < 1:3.93.0-1
%if %mdkversion >= 200910
Obsoletes: kdepim-wizards < 1:3.5.10-2
%endif

%description wizards
KDE Groupware Wizard

%files wizards
%defattr(-,root,root)
%_kde_bindir/groupwarewizard
%_kde_bindir/kolabwizard
%_kde_bindir/sloxwizard
%_kde_bindir/groupwisewizard
%_kde_libdir/kde4/kio_groupwise.so
%_kde_libdir/kde4/kabc_groupwise.so
%_kde_datadir/applications/kde4/groupwarewizard.desktop
%_kde_datadir/config.kcfg/groupwise.kcfg
%_kde_datadir/config.kcfg/kolab.kcfg
%_kde_datadir/config.kcfg/slox.kcfg
%_kde_datadir/kde4/services/groupwise.protocol
%_kde_datadir/kde4/services/groupwises.protocol
%_kde_datadir/kde4/services/kresources/kabc/kabc_groupwise.desktop
%_kde_datadir/kde4/services/kresources/kcal/kcal_groupwise.desktop

#-----------------------------------------------------------------------------

%define kabc_groupwise_major 4
%define libkabcgroupwise %mklibname kabc_groupwise %{kabc_groupwise_major}

%package -n %libkabcgroupwise
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkabcgroupwise
KDE 4 library.

%files -n %libkabcgroupwise
%defattr(-,root,root)
%_kde_libdir/libkabcgroupwise.so.%{kabc_groupwise_major}*

#-----------------------------------------------------------------------------

%define kcal_groupwise_major 4
%define libkcalgroupwise %mklibname kcal_groupwise %{kcal_groupwise_major}

%package -n %libkcalgroupwise
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcalgroupwise
KDE 4 library.

%files -n %libkcalgroupwise
%defattr(-,root,root)
%_kde_libdir/libkcalgroupwise.so.%{kcal_groupwise_major}*

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
%if 0 
%package -n nepomuk-email-feeder
Summary: %{name} nepomuk-email-feeder
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Conflicts: kontact < 2:4.0.83-2

%description -n nepomuk-email-feeder
%{name} nepomuk-email-feeder.
 
%files -n nepomuk-email-feeder 
%defattr(-,root,root)
%_kde_bindir/akonadi_nepomuk_email_feeder
%_kde_datadir/akonadi/agents/nepomukemailfeeder.desktop
%endif
#-----------------------------------------------------------------------------

%define messageviewer_major 0
%define libmessageviewer %mklibname messageviewer %{messageviewer_major}

%package -n %libmessageviewer
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmessageviewer
KDE 4 library.

%files -n %libmessageviewer
%defattr(-,root,root)
%_kde_libdir/libmessageviewer.so.%{messageviewer_major}*

#-----------------------------------------------------------------------------

%define akonadi_next_major 4
%define libakonadi_next %mklibname akonadi-next %{akonadi_next_major}

%package -n %libakonadi_next
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname akonadi_next 4}

%description -n %libakonadi_next
KDE 4 library.

%files -n %libakonadi_next
%defattr(-,root,root)
%_kde_libdir/libakonadi_next.so.%{akonadi_next_major}*

#-----------------------------------------------------------------------------

%define akonadi_kcal_next_major 4
%define libakonadi_kcal_next %mklibname akonadi-kcal_next %{akonadi_kcal_next_major}

%package -n %libakonadi_kcal_next
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_kcal_next
KDE 4 library.

%files -n %libakonadi_kcal_next
%defattr(-,root,root)
%_kde_libdir/libakonadi-kcal_next.so.%{akonadi_kcal_next_major}*

#-----------------------------------------------------------------------------


%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel >= 2:4.2.98
Requires: kdelibs4-experimental-devel >= 4.2.98
Requires: kdepimlibs4-devel >= 2:4.2.98
Requires: kdepim4-runtime-devel >= 4.2.98
Requires: %libkdepim = %epoch:%version
Requires: %libkpgp = %epoch:%version
Requires: %libksieve = %epoch:%version
Requires: %libmimelib = %epoch:%version
Requires: %libakregatorinterfaces = %epoch:%version
Requires: %libakregatorprivate = %epoch:%version
%if %{with_kitchensync}
Requires: %libkitchensyncprivate = %epoch:%version
Requires: %libqopensync = %epoch:%version
%endif
Requires: %libknodecommon = %epoch:%version
Requires: %libkmailnepomukprivate = %epoch:%version
Requires: %libkorg_stdprinting = %epoch:%version
Requires: %libkorganizerprivate = %epoch:%version
Requires: %libkorganizer_calendar = %epoch:%version
Requires: %libkorganizer_eventviewer = %epoch:%version
Requires: %libkorganizer_interfaces = %epoch:%version
Requires: %libkabc_groupdav = %epoch:%version
Requires: %libkabc_slox = %epoch:%version
Requires: %libkabckolab = %epoch:%version
Requires: %libkcal_groupdav = %epoch:%version
Requires: %libkcal_resourceremote = %epoch:%version
Requires: %libkcal_slox = %epoch:%version
Requires: %libkcalkolab = %epoch:%version
Requires: %libkgroupwarebase = %epoch:%version
Requires: %libkgroupwaredav = %epoch:%version
Requires: %libknoteskolab = %epoch:%version
Requires: %libkslox = %epoch:%version
Requires: %libkleo = %epoch:%version
Requires: %libgwsoap = %epoch:%version
Requires: %libkabcgroupwise = %epoch:%version
Requires: %libkcalgroupwise = %epoch:%version
Requires: %libmessagelist = %epoch:%version
Requires: %libmessagecore = %epoch:%version
Requires: %libmessageviewer = %epoch:%version
Requires: %libkalarm_calendar = %epoch:%version
Requires: %libkalarm_resources = %epoch:%version
Requires: %libakonadi_next = %epoch:%version
Requires: %libakonadi_kcal_next = %epoch:%version
%if %mdkversion >= 200910
Obsoletes: kdepim-devel < 1:3.5.10-2
Obsoletes: kdepim-devel-doc < 1:3.5.10-2
%endif

%description  devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_datadir/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep

%if %branch
%setup -q -n kdepim-%version%kde_snapshot
%else
%setup -q -n kdepim-%version
%endif

#%patch0 -p0
%patch1 -p0
%patch200 -p1
%patch201 -p1
%patch202 -p0
%patch300 -p0

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

