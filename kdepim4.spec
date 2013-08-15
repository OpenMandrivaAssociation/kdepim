Summary:	An application suite to manage personal information
Name:		kdepim4
Epoch:		3
Version:	4.11.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		http://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/kdepim-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	grantlee-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kdepim4-runtime-devel
BuildRequires:	libassuan-devel
BuildRequires:	nepomuk-core-devel
BuildRequires:	nepomuk-widgets-devel
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(zlib)
Suggests:	akonadi-common
Suggests:	kleopatra
Suggests:	akregator
Suggests:	knode
Suggests:	kaddressbook
Suggests:	kalarm
Suggests:	ktimetracker
Suggests:	kmail
Suggests:	kmailcvt
Suggests:	knotes
Suggests:	kontact
Suggests:	korganizer
Suggests:	ksendemail
Suggests:	kjots

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer
	  and kalarm.
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
Summary:	Core files for kdepim
Group:		Graphical desktop/KDE
Requires:	kdelibs4-core
Requires:	kdebase4-runtime
Requires:	akonadi-kde >= 3:%{version}

%description core
Core files from kdepim.

%files core -f %{name}.lang
%exclude %{_kde_docdir}/HTML/en/*
%dir %{_kde_services}/kontact
%{_kde_iconsdir}/oxygen/*/mimetypes/x-mail-distribution-list.*

#-----------------------------------------------------------------------------

%define kaddressbookprivate_major 4
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %{libkaddressbookprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkaddressbookprivate}
KDE 4 library.

%files -n %{libkaddressbookprivate}
%{_kde_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*

#-----------------------------------------------------------------------------

%define kontactprivate_major 4
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %{libkontactprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE 4 library.

%files -n %{libkontactprivate}
%{_kde_libdir}/libkontactprivate.so.%{kontactprivate_major}*

#-----------------------------------------------------------------------------

%define korganizer_core_major 4
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE 4 library.

%files -n %{libkorganizer_core}
%{_kde_libdir}/libkorganizer_core.so.%{korganizer_core_major}*

#-----------------------------------------------------------------------------

%define libkdepim %mklibname kdepim 4

%package -n %{libkdepim}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdepim}
KDE 4 library.

%files -n %{libkdepim}
%{_kde_libdir}/libkdepim.so.*
%{_kde_appsdir}/kdepimwidgets
%{_kde_libdir}/kde4/plugins/designer/kdepimwidgets.so

#---------------------------------------------------------------------------

%package -n kincidenceeditor
Summary:	kincidenceeditor
Group:		Graphical desktop/KDE

%description -n kincidenceeditor
New incidince editors

%files -n kincidenceeditor
%{_kde_bindir}/kincidenceeditor

#----------------------------------------------------------------------------

%define libincidenceeditorsngmobile_major 4
%define libincidenceeditorsngmobile %mklibname incidenceeditorssngmobile %{libincidenceeditorsngmobile_major}

%package -n %{libincidenceeditorsngmobile}
Summary:	KDEPIM Mobile Library
Group:		System/Libraries

%description -n %{libincidenceeditorsngmobile}
KDE PIM Mobile library.

%files -n %{libincidenceeditorsngmobile}
%{_kde_libdir}/libincidenceeditorsngmobile.so.%{libincidenceeditorsngmobile_major}*


#-----------------------------------------------------------------------------

%define kpgp_major 4
%define libkpgp %mklibname kpgp %{kpgp_major}

%package -n %{libkpgp}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkpgp}
KDE 4 library.

%files -n %{libkpgp}
%{_kde_libdir}/libkpgp.so.%{kpgp_major}*
#TODO: move away from here
%{_kde_appsdir}/kconf_update/kpgp-3.1-upgrade-address-data.pl
%{_kde_appsdir}/kconf_update/kpgp.upd

#-----------------------------------------------------------------------------

%define kmanagesieve_major 4
%define libkmanagesieve %mklibname kmanagesieve %{kmanagesieve_major}

%package -n %{libkmanagesieve}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkmanagesieve}
KDE 4 library.

%files -n %{libkmanagesieve}
%{_kde_libdir}/libkmanagesieve.so.%{kmanagesieve_major}*

#-----------------------------------------------------------------------------

%define ksieveui_major 4
%define libksieveui %mklibname ksieveui %{ksieveui_major}

%package -n %{libksieveui}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libksieveui}
KDE 4 library.

%files -n %{libksieveui}
%{_kde_libdir}/libksieveui.so.%{ksieveui_major}*

#-----------------------------------------------------------------------------

%package -n kleopatra
Summary:	KDE Certificate Manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kleopatra = %{EVRD}

%description -n kleopatra
KDE Certificate Manager

%files -n kleopatra
%doc %{_kde_docdir}/HTML/en/kleopatra
%doc %{_kde_docdir}/HTML/en/kwatchgnupg
%{_kde_bindir}/kleopatra
%{_kde_bindir}/kgpgconf
%{_kde_bindir}/kwatchgnupg
%{_kde_applicationsdir}/kleopatra.desktop
%{_kde_applicationsdir}/kleopatra_import.desktop
%{_kde_configdir}/libkleopatrarc
%{_kde_appsdir}/kleopatra
%{_kde_appsdir}/libkleopatra
%{_kde_appsdir}/kwatchgnupg
%{_kde_iconsdir}/*/*/apps/kleopatra.*
%{_kde_services}/kleopatra_*
%{_kde_libdir}/kde4/kcm_kleopatra.so

#-----------------------------------------------------------------------------

%define ksieve_major 4
%define libksieve %mklibname ksieve %{ksieve_major}

%package -n %{libksieve}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libksieve}
KDE 4 library.

%files -n %{libksieve}
%{_kde_libdir}/libksieve.so.%{ksieve_major}*

#-----------------------------------------------------------------------------

%define akregatorinterfaces_major 4
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE 4 library.

%files -n %{libakregatorinterfaces}
%{_kde_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#-----------------------------------------------------------------------------

%define akregatorprivate_major 4
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE 4 library.

%files -n %{libakregatorprivate}
%{_kde_libdir}/libakregatorprivate.so.*

#-----------------------------------------------------------------------------

%package -n akregator
Summary:	A Feed Reader for KDE
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Akregator
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-akregator = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

%description -n akregator
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%files -n akregator
%doc %{_kde_docdir}/HTML/en/akregator
%{_kde_bindir}/akregator
%{_kde_bindir}/akregatorstorageexporter
%{_kde_applicationsdir}/akregator.desktop
%{_kde_appsdir}/akregator
%{_kde_appsdir}/akregator_sharemicroblog_plugin
%{_kde_datadir}/config.kcfg/akregator.kcfg
%{_kde_iconsdir}/*/*/apps/akregator.*
%{_kde_iconsdir}/*/*/apps/akregator_empty.*
%{_kde_services}/kontact/akregatorplugin.desktop
%{_kde_services}/akregator_*
%{_kde_services}/feed.protocol
%{_kde_servicetypes}/akregator_plugin.desktop
%{_kde_libdir}/kde4/akregator*
%{_kde_libdir}/kde4/kontact_akregatorplugin.so

#-----------------------------------------------------------------------------

%define knodecommon_major 4
%define libknodecommon %mklibname knodecommon %{knodecommon_major}

%package -n %{libknodecommon}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libknodecommon}
KDE 4 library.

%files -n %{libknodecommon}
%{_kde_libdir}/libknodecommon.so.%{knodecommon_major}*

#-----------------------------------------------------------------------------

%package -n knode
Summary:	A newsreader for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNode
Requires:	%{name}-core = %{EVRD}
Requires:	kdepimlibs4-core
Requires:	kio4-nntp
Provides:	kde4-knode = %{EVRD}

%description -n knode
KNode is a newsreader for the K Desktop Environment.

It is GNKSA compliant (unfortunally a review is still pending), and has
support for MIME and multiple servers.

It is a online-reader, but in combination with a local newsserver like
leafnode also usable with dial-up connections.

