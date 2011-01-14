%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdepim4
Summary: An application suite to manage personal information
Version: 4.5.94.1
%if %branch
Release: %mkrel -c %kde_snapshot 1
%else
Release: %mkrel 1
%endif
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://community.kde.org/KDE_PIM
%if %branch
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdepim-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/unstable/kdepim/%version/src/kdepim-%version.tar.bz2
%endif
Patch0: kdepim-4.5.94-disable-doc-install.patch
Patch301: kdepim-4.5.94-git3e8673b7.patch
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.5.61
BuildRequires: kdepimlibs4-devel >= 2:4.5.74
BuildRequires: kdepim4-runtime-devel >= 4.5.74
BuildRequires: akonadi-devel >= 1:1.4.95
BuildRequires: libx11-devel
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: strigi-devel
BuildRequires: gpgme-devel
BuildRequires: grantlee-devel
BuildRequires: xsltproc
BuildRequires: libassuan-devel
BuildRequires: libxscrnsaver-devel
Suggests: akonadi-common
Suggests: kleopatra
Suggests: akregator
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
Suggests: nepomuk-email-feeder
Obsoletes: kpilot < %epoch:%version
Obsoletes: korn <= 2:4.1.0
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

%files

#----------------------------------------------------------------------

%package core
Summary: Core files for kdepim
Group: Graphical desktop/KDE	
Requires: kdelibs4-core
Requires: kdebase4-runtime
Requires: akonadi-kde >= 2:%{version}
Obsoletes: libkdepim42-common < 1:3.93.0-1
Obsoletes: kdepim4-common < 1:3.93.0-1
Obsoletes: kdepim4-plasma-applets < 1:4.1 
Obsoletes: %{mklibname akonadisearchprovider 4} < 2:3.94.1-0.729215.1
Obsoletes: kode < 2:4.3
Conflicts: akonadi-kde < 2:4.3.85
Conflicts: kde-l10n-af < 4.5.90
Conflicts: kde-l10n-ar < 4.5.90
Conflicts: kde-l10n-ast < 4.5.90
Conflicts: kde-l10n-be < 4.5.90
Conflicts: kde-l10n-bg < 4.5.90
Conflicts: kde-l10n-bn < 4.5.90
Conflicts: kde-l10n-br < 4.5.90
Conflicts: kde-l10n-ca < 4.5.90
Conflicts: kde-l10n-cs < 4.5.90
Conflicts: kde-l10n-cy < 4.5.90
Conflicts: kde-l10n-da < 4.5.90
Conflicts: kde-l10n-de < 4.5.90
Conflicts: kde-l10n-el < 4.5.90
Conflicts: kde-l10n-en_GB < 4.5.90
Conflicts: kde-l10n-eo < 4.5.90
Conflicts: kde-l10n-es < 4.5.90
Conflicts: kde-l10n-et < 4.5.90
Conflicts: kde-l10n-eu < 4.5.90
Conflicts: kde-l10n-fa < 4.5.90
Conflicts: kde-l10n-fi < 4.5.90
Conflicts: kde-l10n-fr < 4.5.90
Conflicts: kde-l10n-fy < 4.5.90
Conflicts: kde-l10n-ga < 4.5.90
Conflicts: kde-l10n-gl < 4.5.90
Conflicts: kde-l10n-he < 4.5.90
Conflicts: kde-l10n-hi < 4.5.90
Conflicts: kde-l10n-hne < 4.5.90
Conflicts: kde-l10n-hr < 4.5.90
Conflicts: kde-l10n-hsb < 4.5.90
Conflicts: kde-l10n-hu < 4.5.90
Conflicts: kde-l10n-ia < 4.5.90
Conflicts: kde-l10n-is < 4.5.90
Conflicts: kde-l10n-it < 4.5.90
Conflicts: kde-l10n-ja < 4.5.90
Conflicts: kde-l10n-ka < 4.5.90
Conflicts: kde-l10n-kk < 4.5.90
Conflicts: kde-l10n-km < 4.5.90
Conflicts: kde-l10n-ko < 4.5.90
Conflicts: kde-l10n-ku < 4.5.90
Conflicts: kde-l10n-lt < 4.5.90
Conflicts: kde-l10n-lv < 4.5.90
Conflicts: kde-l10n-mai < 4.5.90
Conflicts: kde-l10n-mk < 4.5.90
Conflicts: kde-l10n-ms < 4.5.90
Conflicts: kde-l10n-nb < 4.5.90
Conflicts: kde-l10n-nds < 4.5.90
Conflicts: kde-l10n-ne < 4.5.90
Conflicts: kde-l10n-nl < 4.5.90
Conflicts: kde-l10n-nn < 4.5.90
Conflicts: kde-l10n-oc < 4.5.90
Conflicts: kde-l10n-pa < 4.5.90
Conflicts: kde-l10n-pl < 4.5.90
Conflicts: kde-l10n-pt < 4.5.90
Conflicts: kde-l10n-pt_BR < 4.5.90
Conflicts: kde-l10n-ro < 4.5.90
Conflicts: kde-l10n-ru < 4.5.90
Conflicts: kde-l10n-se < 4.5.90
Conflicts: kde-l10n-si < 4.5.90
Conflicts: kde-l10n-sk < 4.5.90
Conflicts: kde-l10n-sl < 4.5.90
Conflicts: kde-l10n-sr < 4.5.90
Conflicts: kde-l10n-sv < 4.5.90
Conflicts: kde-l10n-ta < 4.5.90
Conflicts: kde-l10n-tg < 4.5.90
Conflicts: kde-l10n-th < 4.5.90
Conflicts: kde-l10n-tr < 4.5.90
Conflicts: kde-l10n-uk < 4.5.90
Conflicts: kde-l10n-uz < 4.5.90
Conflicts: kde-l10n-vi < 4.5.90
Conflicts: kde-l10n-wa < 4.5.90
Conflicts: kde-l10n-xh < 4.5.90
Conflicts: kde-l10n-zh_CN < 4.5.90
Conflicts: kde-l10n-zh_TW < 4.5.90

