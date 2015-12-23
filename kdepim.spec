Summary:	An application suite to manage personal information
Name:		kdepim
Epoch:		3
Version:	15.12.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kdepim-kleopatra-conf-link-against-i18n.patch
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	grantlee-devel >= 0.4.0
BuildRequires:	libassuan-devel
BuildRequires:	sasl-devel
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5UiTools)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Declarative)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiCalendar)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5AkonadiSearch)
BuildRequires:	cmake(KF5AkonadiServer)
BuildRequires:	cmake(KF5AlarmCalendar)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Blog)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GAPI)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5Gpgmepp)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5Mbox)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Tnef)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WebKit)
BuildRequires:	cmake(KF5XmlRpcClient)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	cmake(KF5Prison) >= 1.2.1
Suggests:	akonadi-common
Suggests:	kleopatra
Suggests:	akregator
Suggests:	kaddressbook
Suggests:	kalarm
Suggests:	kmail
Suggests:	knotes
Suggests:	kontact
Suggests:	korganizer
Suggests:	ksendemail
%rename		kdepim4

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer
	  and kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client

%files

#----------------------------------------------------------------------

%package core
Summary:	Core files for KDE PIM
Group:		Graphical desktop/KDE
Requires:	storageservicemanager = %{EVRD}
Conflicts:	%{_lib}kdepim4 < 3:4.11.0
Conflicts:	%{_lib}kpgp4 < 3:4.11.0
Conflicts:	%{name}-devel < 3:4.11.0
Obsoletes:	akonadi-folderarchive-agent < 3:4.13.0
Obsoletes:	pimactivity < 3:4.13.0
%rename		kdepim4-core
Provides:	kdepim4-core = 3:4.14.3-1

%description core
Core files for KDE PIM.

%files core -f %{name}.lang
%exclude %{_kde5_docdir}/HTML/en/*
%dir %{_qt5_plugindir}/pimcommon
%{_kde5_bindir}/contactprintthemeeditor
%{_kde5_datadir}/kdepimwidgets
%{_sysconfdir}/xdg/kdepim.categories
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_kde5_docdir}/HTML/en/contactthemeeditor
%{_kde5_datadir}/applications/org.kde.storageservicemanager.desktop
%{_kde5_datadir}/knotifications5/storageservicemanager.notifyrc
%{_qt5_plugindir}/designer/kdepimwidgets.so
%{_qt5_plugindir}/designer/pimcommonwidgets.so
%{_qt5_plugindir}/pimcommon/pimcommon_*.so
%{_kde5_datadir}/applications/org.kde.contactprintthemeeditor.desktop
%{_kde5_datadir}/composereditor/composereditorinitialhtml
%{_kde5_iconsdir}/*/*/*/quickview.png
%{_kde5_iconsdir}/*/*/*/quickview.svgz
%{_kde5_iconsdir}/*/*/*/x-mail-distribution-list.png
%{_kde5_datadir}/kconf_update
%{_libdir}/grantlee/5.0/kde_grantlee_plugin.so
%exclude %{_kde5_datadir}/kconf_update/kalarm*

#-----------------------------------------------------------------------------

%package -n akonadiconsole
Summary:	Console that help to debug akonadi
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Conflicts:	kdepim4-core < 2:4.4.2-5

%description -n akonadiconsole
Console that help to debug akonadi.

%files -n akonadiconsole
%{_kde5_bindir}/akonadiconsole
%{_kde5_applicationsdir}/org.kde.akonadiconsole.desktop
%{_kde5_iconsdir}/hicolor/*/apps/akonadiconsole.png

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_archivemail_agent
%{_kde5_bindir}/akonadi_archivemail_agent
%{_kde5_datadir}/akonadi/agents/archivemailagent.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-followupreminder-agent
Summary:	Akonadi followupreminder agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-followupreminder-agent
Akonadi followup reminder agent allows to remind you when an email was not
answered.

%files -n akonadi-followupreminder-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_followupreminder_agent
%{_kde5_bindir}/akonadi_followupreminder_agent
%{_kde5_datadir}/akonadi/agents/followupreminder.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent
%{_kde5_bindir}/akonadi_mailfilter_agent
%{_kde5_datadir}/akonadi/agents/mailfilteragent.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-notes-agent
Summary:	Akonadi notes agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	knotes = %{EVRD}

%description -n akonadi-notes-agent
Akonadi notes agent. It adds notes received via network and handles note
alarm notifications.

%files -n akonadi-notes-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_notes_agent
%{_kde5_bindir}/akonadi_notes_agent
%{_kde5_datadir}/akonadi/agents/notesagent.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_sendlater_agent
%{_kde5_bindir}/akonadi_sendlater_agent
%{_kde5_datadir}/akonadi/agents/sendlateragent.desktop

#-----------------------------------------------------------------------------

%package -n akregator
Summary:	A Feed Reader for KDE
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Akregator
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-akregator = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77
Conflicts:	%{name}-devel < 3:4.11.0

%description -n akregator
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%files -n akregator
%doc %{_kde5_docdir}/HTML/en/akregator
%{_kde5_bindir}/akregator
%{_kde5_bindir}/akregatorstorageexporter
%{_kde5_applicationsdir}/org.kde.akregator.desktop
%{_kde5_datadir}/akregator
%{_kde5_datadir}/knotifications5/akregator.notifyrc
%{_qt5_plugindir}/akregator*
%{_datadir}/appdata/akregator.appdata.xml
%{_datadir}/kxmlgui5/akregator
%{_kde5_datadir}/kservicetypes5/akregator_plugin.desktop
%{_kde5_datadir}/config.kcfg/akregator.kcfg
%{_kde5_iconsdir}/*/*/apps/akregator.*
%{_kde5_iconsdir}/*/*/apps/akregator_empty.*
%{_kde5_services}/kontact/akregatorplugin.desktop
%{_kde5_services}/akregator_*
%{_kde5_services}/feed.protocol
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml

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
%doc %{_kde5_docdir}/HTML/en/blogilo
%{_kde5_bindir}/blogilo
%{_kde5_applicationsdir}/org.kde.blogilo.desktop
%{_datadir}/appdata/blogilo.appdata.xml
%{_kde5_datadir}/config.kcfg/blogilo.kcfg
%{_kde5_iconsdir}/*/*/apps/blogilo.*
%{_kde5_iconsdir}/*/*/actions/format-text-blockquote.*
%{_kde5_iconsdir}/*/*/actions/format-text-code.*
%{_kde5_iconsdir}/*/*/actions/insert-more-mark.*
%{_kde5_iconsdir}/*/*/actions/remove-link.*
%{_kde5_iconsdir}/*/*/actions/upload-media.*