%files -n knode
%doc %{_kde_docdir}/HTML/en/knode
%doc %{_kde_docdir}/HTML/en/kioslave/news
%{_kde_bindir}/knode
%{_kde_applicationsdir}/KNode.desktop
%{_kde_appsdir}/knode
%{_kde_appsdir}/kconf_update/knode.upd
%{_kde_iconsdir}/*/*/apps/knode.*
%{_kde_services}/kontact/knodeplugin.desktop
%{_kde_services}/knode_config_accounts.desktop
%{_kde_services}/knode_config_appearance.desktop
%{_kde_services}/knode_config_cleanup.desktop
%{_kde_services}/knode_config_identity.desktop
%{_kde_services}/knode_config_post_news.desktop
%{_kde_services}/knode_config_privacy.desktop
%{_kde_services}/knode_config_read_news.desktop
%{_kde_libdir}/kde4/kcm_knode.so
%{_kde_libdir}/kde4/knodepart.so
%{_kde_libdir}/kde4/kontact_knodeplugin.so

#-----------------------------------------------------------------------------

%package -n kaddressbook
Summary:	The KDE addressbook application
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAddressBook
Requires:	%{name}-core = %{EVRD}
# Grantlee is needed for the simple view in kaddressbook
Requires:	grantlee
Requires:	akonadi-common
Provides:	kde4-kaddressbook = %{EVRD}

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%doc %{_kde_docdir}/HTML/en/kabcclient
%{_kde_bindir}/kaddressbook
%{_kde_bindir}/kabc2mutt
%{_kde_bindir}/kabcclient
%{_kde_applicationsdir}/kaddressbook.desktop
%{_kde_appsdir}/kaddressbook
%{_kde_libdir}/kde4/kcm_ldap.so
%{_kde_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_kde_libdir}/kde4/kaddressbookpart.so
%{_kde_libdir}/kde4/kontact_kaddressbookplugin.so
%{_kde_iconsdir}/*/*/apps/kaddressbook.*
%{_kde_services}/kaddressbookpart.desktop
%{_kde_services}/kontact/kaddressbookplugin.desktop
%{_kde_services}/kcmldap.desktop
%{_kde_mandir}/man1/kabcclient.1.*

#-----------------------------------------------------------------------------

%package -n blogilo
Summary:	Blogging client for kde
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

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
%doc %{_kde_docdir}/HTML/en/blogilo
%{_kde_bindir}/blogilo
%{_kde_appsdir}/blogilo
%{_kde_applicationsdir}/blogilo.desktop
%{_kde_datadir}/config.kcfg/blogilo.kcfg
%{_kde_iconsdir}/*/*/apps/blogilo.*
%{_kde_iconsdir}/*/*/actions/format-text-blockquote.*
%{_kde_iconsdir}/*/*/actions/format-text-code.*
%{_kde_iconsdir}/*/*/actions/insert-more-mark.*
%{_kde_iconsdir}/*/*/actions/remove-link.*
%{_kde_iconsdir}/*/*/actions/upload-media.*

#-----------------------------------------------------------------------------

%define messagecore_major 4
%define libmessagecore %mklibname messagecore %{messagecore_major}

%package -n %{libmessagecore}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessagecore}
KDE 4 library.

%files -n %{libmessagecore}
%{_kde_libdir}/libmessagecore.so.%{messagecore_major}*

#-----------------------------------------------------------------------------

%package -n kalarm
Summary:	A personal alarm message, command and email scheduler
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAlarm
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kalarm = %{EVRD}

%description -n kalarm
KAlarm is a personal alarm message, command and email scheduler. It lets you
set up personal alarm messages which pop up on the screen at the chosen time,
or you can schedule commands to be executed or emails to be sent.

%files -n kalarm
%doc %{_kde_docdir}/HTML/en/kalarm
%{_kde_bindir}/kalarm
%{_kde_bindir}/kalarmautostart
%{_kde_libdir}/kde4/libexec/kalarm_helper
%{_kde_applicationsdir}/kalarm.desktop
%{_kde_appsdir}/kalarm
%{_kde_appsdir}/kconf_update/kalarm-1.2.1-general.pl
%{_kde_appsdir}/kconf_update/kalarm-1.9.5-defaults.pl
%{_kde_appsdir}/kconf_update/kalarm-2.0.2-general.pl
%{_kde_appsdir}/kconf_update/kalarm-2.1.5-general.pl
%{_kde_appsdir}/kconf_update/kalarm-version.pl
%{_kde_appsdir}/kconf_update/kalarm.upd
%{_kde_autostart}/kalarm.autostart.desktop
%{_kde_datadir}/config.kcfg/kalarmconfig.kcfg
%{_kde_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_kde_iconsdir}/*/*/apps/kalarm.*
%{_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service

#-----------------------------------------------------------------------------

%package -n ktimetracker
Summary:	Tracks time spent on various tasks
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/Ktimetracker
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-ktimetracker = %{EVRD}

%description -n ktimetracker
KTimeTracker tracks time spent on various tasks. It is useful for tracking
hours to be billed to different clients or just to find out what percentage
of your day is spent playing Doom or reading Slashdot.

%files -n ktimetracker
%doc %{_kde_docdir}/HTML/en/ktimetracker
%{_kde_bindir}/karm
%{_kde_bindir}/ktimetracker
%{_kde_appsdir}/ktimetracker
%{_kde_applicationsdir}/ktimetracker.desktop
%{_kde_iconsdir}/*/*/apps/ktimetracker.*
%{_kde_services}/ktimetrackerpart.desktop
%{_kde_services}/ktimetracker_config_behavior.desktop
%{_kde_services}/ktimetracker_config_display.desktop
%{_kde_services}/ktimetracker_config_storage.desktop
%{_kde_libdir}/kde4/ktimetrackerpart.so
%{_kde_libdir}/kde4/kcm_ktimetracker.so

#-----------------------------------------------------------------------------

%define kmailprivate_major 4
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %{libkmailprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkmailprivate}
KDE 4 library.

%files -n %{libkmailprivate}
%{_kde_libdir}/libkmailprivate.so.%{kmailprivate_major}*

#-----------------------------------------------------------------------------

%define mailcommon_major 4
%define libmailcommon %mklibname mailcommon %{mailcommon_major}

%package -n %{libmailcommon}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmailcommon}
KDE 4 library.

%files -n %{libmailcommon}
%{_kde_libdir}/libmailcommon.so.%{mailcommon_major}*

#-----------------------------------------------------------------------------

%package -n kmail
Summary:	KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Requires:	kdepimlibs4-core
Requires:	sasl-plug-plain
Requires:	sasl-plug-ntlm
Requires:	sasl-plug-login
Requires:	sasl-plug-digestmd5
Requires:	kio4-pop3
Requires:	kio4-smtp
Requires:	kio4-mbox
Requires:	kio4-imap
Requires:	kio4-sieve
Requires:	kmail-common
Requires:	akonadi-archivemail-agent = %{EVRD}
Requires:	akonadi-mailfilter-agent = %{EVRD}
Suggests:	kmailcvt
Suggests:	pinentry-qt4
Suggests:	openssh-askpass-qt4
Suggests:	pimsettingexporter
Suggests:	importwizard
Provides:	kde4-kmail = %{EVRD}
Provides:	kmail2 = %{EVRD}

%description -n kmail
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -n kmail
%doc %{_kde_docdir}/HTML/en/kmail
%{_kde_bindir}/kmail
%{_kde_bindir}/kmail_antivir.sh
%{_kde_bindir}/kmail_clamav.sh
%{_kde_bindir}/kmail_fprot.sh
%{_kde_bindir}/kmail_sav.sh
%{_kde_appsdir}/kmail2
%{_kde_applicationsdir}/KMail2.desktop
%{_kde_applicationsdir}/kmail_view.desktop
%{_kde_appsdir}/kconf_update/kmail*
%{_kde_appsdir}/kconf_update/upgrade-signature.pl
%{_kde_appsdir}/kconf_update/upgrade-transport.pl
%{_kde_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kde_datadir}/config.kcfg/kmail.kcfg
%{_kde_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kde_configdir}/kmail.antispamrc
%{_kde_configdir}/kmail.antivirusrc
%{_kde_datadir}/ontology/kde/messagetag.ontology
%{_kde_datadir}/ontology/kde/messagetag.trig
%{_kde_iconsdir}/*/*/apps/kmail.*
%{_kde_services}/kontact/kmailplugin.desktop
%{_kde_services}/kmail_config_accounts.desktop
%{_kde_services}/kmail_config_appearance.desktop
%{_kde_services}/kmail_config_composer.desktop
%{_kde_services}/kmail_config_identity.desktop
%{_kde_services}/kmail_config_misc.desktop
%{_kde_services}/kmail_config_security.desktop
%{_kde_services}/kcmkmailsummary.desktop
%{_kde_services}/ServiceMenus/kmail_addattachmentservicemenu.desktop
%{_kde_servicetypes}/dbusmail.desktop
%{_kde_libdir}/kde4/kcm_kmail.so
%{_kde_libdir}/kde4/kmailpart.so
%{_kde_libdir}/kde4/kcm_kmailsummary.so
%{_kde_libdir}/kde4/kontact_kmailplugin.so
%{_kde_libdir}/kde4/ktexteditorkabcbridge.so