%description core
Core files from kdepim.

%files core -f %name.lang
%defattr(-,root,root,-)
%exclude %_kde_docdir/HTML/en/*
%_kde_libdir/strigi/*
%dir %_kde_services/kontact
%_kde_iconsdir/oxygen/*/mimetypes/x-mail-distribution-list.*

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

%description -n %libkdepim
KDE 4 library.

%files -n %libkdepim
%defattr(-,root,root)
%_kde_libdir/libkdepim.so.*
%_kde_appsdir/kdepimwidgets
%_kde_libdir/kde4/plugins/designer/kdepimwidgets.so

#---------------------------------------------------------------------------

%package -n kincidenceeditor
Summary: kincidenceeditor
Group: Graphical desktop/KDE
Obsoletes: keventeditor < 2:4.5.68

%description -n kincidenceeditor
New incidince editors 

%files -n kincidenceeditor
%defattr(-,root,root)
%_kde_bindir/kincidenceeditor

#----------------------------------------------------------------------------

%define libincidenceeditorsngmobile_major 4
%define libincidenceeditorsngmobile %mklibname incidenceeditorssngmobile %{libincidenceeditorsngmobile_major}

%package -n %libincidenceeditorsngmobile
Summary: KDEPIM Mobile Library
Group:	System/Libraries

%description -n %libincidenceeditorsngmobile
KDE PIM Mobile library.

%files -n %libincidenceeditorsngmobile

%defattr(-,root,root)
%_kde_libdir/libincidenceeditorsngmobile.so.%{libincidenceeditorsngmobile_major}*


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

%define kmanagesieve_major 4
%define libkmanagesieve %mklibname kmanagesieve %{kmanagesieve_major}

%package -n %libkmanagesieve
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmanagesieve
KDE 4 library.

%files -n %libkmanagesieve
%defattr(-,root,root)
%_kde_libdir/libkmanagesieve.so.%{kmanagesieve_major}*

#-----------------------------------------------------------------------------

%define ksieveui_major 4
%define libksieveui %mklibname ksieveui %{ksieveui_major}

%package -n %libksieveui
Summary: KDE 4 library
Group: System/Libraries

%description -n %libksieveui
KDE 4 library.

%files -n %libksieveui
%defattr(-,root,root)
%_kde_libdir/libksieveui.so.%{ksieveui_major}*

#-----------------------------------------------------------------------------

%package -n kleopatra
Summary: KDE Certificate Manager
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kleopatra < 1:3.93.0-1
Obsoletes: kde4-kleopatra < 2:4.0.68
Provides: kde4-kleopatra = %epoch:%version
Conflicts: %{_lib}kleo4 < 4.0.80-3
Conflicts: %name-core < 2:4.5.77

%description -n kleopatra
KDE Certificate Manager