#-----------------------------------------------------------------------------

%package -n headerthemeeditor
Summary:	KMail Header Theme Editor
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}

%description -n headerthemeeditor
KMail Header Theme Editor.

%files -n headerthemeeditor
%doc %{_kde5_docdir}/HTML/en/headerthemeeditor
%{_kde5_bindir}/headerthemeeditor
%{_kde5_applicationsdir}/org.kde.headerthemeeditor.desktop

#-----------------------------------------------------------------------------

%package -n contactthemeeditor
Summary:	KDE Contact Theme Editor
Group:		Graphical desktop/KDE
Requires:	kaddressbook = %{EVRD}

%description -n contactthemeeditor
KDE Contact Theme Editor.

%files -n contactthemeeditor
%doc %{_kde5_docdir}/HTML/en/contactthemeeditor
%{_kde5_bindir}/contactthemeeditor
%{_kde5_applicationsdir}/org.kde.contactthemeeditor.desktop

#-----------------------------------------------------------------------------

%package -n importwizard
Summary:	Import Wizard allows to migrate data from mailer as thunderbird/evolution etc
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}

%description -n importwizard
Import Wizard allows to migrate data from mailer as thunderbird/evolution etc.

%files -n importwizard
%doc %{_kde5_docdir}/HTML/en/importwizard
%{_kde5_bindir}/importwizard
%{_kde5_applicationsdir}/org.kde.importwizard.desktop
%{_kde5_datadir}/importwizard
%{_kde5_iconsdir}/*/*/apps/kontact-import-wizard.*

#-----------------------------------------------------------------------------

%package -n kaddressbook
Summary:	The KDE addressbook application
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAddressBook
Requires:	%{name}-core = %{EVRD}
# Grantlee is needed for the simple view in kaddressbook
Requires:	grantlee
Requires:	akonadi-common
Suggests:	contactthemeeditor = %{EVRD}
Provides:	kde4-kaddressbook = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%{_kde5_bindir}/kaddressbook
%{_kde5_applicationsdir}/org.kde.kaddressbook.desktop
%{_kde5_datadir}/kaddressbook
%{_sysconfdir}/xdg/kaddressbook_themes.knsrc
%{_qt5_plugindir}/kcm_ldap.so
%{_kde5_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_kde5_iconsdir}/*/*/apps/kaddressbook.*
%{_kde5_services}/kaddressbookpart.desktop
%{_kde5_services}/kontact/kaddressbookplugin.desktop
%{_kde5_services}/kcmldap.desktop
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_qt5_plugindir}/kaddressbookpart.so
%{_kde5_datadir}/appdata/kaddressbook.appdata.xml
%{_kde5_datadir}/kxmlgui5/kaddressbook
%{_kde5_datadir}/applications/kaddressbook-importer.desktop

#-----------------------------------------------------------------------------

%package -n kalarm
Summary:	A personal alarm message, command and email scheduler
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAlarm
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kalarm = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kalarm
KAlarm is a personal alarm message, command and email scheduler. It lets you
set up personal alarm messages which pop up on the screen at the chosen time,
or you can schedule commands to be executed or emails to be sent.

%files -n kalarm
%doc %{_kde5_docdir}/HTML/en/kalarm
%{_kde5_bindir}/kalarm
%{_kde5_bindir}/kalarmautostart
%{_kde5_libexecdir}/kalarm_helper
%{_sysconfdir}/xdg/autostart/kalarm.autostart.desktop
%{_kde5_applicationsdir}/org.kde.kalarm.desktop
%{_kde5_datadir}/kalarm
%{_kde5_datadir}/kconf_update/kalarm-1.2.1-general.pl
%{_kde5_datadir}/kconf_update/kalarm-1.9.5-defaults.pl
%{_kde5_datadir}/kconf_update/kalarm-2.0.2-general.pl
%{_kde5_datadir}/kconf_update/kalarm-2.1.5-general.pl
%{_kde5_datadir}/kconf_update/kalarm-version.pl
%{_kde5_datadir}/kconf_update/kalarm.upd
%{_kde5_datadir}/kconf_update/kalarm-*-kickoff.sh
%{_kde5_datadir}/config.kcfg/kalarmconfig.kcfg
%{_kde5_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_kde5_iconsdir}/*/*/apps/kalarm.*
%{_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_kde5_datadir}/appdata/kalarm.appdata.xml
%{_kde5_datadir}/kxmlgui5/kalarm

#---------------------------------------------------------------------------

%package -n kincidenceeditor
Summary:	kincidenceeditor
Group:		Graphical desktop/KDE

%description -n kincidenceeditor
New incidince editor.

%files -n kincidenceeditor
%{_kde5_bindir}/kincidenceeditor

#-----------------------------------------------------------------------------

%package -n kleopatra
Summary:	KDE Certificate Manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kleopatra = %{EVRD}

%description -n kleopatra
KDE Certificate Manager.

