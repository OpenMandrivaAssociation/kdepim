Summary:	An application suite to manage personal information
Name:		kdepim
Epoch:		3
Version:	16.08.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Concurrent)
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
BuildRequires:	cmake(KF5MailCommon)
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
BuildRequires:	cmake(KF5IncidenceEditor)
BuildRequires:	cmake(KF5LibKSieve)
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
Requires:	kdepim-runtime >= 3:16.08.3
Requires:	akonadi-contacts >= 3:16.08.3
Requires:	kdepim-addons >= 1:16.08.3
Conflicts:	%{_lib}kdepim4 < 3:4.11.0
Conflicts:	%{_lib}kpgp4 < 3:4.11.0
Conflicts:	%{name}-devel < 3:4.11.0
Obsoletes:	akonadi-folderarchive-agent < 3:4.13.0
Obsoletes:	pimactivity < 3:4.13.0
%rename		kdepim4-core
Provides:	kdepim4-core = 3:4.14.3-1
Provides:	kdepim4-core = 3:4.14.10-1
Obsoletes:	kdepim4-core < 3:4.14.10-3

%description core
Core files for KDE PIM.

%files core -f %{name}.lang
%exclude %{_kde5_docdir}/HTML/en/*
%{_kde5_docdir}/HTML/en/contactthemeeditor
%{_datadir}/applications/org.kde.storageservicemanager.desktop
%{_datadir}/knotifications5/storageservicemanager.notifyrc
%{_kde5_iconsdir}/*/*/*/quickview.png
%{_kde5_iconsdir}/*/*/*/quickview.svgz
%{_datadir}/kconf_update
%exclude %{_datadir}/kconf_update/kalarm*

#-----------------------------------------------------------------------------

%package -n akonadiconsole
Summary:	Console that help to debug akonadi
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Conflicts:	kdepim4-core < 2:4.4.2-5

%description -n akonadiconsole
Console that help to debug akonadi.

%files -n akonadiconsole
%{_sysconfdir}/xdg/akonadiconsole.categories
%{_bindir}/akonadiconsole
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
%{_bindir}/akonadi_archivemail_agent
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/config.kcfg/archivemailagentsettings.kcfg

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
%{_bindir}/akonadi_followupreminder_agent
%{_datadir}/akonadi/agents/followupreminder.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent
%{_bindir}/akonadi_mailfilter_agent
%{_datadir}/akonadi/agents/mailfilteragent.desktop

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
%{_bindir}/akonadi_notes_agent
%{_datadir}/akonadi/agents/notesagent.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_sendlater_agent
%{_bindir}/akonadi_sendlater_agent
%{_datadir}/akonadi/agents/sendlateragent.desktop

#-----------------------------------------------------------------------------

%package -n akregator
Summary:	A Feed Reader for KDE
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Akregator
Requires:	%{name}-core = %{EVRD}
# (tpg) https://issues.openmandriva.org/show_bug.cgi?id=1462
Requires:	khtml >= 5.17.0
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
%{_sysconfdir}/xdg/akregator.categories
%{_bindir}/akregator
%{_bindir}/akregatorstorageexporter
%{_kde5_applicationsdir}/org.kde.akregator.desktop
%{_datadir}/akregator
%{_datadir}/metainfo/org.kde.akregator.appdata.xml
%{_datadir}/knotifications5/akregator.notifyrc
%{_qt5_plugindir}/akregator*
%{_datadir}/kxmlgui5/akregator
%{_datadir}/kservicetypes5/akregator_plugin.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_kde5_iconsdir}/*/*/apps/akregator.*
%{_kde5_iconsdir}/*/*/apps/akregator_empty.*
%{_kde5_services}/kontact/akregatorplugin.desktop
%{_kde5_services}/akregator_*
%{_kde5_services}/feed.protocol
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_datadir}/messageviewer/about/default/introduction_akregator.html

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
%{_sysconfdir}/xdg/blogilo.categories
%{_bindir}/blogilo
%{_bindir}/composerhtmleditor
%{_datadir}/composereditorwebengine/composereditorinitialhtml
%{_datadir}/kxmlgui5/composerhtmleditor/composerhtmleditorui.rc
%{_datadir}/metainfo/org.kde.blogilo.appdata.xml
%{_kde5_applicationsdir}/org.kde.blogilo.desktop
%{_datadir}/config.kcfg/blogilo.kcfg
%{_kde5_iconsdir}/*/*/apps/blogilo.*
%{_kde5_iconsdir}/*/*/actions/format-text-blockquote.*
%{_kde5_iconsdir}/*/*/actions/format-text-code.*
%{_kde5_iconsdir}/*/*/actions/insert-more-mark.*
%{_kde5_iconsdir}/*/*/actions/remove-link.*
%{_kde5_iconsdir}/*/*/actions/upload-media.*