#-----------------------------------------------------------------------------

%package -n kmail-common
Summary:	KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Provides:	kmail2-common = %{EVRD}

%description -n kmail-common
Common files needed by kmail and kmail-mobile used to view messages.

%files -n kmail-common
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_application_mstnef.so
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_text_calendar.so
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_text_vcard.so
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_text_xdiff.so
%{_kde_services}/kcm_kpimidentities.desktop
%{_kde_libdir}/kde4/kcm_kpimidentities.so
%{_kde_appsdir}/libmessageviewer
%{_kde_appsdir}/messageviewer
%{_kde_appsdir}/messagelist

#-----------------------------------------------------------------------------

%package -n kmailcvt
Summary:	KDE Mail Import tool
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kmailcvt = %{EVRD}

%description -n kmailcvt
KDE Mail Import tool

%files -n kmailcvt
%{_kde_bindir}/kmailcvt
%{_kde_appsdir}/kmailcvt/pics/step1.png
%{_kde_iconsdir}/*/*/apps/kmailcvt.*

#-----------------------------------------------------------------------------

%package -n pimsettingexporter
Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Group:		Graphical desktop/KDE
Requires:	kmail
Obsoletes:	backupmail < 3:4.10.0

%description -n pimsettingexporter
Allows to save data from KDE PIM applications and restore them in other
systems. Successor of Backup Mail from KDE 4.9.

%files -n pimsettingexporter
%{_kde_bindir}/pimsettingexporter
%{_kde_appsdir}/pimsettingexporter/pimsettingexporter.rc

#-----------------------------------------------------------------------------

%package -n importwizard
Summary:	Import Wizard allows to migrate data from mailer as thunderbird/evolution etc
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n importwizard
Import Wizard allows to migrate data from mailer as thunderbird/evolution etc.

%files -n importwizard
%{_kde_bindir}/importwizard
%{_kde_applicationsdir}/importwizard.desktop
%{_kde_iconsdir}/*/*/apps/kontact-import-wizard.*

#-----------------------------------------------------------------------------

%package -n knotes
Summary:	Notes for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNotes
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-kresources
Requires:	kio4-nntp
Provides:	kde4-knotes = %{EVRD}

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%doc %{_kde_docdir}/HTML/en/knotes
%{_kde_bindir}/knotes
%{_kde_applicationsdir}/knotes.desktop
%{_kde_datadir}/config.kcfg/knoteconfig.kcfg
%{_kde_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_kde_appsdir}/knotes
%{_kde_iconsdir}/*/*/apps/knotes.*
%{_kde_iconsdir}/*/*/actions/knotes_*
%{_kde_services}/kontact/knotesplugin.desktop
%{_kde_services}/kresources/knotes/local.desktop
%{_kde_services}/kresources/knotes_manager.desktop
%{_kde_services}/knote_config_action.desktop
%{_kde_services}/knote_config_display.desktop
%{_kde_services}/knote_config_editor.desktop
%{_kde_services}/knote_config_network.desktop
%{_kde_services}/knote_config_style.desktop
%{_kde_libdir}/kde4/knotes_local.so
%{_kde_libdir}/kde4/kcm_knote.so
%{_kde_libdir}/kde4/kontact_knotesplugin.so

#-----------------------------------------------------------------------------

%package -n kontact
Summary:	Kontact Container
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Kontact
Requires:	%{name}-core = %{EVRD}
Requires:	kio4-ldap
Provides:	kde4-kontact = %{EVRD}
Suggests:	akregator
Suggests:	kmail
Suggests:	knotes
Suggests:	ktimetracker
Suggests:	knode
Suggests:	kalarm
Suggests:	kaddressbook
Suggests:	korganizer

%description -n kontact
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -n kontact
%doc %{_kde_docdir}/HTML/en/kontact
%doc %{_kde_docdir}/HTML/en/kontact-admin
%{_kde_bindir}/kontact
%{_kde_appsdir}/kontact
%{_kde_appsdir}/kontactsummary
%{_kde_applicationsdir}/Kontact.desktop
%{_kde_applicationsdir}/kontact-admin.desktop
%{_kde_datadir}/config.kcfg/kontact.kcfg
%{_kde_iconsdir}/*/*/apps/kontact.*
%{_kde_services}/kontactconfig.desktop
%{_kde_services}/kcmapptsummary.desktop
%{_kde_services}/kcmkontactsummary.desktop
%{_kde_services}/kcmsdsummary.desktop
%{_kde_services}/kontact/summaryplugin.desktop
%{_kde_services}/kontact/specialdatesplugin.desktop
%{_kde_libdir}/kde4/kcm_apptsummary.so
%{_kde_libdir}/kde4/kcm_kontact.so
%{_kde_libdir}/kde4/kcm_kontactsummary.so
%{_kde_libdir}/kde4/kontact_journalplugin.so
%{_kde_libdir}/kde4/kcm_sdsummary.so
%{_kde_libdir}/kde4/kontact_specialdatesplugin.so
%{_kde_libdir}/kde4/kontact_summaryplugin.so

#-----------------------------------------------------------------------------

%define korganizer_interfaces_major 4
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE 4 library.

%files -n %{libkorganizer_interfaces}
%{_kde_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#-----------------------------------------------------------------------------

%package -n korganizer
Summary:	Calendar and scheduling component
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KOrganizer
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-kresources
Requires:	kio4-ldap
Suggests:	kincidenceeditor
Provides:	kde4-korganizer = %{EVRD}

%description -n korganizer
KOrganizer provides management of events and tasks, alarm notification,
web export, network transparent handling of data, group scheduling,
import and export of calendar files and more. It is able to work together
with a wide variety of groupware servers, for example Kolab, Open-Xchange,
Citadel or OpenGroupware.org.

%files -n korganizer
%doc %{_kde_docdir}/HTML/en/korganizer
%doc %{_kde_docdir}/HTML/en/konsolekalendar
%{_kde_bindir}/ical2vcal
%{_kde_bindir}/konsolekalendar
%{_kde_bindir}/korgac
%{_kde_bindir}/korganizer
%{_kde_applicationsdir}/konsolekalendar.desktop
%{_kde_applicationsdir}/korganizer-import.desktop
%{_kde_applicationsdir}/korganizer.desktop
%{_kde_appsdir}/kconf_update/korganizer.upd
%{_kde_appsdir}/korgac
%{_kde_appsdir}/korganizer
%{_kde_iconsdir}/*/*/apps/konsolekalendar.*
%{_kde_iconsdir}/*/*/apps/korganizer.*
%{_kde_iconsdir}/*/*/actions/checkmark.*
%{_kde_iconsdir}/*/*/actions/smallclock.*
%{_kde_iconsdir}/*/*/actions/upindicator.*
%{_kde_iconsdir}/*/*/apps/korg-journal.*
%{_kde_iconsdir}/*/*/apps/korg-todo.*
%{_kde_autostart}/korgac.desktop
%{_kde_datadir}/config.kcfg/korganizer.kcfg
%{_kde_configdir}/korganizer.knsrc
%{_kde_services}/kontact/korganizerplugin.desktop
%{_kde_services}/kontact/todoplugin.desktop
%{_kde_services}/kcmtodosummary.desktop
%{_kde_services}/kontact/journalplugin.desktop
%{_kde_services}/korganizer*
%{_kde_services}/webcal.protocol
%{_kde_servicetypes}/calendardecoration.desktop
%{_kde_servicetypes}/calendarplugin.desktop
%{_kde_servicetypes}/dbuscalendar.desktop
%{_kde_servicetypes}/korganizerpart.desktop
%{_kde_servicetypes}/korgprintplugin.desktop
%{_kde_libdir}/kde4/kcm_todosummary.so
%{_kde_libdir}/kde4/kontact_todoplugin.so
%{_kde_libdir}/kde4/kcm_korganizer.so
%{_kde_libdir}/kde4/korg_*
%{_kde_libdir}/kde4/korganizerpart.so
%{_kde_libdir}/kde4/kontact_korganizerplugin.so

#-----------------------------------------------------------------------------

%define korganizerprivate_major 4
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %{libkorganizerprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkorganizerprivate}
KDE 4 library.

%files -n %{libkorganizerprivate}
%{_kde_libdir}/libkorganizerprivate.so.%{korganizerprivate_major}*

#------------------------------------------------------------------------------

%define libcalendarsupport_major 4
%define libcalendarsupport %mklibname calendarsupport %{libcalendarsupport_major}

%package -n %{libcalendarsupport}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libcalendarsupport}
KDE 4 library for korganizer-Mobile.