%files -n kleopatra
%doc %{_kde5_docdir}/HTML/en/kleopatra
%doc %{_kde5_docdir}/HTML/en/kwatchgnupg
%{_sysconfdir}/xdg/libkleopatrarc
%{_kde5_bindir}/kleopatra
%{_kde5_bindir}/kwatchgnupg
%{_kde5_applicationsdir}/org.kde.kleopatra.desktop
%{_kde5_applicationsdir}/kleopatra_import.desktop
%{_kde5_datadir}/kleopatra
%{_kde5_datadir}/libkleopatra
%{_kde5_datadir}/kwatchgnupg
%{_kde5_iconsdir}/*/*/apps/kleopatra.*
%{_kde5_services}/kleopatra_*
%{_qt5_plugindir}/kcm_kleopatra.so
%{_kde5_datadir}/appdata/kleopatra.appdata.xml

#-----------------------------------------------------------------------------

%package -n kmail
Summary:	KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Requires:	kdepimlibs-core
Requires:	sasl-plug-plain
Requires:	sasl-plug-ntlm
Requires:	sasl-plug-login
Requires:	sasl-plug-digestmd5
Requires:	kio-pop3
Requires:	kio-smtp
Requires:	kio-mbox
Requires:	kio-imap
Requires:	kio-sieve
Requires:	akonadi-archivemail-agent = %{EVRD}
Requires:	akonadi-followupreminder-agent = %{EVRD}
Requires:	akonadi-mailfilter-agent = %{EVRD}
Requires:	akonadi-sendlater-agent = %{EVRD}
Requires:	headerthemeeditor = %{EVRD}
Requires:	messageviewer = %{EVRD}
Suggests:	kaddressbook = %{EVRD}
Suggests:	pinentry-qt4
Suggests:	openssh-askpass-qt4
Suggests:	pimsettingexporter
Suggests:	importwizard
Suggests:	mboximporter
Suggests:	sieveeditor
Provides:	kde4-kmail = %{EVRD}
Provides:	kmail2 = %{EVRD}
Conflicts:	kmail-common < 3:4.11.0
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kmail
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -n kmail
%doc %{_kde5_docdir}/HTML/en/kmail
%{_kde5_bindir}/kmail
%{_sysconfdir}/xdg/kmail.*
%{_sysconfdir}/xdg/ksieve_script.knsrc
%{_kde5_applicationsdir}/kmail_view.desktop
%{_kde5_datadir}/kmail2
%{_kde5_datadir}/kxmlgui5/kmail2
%{_kde5_datadir}/sieve
%{_kde5_datadir}/messagelist
%{_kde5_datadir}/knotifications5/kmail2.notifyrc
%{_kde5_datadir}/applications/org.kde.kmail.desktop
%{_kde5_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kde5_datadir}/config.kcfg/kmail.kcfg
%{_kde5_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kde5_datadir}/knotifications5/akonadi_archivemail_agent.notifyrc
%{_kde5_datadir}/knotifications5/akonadi_mailfilter_agent.notifyrc
%{_kde5_datadir}/knotifications5/akonadi_followupreminder_agent.notifyrc
%{_kde5_datadir}/knotifications5/akonadi_sendlater_agent.notifyrc
%{_kde5_iconsdir}/*/*/apps/kmail.*
%{_kde5_services}/kontact/kmailplugin.desktop
%{_kde5_services}/kmail_config_accounts.desktop
%{_kde5_services}/kmail_config_appearance.desktop
%{_kde5_services}/kmail_config_composer.desktop
%{_kde5_services}/kmail_config_identity.desktop
%{_kde5_services}/kmail_config_misc.desktop
%{_kde5_services}/kmail_config_security.desktop
%{_kde5_services}/kcmkmailsummary.desktop
%{_kde5_services}/kcm_kpimidentities.desktop
%{_kde5_services}/ServiceMenus/kmail_addattachmentservicemenu.desktop
%{_qt5_plugindir}/kcm_kmail.so
%{_qt5_plugindir}/kcm_kpimidentities.so
%{_qt5_plugindir}/kcm_kmailsummary.so
%{_qt5_plugindir}/kmailpart.so
%{_qt5_plugindir}/designer/mailcommonwidgets.so
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmail.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
%{_kde5_datadir}/appdata/org.kde.kmail.appdata.xml
%{_kde5_datadir}/kservicetypes5/dbusmail.desktop

#------------------------------------------------------------------------------

%package accountwizard
Summary: kincidenceeditor
Group: Graphical desktop/KDE

%description accountwizard
New incidence editors

%files accountwizard
%{_kde5_bindir}/accountwizard
%{_kde5_bindir}/ispdb
%{_sysconfdir}/xdg/accountwizard.knsrc
%{_qt5_plugindir}/accountwizard_plugin.so
%{_kde5_datadir}/akonadi/accountwizard
%{_kde5_datadir}/mime/packages/accountwizard-mime.xml
%{_kde5_datadir}/applications/org.kde.accountwizard.desktop

#-----------------------------------------------------------------------------