%files -n kleopatra
%defattr(-,root,root)
%_kde_bindir/kleopatra
%_kde_bindir/kgpgconf
%_kde_bindir/kwatchgnupg
%_kde_applicationsdir/kleopatra.desktop
%_kde_configdir/libkleopatrarc
%_kde_applicationsdir/kleopatra_import.desktop
%_kde_appsdir/kleopatra
%_kde_appsdir/libkleopatra
%_kde_iconsdir/*/*/apps/kleopatra.*
%_kde_appsdir/kwatchgnupg
%_kde_services/kleopatra_*
%_kde_libdir/kde4/kcm_kleopatra.so
%doc %_kde_docdir/HTML/en/kleopatra
%doc %_kde_docdir/HTML/en/kwatchgnupg

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
URL: http://userbase.kde.org/Akregator
Requires: %name-core = %epoch:%version
Obsoletes: %name-akregator < 1:3.93.0-1
Obsoletes: kde4-akregator < 2:4.0.68
Provides: kde4-akregator = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: %name-core < 2:4.5.77

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
%_kde_applicationsdir/akregator.desktop
%_kde_appsdir/akregator
%_kde_appsdir/akregator_sharemicroblog_plugin
%_kde_datadir/config.kcfg/akregator.kcfg
%_kde_iconsdir/*/*/apps/akregator.*
%_kde_iconsdir/*/*/apps/akregator_empty.*
%_kde_services/kontact/akregatorplugin.desktop
%_kde_services/akregator_*
%_kde_services/feed.protocol
%_kde_servicetypes/akregator_plugin.desktop
%_kde_libdir/kde4/akregator*
%_kde_libdir/kde4/kontact_akregatorplugin.so
%doc %_kde_docdir/HTML/en/akregator

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
URL: http://userbase.kde.org/KNode
Requires: %name-core = %epoch:%version
Requires: kdepimlibs4-core
Obsoletes: %name-knode < 1:3.93.0-1
Obsoletes: kde4-knode < 2:4.0.68
Provides: kde4-knode = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: %name-core < 2:4.5.77
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
%_kde_applicationsdir/KNode.desktop
%_kde_appsdir/knode
%_kde_appsdir/kconf_update/knode.upd
%_kde_iconsdir/*/*/apps/knode.*
%_kde_iconsdir/*/*/apps/knode2.*
%_kde_services/kontact/knodeplugin.desktop
%_kde_services/knewsservice.protocol
%_kde_services/knode_config_accounts.desktop
%_kde_services/knode_config_appearance.desktop
%_kde_services/knode_config_cleanup.desktop
%_kde_services/knode_config_identity.desktop
%_kde_services/knode_config_post_news.desktop
%_kde_services/knode_config_privacy.desktop
%_kde_services/knode_config_read_news.desktop
%_kde_libdir/kde4/kcm_knode.so
%_kde_libdir/kde4/knodepart.so
%_kde_libdir/kde4/kontact_knodeplugin.so
%doc %_kde_docdir/HTML/en/knode
%doc %_kde_docdir/HTML/en/kioslave/news

#-----------------------------------------------------------------------------

%package -n kaddressbook
Summary: The KDE addressbook application
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KAddressBook
Requires: %name-core = %epoch:%version
# Grantlee is needed for the simple view in kaddressbook
Requires: grantlee

Obsoletes: %name-kaddressbook < 1:3.93.0-1
Obsoletes: kde4-kaddressbook < 2:4.0.68
Provides: kde4-kaddressbook = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim4-core < 2:4.5.77
Requires: akonadi-common 

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%defattr(-,root,root)
%_kde_bindir/kaddressbook
%_kde_bindir/kabc2mutt        
%_kde_bindir/kabcclient
%_kde_applicationsdir/kaddressbook.desktop
%_kde_appsdir/kaddressbook
%_kde_libdir/kde4/kcm_ldap.so
%_kde_libdir/akonadi/contact/editorpageplugins/cryptopageplugin.so
%_kde_libdir/kde4/kaddressbookpart.so
%_kde_libdir/kde4/kontact_kaddressbookplugin.so
%_kde_iconsdir/*/*/apps/kaddressbook.*
%_kde_datadir/kde4/services/kaddressbookpart.desktop
%_kde_datadir/kde4/services/kontact/kaddressbookplugin.desktop
%_kde_datadir/kde4/services/kcmldap.desktop
%_kde_mandir/man1/kabcclient.1.*
%doc %_kde_docdir/HTML/en/kabcclient

