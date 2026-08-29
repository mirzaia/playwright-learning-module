# Module 11: Complex Browser Workflows

Handle interactions that do not fit a single page and click: iframes, new tabs, popups, dialogs, permissions, geolocation, clipboard, and time-dependent behavior. These are common in payment flows, identity providers, maps, reporting tools, and multi-window admin consoles.

The key engineering idea is to register an event expectation before the action that causes it. A popup, download, dialog, or navigation is an event; waiting after the click can miss it.