%package -n knotes
Summary:	Notes for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNotes
Requires:	%{name}-core = %{EVRD}
Requires:	akonadi-notes-agent = %{EVRD}
Requires:	kio-nntp
Provides:	kde4-knotes = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%doc %{_kde5_docdir}/HTML/en/knotes
%{_kde5_bindir}/knotes
%{_sysconfdir}/xdg/knotes_printing_theme.knsrc
%{_kde5_applicationsdir}/org.kde.knotes.desktop
%{_kde5_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_kde5_datadir}/knotes
%{_kde5_datadir}/kxmlgui5/knotes
%{_kde5_iconsdir}/*/*/apps/knotes.*
%{_kde5_iconsdir}/*/*/actions/knotes_*
%{_kde5_services}/kcmknotessummary.desktop
%{_kde5_services}/kontact/knotesplugin.desktop
%{_kde5_services}/knote_config_action.desktop
%{_kde5_services}/knote_config_collection.desktop
%{_kde5_services}/knote_config_display.desktop
%{_kde5_services}/knote_config_editor.desktop
%{_kde5_services}/knote_config_misc.desktop
%{_kde5_services}/knote_config_network.desktop
%{_kde5_services}/knote_config_print.desktop
%{_qt5_plugindir}/kcm_knote.so
%{_qt5_plugindir}/kcm_knotessummary.so
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_kde5_datadir}/appdata/knotes.appdata.xml
%{_kde5_datadir}/knotifications5/akonadi_notes_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n kontact
Summary:	Kontact Container
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Kontact
Requires:	%{name}-core = %{EVRD}
Requires:	kio-ldap
Provides:	kde4-kontact = %{EVRD}
Suggests:	akregator
Suggests:	kmail
Suggests:	knotes
Suggests:	kalarm
Suggests:	kaddressbook
Suggests:	korganizer
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kontact
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -n kontact
%doc %{_kde5_docdir}/HTML/en/kontact
%doc %{_kde5_docdir}/HTML/en/kontact-admin
%{_kde5_bindir}/kontact
%{_kde5_datadir}/kontact
%{_kde5_applicationsdir}/org.kde.kontact.desktop
%{_kde5_applicationsdir}/kontact-admin.desktop
%{_kde5_datadir}/config.kcfg/kontact.kcfg
%{_kde5_iconsdir}/*/*/apps/kontact.*
%{_kde5_services}/kontactconfig.desktop
%{_kde5_services}/kcmapptsummary.desktop
%{_kde5_services}/kcmkontactsummary.desktop
%{_kde5_services}/kcmsdsummary.desktop
%{_kde5_services}/kontact/summaryplugin.desktop
%{_kde5_services}/kontact/specialdatesplugin.desktop
%{_qt5_plugindir}/kcm_apptsummary.so
%{_qt5_plugindir}/kcm_kontact.so
%{_qt5_plugindir}/kcm_kontactsummary.so
%{_qt5_plugindir}/kcm_sdsummary.so
%{_qt5_plugindir}/kontact_*
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_kde5_datadir}/appdata/Kontact.appdata.xml
%{_kde5_datadir}/kxmlgui5/kontact
%{_kde5_datadir}/kxmlgui5/kontactsummary

#-----------------------------------------------------------------------------

%package -n korganizer
Summary:	Calendar and scheduling component
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KOrganizer
Requires:	%{name}-core = %{EVRD}
Requires:	kio-ldap
Suggests:	kincidenceeditor
Provides:	kde4-korganizer = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n korganizer
KOrganizer provides management of events and tasks, alarm notification,
web export, network transparent handling of data, group scheduling,
import and export of calendar files and more. It is able to work together
with a wide variety of groupware servers, for example Kolab, Open-Xchange,
Citadel or OpenGroupware.org.

%files -n korganizer
%doc %{_kde5_docdir}/HTML/en/korganizer
%doc %{_kde5_docdir}/HTML/en/konsolecalendar

%{_kde5_bindir}/calendarjanitor
%{_kde5_bindir}/ical2vcal
%{_kde5_bindir}/konsolekalendar
%{_kde5_bindir}/korgac
%{_kde5_bindir}/korganizer
%{_kde5_applicationsdir}/konsolekalendar.desktop
%{_kde5_applicationsdir}/korganizer-import.desktop
%{_kde5_applicationsdir}/org.kde.korganizer.desktop
%{_sysconfdir}/xdg/korganizer.knsrc
%{_kde5_datadir}/korgac
%{_kde5_datadir}/korganizer
%{_kde5_iconsdir}/*/*/apps/konsolekalendar.*
%{_kde5_iconsdir}/*/*/apps/korganizer.*
%{_kde5_iconsdir}/*/*/actions/checkmark.*
%{_kde5_iconsdir}/*/*/actions/smallclock.*
%{_kde5_iconsdir}/*/*/actions/upindicator.*
%{_kde5_iconsdir}/*/*/apps/korg-journal.*
%{_kde5_iconsdir}/*/*/apps/korg-todo.*
%{_kde5_datadir}/config.kcfg/korganizer.kcfg
%{_kde5_services}/kontact/korganizerplugin.desktop
%{_kde5_services}/kontact/todoplugin.desktop
%{_kde5_services}/kcmtodosummary.desktop
%{_kde5_services}/kontact/journalplugin.desktop
%{_kde5_services}/korganizer*
%{_kde5_services}/webcal.protocol
%{_sysconfdir}/xdg/autostart/org.kde.korgac.desktop
%{_qt5_plugindir}/kcm_todosummary.so
%{_qt5_plugindir}/kcm_korganizer.so
%{_qt5_plugindir}/korganizerpart.so
%{_qt5_plugindir}/korg_*
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_kde5_datadir}/appdata/korganizer.appdata.xml
%{_kde5_datadir}/kxmlgui5/korganizer
%{_kde5_datadir}/kservicetypes5/calendardecoration.desktop
%{_kde5_datadir}/kservicetypes5/calendarplugin.desktop
%{_kde5_datadir}/kservicetypes5/dbuscalendar.desktop

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
%doc %{_kde5_docdir}/HTML/en/ktnef
%{_kde5_bindir}/ktnef
%{_kde5_applicationsdir}/org.kde.ktnef.desktop
%{_kde5_iconsdir}/*/*/apps/ktnef*.*
%{_kde5_iconsdir}/*/*/actions/ktnef*.*

#-----------------------------------------------------------------------------

%package -n mboximporter
Summary:	MBoxImporter allows to migrate data from MBox
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n mboximporter
MBoxImporter allows to migrate data from MBox.

%files -n mboximporter
%{_kde5_bindir}/mboximporter
%{_kde5_applicationsdir}/org.kde.mboximporter.desktop

#-----------------------------------------------------------------------------

%package -n messageviewer
Summary:	Message viewer for KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Conflicts:	akonadi-mailfilter-agent < 3:4.11.0
Conflicts:	kmail-common < 3:4.11.0
Obsoletes:	kmail-common < 3:4.11.0

%description -n messageviewer
Message viewer for KDE Email Client.