#-----------------------------------------------------------------------------

%package -n blogilo
Summary: Blogging client for kde
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Conflicts: %name-core < 2:4.5.77

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
%_kde_applicationsdir/blogilo.desktop
%_kde_datadir/config.kcfg/blogilo.kcfg
%_kde_iconsdir/*/*/apps/blogilo.*
%_kde_iconsdir/*/*/actions/format-text-blockquote.*
%_kde_iconsdir/*/*/actions/format-text-code.*
%_kde_iconsdir/*/*/actions/insert-more-mark.*
%_kde_iconsdir/*/*/actions/remove-link.*
%_kde_iconsdir/*/*/actions/upload-media.*
%doc %_kde_docdir/HTML/en/blogilo
%_kde_appsdir/blogilo

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
URL: http://userbase.kde.org/KAlarm
Requires: %name-core = %epoch:%version
Obsoletes: %name-kalarm < 1:3.93.0-1
Obsoletes: kde4-kalarm < 2:4.0.68
Provides: kde4-kalarm = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: %name-core < 2:4.5.77

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
%_kde_applicationsdir/kalarm.desktop
%_kde_appsdir/kalarm
%_kde_appsdir/kconf_update/kalarm-1.2.1-general.pl
%_kde_appsdir/kconf_update/kalarm-1.9.5-defaults.pl
%_kde_appsdir/kconf_update/kalarm-2.0.2-general.pl
%_kde_appsdir/kconf_update/kalarm-2.1.5-general.pl
%_kde_appsdir/kconf_update/kalarm-version.pl
%_kde_appsdir/kconf_update/kalarm.upd
%_kde_datadir/autostart/kalarm.autostart.desktop
%_kde_datadir/config.kcfg/kalarmconfig.kcfg
%_kde_iconsdir/*/*/apps/kalarm.*
%doc %_kde_docdir/HTML/en/kalarm
%_kde_services/kresources/alarms/local.desktop
%_kde_services/kresources/alarms/localdir.desktop
%_kde_services/kresources/alarms/remote.desktop
%_kde_services/kresources/kalarm_manager.desktop

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
URL: http://community.kde.org/Ktimetracker
Requires: %name-core = %epoch:%version
Obsoletes: %name-ktimetracker < 1:3.93.0-1
Obsoletes: kde4-ktimetracker < 2:4.0.68
Provides: kde4-ktimetracker = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: %name-core < 2:4.5.77

%description -n ktimetracker
KTimeTracker tracks time spent on various tasks. It is useful for tracking
hours to be billed to different clients or just to find out what percentage
of your day is spent playing Doom or reading Slashdot.

%files -n ktimetracker
%defattr(-,root,root)
%_kde_bindir/karm
%_kde_bindir/ktimetracker
%_kde_appsdir/ktimetracker
%_kde_applicationsdir/ktimetracker.desktop
%_kde_iconsdir/*/*/apps/ktimetracker.*
%_kde_services/ktimetrackerpart.desktop
%_kde_services/ktimetracker_config_behavior.desktop
%_kde_services/ktimetracker_config_display.desktop
%_kde_services/ktimetracker_config_storage.desktop
%_kde_services/kontact/ktimetracker_plugin.desktop
%_kde_libdir/kde4/ktimetrackerpart.so
%_kde_libdir/kde4/kcm_ktimetracker.so
%_kde_libdir/kde4/kontact_ktimetrackerplugin.so
%_kde_docdir/HTML/en/ktimetracker

#-----------------------------------------------------------------------------

%define kmailprivate_major 4
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %libkmailprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkmailprivate
KDE 4 library.

%files -n %libkmailprivate
%defattr(-,root,root)
%_kde_libdir/libkmailprivate.so.%{kmailprivate_major}*

#-----------------------------------------------------------------------------

%define mailcommon_major 4
%define libmailcommon %mklibname mailcommon %{mailcommon_major}

%package -n %libmailcommon
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmailcommon
KDE 4 library.

%files -n %libmailcommon
%defattr(-,root,root)
%_kde_libdir/libmailcommon.so.%{mailcommon_major}*

#-----------------------------------------------------------------------------