%libpackage composereditorwebengineprivate 5

#-----------------------------------------------------------------------------

%package -n grantleeeditor
Summary:	Grantlee editor for KDE PIM applications
Group:		Graphical desktop/KDE
Conflicts:	%{name}-core < 3:16.08.2
Conflicts:	contactthemeeditor < 3:16.08.2
Conflicts:	headerthemeeditor < 3:16.08.2
Obsoletes:	contactthemeeditor < 3:16.08.2
Obsoletes:	headerthemeeditor < 3:16.08.2

%description -n grantleeeditor
Grantlee editor for KDE PIM applications.

%files -n grantleeeditor
%{_datadir}/applications/org.kde.contactprintthemeeditor.desktop
%{_datadir}/applications/org.kde.contactthemeeditor.desktop
%{_datadir}/applications/org.kde.headerthemeeditor.desktop
%{_bindir}/contactprintthemeeditor
%{_bindir}/contactthemeeditor
%{_bindir}/headerthemeeditor
%{_kde5_datadir}/config.kcfg/grantleethemeeditor.kcfg
%{_kde5_docdir}/*/*/contactthemeeditor
%{_kde5_docdir}/*/*/headerthemeeditor
%{_sysconfdir}/xdg/grantleeditor.categories

#-----------------------------------------------------------------------------

%package -n importwizard
Summary:	Import Wizard allows to migrate data from mailer as thunderbird/evolution etc
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}

%description -n importwizard
Import Wizard allows to migrate data from mailer as thunderbird/evolution etc.

%files -n importwizard
%doc %{_kde5_docdir}/HTML/en/importwizard
%{_sysconfdir}/xdg/importwizard.categories
%{_bindir}/importwizard
%{_kde5_applicationsdir}/org.kde.importwizard.desktop
%{_datadir}/importwizard
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
Suggests:	grantleeeditor = %{EVRD}
Provides:	kde4-kaddressbook = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%{_sysconfdir}/xdg/kaddressbook.categories
%{_bindir}/kaddressbook
%{_kde5_applicationsdir}/org.kde.kaddressbook.desktop
%{_datadir}/kaddressbook
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
%{_sysconfdir}/xdg/kaddressbook_themes.knsrc
%{_kde5_iconsdir}/*/*/apps/kaddressbook.*
%{_kde5_services}/kaddressbookpart.desktop
%{_kde5_services}/kontact/kaddressbookplugin.desktop
%{_qt5_plugindir}/kaddressbookpart.so
%{_datadir}/kxmlgui5/kaddressbook
%{_datadir}/applications/kaddressbook-importer.desktop

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
%{_sysconfdir}/xdg/kalarm.categories
%{_bindir}/kalarm
%{_bindir}/kalarmautostart
%{_kde5_libexecdir}/kalarm_helper
%{_datadir}/metainfo/org.kde.kalarm.appdata.xml
%{_sysconfdir}/xdg/autostart/kalarm.autostart.desktop
%{_kde5_applicationsdir}/org.kde.kalarm.desktop
%{_datadir}/kalarm
%{_datadir}/kconf_update/kalarm-1.2.1-general.pl
%{_datadir}/kconf_update/kalarm-1.9.5-defaults.pl
%{_datadir}/kconf_update/kalarm-2.0.2-general.pl
%{_datadir}/kconf_update/kalarm-2.1.5-general.pl
%{_datadir}/kconf_update/kalarm-version.pl
%{_datadir}/kconf_update/kalarm.upd
%{_datadir}/kconf_update/kalarm-*-kickoff.sh
%{_datadir}/config.kcfg/kalarmconfig.kcfg
%{_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_kde5_iconsdir}/*/*/apps/kalarm.*
%{_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_datadir}/kxmlgui5/kalarm