%files -n messageviewer
%dir %{_qt5_plugindir}/messageviewer
%{_kde5_datadir}/libmessageviewer
%{_kde5_datadir}/messageviewer
%{_kde5_datadir}/knotifications5/messageviewer.notifyrc
%{_qt5_plugindir}/grantlee/5.0/grantlee_messageheaderfilters.so
%{_qt5_plugindir}/messageviewer/messageviewer_*.so
%{_sysconfdir}/xdg/messageviewer_header_themes.knsrc

#-----------------------------------------------------------------------------

%define pimsettingexporterprivate_major 5
%define libpimsettingexporterprivate %mklibname pimsettingexporterprivate %{pimsettingexporterprivate_major}

%package -n %{libpimsettingexporterprivate}
Summary:        KDE 5 library
Group:          System/Libraries

%description -n %{libpimsettingexporterprivate}
KDE 5 library for korganizer-Mobile.

%files -n %{libpimsettingexporterprivate}
%{_kde5_libdir}/libpimsettingexporterprivate.so.%{pimsettingexporterprivate_major}*

#-----------------------------------------------------------------------------

%package -n pimsettingexporter
Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}
Obsoletes:	backupmail < 3:4.10.0
Requires:	%{mklibname pimsettingexporterprivate 5}

%description -n pimsettingexporter
Allows to save data from KDE PIM applications and restore them in other
systems. Successor of Backup Mail from KDE.9.

%files -n pimsettingexporter
%doc %{_kde5_docdir}/HTML/en/pimsettingexporter
%{_kde5_bindir}/pimsettingexporter
%{_kde5_bindir}/pimsettingexporterconsole
%{_kde5_datadir}/applications/org.kde.pimsettingexporter.desktop
#-----------------------------------------------------------------------------

%package -n sieveeditor
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n sieveeditor
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n sieveeditor
%doc %{_kde5_docdir}/HTML/en/sieveeditor
%{_kde5_bindir}/sieveeditor
%{_kde5_applicationsdir}/org.kde.sieveeditor.desktop

#-----------------------------------------------------------------------------

%package -n storageservicemanager
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n storageservicemanager
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n storageservicemanager
%{_kde5_bindir}/storageservicemanager
%{_kde5_iconsdir}/*/*/apps/kdepim-dropbox.*

#-----------------------------------------------------------------------------

%define akregatorinterfaces_major 5
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE library.

%files -n %{libakregatorinterfaces}
%{_kde5_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#-----------------------------------------------------------------------------
%define akregatorprivate_major 5
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE library.

%files -n %{libakregatorprivate}
%{_kde5_libdir}/libakregatorprivate.so.%{akregatorprivate_major}*

#------------------------------------------------------------------------------

%define KF5CalendarSupport_major 5
%define libKF5CalendarSupport %mklibname KF5CalendarSupport %{KF5CalendarSupport_major}

%package -n %{libKF5CalendarSupport}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname calendarsupportcollectionpage 5.0.3.0} < 3:5.12.0
Provides:	%{mklibname calendarsupportcollectionpage 5.0.3.0} = 3:5.12.0
Obsoletes:	%{mklibname calendarsupport 5} < 3:5.12.0
Provides:	%{mklibname calendarsupport 5} = 3:5.12.0

%description -n %{libKF5CalendarSupport}
KDE library for korganizer-Mobile.

%files -n %{libKF5CalendarSupport}
%{_kde5_libdir}/libKF5CalendarSupport.so.%{KF5CalendarSupport_major}*

#-----------------------------------------------------------------------------
%define KF5ComposerEditorNG_major 5
%define libKF5ComposerEditorNG %mklibname KF5ComposerEditorNG %{KF5ComposerEditorNG_major}

%package -n %{libKF5ComposerEditorNG}
Summary:	Library providing autospell checking
Group:		System/Libraries
Obsoletes:	%{mklibname composereditorng 5} < 3:5.12.0
Provides:	%{mklibname composereditorng 5} = 3:5.12.0

%description -n %{libKF5ComposerEditorNG}
This library provides autospell checking.

%files -n %{libKF5ComposerEditorNG}
%{_kde5_libdir}/libKF5ComposerEditorNG.so.%{KF5ComposerEditorNG_major}*

#-----------------------------------------------------------------------------

%define KF5EventViews_major 5
%define libKF5EventViews %mklibname KF5EventViews %{KF5EventViews_major}

%package -n %{libKF5EventViews}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname eventviews 5} < 3:5.12.0
Provides:	%{mklibname eventviews 5} = 3:5.12.0

%description -n %{libKF5EventViews}
KDE library.

%files -n %{libKF5EventViews}
%{_kde5_libdir}/libKF5EventViews.so.%{KF5EventViews_major}*

#-----------------------------------------------------------------------------

%define KF5FollowupReminder_major 5
%define libKF5FollowupReminder %mklibname KF5FollowupReminder %{KF5FollowupReminder_major}

%package -n %{libKF5FollowupReminder}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname followupreminder 5} < 3:5.12.0
Provides:	%{mklibname followupreminder 5} = 3:5.12.0

%description -n %{libKF5FollowupReminder}
KDE library.

%files -n %{libKF5FollowupReminder}
%{_kde5_libdir}/libKF5FollowupReminder.so.%{KF5FollowupReminder_major}*

#-----------------------------------------------------------------------------

%define KF5GrantleeTheme_major 5
%define libKF5GrantleeTheme %mklibname KF5GrantleeTheme %{KF5GrantleeTheme_major}

%package -n %{libKF5GrantleeTheme}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname grantletheme 5} < 3:5.12.0
Provides:	%{mklibname grantletheme 5} = 3:5.12.0

%description -n %{libKF5GrantleeTheme}
KDE library.

%files -n %{libKF5GrantleeTheme}
%{_kde5_libdir}/libKF5GrantleeTheme.so.%{KF5GrantleeTheme_major}*

#-----------------------------------------------------------------------------

%define KF5KF5Gravatar_major 5
%define libKF5KF5Gravatar %mklibname KF5Gravatar %{KF5Gravatar_major}