%package -n kmail
Summary: KDE Email Client
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KMail
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
Requires: kmail-common
Suggests: kmailcvt
Suggests: pinentry-qt4
Suggests: openssh-askpass-qt4
Obsoletes: kde4-kmail < 2:4.0.68
Obsoletes: kdepim4-plugins <= 2:4.0.83
Obsoletes: %name-kmail < 1:3.93.0-1
Conflicts: kontact < 2:4.0.83-2
Provides: kde4-kmail = %epoch:%version
Provides: kmail2 = %epoch:%version
Conflicts: %name-core < 2:4.5.77

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
%_kde_appsdir/kmail2
%_kde_datadir/kde4/services/kontact/kmailplugin.desktop
%_kde_applicationsdir/KMail2.desktop
%_kde_applicationsdir/kmail_view.desktop
%_kde_appsdir/kconf_update/kmail*
%_kde_appsdir/kconf_update/upgrade-signature.pl
%_kde_appsdir/kconf_update/upgrade-transport.pl
%_kde_datadir/config.kcfg/custommimeheader.kcfg
%_kde_datadir/config.kcfg/customtemplates_kfg.kcfg
%_kde_datadir/config.kcfg/kmail.kcfg
%_kde_datadir/config.kcfg/templatesconfiguration_kfg.kcfg
%_kde_datadir/config/kmail.antispamrc
%_kde_datadir/config/kmail.antivirusrc
%_kde_iconsdir/*/*/apps/kmail.*
%_kde_services/kmail_config_accounts.desktop
%_kde_services/kmail_config_appearance.desktop
%_kde_services/kmail_config_composer.desktop
%_kde_services/kmail_config_identity.desktop
%_kde_services/kmail_config_misc.desktop
%_kde_services/kmail_config_security.desktop
%_kde_servicetypes/dbusmail.desktop
%_kde_libdir/kde4/kcm_kmail.so
%_kde_libdir/kde4/kmailpart.so
%_kde_libdir/kde4/kcm_kmailsummary.so
%_kde_libdir/kde4/kontact_kmailplugin.so
%_kde_libdir/kde4/ktexteditorkabcbridge.so
%_kde_services/kcmkmailsummary.desktop
%_kde_services/ServiceMenus/kmail_addattachmentservicemenu.desktop
%_kde_docdir/HTML/en/kmail

#-----------------------------------------------------------------------------

%package -n kmail-common
Summary: KDE Email Client
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KMail
Provides: kmail2-common = %epoch:%version-%release

%description -n kmail-common
Common files needed by kmail and kmail-mobile used to view messages.

%files -n kmail-common
%defattr(-,root,root)
%_kde_libdir/kde4/messageviewer_bodypartformatter_application_mstnef.so
%_kde_libdir/kde4/messageviewer_bodypartformatter_text_calendar.so
%_kde_libdir/kde4/messageviewer_bodypartformatter_text_vcard.so
%_kde_libdir/kde4/messageviewer_bodypartformatter_text_xdiff.so
%_kde_services/kcm_kpimidentities.desktop
%_kde_libdir/kde4/kcm_kpimidentities.so 
%_kde_appsdir/libmessageviewer
%_kde_appsdir/messageviewer
%_kde_appsdir/messagelist

#-----------------------------------------------------------------------------

%package -n kmailcvt
Summary: KDE Mail Import tool
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KMail
Requires: %name-core = %epoch:%version
Obsoletes: %name-kmailcvt < 1:3.93.0-1
Obsoletes: kde4-kmailcvt < 2:4.0.68
Provides: kde4-kmailcvt = %epoch:%version
Conflicts: %name-core < 2:4.5.77

%description -n kmailcvt
KDE Mail Import tool

%files -n kmailcvt
%defattr(-,root,root)
%_kde_bindir/kmailcvt
%_kde_appsdir/kmailcvt/pics/step1.png
%_kde_iconsdir/*/*/apps/kmailcvt.*

#-----------------------------------------------------------------------------