#-----------------------------------------------------------------------------

%package -n kmail
Summary:	KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Requires:	sasl-plug-plain
Requires:	sasl-plug-ntlm
Requires:	sasl-plug-login
Requires:	sasl-plug-digestmd5
Requires:	akonadi-archivemail-agent = %{EVRD}
Requires:	akonadi-followupreminder-agent = %{EVRD}
Requires:	akonadi-mailfilter-agent = %{EVRD}
Requires:	akonadi-sendlater-agent = %{EVRD}
Requires:	grantleeeditor = %{EVRD}
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
Obsoletes:	messageviewer

%description -n kmail
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -n kmail
%doc %{_kde5_docdir}/HTML/en/kmail
%{_sysconfdir}/xdg/kmail.categories
%{_bindir}/kmail
%{_kde5_applicationsdir}/kmail_view.desktop
%{_datadir}/kmail2
%{_datadir}/kxmlgui5/kmail2
%{_datadir}/knotifications5/kmail2.notifyrc
%{_datadir}/applications/org.kde.kmail.desktop
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/knotifications5/akonadi_archivemail_agent.notifyrc
%{_datadir}/knotifications5/akonadi_mailfilter_agent.notifyrc
%{_datadir}/knotifications5/akonadi_followupreminder_agent.notifyrc
%{_datadir}/knotifications5/akonadi_sendlater_agent.notifyrc
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
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmail.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
%{_datadir}/metainfo/org.kde.kmail.appdata.xml
%{_datadir}/kservicetypes5/dbusmail.desktop
%{_datadir}/messageviewer/about/default/introduction_kmail.html
#------------------------------------------------------------------------------

%package accountwizard
Summary: kincidenceeditor
Group: Graphical desktop/KDE
Requires: kross

%description accountwizard
New incidence editors.

%files accountwizard
%{_sysconfdir}/xdg/accountwizard.categories
%{_bindir}/accountwizard
%{_bindir}/ispdb
%{_sysconfdir}/xdg/accountwizard.knsrc
%{_qt5_plugindir}/accountwizard_plugin.so
%{_datadir}/akonadi/accountwizard
%{_datadir}/mime/packages/accountwizard-mime.xml
%{_datadir}/applications/org.kde.accountwizard.desktop

#-----------------------------------------------------------------------------

%package -n knotes
Summary:	Notes for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNotes
Requires:	%{name}-core = %{EVRD}
Requires:	akonadi-notes-agent = %{EVRD}
Provides:	kde4-knotes = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%doc %{_kde5_docdir}/HTML/en/knotes
%{_sysconfdir}/xdg/knotes.categories
%{_bindir}/knotes
%{_sysconfdir}/xdg/knotes_printing_theme.knsrc
%{_datadir}/metainfo/org.kde.knotes.appdata.xml
%{_kde5_applicationsdir}/org.kde.knotes.desktop
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/knotes
%{_datadir}/kxmlgui5/knotes
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
%{_datadir}/knotifications5/akonadi_notes_agent.notifyrc
%{_datadir}/config.kcfg/notesagentsettings.kcfg

#-----------------------------------------------------------------------------