%package -n %{libKF5Gravatar}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libKF5Gravatar}
KDE library.

%files -n %{libKF5Gravatar}
%{_kde5_libdir}/libKF5Gravatar.so.%{KF5Gravatar_major}*

#-----------------------------------------------------------------------------

%define KF5IncidenceEditorsng_major 5
%define libKF5IncidenceEditorsng %mklibname KF5IncidenceEditorsng %{KF5IncidenceEditorsng_major}

%package -n %{libKF5IncidenceEditorsng}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{_lib}incidenceeditors4 < 2:4.5.68
Obsoletes:	%{mklibname incidenceeditorsng 5} < 3:5.12.0
Provides:	%{mklibname incidenceeditorsng 5} = 3:5.12.0
Obsoletes:	%{mklibname incidenceeditorssngmobile 5} < 3:5.12.0
Provides:	%{mklibname incidenceeditorssngmobile 5} = 3:5.12.0

%description -n %{libKF5IncidenceEditorsng}
KDE library.

%files -n %{libKF5IncidenceEditorsng}
%{_kde5_libdir}/libKF5IncidenceEditorsng.so.%{KF5IncidenceEditorsng_major}*

#-----------------------------------------------------------------------------

%define KF5KaddressbookGrantlee_major 5
%define libKF5KaddressbookGrantlee %mklibname KF5KaddressbookGrantlee %{KF5KaddressbookGrantlee_major}

%package -n %{libKF5KaddressbookGrantlee}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname kaddressbookgrantlee 5} < 3:5.12.0
Provides:	%{mklibname kaddressbookgrantlee 5} = 3:5.12.0

%description -n %{libKF5KaddressbookGrantlee}
KDE library.

%files -n %{libKF5KaddressbookGrantlee}
%{_kde5_libdir}/libKF5KaddressbookGrantlee.so.%{KF5KaddressbookGrantlee_major}*

#-----------------------------------------------------------------------------

%define KF5KDGantt2_major 5
%define libKF5KDGantt2 %mklibname KF5KDGantt2 _%{KF5KDGantt2_major}

%package -n %{libKF5KDGantt2}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname kdgantt2 1} < 3:5.12.0
Provides:	%{mklibname kdgantt2 1} = 3:5.12.0

%description -n %{libKF5KDGantt2}
KDE library.

%files -n %{libKF5KDGantt2}
%{_kde5_libdir}/libKF5KDGantt2.so.%{KF5KDGantt2_major}*

#-----------------------------------------------------------------------------

%define KF5KManageSieve_major 5
%define libKF5KManageSieve %mklibname KF5KManageSieve %{KF5KManageSieve_major}

%package -n %{libKF5KManageSieve}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname managesieve 5} < 3:5.12.0
Provides:	%{mklibname managesieve 5} = 3:5.12.0

%description -n %{libKF5KManageSieve}
KDE library.

%files -n %{libKF5KManageSieve}
%{_kde5_libdir}/libKF5KManageSieve.so.%{KF5KManageSieve_major}*

#-----------------------------------------------------------------------------

%define KF5KSieve_major 5
%define libKF5KSieve %mklibname KF5KSieve %{KF5KSieve_major}

%package -n %{libKF5KSieve}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname ksieve 5} < 3:5.12.0
Provides:	%{mklibname ksieve 5} = 3:5.12.0

%description -n %{libKF5KSieve}
KDE library.

%files -n %{libKF5KSieve}
%{_kde5_libdir}/libKF5KSieve.so.%{KF5KSieve_major}*

#-----------------------------------------------------------------------------

%define KF5KSieveUi_major 5
%define libKF5KSieveUi %mklibname KF5KSieveUi %{KF5KSieveUi_major}

%package -n %{libKF5KSieveUi}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname ksieveui 5} < 3:5.12.0
Provides:	%{mklibname ksieveui 5} = 3:5.12.0

%description -n %{libKF5KSieveUi}
KDE library.

%files -n %{libKF5KSieveUi}
%{_kde5_libdir}/libKF5KSieveUi.so.%{KF5KSieveUi_major}*

#-----------------------------------------------------------------------------

%define KF5KaddressbookGrantlee_major 5
%define libKF5KaddressbookGrantlee %mklibname KF5KaddressbookGrantlee %{KF5KaddressbookGrantlee_major}

%package -n %{libKF5KaddressbookGrantlee}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libKF5KaddressbookGrantlee}
KDE library.

%files -n %{libKF5KaddressbookGrantlee}
%{_kde5_libdir}/libKF5KaddressbookGrantlee.so.%{KF5KaddressbookGrantlee_major}*

#-----------------------------------------------------------------------------

%define KF5KdepimDBusInterfaces_major 5
%define libKF5KdepimDBusInterfaces %mklibname KF5KdepimDBusInterfaces %{KF5KdepimDBusInterfaces_major}

%package -n %{libKF5KdepimDBusInterfaces}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname kdepimdbusinterfaces 5} < 3:5.12.0
Provides:	%{mklibname kdepimdbusinterfaces 5} = 3:5.12.0

%description -n %{libKF5KdepimDBusInterfaces}
KDE library.

%files -n %{libKF5KdepimDBusInterfaces}
%{_kde5_libdir}/libKF5KdepimDBusInterfaces.so.%{KF5KdepimDBusInterfaces_major}*

#-----------------------------------------------------------------------------

%define KF5Libkdepim_major 5
%define libKF5Libkdepim %mklibname KF5Libkdepim %{KF5Libkdepim_major}

%package -n %{libKF5Libkdepim}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname kdepim 5} < 3:5.12.0
Provides:	%{mklibname kdepim 5} = 3:5.12.0

%description -n %{libKF5Libkdepim}
KDE library.

%files -n %{libKF5Libkdepim}
%{_kde5_libdir}/libKF5Libkdepim.so.%{KF5Libkdepim_major}*

#-----------------------------------------------------------------------------