%files -n %{libcalendarsupport}
%{_kde_libdir}/libcalendarsupport.so.%{libcalendarsupport_major}*

#-----------------------------------------------------------------------------

%define messagelist_major 4
%define libmessagelist %mklibname messagelist %{messagelist_major}

%package -n %{libmessagelist}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessagelist}
KDE 4 library.

%files -n %{libmessagelist}
%{_kde_libdir}/libmessagelist.so.%{messagelist_major}*

#-----------------------------------------------------------------------------

%define kcal_resourceblog 4
%define libkcal_resourceblog %mklibname kcal_resourceblog %{kcal_resourceblog}

%package -n %{libkcal_resourceblog}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkcal_resourceblog}
KDE 4 library.

%files -n %{libkcal_resourceblog}
%{_kde_libdir}/libkcal_resourceblog.so.%{kcal_resourceblog}*

#-----------------------------------------------------------------------------

%define kcal_resourceremote_major 4
%define libkcal_resourceremote %mklibname kcal_resourceremote %{kcal_resourceremote_major}

%package -n %{libkcal_resourceremote}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkcal_resourceremote}
KDE 4 library.

%files -n %{libkcal_resourceremote}
%{_kde_libdir}/libkcal_resourceremote.so.%{kcal_resourceremote_major}*

#-----------------------------------------------------------------------


%define libkdgantt2_major 0
%define libkdgantt2 %mklibname kdgantt2 %{libkdgantt2_major}

%package -n %{libkdgantt2}
Summary:	KDE4 library
Group:		System/Libraries

%description -n %{libkdgantt2}
KDE 4 library.

%files -n %{libkdgantt2}
%{_kde_libdir}/libkdgantt2.so.%{libkdgantt2_major}*

#-----------------------------------------------------------------------------

%define kleo_major 4
%define libkleo %mklibname kleo %{kleo_major}

%package -n %{libkleo}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkleo}
KDE 4 library.

%files -n %{libkleo}
%{_kde_libdir}/libkleo.so.%{kleo_major}*

#-----------------------------------------------------------------------------

%package kresources
Summary:	KDE pim resource plugins
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description kresources
This package includes several plugins needed to interface with groupware
servers. It also includes plugins for features such as blogging and
tracking feature plans.

%files kresources
%{_kde_libdir}/kde4/kcal_blog.so
%{_kde_libdir}/kde4/kcal_remote.so
%{_kde_services}/kresources/kcal/blog.desktop
%{_kde_services}/kresources/kcal/remote.desktop

#-----------------------------------------------------------------------------

%package -n ksendemail
Summary:	%{name} ksendemail
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n ksendemail
%{name} ksendemail.

%files -n ksendemail
%{_kde_bindir}/ksendemail

#-----------------------------------------------------------------------------

%package -n akonadiconsole
Summary:	Console that help to debug akonadi
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Conflicts:	kdepim4-core < 2:4.4.2-5

%description -n akonadiconsole
Console that help to debug akonadi

%files -n akonadiconsole
%{_kde_bindir}/akonadiconsole
%{_kde_applicationsdir}/akonadiconsole.desktop
%{_kde_appsdir}/akonadiconsole/akonadiconsoleui.rc
%{_kde_iconsdir}/hicolor/*/apps/akonadiconsole.png

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent
%{_kde_bindir}/akonadi_archivemail_agent
%{_kde_datadir}/akonadi/agents/archivemailagent.desktop
%{_kde_appsdir}/akonadi_archivemail_agent

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent
%{_kde_bindir}/akonadi_mailfilter_agent
%{_kde_plugindir}/accessible/messagevieweraccessiblewidgetfactory.so
%{_kde_datadir}/akonadi/agents/mailfilteragent.desktop
%{_kde_appsdir}/akonadi_mailfilter_agent
%{_kde_appsdir}/kconf_update/mailfilteragent.upd
%{_kde_appsdir}/kconf_update/migrate-kmail-filters.pl

#-----------------------------------------------------------------------------

%define messageviewer_major 4
%define libmessageviewer %mklibname messageviewer %{messageviewer_major}

%package -n %{libmessageviewer}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessageviewer}
KDE 4 library.

%files -n %{libmessageviewer}
%{_kde_libdir}/libmessageviewer.so.%{messageviewer_major}*

#-----------------------------------------------------------------------------

%define akonadi_next_major 4
%define libakonadi_next %mklibname akonadi-next %{akonadi_next_major}

%package -n %{libakonadi_next}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakonadi_next}
KDE 4 library.

%files -n %{libakonadi_next}
%{_kde_libdir}/libakonadi_next.so.%{akonadi_next_major}*

#-----------------------------------------------------------------------------

%define eventviews_major 4
%define libeventviews %mklibname eventviews %{eventviews_major}

%package -n %{libeventviews}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libeventviews}
KDE 4 library.

%files -n %{libeventviews}
%{_kde_libdir}/libeventviews.so.%{eventviews_major}*

#-----------------------------------------------------------------------------

%define libincidenceeditorsng_major 4
%define libincidenceeditorsng %mklibname incidenceeditorsng %{libincidenceeditorsng_major}

%package -n %{libincidenceeditorsng}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}incidenceeditors4 < 2:4.5.68

%description -n %{libincidenceeditorsng}
KDE 4 library.

%files -n %{libincidenceeditorsng}
%{_kde_libdir}/libincidenceeditorsng.so.%{libincidenceeditorsng_major}*

#-----------------------------------------------------------------------------

%define kdepimdbusinterfaces_major 4
%define libkdepimdbusinterfaces %mklibname kdepimdbusinterfaces %{kdepimdbusinterfaces_major}

%package -n %{libkdepimdbusinterfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdepimdbusinterfaces}
KDE 4 library.

%files -n %{libkdepimdbusinterfaces}
%{_kde_libdir}/libkdepimdbusinterfaces.so.%{kdepimdbusinterfaces_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientcore_major 0
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %{libkleopatraclientcore}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientcore4 <= 2:4.5

%description -n %{libkleopatraclientcore}
KDE 4 library.

%files -n %{libkleopatraclientcore}
%{_kde_libdir}/libkleopatraclientcore.so.%{kleopatraclientcore_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientgui_major 0
%define libkleopatraclientgui %mklibname kleopatraclientgui %{kleopatraclientgui_major}

%package -n %{libkleopatraclientgui}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientgui4 <= 2:4.5

%description -n %{libkleopatraclientgui}
KDE 4 library.

%files -n %{libkleopatraclientgui}
%{_kde_libdir}/libkleopatraclientgui.so.%{kleopatraclientgui_major}*

#-----------------------------------------------------------------------------

%define messagecomposer_major 4
%define libmessagecomposer %mklibname messagecomposer %{messagecomposer_major}

%package -n %{libmessagecomposer}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessagecomposer}
KDE 4 library.

%files -n %{libmessagecomposer}
%{_kde_libdir}/libmessagecomposer.so.%{messagecomposer_major}*

#-----------------------------------------------------------------------------

%define templateparser_major 4
%define libtemplateparser %mklibname templateparser %{templateparser_major}

%package -n %{libtemplateparser}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libtemplateparser}
KDE 4 library.

%files -n %{libtemplateparser}
%{_kde_libdir}/libtemplateparser.so.%{templateparser_major}*

#-----------------------------------------------------------------------------

%define libcomposereditorng_major 4
%define libcomposereditorng %mklibname composereditorng %{libcomposereditorng_major}

%package -n %{libcomposereditorng}
Summary:	Library providing autospell checking
Group:		System/Libraries

%description -n %{libcomposereditorng}
This library provides autospell checking.

%files -n %{libcomposereditorng}
%{_kde_libdir}/libcomposereditorng.so.%{libcomposereditorng_major}*

#-----------------------------------------------------------------------------

%define libgrammar_major 4
%define libgrammar %mklibname grammar %{libgrammar_major}

%package -n %{libgrammar}
Summary:	Library providing grammar support
Group:		System/Libraries

%description -n %{libgrammar}
This library provides grammar support.

%files -n %{libgrammar}
%{_kde_libdir}/libgrammar.so.%{libgrammar_major}*

#-----------------------------------------------------------------------------

%define mailimporter_major 4
%define libmailimporter %mklibname mailimporter %{mailimporter_major}

%package -n %{libmailimporter}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmailimporter}
KDE 4 library.

%files -n %{libmailimporter}
%{_kde_libdir}/libmailimporter.so.%{mailimporter_major}*

#-----------------------------------------------------------------------------

%define libpimcommon_major 4
%define libpimcommon %mklibname pimcommon %{libpimcommon_major}

%package -n %{libpimcommon}
Summary:	Library to import/export PIM configuration
Group:		System/Libraries

%description -n %{libpimcommon}
This library provides the tool to import/export PIM configuration.

%files -n %{libpimcommon}
%{_kde_libdir}/libpimcommon.so.%{libpimcommon_major}*

#-----------------------------------------------------------------------------

%define sendlater_major 4
%define libsendlater %mklibname sendlater %{sendlater_major}

%package -n %{libsendlater}
Summary:	KDE PIM library
Group:		System/Libraries

%description -n %{libsendlater}
KDE PIM library.

%files -n %{libsendlater}
%{_kde_libdir}/libsendlater.so.%{sendlater_major}*

#-----------------------------------------------------------------------------

%package -n kjots
Summary:	KDE note taking utility
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KJots
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kjots = %{EVRD}

%description -n kjots
A small program which is handy for keeping and organizing miscellaneous
notes.

%files -n kjots
%doc %{_kde_docdir}/HTML/en/kjots
%{_kde_bindir}/kjots
%{_kde_appsdir}/desktoptheme/default/widgets/stickynote.svgz
%{_kde_appsdir}/kjots
%{_kde_applicationsdir}/Kjots.desktop
%{_kde_libdir}/kde4/kcm_kjots.so
%{_kde_libdir}/kde4/kjotspart.so
%{_kde_libdir}/kde4/kontact_kjotsplugin.so
%{_kde_libdir}/kde4/plasma_applet_akonotes_list.so
%{_kde_libdir}/kde4/plasma_applet_akonotes_note.so
%{_kde_datadir}/config.kcfg/kjots.kcfg
%{_kde_iconsdir}/*/*/apps/kjots.*
%{_kde_iconsdir}/*/*/actions/edit-delete-page.*
%{_kde_services}/akonotes_list.desktop
%{_kde_services}/akonotes_note.desktop
%{_kde_services}/kjots_config_misc.desktop
%{_kde_services}/kjotspart.desktop
%{_kde_services}/kontact/kjots_plugin.desktop

