# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

# Backend to use to display websites. qutebrowser supports two different
# web rendering engines / backends, QtWebKit and QtWebEngine. QtWebKit
# was discontinued by the Qt project with Qt 5.6, but picked up as a
# well maintained fork: https://github.com/annulen/webkit/wiki -
# qutebrowser only supports the fork. QtWebEngine is Qt's official
# successor to QtWebKit. It's slightly more resource hungry than
# QtWebKit and has a couple of missing features in qutebrowser, but is
# generally the preferred choice.
# Type: String
# Valid values:
#   - webengine: Use QtWebEngine (based on Chromium).
#   - webkit: Use QtWebKit (based on WebKit, similar to Safari).
c.backend = 'webengine'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#666666'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = 'grey'

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = '#ccc'

# Height (in pixels or as percentage of the window) of the completion.
# Type: PercOrInt
c.completion.height = '25%'

# Width (in pixels) of the scrollbar in the completion window.
# Type: Int
c.completion.scrollbar.width = 0

# Shrink the completion to be smaller than the configured size if there
# are no scrollbars.
# Type: Bool
c.completion.shrink = True

# Execute the best-matching command on a partial match.
# Type: Bool
c.completion.use_best_match = True

# Number of URLs to show in the web history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.web_history_max_items = 500

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
c.content.default_encoding = 'utf-8'

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.geolocation = False

# Value to send in the `Accept-Language` header.
# Type: String
c.content.headers.accept_language = 'en-GB,en'

# User agent to send. Unset to send the default.
# Type: String
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# List of URLs of lists which contain hosts to block.  The file can be
# in one of the following formats:  - An `/etc/hosts`-like file - One
# host per line - A zip-file of any of the above, with either only one
# file, or a file   named `hosts` (with any extension).
# Type: List of Url
c.content.host_blocking.lists = ['https://www.malwaredomainlist.com/hostslist/hosts.txt', 'http://someonewhocares.org/hosts/hosts', 'http://winhelp2002.mvps.org/hosts.zip', 'http://malwaredomains.lehigh.edu/files/justdomains.zip', 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext']

# List of domains that should always be loaded, despite being ad-
# blocked. Domains may contain * and ? wildcards and are otherwise
# required to exactly match the requested domain. Local domains are
# always exempt from hostblocking.
# Type: List of String
c.content.host_blocking.whitelist = []

# Allow websites to record audio/video.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.media_capture = False

# Limit fullscreen to the browser window (does not expand to fill the
# screen).
# Type: Bool
c.content.windowed_fullscreen = True

# Monitor load requests for cross-site scripting attempts. Suspicious
# scripts will be blocked and reported in the inspector's JavaScript
# console. Enabling this feature might have an impact on performance.
# Type: Bool
c.content.xss_auditing = True

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '/home/eled/downloads'

# What to display in the download filename input.
# Type: String
# Valid values:
#   - path: Show only the download path.
#   - filename: Show only download filename.
#   - both: Show download path and filename.
c.downloads.location.suggestion = 'both'

# Where to show the downloaded files.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.downloads.position = 'bottom'

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = 1000

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined: * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['xterm', '-e', 'vim', '{}']

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 9.5pt monospace'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '9.5pt monospace'

# Font used for the debugging console.
# Type: QtFont
c.fonts.debug_console = '9.5pt monospace'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '9.5pt monospace'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 9.5pt monospace'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '9.5pt monospace'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '9.5pt monospace'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '9.5pt monospace'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '9.5pt monospace'

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = '"DejaVu Sans Mono", Monospace, Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '9.5pt sans-serif'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '9.5pt monospace'

# Font used in the tab bar.
# Type: QtFont
c.fonts.tabs = '9.5pt monospace'

# Font family for fixed fonts.
# Type: FontFamily
c.fonts.web.family.fixed = 'monospace'

# Font family for sans-serif fonts.
# Type: FontFamily
c.fonts.web.family.sans_serif = None

# Font family for serif fonts.
# Type: FontFamily
c.fonts.web.family.serif = None

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = 'sans-serif'

# Default font size (in pixels) for regular text.
# Type: Int
c.fonts.web.size.default = 14

# Default font size (in pixels) for fixed-pitch text.
# Type: Int
c.fonts.web.size.default_fixed = 12

# How to open links in an existing instance if a new one is launched.
# This happens when e.g. opening a link from a terminal. See
# `new_instance_open_target_window` to customize in which window the
# link is opened in.
# Type: String
# Valid values:
#   - tab: Open a new tab in the existing window and activate the window.
#   - tab-bg: Open a new background tab in the existing window and activate the window.
#   - tab-silent: Open a new tab in the existing window without activating the window.
#   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
#   - window: Open in a new window.
c.new_instance_open_target = 'window'

# Show a filebrowser in upload/download prompts.
# Type: Bool
c.prompt.filebrowser = False

# Rounding radius (in pixels) for the edges of prompts.
# Type: Int
c.prompt.radius = 0

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = False

# Name of the session to save by default. If this is set to null, the
# session which was last loaded is saved.
# Type: SessionName
c.session.default_name = 'default'

# Padding (in pixels) for tab indicators.
# Type: Padding
c.tabs.indicator.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 4}

# How to behave when the last tab is closed.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'close'

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'top'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{title}`: Title of the
# current web page. * `{title_sep}`: The string ` - ` if a title is set,
# empty otherwise. * `{index}`: Index of this tab. * `{id}`: Internal
# tab ID of this tab. * `{scroll_pos}`: Page scroll position. *
# `{host}`: Host of the current web page. * `{backend}`: Either
# ''webkit'' or ''webengine'' * `{private}`: Indicates when private mode
# is enabled. * `{current_url}`: URL of the current web page. *
# `{protocol}`: Protocol (http/https/...) of the current web page.
# Type: FormatString
c.tabs.title.format = '{perc}{title}'

# Format to use for the tab title for pinned tabs. The same placeholders
# like for `tabs.title.format` are defined.
# Type: FormatString
c.tabs.title.format_pinned = None

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'file:///home/eled/coding/misc/startpage/home.html'

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'pydoc': 'file:///usr/share/doc/python/html/search.html?q={}&check_keywords=false&area=default', 'pons': 'https://en.pons.com/translate?q={}&l=deen&in=&lf=de', 'tex': 'https://en.wikibooks.org/wiki/Special:Search?search={}&prefix=LaTeX%2F', 'man': 'https://jlk.fjfi.cvut.cz/arch/manpages/man/{}', 'aw': 'https://wiki.archlinux.org/index.php?search={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'file:///home/eled/coding/misc/startpage/home.html'

# Bindings for normal mode
config.bind(';n', 'hint all window')
config.bind(';p', 'hint links run open -p {hint-url}')

# Bindings for command mode
config.bind('<ctrl+w>', 'rl-unix-filename-rubout', mode='command')

# Bindings for insert mode
config.bind('<ctrl+w>', 'fake-key <ctrl-backspace>', mode='insert')