%define KF5Libkleo_major 5
%define libKF5Libkleo %mklibname KF5Libkleo %{KF5Libkleo_major}

%package -n %{libKF5Libkleo}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname kleo 5} < 3:5.12.0
Provides:	%{mklibname kleo 5} = 3:5.12.0
Obsoletes:	%{mklibname kpgp 5} < 3:5.12.0
Provides:	%{mklibname kpgp 5} = 3:5.12.0

%description -n %{libKF5Libkleo}
KDE library.

%files -n %{libKF5Libkleo}
%{_kde5_libdir}/libKF5Libkleo.so.%{KF5Libkleo_major}*

#-----------------------------------------------------------------------------

%define KF5MailCommon_major 5
%define libKF5MailCommon %mklibname KF5MailCommon %{KF5MailCommon_major}

%package -n %{libKF5MailCommon}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname mailcommon 5} < 3:5.12.0
Provides:	%{mklibname mailcommon 5} = 3:5.12.0

%description -n %{libKF5MailCommon}
KDE library.

%files -n %{libKF5MailCommon}
%{_kde5_libdir}/libKF5MailCommon.so.%{KF5MailCommon_major}*

#-----------------------------------------------------------------------------

%define KF5MailImporter_major 5
%define libKF5MailImporter %mklibname KF5MailImporter %{KF5MailImporter_major}

%package -n %{libKF5MailImporter}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname mailimporter 5} < 3:5.12.0
Provides:	%{mklibname mailimporter 5} = 3:5.12.0

%description -n %{libKF5MailImporter}
KDE library.

%files -n %{libKF5MailImporter}
%{_kde5_libdir}/libKF5MailImporter.so.%{KF5MailImporter_major}*

#-----------------------------------------------------------------------------

%define KF5MessageComposer_major 5
%define libKF5MessageComposer %mklibname KF5MessageComposer %{KF5MessageComposer_major}

%package -n %{libKF5MessageComposer}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname messagecomposer 5} < 3:5.12.0
Provides:	%{mklibname messagecomposer 5} = 3:5.12.0

%description -n %{libKF5MessageComposer}
KDE library.

%files -n %{libKF5MessageComposer}
%{_kde5_libdir}/libKF5MessageComposer.so.%{KF5MessageComposer_major}*

#-----------------------------------------------------------------------------

%define KF5MessageCore_major 5
%define libKF5MessageCore %mklibname KF5MessageCore %{KF5MessageCore_major}

%package -n %{libKF5MessageCore}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname messagecore 5} < 3:5.12.0
Provides:	%{mklibname messagecore 5} = 3:5.12.0

%description -n %{libKF5MessageCore}
KDE library.

%files -n %{libKF5MessageCore}
%{_kde5_libdir}/libKF5MessageCore.so.%{KF5MessageCore_major}*

#-----------------------------------------------------------------------------

%define KF5MessageList_major 5
%define libKF5MessageList %mklibname KF5MessageList %{KF5MessageList_major}

%package -n %{libKF5MessageList}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname messagelist 5} < 3:5.12.0
Provides:	%{mklibname messagelist 5} = 3:5.12.0

%description -n %{libKF5MessageList}
KDE library.

%files -n %{libKF5MessageList}
%{_kde5_libdir}/libKF5MessageList.so.%{KF5MessageList_major}*

#-----------------------------------------------------------------------------

%define KF5MessageViewer_major 5
%define libKF5MessageViewer %mklibname KF5MessageViewer %{KF5MessageViewer_major}

%package -n %{libKF5MessageViewer}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname messageviewer 5} < 3:5.12.0
Provides:	%{mklibname messageviewer 5} = 3:5.12.0

%description -n %{libKF5MessageViewer}
KDE library.

%files -n %{libKF5MessageViewer}
%{_kde5_libdir}/libKF5MessageViewer.so.%{KF5MessageViewer_major}*

#-----------------------------------------------------------------------------

%define KF5NoteShared_major 5
%define libKF5NoteShared %mklibname KF5NoteShared %{KF5NoteShared_major}

%package -n %{libKF5NoteShared}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname noteshared 5} < 3:5.12.0
Provides:	%{mklibname noteshared 5} = 3:5.12.0

%description -n %{libKF5NoteShared}
KDE library.

%files -n %{libKF5NoteShared}
%{_kde5_libdir}/libKF5NoteShared.so.%{KF5NoteShared_major}*

#-----------------------------------------------------------------------------

%define KF5PimCommon_major 5
%define libKF5PimCommon %mklibname KF5PimCommon %{KF5PimCommon_major}

%package -n %{libKF5PimCommon}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname pimcommon 5} < 3:5.12.0
Provides:	%{mklibname pimcommon 5} = 3:5.12.0

%description -n %{libKF5PimCommon}
KDE library.

%files -n %{libKF5PimCommon}
%{_kde5_libdir}/libKF5PimCommon.so.%{KF5PimCommon_major}*

#-----------------------------------------------------------------------------

%define KF5SendLater_major 5
%define libKF5SendLater %mklibname KF5SendLater %{KF5SendLater_major}

%package -n %{libKF5SendLater}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname sendlater 5} < 3:5.12.0
Provides:	%{mklibname sendlater 5} = 3:5.12.0

%description -n %{libKF5SendLater}
KDE library.

%files -n %{libKF5SendLater}
%{_kde5_libdir}/libKF5SendLater.so.%{KF5SendLater_major}*

#-----------------------------------------------------------------------------

%define KF5TemplateParser_major 5
%define libKF5TemplateParser %mklibname KF5TemplateParser %{KF5TemplateParser_major}

%package -n %{libKF5TemplateParser}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{mklibname templateparser 5} < 3:5.12.0
Provides:	%{mklibname templateparser 5} = 3:5.12.0

%description -n %{libKF5TemplateParser}
KDE library.

%files -n %{libKF5TemplateParser}
%{_kde5_libdir}/libKF5TemplateParser.so.%{KF5TemplateParser_major}*

