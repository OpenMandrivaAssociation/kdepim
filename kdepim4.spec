# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kdepim4
Summary:	An application suite to manage personal information
Version: 4.9.0
Release: 1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://community.kde.org/KDE_PIM
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdepim-%{version}.tar.xz
Patch0:		kdepim-4.8.97-l10n-ru.patch
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	grantlee-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kdepim4-runtime-devel
BuildRequires:	libassuan-devel
BuildRequires:	xsltproc
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
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
Obsoletes:	kpilot < %{EVRD}
Obsoletes:	ktnef < %{EVRD}

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
Conflicts:	kde-l10n-ar < 4.6.3-2
Conflicts:	kde-l10n-bg < 4.6.3-2
Conflicts:	kde-l10n-bn_IN < 4.3.98-4
Conflicts:	kde-l10n-ca < 4.6.3-2
Conflicts:	kde-l10n-cs < 4.6.3-2
Conflicts:	kde-l10n-csb < 4.4.95-7
Conflicts:	kde-l10n-da < 4.6.3-2
Conflicts:	kde-l10n-de < 4.6.3-2
Conflicts:	kde-l10n-el < 4.6.3-2
Conflicts:	kde-l10n-en_GB < 4.6.3-2
Conflicts:	kde-l10n-eo < 4.5.95-6
Conflicts:	kde-l10n-es < 4.6.3-2
Conflicts:	kde-l10n-et < 4.6.3-2
Conflicts:	kde-l10n-eu < 4.6.3-2
Conflicts:	kde-l10n-fa < 4.2.96-5
Conflicts:	kde-l10n-fi < 4.6.3-2
Conflicts:	kde-l10n-fr < 4.6.3-2
Conflicts:	kde-l10n-fy < 4.5.95-6
Conflicts:	kde-l10n-ga < 4.6.3-2
Conflicts:	kde-l10n-gl < 4.6.3-2
Conflicts:	kde-l10n-gu < 4.6.3-2
Conflicts:	kde-l10n-he < 4.6.3-2
Conflicts:	kde-l10n-hi < 4.6.3-2
Conflicts:	kde-l10n-hne < 4.3.98-4
Conflicts:	kde-l10n-hr < 4.6.3-2
Conflicts:	kde-l10n-hu < 4.6.3-2
Conflicts:	kde-l10n-id < 4.6.3-2
Conflicts:	kde-l10n-is < 4.6.3-2
Conflicts:	kde-l10n-it < 4.6.3-2
Conflicts:	kde-l10n-ja < 4.6.3-2
Conflicts:	kde-l10n-kk < 4.6.3-2
Conflicts:	kde-l10n-km < 4.6.3-2
Conflicts:	kde-l10n-kn < 4.6.3-2
Conflicts:	kde-l10n-ko < 4.6.3-2
Conflicts:	kde-l10n-ku < 4.3.2-4
Conflicts:	kde-l10n-lt < 4.6.3-2
Conflicts:	kde-l10n-lv < 4.6.3-2
Conflicts:	kde-l10n-mai < 4.6.3-2
Conflicts:	kde-l10n-mk < 4.4.95-7
Conflicts:	kde-l10n-ml < 4.5.95-6
Conflicts:	kde-l10n-mr < 4.3.98-4
Conflicts:	kde-l10n-nb < 4.6.3-2
Conflicts:	kde-l10n-nds < 4.6.3-2
Conflicts:	kde-l10n-ne < 4.2.96-5
Conflicts:	kde-l10n-nl < 4.6.3-2
Conflicts:	kde-l10n-nn < 4.6.3-2
Conflicts:	kde-l10n-pa < 4.6.3-2
Conflicts:	kde-l10n-pl < 4.6.3-2
Conflicts:	kde-l10n-pt < 4.6.3-2
Conflicts:	kde-l10n-pt_BR < 4.6.3-2
Conflicts:	kde-l10n-ro < 4.6.3-2
Conflicts:	kde-l10n-ru < 4.6.3-4
Conflicts:	kde-l10n-se < 4.2.96-6
Conflicts:	kde-l10n-si < 4.4.95-7
Conflicts:	kde-l10n-sk < 4.6.3-2
Conflicts:	kde-l10n-sl < 4.6.3-2
Conflicts:	kde-l10n-sr < 4.6.3-2
Conflicts:	kde-l10n-sv < 4.6.3-2
Conflicts:	kde-l10n-ta < 4.2.96-5
Conflicts:	kde-l10n-tg < 4.4.95-7
Conflicts:	kde-l10n-th < 4.6.3-2
Conflicts:	kde-l10n-tr < 4.6.3-2
Conflicts:	kde-l10n-uk < 4.6.3-2
Conflicts:	kde-l10n-wa < 4.6.3-2
Conflicts:	kde-l10n-zh_CN < 4.6.3-2
Conflicts:	kde-l10n-zh_TW < 4.6.3-2