%package -n knotes
Summary: Notes for the K Desktop Environment
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KNotes
Requires: %name-core = %epoch:%version
Requires: %name-kresources
Requires: kio4-nntp
Obsoletes: kde4-knotes < 2:4.0.68
Obsoletes: %name-knotes < 1:3.93.0-1
Provides: kde4-knotes = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: %name-core < 2:4.5.77

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%defattr(-,root,root)
%_kde_bindir/knotes
%_kde_applicationsdir/knotes.desktop
%_kde_datadir/kde4/services/kontact/knotesplugin.desktop
%_kde_datadir/config.kcfg/knoteconfig.kcfg
%_kde_datadir/config.kcfg/knotesglobalconfig.kcfg
%_kde_appsdir/knotes
%_kde_iconsdir/*/*/apps/knotes.*
%_kde_services/kresources/knotes/local.desktop
%_kde_services/kresources/knotes_manager.desktop
%_kde_services/knote_config_action.desktop
%_kde_services/knote_config_display.desktop
%_kde_services/knote_config_editor.desktop
%_kde_services/knote_config_network.desktop
%_kde_services/knote_config_style.desktop
%_kde_libdir/kde4/knotes_local.so
%_kde_libdir/kde4/kcm_knote.so
%_kde_docdir/HTML/en/knotes
%_kde_libdir/kde4/kontact_knotesplugin.so

#-----------------------------------------------------------------------------

%package -n kontact
Summary: Kontact Container
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/Kontact
Requires: %name-core = %epoch:%version
Obsoletes: %name-kontact < 1:3.93.0-1
Obsoletes: kde4-kontact < 2:4.0.68
Conflicts: %name-core < 2:4.5.77
Requires: kio4-ldap
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
%_kde_iconsdir/*/*/apps/kontact.*
%_kde_services/kontactconfig.desktop
%_kde_services/kcmapptsummary.desktop
%_kde_services/kcmkontactsummary.desktop
%_kde_services/kcmsdsummary.desktop
%_kde_services/kontact/summaryplugin.desktop
%_kde_services/kontact/specialdatesplugin.desktop
%_kde_libdir/kde4/kcm_apptsummary.so
%_kde_libdir/kde4/kcm_kontact.so
%_kde_libdir/kde4/kcm_kontactsummary.so
%_kde_libdir/kde4/kontact_journalplugin.so
%_kde_libdir/kde4/kcm_sdsummary.so
%_kde_libdir/kde4/kontact_specialdatesplugin.so
%_kde_libdir/kde4/kontact_summaryplugin.so
%_kde_applicationsdir/Kontact.desktop
%_kde_applicationsdir/kontact-admin.desktop
%_kde_docdir/HTML/en/kontact
%_kde_docdir/HTML/en/kontact-admin

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
URL: http://userbase.kde.org/KOrganizer
Requires: %name-core = %epoch:%version
Requires: %name-kresources
Obsoletes: kde4-korganizer < 2:4.0.68
Obsoletes: %name-korganizer < 1:3.93.0-1
Requires: kio4-ldap
Suggests: kincidenceeditor
Provides: kde4-korganizer = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim4-core < 2:4.5.77

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
%_kde_services/kontact/korganizerplugin.desktop
%_kde_applicationsdir/korganizer-import.desktop
%_kde_applicationsdir/korganizer.desktop
%_kde_appsdir/kconf_update/korganizer.upd
%_kde_appsdir/korgac
%_kde_appsdir/korganizer
%_kde_iconsdir/*/*/apps/korganizer.*
%_kde_iconsdir/*/*/actions/checkmark.*
%_kde_iconsdir/*/*/actions/smallclock.*
%_kde_iconsdir/*/*/actions/upindicator.*
%_kde_services/kontact/todoplugin.desktop
%_kde_services/kcmtodosummary.desktop
%_kde_services/kontact/journalplugin.desktop
%_kde_libdir/kde4/kcm_todosummary.so
%_kde_libdir/kde4/kontact_todoplugin.so
%_kde_datadir/autostart/korgac.desktop
%_kde_datadir/config.kcfg/korganizer.kcfg
%_kde_datadir/config/korganizer.knsrc
%_kde_services/korganizer*
%_kde_services/webcal.protocol
%_kde_servicetypes/calendardecoration.desktop
%_kde_servicetypes/calendarplugin.desktop
%_kde_servicetypes/dbuscalendar.desktop
%_kde_servicetypes/korganizerpart.desktop
%_kde_servicetypes/korgprintplugin.desktop
%_kde_libdir/kde4/kcm_korganizer.so
%_kde_libdir/kde4/korg_*
%_kde_libdir/kde4/korganizerpart.so
%_kde_libdir/kde4/kontact_korganizerplugin.so
%_kde_bindir/konsolekalendar
%_kde_applicationsdir/konsolekalendar.desktop
%_kde_iconsdir/*/*/apps/konsolekalendar.*
%doc %_kde_docdir/HTML/en/korganizer
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

#------------------------------------------------------------------------------