%package -n kontact
Summary:	Kontact Container
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Kontact
Requires:	%{name}-core = %{EVRD}
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
%{_sysconfdir}/xdg/kontact.categories
%{_datadir}/metainfo/org.kde.kontact.appdata.xml
%{_bindir}/kontact
%{_datadir}/kontact
%{_kde5_applicationsdir}/org.kde.kontact.desktop
%{_kde5_applicationsdir}/kontact-admin.desktop
%{_datadir}/config.kcfg/kontact.kcfg
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
%{_datadir}/kxmlgui5/kontact
%{_datadir}/kxmlgui5/kontactsummary
%{_datadir}/messageviewer/about/default/introduction_kontact.html
%{_datadir}/messageviewer/about/default/loading_kontact.html

#-----------------------------------------------------------------------------

%package -n korganizer
Summary:	Calendar and scheduling component
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KOrganizer
Requires:	%{name}-core = %{EVRD}
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
%{_sysconfdir}/xdg/console.categories
%{_sysconfdir}/xdg/korganizer.categories
%{_bindir}/calendarjanitor
%{_bindir}/ical2vcal
%{_bindir}/konsolekalendar
%{_bindir}/korgac
%{_bindir}/korganizer
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_kde5_applicationsdir}/konsolekalendar.desktop
%{_kde5_applicationsdir}/korganizer-import.desktop
%{_kde5_applicationsdir}/org.kde.korganizer.desktop
%{_sysconfdir}/xdg/korganizer.knsrc
%{_datadir}/korgac
%{_datadir}/korganizer
%{_kde5_iconsdir}/*/*/apps/konsolekalendar.*
%{_kde5_iconsdir}/*/*/apps/korganizer.*
%{_kde5_iconsdir}/*/*/actions/checkmark.*
%{_kde5_iconsdir}/*/*/actions/smallclock.*
%{_kde5_iconsdir}/*/*/actions/upindicator.*
%{_kde5_iconsdir}/*/*/apps/korg-journal.*
%{_kde5_iconsdir}/*/*/apps/korg-todo.*
%{_datadir}/config.kcfg/korganizer.kcfg
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
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_datadir}/kxmlgui5/korganizer
%{_datadir}/kservicetypes5/dbuscalendar.desktop

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
%{_sysconfdir}/xdg/ktnef.categories
%{_bindir}/ktnef
%{_kde5_applicationsdir}/org.kde.ktnef.desktop
%{_kde5_iconsdir}/*/*/apps/ktnef*.*
%{_kde5_iconsdir}/*/*/actions/ktnef*.*


%libpackage notesharedprivate 5

#-----------------------------------------------------------------------------

%package -n mboximporter
Summary:	MBoxImporter allows to migrate data from MBox
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n mboximporter
MBoxImporter allows to migrate data from MBox.

%files -n mboximporter
%{_bindir}/mboximporter
%{_kde5_applicationsdir}/org.kde.mboximporter.desktop

#-----------------------------------------------------------------------------

%define pimsettingexporterprivate_major 5
%define libpimsettingexporterprivate %mklibname pimsettingexporterprivate %{pimsettingexporterprivate_major}

%package -n %{libpimsettingexporterprivate}
Summary:        KDE 5 library
Group:          System/Libraries

%description -n %{libpimsettingexporterprivate}
KDE 5 library for korganizer-Mobile.

