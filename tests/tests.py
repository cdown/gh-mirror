#!/usr/bin/env python2

import os
import ghm
from nose.tools import eq_
from mock import patch


try:  # Python 2 fallback
    range = xrange
except NameError:
    pass


def relative(filename):
    return os.path.join(os.path.dirname(__file__), filename)


@patch("ghm.urlopen")
def test_repos(urlopen_mock):
    files = [open(relative("output/repos/%d.json" % i), "rb") for i in range(1, 3)]
    urlopen_mock.side_effect = files

    repos = ghm.repos("!?")

    eq_(
        list(repos),
        [
            {
                "description": "An Apache handler to dynamically generate ETags.",
                "url": "git://github.com/cdown/Apache-ETag.git",
            },
            {
                "description": "Simple AUR download utility.",
                "url": "git://github.com/cdown/aurdl.git",
            },
            {
                "description": "Simple AUR search utility.",
                "url": "git://github.com/cdown/aursc.git",
            },
            {
                "description": "Simple battery status tool in POSIX sh.",
                "url": "git://github.com/cdown/bats.git",
            },
            {
                "description": "Minimalist configuration management.",
                "url": "git://github.com/cdown/ceci.git",
            },
            {
                "description": "Personal ceci configs.",
                "url": "git://github.com/cdown/ceci-configs.git",
            },
            {
                "description": "Battery status in the console (Linux only).",
                "url": "git://github.com/cdown/cellout.git",
            },
            {
                "description": 'Simple "correct horse battery staple"-style generator.',
                "url": "git://github.com/cdown/chbs.git",
            },
            {
                "description": "A tiny wrapper around the Arch checkupdates script for use in a cronjob.",
                "url": "git://github.com/cdown/checkupdates-cron.git",
            },
            {
                "description": "Simple URL shortener.",
                "url": "git://github.com/cdown/chopurl.git",
            },
            {
                "description": "The code powering chrisdown.name.",
                "url": "git://github.com/cdown/chrisdown.name.git",
            },
            {
                "description": "Concise IRC client library for node.js.",
                "url": "git://github.com/cdown/circl.git",
            },
            {
                "description": "Digital signage suite (deprecated, use osmo instead).",
                "url": "git://github.com/cdown/clarity.git",
            },
            {
                "description": "Personal configuration files.",
                "url": "git://github.com/cdown/dotfiles.git",
            },
            {
                "description": "Downloads the original individual images from Flickr sets.",
                "url": "git://github.com/cdown/download-flickr-set.git",
            },
            {
                "description": "Dynamic window manager for X.",
                "url": "git://github.com/cdown/dwm.git",
            },
            {
                "description": "Databaseless digital signage client (deprecated: use osmo instead).",
                "url": "git://github.com/cdown/elision.git",
            },
            {
                "description": "Simple URL shortener with support for custom identities.",
                "url": "git://github.com/cdown/fwd.git",
            },
            {
                "description": "Mirror all GitHub repositories for a user, maintaining metadata.",
                "url": "git://github.com/cdown/gh-mirror.git",
            },
            {
                "description": "Gets direct URLs to images from imgur albums.",
                "url": "git://github.com/cdown/imurl.git",
            },
            {
                "description": "A sane initscript template. Ideally, edit two variables and you're done.",
                "url": "git://github.com/cdown/initscript-template.git",
            },
            {
                "description": "Remove mouse acceleration on Mac OSX.",
                "url": "git://github.com/cdown/mac-cel.git",
            },
            {
                "description": "dmenu frontend to MPD.",
                "url": "git://github.com/cdown/mpdmenu.git",
            },
            {
                "description": "Script to migrate OpenVZ containers to LXC.",
                "url": "git://github.com/cdown/openvz-to-lxc.git",
            },
            {
                "description": "Digital signage for minimalists.",
                "url": "git://github.com/cdown/osmo.git",
            },
            {
                "description": "Simple CLI Pushover interface.",
                "url": "git://github.com/cdown/pushover-cli.git",
            },
            {
                "description": "Arch User Repository interface.",
                "url": "git://github.com/cdown/pyaur.git",
            },
            {
                "description": "Really awesome deployment on your local machines.",
                "url": "git://github.com/cdown/rad.git",
            },
            {
                "description": "Web interface to RADIUS.",
                "url": "git://github.com/cdown/radiusweb.git",
            },
            {
                "description": "Rebuild a Debian ISO with preseed/custom files.",
                "url": "git://github.com/cdown/rebuild-debian-iso.git",
            },
            {
                "description": "Gets direct URLs to streaming media from SoundCloud song pages. ",
                "url": "git://github.com/cdown/scurl.git",
            },
            {
                "description": "IRC bot to help finding a TF2 merc/ringer.",
                "url": "git://github.com/cdown/tf2mercbot.git",
            },
            {
                "description": "Set the system timezone based on IP geolocation.",
                "url": "git://github.com/cdown/tzupdate.git",
            },
            {
                "description": "Automatically log in to captive portals.",
                "url": "git://github.com/cdown/wifilogin.git",
            },
            {
                "description": "Get direct URLs to YouTube videos.",
                "url": "git://github.com/cdown/yturl.git",
            },
        ],
    )