%define libcalendarsupport_major 4
%define libcalendarsupport %mklibname calendarsupport %{libcalendarsupport_major}

%package -n %libcalendarsupport
Summary: KDE 4 library
Group: System/Libraries

%description -n %libcalendarsupport
KDE 4 library for korganizer-Mobile.

%files -n %libcalendarsupport
%defattr(-,root,root)
%_kde_libdir/libcalendarsupport.so.%{libcalendarsupport_major}*

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

#-----------------------------------------------------------------------


%define libkdgantt2_major 0
%define libkdgantt2 %mklibname kdgantt2 %{libkdgantt2_major}

%package -n %libkdgantt2
Summary: KDE4 library
Group: System/Libraries

%description -n %libkdgantt2
KDE 4 library.

%files -n %libkdgantt2
%defattr(-,root,root)
%_kde_libdir/libkdgantt2.so.%{libkdgantt2_major}*

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
%_kde_libdir/kde4/kcal_blog.so
%_kde_libdir/kde4/kcal_groupwise.so
%_kde_libdir/kde4/kcal_remote.so
%_kde_services/kresources/kcal/blog.desktop
%_kde_services/kresources/kcal/remote.desktop

#-----------------------------------------------------------------------------

%package wizards
Summary: KDE Groupware Wizard
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-wizards < 1:3.93.0-1

%description wizards
KDE Groupware Wizard

%files wizards
%defattr(-,root,root)
%_kde_bindir/groupwarewizard
%_kde_bindir/groupwisewizard
%_kde_libdir/kde4/kio_groupwise.so
%_kde_libdir/kde4/kabc_groupwise.so
%_kde_applicationsdir/groupwarewizard.desktop
%_kde_datadir/config.kcfg/groupwise.kcfg
%_kde_services/groupwise.protocol
%_kde_services/groupwises.protocol
%_kde_services/kresources/kabc/kabc_groupwise.desktop
%_kde_services/kresources/kcal/kcal_groupwise.desktop

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

#-----------------------------------------------------------------------------

%package -n akonadiconsole
Summary:Console that help to debug akonadi
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Conflicts: kontact < 2:4.0.83-2
Conflicts: kdepim4-core < 2:4.4.2-5

%description -n akonadiconsole
Console that help to debug akonadi

%files -n akonadiconsole
%defattr(-,root,root)
%_kde_bindir/akonadiconsole
%_kde_applicationsdir/akonadiconsole.desktop
%_kde_appsdir/akonadiconsole/akonadiconsoleui.rc

#-----------------------------------------------------------------------------

%define messageviewer_major 4
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

%define eventviews_major 4
%define libeventviews %mklibname eventviews %{eventviews_major}

%package -n %libeventviews
Summary: KDE 4 library
Group: System/Libraries

%description -n %libeventviews
KDE 4 library.

%files -n %libeventviews
%defattr(-,root,root)
%_kde_libdir/libeventviews.so.%{eventviews_major}*

#-----------------------------------------------------------------------------

%define libincidenceeditorsng_major 4
%define libincidenceeditorsng %mklibname incidenceeditorsng %{libincidenceeditorsng_major}

%package -n %libincidenceeditorsng
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}incidenceeditors4 < 2:4.5.68

%description -n %libincidenceeditorsng
KDE 4 library.

%files -n %libincidenceeditorsng
%defattr(-,root,root)
%_kde_libdir/libincidenceeditorsng.so.%{libincidenceeditorsng_major}*

#-----------------------------------------------------------------------------

%define kdepimdbusinterfaces_major 4
%define libkdepimdbusinterfaces %mklibname kdepimdbusinterfaces %{kdepimdbusinterfaces_major}

%package -n %libkdepimdbusinterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdepimdbusinterfaces
KDE 4 library.