%files -n %{libpimsettingexporterprivate}
%{_libdir}/libpimsettingexporterprivate.so.%{pimsettingexporterprivate_major}*

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
%{_sysconfdir}/xdg/pimsettingexporter.categories
%{_bindir}/pimsettingexporter
%{_bindir}/pimsettingexporterconsole
%{_datadir}/applications/org.kde.pimsettingexporter.desktop
%{_datadir}/config.kcfg/pimsettingexporterglobalconfig.kcfg

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
%{_sysconfdir}/xdg/sieveeditor.categories
%{_bindir}/sieveeditor
%{_kde5_applicationsdir}/org.kde.sieveeditor.desktop
%{_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg

#-----------------------------------------------------------------------------

%package -n storageservicemanager
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n storageservicemanager
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n storageservicemanager
%{_sysconfdir}/xdg/storageservicemanager.categories
%{_bindir}/storageservicemanager
%{_datadir}/config.kcfg/storageservicemanagerglobalconfig.kcfg
#-----------------------------------------------------------------------------

%define akregatorinterfaces_major 5
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE library.

%files -n %{libakregatorinterfaces}
%{_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#-----------------------------------------------------------------------------
%define akregatorprivate_major 5
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE library.

%files -n %{libakregatorprivate}
%{_libdir}/libakregatorprivate.so.%{akregatorprivate_major}*

#-----------------------------------------------------------------------------

%define kaddressbookprivate_major 5
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %{libkaddressbookprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkaddressbookprivate}
KDE library.

%files -n %{libkaddressbookprivate}
%{_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*

#-----------------------------------------------------------------------------

%define kmailprivate_major 5
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %{libkmailprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkmailprivate}
KDE library.

%files -n %{libkmailprivate}
%{_libdir}/libkmailprivate.so.%{kmailprivate_major}*

#-----------------------------------------------------------------------------

%define knotesprivate_major 5
%define libknotesprivate %mklibname knotesprivate %{knotesprivate_major}

%package -n %{libknotesprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libknotesprivate}
KDE library.

%files -n %{libknotesprivate}
%{_libdir}/libknotesprivate.so.%{knotesprivate_major}*

#-----------------------------------------------------------------------------

%define kontactprivate_major 5
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %{libkontactprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE library.

%files -n %{libkontactprivate}
%{_libdir}/libkontactprivate.so.%{kontactprivate_major}*

#-----------------------------------------------------------------------------

%define korganizer_core_major 5
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE library.

%files -n %{libkorganizer_core}
%{_libdir}/libkorganizer_core.so.%{korganizer_core_major}*

#-----------------------------------------------------------------------------

%define korganizer_interfaces_major 5
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE library.

%files -n %{libkorganizer_interfaces}
%{_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#-----------------------------------------------------------------------------

%define korganizerprivate_major 5
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %{libkorganizerprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizerprivate}
KDE library.

%files -n %{libkorganizerprivate}
%{_libdir}/libkorganizerprivate.so.%{korganizerprivate_major}*

#-----------------------------------------------------------------------------

%define grantleethemeeditor_major 5
%define libgrantleethemeeditor %mklibname grantleethemeeditor %{grantleethemeeditor_major}

%package -n %{libgrantleethemeeditor}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libgrantleethemeeditor}
KDE library.

%files -n %{libgrantleethemeeditor}
%{_libdir}/libgrantleethemeeditor.so.%{grantleethemeeditor_major}*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}
%apply_patches

# omit icons conflicting with oxygen-icons-5.19
# https://bugzilla.redhat.com/show_bug.cgi?id=1308358
sed -i -e 's|^add_subdirectory(icons)|#add_subdirectory(icons)|g' CMakeLists.txt ||:
mv icons icons.BAK ||:

%cmake_kde5 -DKDEPIM_BUILD_MOBILE:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build

# akonadi_folderarchive_agent was removed, no need to keep desktop file
rm -f %{buildroot}%{_datadir}/akonadi/agents/folderarchiveagent.desktop

# Remove .so files, we don't have any headers for -devel anyway
rm -fv %{buildroot}%{_libdir}/lib*.so

# (tpg) fix bug https://issues.openmandriva.org/show_bug.cgi?id=1607
desktop-file-install --vendor="" --add-only-show-in="KDE;" --delete-original --dir=%{buildroot}%{_sysconfdir}/xdg/autostart %{buildroot}%{_sysconfdir}/xdg/autostart/kalarm.autostart.desktop

%find_lang %{name} --all-name --with-html