#-----------------------------------------------------------------------------

%package -n ktnef
Summary:	KDE TNEF File Viewer
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n ktnef
The TNEF File Viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n ktnef
%doc %{_kde_docdir}/HTML/en/ktnef
%{_kde_bindir}/ktnef
%{_kde_applicationsdir}/ktnef.desktop
%{_kde_appsdir}/ktnef
%{_kde_iconsdir}/*/*/apps/ktnef*.*
%{_kde_iconsdir}/*/*/actions/ktnef*.*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	kdepimlibs4-devel
Requires:	kdepim4-runtime-devel
Requires:	%{libcomposereditorng} = %{EVRD}
Requires:	%{libgrammar} = %{EVRD}
Requires:	%{libkdepim} = %{EVRD}
Requires:	%{libsendlater} = %{EVRD}
Requires:	%{libeventviews} = %{EVRD}
Requires:	%{libkleopatraclientcore} = %{EVRD}
Requires:	%{libincidenceeditorsng} = %{EVRD}
Requires:	%{libtemplateparser} = %{EVRD}
Requires:	%{libmessagecomposer} = %{EVRD}
Requires:	%{libkleopatraclientgui} = %{EVRD}
Requires:	%{libkdepimdbusinterfaces} = %{EVRD}
Requires:	%{libkpgp} = %{EVRD}
Requires:	%{libksieve} = %{EVRD}
Requires:	%{libakregatorinterfaces} = %{EVRD}
Requires:	%{libakregatorprivate} = %{EVRD}
Requires:	%{libknodecommon} = %{EVRD}
Requires:	%{libkmailprivate} = %{EVRD}
Requires:	%{libmailcommon} = %{EVRD}
Requires:	%{libkorganizerprivate} = %{EVRD}
Requires:	%{libkorganizer_interfaces} = %{EVRD}
Requires:	%{libkcal_resourceremote} = %{EVRD}
Requires:	%{libkcal_resourceblog} = %{EVRD}
Requires:	%{libkleo} = %{EVRD}
Requires:	%{libmessagelist} = %{EVRD}
Requires:	%{libmessagecore} = %{EVRD}
Requires:	%{libmessageviewer} = %{EVRD}
Requires:	%{libakonadi_next} = %{EVRD}
Requires:	%{libkdgantt2} = %{EVRD}
Requires:	%{libincidenceeditorsngmobile} = %{EVRD}
Requires:	%{libcalendarsupport} = %{EVRD}
Requires:	%{libkmanagesieve} = %{EVRD}
Requires:	%{libksieveui} = %{EVRD}
Requires:	%{libmailimporter} = %{EVRD}
Requires:	%{libpimcommon} = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%{_kde_libdir}/*.so
%{_kde_datadir}/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}

%build
%cmake_kde4 -DKDEPIM_BUILD_MOBILE=false
%make

%install
%makeinstall_std -C build

%find_lang %{name} --all-name --with-html

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Add pkgconfig(libkactivities) to BuildRequires
- New subpackages libcomposereditorng, libgrammar, libsendlater

* Fri Jul 19 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-2
- Update BuildRequires
- Cleanup Conflicts

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2
- Update files (add kontact-import-wizard icons)

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0
- Add BuildRequires nepomuk-core-devel and nepomuk-widgets-devel
- Replace backupmail subpackage with pimsettingexporter
- New library subpackage added - libpimcommon
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97
- Convert BuildRequires to pkgconfig style
- Make better usage of KDE4 path macros
- Re-diff and enable l10n-ru patch

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Update to 4.8.95
- Re-diff l10n patch

* Wed Jun 27 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.90-1
- Update to 4.8.90
- New subpackage akonadi-archivemail-agent
- New subpackage backupmail
- New subpackage importwizard
- Update file lists
- Major spec cleanup

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 3:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 3:4.8.3-1
- update to 4.8.3

* Mon Apr 16 2012 Mikhail Kompaniets <mkompan@mezon.ru> 3:4.8.2-2
- Russian localization for .desktop files

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 3:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 3:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.8.0-1
+ Revision: 762518
- New upstream tarball

* Sat Jan 07 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.97-1
+ Revision: 758477
- Fix file list
- Fix file list
- Fix file list
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.95-1
+ Revision: 748919
- New version

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.90-1
+ Revision: 739335
- New upstream tarball

* Thu Dec 08 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 3:4.7.80-1
+ Revision: 739025
- tiny fix of description length and formatting
- remove nepomuk-email-feeder
- add akonadi-mailfilter-agent
- update files for kalarm

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Mon Oct 10 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.41-1
+ Revision: 703980
- Fix Kalarm File list
- Fix Kmail file list
- New version 4.7.41

* Sat Jun 11 2011 Funda Wang <fwang@mandriva.org> 3:4.6.0-2
+ Revision: 684205
- correct conflicts

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add icons in file list
    - Fix file list
    - Update to version 4.6.0

* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 3:4.4.11.1-2
+ Revision: 674405
- clean up br

* Fri Apr 29 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.11.1-1
+ Revision: 660536
- Fix file list
- Fix file list
- Do not build nepomuk support for now
- Add missing patch
- Revert to version 4.4.11.1
  Remove merged patches
- Remove mkrel

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - Update to beta5 (from neoclust | 2011-04-12 14:39:41 +0200)

* Fri Jan 14 2011 Funda Wang <fwang@mandriva.org> 2:4.5.94.1-1
+ Revision: 631030
- drop merged patch
- new version 4.5.94.1
- update URL

* Sat Jan 08 2011 Funda Wang <fwang@mandriva.org> 2:4.5.94-1mdv2011.0
+ Revision: 630554
- add upstream patch to build with kde 4.6
- disable doc for now, it throws out a lot of errors
- new version 4.5.94

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 2:4.5.93-1mdv2011.0
+ Revision: 624458
- 4.6 beta3
- update description

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Sun Dec 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.85-1mdv2011.0
+ Revision: 620591
- Remove all the mobile sub packages
- Do not build kontact mobile
- New upstream tarball

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 2:4.5.80-1mdv2011.0
+ Revision: 601539
- new version 4.5.80 (aka 4.6 beta1)
- bump requires on runtime
- thre is no kitchensync now

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 2:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599147
- update file list
- new snapshot 4.5.77

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1196728.1mdv2011.0
+ Revision: 597502
- update file list
- refresh tarball
- update file list
- update file list
- new snapshot 4.5.76

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 2:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589831
- fix file ext
- New snapshot 4.5.74

* Fri Oct 08 2010 John Balcaen <mikala@mandriva.org> 2:4.5.71-0.svn1183615.2mdv2011.0
+ Revision: 584210
- Add patch0 from upstream to fix headers

  + Funda Wang <fwang@mandriva.org>
    - update summary

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1183615.1mdv2011.0
+ Revision: 584162
- New snapshot 4.5.71

* Mon Sep 20 2010 Funda Wang <fwang@mandriva.org> 2:4.5.68-2mdv2011.0
+ Revision: 579909
- fix obsoletes

* Fri Sep 17 2010 Funda Wang <fwang@mandriva.org> 2:4.5.68-1mdv2011.0
+ Revision: 579169
- fix pkg name
- New snapshot 4.5.68

* Thu Sep 09 2010 John Balcaen <mikala@mandriva.org> 2:4.5.67-1mdv2011.0
+ Revision: 576891
- Fix Group for kdepim4-mobile
- Add a suggest for keventeditor in korganizer
- Add patch1 to fix messagelist install path
- Add several packages for kdepim-mobile
- Use more kde macros
- Add grantee as a require on kadressbook (needed for the sample view)
- Clean BR

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add grantlee-devel as Buildrequires
    - Fix file list
    - More include fixes
    - Fix build
    - New version 4.5.67

* Wed Aug 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.5-1mdv2011.0
+ Revision: 569028
- Update  to kdepim 4.4.5
  Remove merged patches

* Mon Jun 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-12mdv2010.1
+ Revision: 549436
- Add one more icon
- Fix new icons install
- Fix kleopatra icon under gnome

* Mon May 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-11mdv2010.1
+ Revision: 546716
- Add branches patches fixing crashes
- Add branches patches fixing crashes

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-10mdv2010.1
+ Revision: 546145
- Rebuild in release mode

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-9mdv2010.1
+ Revision: 545886
- Fix file list
- Update nepomuk patch

* Sat May 08 2010 Funda Wang <fwang@mandriva.org> 2:4.4.3-8mdv2010.1
+ Revision: 543557
- add missing requires on actural libfile

* Thu May 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-7mdv2010.1
+ Revision: 542789
- Remove P301 : Merged upstream
- Update to version 4.4.3

* Wed Apr 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-7mdv2010.1
+ Revision: 540313
- Add a patch fixing disribution list

* Tue Apr 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-6mdv2010.1
+ Revision: 539828
- Split akonadiconsole in its own rpm

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild so that shared libraries are properly stripped again

* Wed Apr 21 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-4mdv2010.1
+ Revision: 537751
- Remove kmail ksni patch

* Tue Apr 20 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-3mdv2010.1
+ Revision: 537268
- Update kmail patch

* Fri Apr 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-2mdv2010.1
+ Revision: 535465
- Add kmail KStatusNotifierItem patch

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-1mdv2010.1
+ Revision: 530104
- akonadi_nepomuk_email_feeder is disabled for the moment
- Fix patch apply
- Update to version 4.4.2
- Kadressbook does not need to have akonadi started anymore

* Wed Mar 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-4mdv2010.1
+ Revision: 527274
- Fix typo   tks Anssi

* Wed Mar 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-3mdv2010.1
+ Revision: 527219
- Add scribo-devel as buildrequire
- Reapply nepomuk patch
- Fix typo
- Fix file list
- Add patches about akonadi start
- Bump release
- Fix file list
- Fix and apply nepomuk patch
- Add akonadi-kde as Requires on the main package
  Start to add kmail-nepomuk ( not applied yet )

* Fri Mar 12 2010 Funda Wang <fwang@mandriva.org> 2:4.4.1-1mdv2010.1
+ Revision: 518430
- update file list

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix file list
    - Update to version 4.4.1
    - Kaddressbook requires akonadi

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-1mdv2010.1
+ Revision: 502615
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-1mdv2010.1
+ Revision: 499230
- Fix file list
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Tue Jan 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-1mdv2010.1
+ Revision: 496510
- Fix file list
- Fix previous commit
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Remove the file copy as the culprit files are not on this package
- Fix menu files
- Fix cp macro
- Add missing icons in hicolor

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-1mdv2010.1
+ Revision: 488615
- Fix typo
- Fix file list
- Remove patch2
- Update to kde 4.4 rc1

* Wed Dec 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-2mdv2010.1
+ Revision: 481699
- Add back Suggests: nepomuk-email-feeder when it will be built again

* Tue Dec 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-1mdv2010.1
+ Revision: 481251
- Update to kde 4.4 beta2
  Disable nepomuk_feeder for now
  Fix major in packages
  Fix file list
- Fix comment

* Mon Dec 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-3mdv2010.1
+ Revision: 478464
- disable libindicate support ( asked by thiago)

* Fri Dec 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-2mdv2010.1
+ Revision: 476467
- Remove last kpilot switch
- Remove kpilot occurence in %%description
- Say goodbye to Kpilot
- Add libindicate-qt-devel as Buildrequires

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-1mdv2010.1
+ Revision: 473316
- Fix File list
  KPilot isn't provided for kde 4.4
- KDE 4.4 beta1

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-1mdv2010.1
+ Revision: 470979
- Fix file lists
- Fix file list in Kalarm who is back
  2 now packages:
        - libkalarm_calendar
        - libkalarm_resources
- Update to kde 4.3.77

* Fri Nov 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-2mdv2010.1
+ Revision: 467622
- Fix libmessageviewer libs

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-1mdv2010.1
+ Revision: 467049
- Update to kde 4.3.75
  New package:
        - nepomuk-email-feeder

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-2mdv2010.1
+ Revision: 464928
- Remove patch2
- Rebuild against new qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-1mdv2010.1
+ Revision: 462812
- Update to kde 4.3.73
  Remove merged patches
  Fix file list

* Mon Oct 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-2mdv2010.0
+ Revision: 456701
- add patches from branch ( bugfixes, crash fixes, ...)

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-1mdv2010.0
+ Revision: 454427
- New upstream release 4.3.2.

* Fri Sep 25 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-10mdv2010.0
+ Revision: 448941
- Replace suggests as requires for ldap, imap and sieve

* Fri Sep 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-9mdv2010.0
+ Revision: 448597
- Add back desktop file patch

* Thu Sep 24 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-8mdv2010.0
+ Revision: 448456
- Make kmail, knode and kontact make use of proper kioslaves

* Wed Sep 23 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-6mdv2010.0
+ Revision: 447852
- Update imap crash patch with single one

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-5mdv2010.0
+ Revision: 443110
- pinentry-qt4 and openssh-askpass-qt4 as suggests ( because what is a few kilobytes ) :-)
- kmailcvt as suggests too for kmail

* Mon Sep 14 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-3mdv2010.0
+ Revision: 440676
- Fix major disconnected imap issue in kmail. Renaming folders in disconnectec imap can ocasionally delete mails in main imap server

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add pinentry-qt4 as Requires to allow users to sign mails

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-1mdv2010.0
+ Revision: 423205
- New upstream release 4.3.1.

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.0-1mdv2010.0
+ Revision: 409401
- New upstream release 4.3.0.

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.98-1mdv2010.0
+ Revision: 398737
- Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.96-1mdv2010.0
+ Revision: 394872
- Update to Rc2
- Fix requires in kmail

* Wed Jul 01 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.95-3mdv2010.0
+ Revision: 391248
- Obsoletes kode which is no longer available

* Tue Jun 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-2mdv2010.0
+ Revision: 390790
- Versionnate buildrequires
- New tarball for Rc1
- Add korganizer a suggests in kontact
- Add back kmail first message ( rediffed because of the lose of qt3support)

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-1mdv2010.0
+ Revision: 389421
- Update to kde 4.3Rc1

* Mon Jun 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.90-1mdv2010.0
+ Revision: 383846
- Fix file list
- Fix file list
- Update to beta2

* Sat May 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.88-1mdv2010.0
+ Revision: 381526
- Fix file list
- Remove  merged patch
- Update to kde 4.2.88

* Sun May 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.87-1mdv2010.0
+ Revision: 379316
- Fix file list
- Fix build
- Update to kde 4.2.87

* Mon May 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-7mdv2010.0
+ Revision: 376800
- Fix Requires

* Sun May 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-6mdv2010.0
+ Revision: 376678
- [Bugfix]Add some Requires (Bug #50943)

* Sun May 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-5mdv2010.0
+ Revision: 376605
- Fix excluded files
- [Bugfix]Fix Requires for akonadi package ( But #50950)
- Do not package nco.trig and .desktop files, they are on kdebase4-runtime

* Sun May 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-3mdv2010.0
+ Revision: 374048
- Fix file list
- Change Requires on devel package

* Sun May 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-2mdv2010.0
+ Revision: 373914
- Remove dupplicate file with oxygen theme

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-1mdv2010.0
+ Revision: 373654
- Update to kde 4.2.85
- Add some suggests for default kontact
- Remove old macros ( step 2 )
- Remove old macros
- Update to kde 4.2.71

* Sat May 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 370594
- Update to kde 4.2.70
  Remove merged patches

* Sat Apr 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-13mdv2009.1
+ Revision: 367954
- Add patches from 4.2 branch :
    - Patch 141: Re-enable notifications
    - Patch 142: Fix Restore size
- Do not package kmobiletool

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-12mdv2009.1
+ Revision: 365926
- Add some upstream patches from branch
        - Patch139: Fix crash ( kolab issue 2979 )
        - Patch140: Knotes: Fix KDE bug 189050

* Thu Apr 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-11mdv2009.1
+ Revision: 365487
- Disable patch102: seems to slow down searches a lot
- Add some upstream patches from branch
        - Patch137: Do not search on ldap when we disable completion
        - Patch138: Fix minor leak (it cleans when we close composer)
- Add some upstream patches from branch
        - Patch133: KAlarm: Use more suitable email icon
        - Patch134: KNode: Backport of r945792 to the 4.2 branch
        - Patch135: KNode: Fix the "cut" action in KNode's composer.
        - Patch136: KNode: Don't let KIO handle authentication for us, nullify the uiDelegate.

* Wed Apr 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-8mdv2009.1
+ Revision: 365221
- Add some upstream patches from branch
    - Patch132: defined smtp as default transport, otherwise we don't see a default smtp

* Wed Apr 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-7mdv2009.1
+ Revision: 365114
- Add patches fro 4.2 branch

* Mon Apr 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-6mdv2009.1
+ Revision: 364557
- Add some upstream patches from branch
    - Patch126: Little fix on kmail destructor ( cosmetic )

* Mon Apr 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-5mdv2009.1
+ Revision: 364474
- Add some upstream patches from branch
        - Patch125: Wizards: don't save passwd in Folder-*

* Mon Apr 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-4mdv2009.1
+ Revision: 364388
- Add some upstream patches from branch
        - Patch119: KAdressBook: Add autofillbackground
        - Patch120: KAdressBook: don't exec proc if we canceled it
        - Patch121: KOrganizer:  Fix potential crash
        - Patch122: KNode: Don't crash on closing an article widget opened by clicking a reference while the article isn't fully loaded yet
        - Patch123: KMail: fix enable/disable actions
        - Patch124: KMail->filters : We must accept html it's html

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-3mdv2009.1
+ Revision: 364124
- There are circumstances under which QtConcurrent::run() may use the calling thread to execute the job, which is unfortunate

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-2mdv2009.1
+ Revision: 364104
- Add some upstream patches from branch
        - Patch100: Code refactoring
        - Patch101: Refresh when we cancel create new script.
        - Patch102: Fix search in Kadressbook when some fields occurs more than once
        - Patch103: Fix kolab issue 2150
        - Patch104: Fix issue kolab 2846
        - Patch105: Automatically remove empty lines in the recipients-editor
        - Patch106: Show the size on the server for IMAP messages
        - Patch107: Put the brightness factor in a constant, and increase the contrast slightly
        - Patch108: Fix crash kolab issue 3312
        - Patch109: Fix plugin loading and/or unloading segfault
        - Patch110: Fix kolab issue 3480
        - Patch111: Sieve doesn't accept empty script
        - Patch112: KOrganizer: don't add empty string
        - Patch113: Let me jump to readonly folders too
        - Patch114: Calculate and show the correct folder size of IMAP folders
        - Patch115: Add focus
        - Patch116: Fix minor mem leak
        - Patch117: Don't try to show a menu when there is not entry
- Remove old tarball

* Sat Mar 28 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-1mdv2009.1
+ Revision: 361810
- Update with 4.2.2 try#1 packages
- Korganizer view fix from branches.
- KDE 4.2.1 try#1 upstream release
- KDE 4.2.1 try#1 upstream release

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - [trunk] Fix column size saving (Bug #48513)
    - Add a Welcome message at first start of KMail
    - Fix Requires

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-2mdv2009.1
+ Revision: 340888
- Rebuild against qt4.5

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-1mdv2009.1
+ Revision: 334694
- Update with official 4.2.0 upstream tarball

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-1mdv2009.1
+ Revision: 327481
- Package doc

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Mon Dec 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-2mdv2009.1
+ Revision: 317397
- Fix back menu desktop entries

* Fri Dec 12 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.85-1mdv2009.1
+ Revision: 313713
- Update with Beta 1 - 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.82-1mdv2009.1
+ Revision: 313410
- Remove unneeded patch
- Update to kde 4.1.82
- Update to kde 4.1.82

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.81-1mdv2009.1
+ Revision: 308634
- versionnate buildrequires
- Update to kde 4.1.81
- Fix File List

  + Anssi Hannula <anssi@mandriva.org>
    - kaddressbook obsoletes kdeaddons-kaddressbook-plugins

* Wed Nov 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-2mdv2009.1
+ Revision: 307155
- Fix obsoletes
- Obsoletes old kde3 packages

  + Funda Wang <fwang@mandriva.org>
    - update url

* Sat Nov 22 2008 Funda Wang <fwang@mandriva.org> 2:4.1.80-1mdv2009.1
+ Revision: 305868
- add kio_news doc
- try parallel build
- kdepim has nothing to do with workspace now

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-1mdv2009.1
+ Revision: 303167
- Update to kde 4.1.73

* Sun Oct 26 2008 Funda Wang <fwang@mandriva.org> 2:4.1.71-3mdv2009.1
+ Revision: 297405
- rebuild for new gnokii

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.71-2mdv2009.1
+ Revision: 297136
- Fix File List (Bug #45299)

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.71-1mdv2009.1
+ Revision: 297094
- New version 4.1.71
- kdepim4 is a metapackage so change Requires into Suggests
- Remove Requires for kdepim4-core in kdepim4 main package

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.70-1mdv2009.1
+ Revision: 295837
- Update to kde 4.1.70
- Update to kde 4.1.70

* Thu Oct 02 2008 Frederic Crozat <fcrozat@mandriva.com> 2:4.1.2-2mdv2009.0
+ Revision: 290838
- Add conflicts to ease upgrade from Mdv 2008.1

* Fri Sep 26 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-1mdv2009.0
+ Revision: 288503
- KDE 4.1.2 arriving.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - [BUGFIX] Fix Requires for Knode (Bug #41138)

* Tue Sep 02 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-1mdv2009.0
+ Revision: 279058
- Disable nie akonadi nepomuk compilation
- Fix file list
- Upgrade to forthcoming 4.1.1 packages

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - ByeBye Ktnef
    - [BUGFIX] Add sasl-plug-plain as Requires of KMail (Bug #42301)
    - Disable build of ktnef
    - Use <= on the versionnate
    - Obsolete Korn as it do not exist anymore on the package

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-3mdv2009.0
+ Revision: 263403
- Added missing files
- Update with current branch 4.1 patches

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Rebuild because of B/S Failure

* Sun Jul 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-1mdv2009.0
+ Revision: 250697
- Fix file list ( Byebye Korn)
- Remove merged patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.0

* Sun Jul 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.98-5mdv2009.0
+ Revision: 239001
- This patch should not have been commited
- [BUGFIX] Fix crash in Akregator when adding a RSS feed (Bug #42111)
- Better packaging pratice use exclude instead of rm -fr (tks helio)

* Sun Jul 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.98-3mdv2009.0
+ Revision: 234389
- Fix conflicts with oxygen pacakge

* Sun Jul 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.98-2mdv2009.0
+ Revision: 234387
- Fix file list
- [BUGFIX] Autostart Kalarm only on KDE (Bug #41884)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.85-2mdv2009.0
+ Revision: 232626
- Fix KOrn menu entry (KDE menu cleaning task )

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.85-1mdv2009.0
+ Revision: 232535
- New version kde 4.0.85
- Do not show Kalarm on the menu (menu cleaning task)

  + Funda Wang <fwang@mandriva.org>
    - add missing epoch when obsoleting

* Mon Jun 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.84-2mdv2009.0
+ Revision: 230416
- Move kaddressbook and korganizer in internet menu
- [BUGFIX] Remove ktnef from menus (Bug #41765)

* Sat Jun 28 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.84-1mdv2009.0
+ Revision: 229606
- Update with new snapshot tarballs 4.0.84

* Tue Jun 24 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.83-5mdv2009.0
+ Revision: 228530
- Updated from recent upstream tarball ( imap code changes )

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Start to fix menu entries
    - Rebuild against fixed rpm

* Sun Jun 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.83-2mdv2009.0
+ Revision: 227843
- [BUGFIX] Fix File list (Bug #41455)

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.83-1mdv2009.0
+ Revision: 227578
- Fixed kontact plugins placement.
- Removed useless package kdepim4-plugins and moved it back to kmail
- Fixed file list
- Update with new snapshot tarballs 4.0.83

  + Funda Wang <fwang@mandriva.org>
    - improve summary and descriptions

* Wed Jun 11 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.82-1mdv2009.0
+ Revision: 218219
- Update with new snapshot tarballs 4.0.82

* Mon Jun 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.81-3mdv2009.0
+ Revision: 217276
- Fix Obsoletes when packages are not built

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jun 04 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.81-2mdv2009.0
+ Revision: 215030
- Filex file list
- Added switch for kmobiletools and kpilot, not enabled in this release
- Update with new snapshot tarballs 4.0.81

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix file list
    - Fix Requires ( reported on cooker ML )

* Sun May 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.80-1mdv2009.0
+ Revision: 211151
- Fix File list
- Add new package Kjots ( was on kdeutils4 before )
  Add 3 new library packages ( %%libkontactinterfaces %%libkcal_groupwise %%libgwsoap and %%libkabc_groupwise
  Remove %%libkpinterfaces library package
- Own %%{_kde_appsdir}/kontactsummary and %%{_kde_appsdir}/kontact
- Own %%{_kde_appsdir}/kpilot
- Own %%{_kde_appsdir}/ktimetracker
- Own %%{_kde_appsdir}/kxforms
- Own %%{_kde_appsdir}/libkleopatra
- Own %%{_kde_appsdir}/akonadi and %%{_kde_appsdir}/akonadiconsole
- own %%{_kde_appsdir}/kcontactmanager

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.74-1mdv2009.0
+ Revision: 208263
- Update to kde 4.0.74
  Remove libkfeed ( will be on its own package)
  Fix File list
- Fix Requires

* Fri May 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.73-2mdv2009.0
+ Revision: 204790
- Update to kde 4.0.73
- Fix conflicts

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.72-2mdv2009.0
+ Revision: 202741
- Fix BuildRequires
- Fix BuildRequires
- Fix File list
- Update to kde 4.0.72
- Add Buildrequire
- Add forgotten build patch
- Fix file list
  Remove libakonadiprivate ( now on its own source package ( akonadi )
- Update to kde4 4.0.70
- New snapshot

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE.

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 26 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.97.1-0.752060.2mdv2008.1
+ Revision: 137824
+ rebuild (emptylog)

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.97.1-0.752060.1mdv2008.1
+ Revision: 137422
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.97.1-0.747029.1mdv2008.1
+ Revision: 117085
- New snapshot

* Fri Nov 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.96.1-0.742825.1mdv2008.1
+ Revision: 114097
- New snapshot

* Fri Nov 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.96.1-0.740266.1mdv2008.1
+ Revision: 111412
- New snapshot

* Sat Nov 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.96.0-0.737116.1mdv2008.1
+ Revision: 109546
- KDE4 Rc1
  Fix file list

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.95.2-0.734816.1mdv2008.1
+ Revision: 107526
- New snapshot

* Sun Nov 04 2007 Funda Wang <fwang@mandriva.org> 2:3.95.1-0.731772.2mdv2008.1
+ Revision: 105844
- Rebuild against new libopensync

* Fri Nov 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.95.1-0.731772.1mdv2008.1
+ Revision: 105417
- Fix file list
- Fix file list
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.94.1-0.730680.1mdv2008.1
+ Revision: 103977
- Fix File list

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.94.1-0.729215.1mdv2008.1
+ Revision: 102198
- Fix File list
- Add back boost-devel
- New snapshot
- Fix conflict

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.94.0-0.726734.2mdv2008.1
+ Revision: 100758
- Fix upgrade

* Fri Oct 19 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.94.0-0.726734.1mdv2008.1
+ Revision: 100209
- Fix Buildrequire
- Fix Buildrequires
- Kde 4 Beta3

  + Funda Wang <fwang@mandriva.org>
    - build agsint opensync 0.33

* Tue Sep 25 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:3.93.0-0.714150.1mdv2008.0
+ Revision: 92916
+ rebuild (emptylog)

* Fri Sep 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.93.0-1mdv2008.0
+ Revision: 91864
- Update snapshot
- Make obsoletes tags versioned
- Add a patch fixing kpilot installation

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with revision 708397
    - Update to revision 698242
    - First working kdepim4 package
    - Update to revision 694342

  + Adam Williamson <awilliamson@mandriva.org>
    - disable libmal buildrequires (mal conduit is disabled upstream)

* Thu May 03 2007 Laurent Montel <lmontel@mandriva.org> 1:3.80.3-0.20070502.5mdv2008.0
+ Revision: 21328
- Fix BR
- New version
- 3.80.3


* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070311.5mdv2007.1
+ Revision: 141267
- new snapshot
- Fix spec file
- new snapshot

* Wed Feb 28 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.3-0.20070228.4mdv2007.1
+ Revision: 126885
- new snapshot
- 3.80.3

* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070215.3mdv2007.1
+ Revision: 121632
- new snapshot
- new snapshot
- Fix spec file
- new snapshot

* Sun Jan 14 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070117.1mdv2007.1
+ Revision: 108638
- Fix group
- Fix bug #28093

* Wed Jan 10 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.1mdv2007.1
+ Revision: 106935
- Update snapshot

* Fri Jan 05 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.6mdv2007.1
+ Revision: 104387
- Fix lib

* Fri Jan 05 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.5mdv2007.1
+ Revision: 104327
- Fix file list (based on patch from neoclust)
  Remove some post and postun empty

* Thu Jan 04 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.4mdv2007.1
+ Revision: 104150
- Fix provides (patch from neoclust)
  Remove old obsolete

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.3mdv2007.1
+ Revision: 103910
- Fix buildrequires
- Fix buildrequires
- Fix spec files
- Import kdepim4

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 3.5.5-4mdv2007.0
- kde4