%files -n %libkdepimdbusinterfaces
%defattr(-,root,root)
%_kde_libdir/libkdepimdbusinterfaces.so.%{kdepimdbusinterfaces_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientcore_major 0
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %libkleopatraclientcore
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kleopatraclientcore4 <= 2:4.5-0.beta1.1

%description -n %libkleopatraclientcore
KDE 4 library.

%files -n %libkleopatraclientcore
%defattr(-,root,root)
%_kde_libdir/libkleopatraclientcore.so.%{kleopatraclientcore_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientgui_major 0
%define libkleopatraclientgui %mklibname kleopatraclientgui %{kleopatraclientgui_major}

%package -n %libkleopatraclientgui
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kleopatraclientgui4 <= 2:4.5-0.beta1.1

%description -n %libkleopatraclientgui
KDE 4 library.

%files -n %libkleopatraclientgui
%defattr(-,root,root)
%_kde_libdir/libkleopatraclientgui.so.%{kleopatraclientgui_major}*

#-----------------------------------------------------------------------------

%define messagecomposer_major 4
%define libmessagecomposer %mklibname messagecomposer %{messagecomposer_major}

%package -n %libmessagecomposer
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmessagecomposer
KDE 4 library.

%files -n %libmessagecomposer
%defattr(-,root,root)
%_kde_libdir/libmessagecomposer.so.%{messagecomposer_major}*

#-----------------------------------------------------------------------------

%define templateparser_major 4
%define libtemplateparser %mklibname templateparser %{templateparser_major}

%package -n %libtemplateparser
Summary: KDE 4 library
Group: System/Libraries

%description -n %libtemplateparser
KDE 4 library.

%files -n %libtemplateparser
%defattr(-,root,root)
%_kde_libdir/libtemplateparser.so.%{templateparser_major}*

#-----------------------------------------------------------------------------

%package -n kjots
Summary: KDE note taking utility
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KJots
Requires: %name-core = %epoch:%version
Obsoletes: %name-kjots < 3.93.0-0.714053.1
Obsoletes: kde4-kjots < 4.0.68
Provides: kde4-kjots = %version
Conflicts: kontact < 2:4.0.83-2
Conflicts: %name-core < 2:4.5.77

%description -n kjots
A small program which is handy for keeping and organizing miscellaneous
notes.

%files -n kjots
%defattr(-,root,root)
%_kde_bindir/kjots
%_kde_libdir/kde4/kcm_kjots.so
%_kde_libdir/kde4/kjotspart.so
%_kde_libdir/kde4/kontact_kjotsplugin.so
%_kde_libdir/kde4/plasma_applet_akonotes_list.so
%_kde_libdir/kde4/plasma_applet_akonotes_note.so
%_kde_applicationsdir/Kjots.desktop
%_kde_appsdir/kjots
%_kde_datadir/config.kcfg/kjots.kcfg
%_kde_iconsdir/*/*/apps/kjots.*
%_kde_iconsdir/*/*/actions/edit-delete-page.*
%doc %_kde_docdir/HTML/en/kjots
%_kde_services/akonotes_list.desktop
%_kde_services/akonotes_note.desktop
%_kde_services/kjots_config_misc.desktop
%_kde_services/kjotspart.desktop
%_kde_services/kontact/kjots_plugin.desktop
%_kde_appsdir/desktoptheme/default/widgets/stickynote.svgz

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:4.5.61
Requires: kdepimlibs4-devel >= 2:4.5.61
Requires: kdepim4-runtime-devel >= 4.5.61
Requires: %libkdepim = %epoch:%version
Requires: %libeventviews = %epoch:%version
Requires: %libkleopatraclientcore = %epoch:%version
Requires: %libincidenceeditorsng = %epoch:%version
Requires: %libtemplateparser = %epoch:%version
Requires: %libmessagecomposer = %epoch:%version
Requires: %libkleopatraclientgui = %epoch:%version
Requires: %libkdepimdbusinterfaces = %epoch:%version
Requires: %libkpgp = %epoch:%version
Requires: %libksieve = %epoch:%version
Requires: %libakregatorinterfaces = %epoch:%version
Requires: %libakregatorprivate = %epoch:%version
Requires: %libknodecommon = %epoch:%version
Requires: %libkmailprivate = %epoch:%version
Requires: %libmailcommon = %epoch:%version
Requires: %libkorganizerprivate = %epoch:%version
Requires: %libkorganizer_interfaces = %epoch:%version
Requires: %libkcal_resourceremote = %epoch:%version
Requires: %libkcal_resourceblog = %epoch:%version
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
Requires: %libkdgantt2 = %epoch:%version
Requires: %libincidenceeditorsngmobile = %epoch:%version
Requires: %libcalendarsupport = %epoch:%version
Requires: %libkmanagesieve = %epoch:%version
Requires: %libksieveui = %epoch:%version

%description devel
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

%build
%cmake_kde4 -DKDEPIM_BUILD_MOBILE=false
%make

%install
%__rm -fr %buildroot

%makeinstall_std -C build

%find_lang %name --all-name --with-html

%clean
%__rm -fr %buildroot