%description core
Core files from kdepim.

%files core -f %{name}.lang
%exclude %{_kde_docdir}/HTML/en/*
%{_kde_libdir}/strigi/*
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
Obsoletes:	keventeditor < 2:4.5.68

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
Conflicts:	%{name}-core < 2:4.5.77

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
URL:		http://userbase.kde.org/Akregator
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
URL:		http://userbase.kde.org/KNode
Requires:	%{name}-core = %{EVRD}
Requires:	kdepimlibs4-core
Requires:	kio4-nntp
Provides:	kde4-knode = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

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
URL:		http://userbase.kde.org/KAddressBook
Requires:	%{name}-core = %{EVRD}
# Grantlee is needed for the simple view in kaddressbook
Requires:	grantlee
Requires:	akonadi-common
Provides:	kde4-kaddressbook = %{EVRD}
Conflicts:	kdepim4-core < 2:4.5.77

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
Conflicts:	%{name}-core < 2:4.5.77

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
URL:		http://userbase.kde.org/KAlarm
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kalarm = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

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
URL:		http://community.kde.org/Ktimetracker
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-ktimetracker = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

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
%{_kde_services}/kontact/ktimetracker_plugin.desktop
%{_kde_libdir}/kde4/ktimetrackerpart.so
%{_kde_libdir}/kde4/kcm_ktimetracker.so
%{_kde_libdir}/kde4/kontact_ktimetrackerplugin.so

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
URL:		http://userbase.kde.org/KMail
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
Suggests:	backupmail
Suggests:	importwizard
Provides:	kde4-kmail = %{EVRD}
Provides:	kmail2 = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

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
%{_kde_appsdir}/kmail
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
URL:		http://userbase.kde.org/KMail
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
URL:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kmailcvt = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

%description -n kmailcvt
KDE Mail Import tool

%files -n kmailcvt
%{_kde_bindir}/kmailcvt
%{_kde_appsdir}/kmailcvt/pics/step1.png
%{_kde_iconsdir}/*/*/apps/kmailcvt.*

#-----------------------------------------------------------------------------

%package -n backupmail
Summary:	Backup Mail allows to save all data from kmail and restore them in other system
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n backupmail
Backup Mail allows to save all data from kmail and restore them in
other system.

%files -n backupmail
%{_kde_bindir}/backupmail
%{_kde_appsdir}/backupmail

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

#-----------------------------------------------------------------------------

%package -n knotes
Summary:	Notes for the K Desktop Environment
Group:		Graphical desktop/KDE
URL:		http://userbase.kde.org/KNotes
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-kresources
Requires:	kio4-nntp
Provides:	kde4-knotes = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

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
URL:		http://userbase.kde.org/Kontact
Requires:	%{name}-core = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77
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
URL:		http://userbase.kde.org/KOrganizer
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-kresources
Requires:	kio4-ldap
Suggests:	kincidenceeditor
Provides:	kde4-korganizer = %{EVRD}
Conflicts:	kdepim4-core < 2:4.5.77

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

%package -n kjots
Summary:	KDE note taking utility
Group:		Graphical desktop/KDE
URL:		http://userbase.kde.org/KJots
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kjots = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77

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
Requires:	%{libkdepim} = %{EVRD}
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

%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%{_kde_libdir}/*.so
%{_kde_datadir}/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}
#%patch0 -p1

%build
%cmake_kde4 -DKDEPIM_BUILD_MOBILE=false
%make

%install
%makeinstall_std -C build

%find_lang %{name} --all-name --with-html