#-----------------------------------------------------------------------------

%define kaddressbookprivate_major 5
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %{libkaddressbookprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkaddressbookprivate}
KDE library.

%files -n %{libkaddressbookprivate}
%{_kde5_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*

#-----------------------------------------------------------------------------

%define kmailprivate_major 5
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %{libkmailprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkmailprivate}
KDE library.

%files -n %{libkmailprivate}
%{_kde5_libdir}/libkmailprivate.so.%{kmailprivate_major}*

#-----------------------------------------------------------------------------

%define knotesprivate_major 5
%define libknotesprivate %mklibname knotesprivate %{knotesprivate_major}

%package -n %{libknotesprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libknotesprivate}
KDE library.

%files -n %{libknotesprivate}
%{_kde5_libdir}/libknotesprivate.so.%{knotesprivate_major}*

#-----------------------------------------------------------------------------

%define kontactprivate_major 5
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %{libkontactprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE library.

%files -n %{libkontactprivate}
%{_kde5_libdir}/libkontactprivate.so.%{kontactprivate_major}*

#-----------------------------------------------------------------------------

%define korganizer_core_major 5
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE library.

%files -n %{libkorganizer_core}
%{_kde5_libdir}/libkorganizer_core.so.%{korganizer_core_major}*

#-----------------------------------------------------------------------------

%define korganizer_interfaces_major 5
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE library.

%files -n %{libkorganizer_interfaces}
%{_kde5_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#-----------------------------------------------------------------------------

%define korganizerprivate_major 5
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %{libkorganizerprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizerprivate}
KDE library.

%files -n %{libkorganizerprivate}
%{_kde5_libdir}/libkorganizerprivate.so.%{korganizerprivate_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientcore_major 1
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %{libkleopatraclientcore}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientcore4 <= 2:4.5

%description -n %{libkleopatraclientcore}
KDE library.

%files -n %{libkleopatraclientcore}
%{_kde5_libdir}/libkleopatraclientcore.so.%{kleopatraclientcore_major}*

#-----------------------------------------------------------------------------
%define kleopatraclientgui_major 1
%define libkleopatraclientgui %mklibname kleopatraclientgui %{kleopatraclientgui_major}

%package -n %{libkleopatraclientgui}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientgui4 <= 2:4.5

%description -n %{libkleopatraclientgui}
KDE library.

%files -n %{libkleopatraclientgui}
%{_kde5_libdir}/libkleopatraclientgui.so.%{kleopatraclientgui_major}*

#-----------------------------------------------------------------------------

%define grantleethemeeditor_major 5
%define libgrantleethemeeditor %mklibname grantleethemeeditor %{grantleethemeeditor_major}

%package -n %{libgrantleethemeeditor}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libgrantleethemeeditor}
KDE library.

%files -n %{libgrantleethemeeditor}
%{_kde5_libdir}/libgrantleethemeeditor.so.%{grantleethemeeditor_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdepimlibs-devel
Requires:	%{libakregatorinterfaces} = %{EVRD}
Requires:	%{libakregatorprivate} = %{EVRD}
Requires:	%{libkaddressbookprivate} = %{EVRD}
Requires:	%{libgrantleethemeeditor} = %{EVRD}
Requires:	%{libkleopatraclientcore} = %{EVRD}
Requires:	%{libkleopatraclientgui} = %{EVRD}
Requires:	%{libkmailprivate} = %{EVRD}
Requires:	%{libknotesprivate} = %{EVRD}
Requires:	%{libkontactprivate} = %{EVRD}
Requires:	%{libkorganizer_core} = %{EVRD}
Requires:	%{libkorganizer_interfaces} = %{EVRD}
Requires:	%{libkorganizerprivate} = %{EVRD}
Requires:	%{libpimsettingexporterprivate} = %{EVRD}
Requires:	%{libKF5CalendarSupport} = %{EVRD}
Requires:	%{libKF5ComposerEditorNG} = %{EVRD}
Requires:	%{libKF5EventViews} = %{EVRD}
Requires:	%{libKF5FollowupReminder} = %{EVRD}
Requires:	%{libKF5GrantleeTheme} = %{EVRD}
Requires:	%{libKF5IncidenceEditorsng} = %{EVRD}
Requires:	%{libKF5KDGantt2} = %{EVRD}
Requires:	%{libKF5KF5Gravatar} = %{EVRD}
Requires:	%{libKF5KManageSieve} = %{EVRD}
Requires:	%{libKF5KSieveUi} = %{EVRD}
Requires:	%{libKF5KSieve} = %{EVRD}
Requires:	%{libKF5KaddressbookGrantlee} = %{EVRD}
Requires:	%{libKF5KdepimDBusInterfaces} = %{EVRD}
Requires:	%{libKF5Libkdepim} = %{EVRD}
Requires:	%{libKF5Libkleo} = %{EVRD}
Requires:	%{libKF5MailCommon} = %{EVRD}
Requires:	%{libKF5MailImporter} = %{EVRD}
Requires:	%{libKF5MessageComposer} = %{EVRD}
Requires:	%{libKF5MessageCore} = %{EVRD}
Requires:	%{libKF5MessageList} = %{EVRD}
Requires:	%{libKF5MessageViewer} = %{EVRD}
Requires:	%{libKF5NoteShared} = %{EVRD}
Requires:	%{libKF5PimCommon} = %{EVRD}
Requires:	%{libKF5SendLater} = %{EVRD}
Requires:	%{libKF5TemplateParser} = %{EVRD}
%rename		kdepim4-devel

%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%{_kde5_libdir}/*.so

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}
%apply_patches
%cmake_kde5 -DKDEPIM_BUILD_MOBILE:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build

# akonadi_folderarchive_agent was removed, no need to keep desktop file
rm -f %{buildroot}%{_kde5_datadir}/akonadi/agents/folderarchiveagent.desktop

%find_lang %{name} --all-name --with-html
