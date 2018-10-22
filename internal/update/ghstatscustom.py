#!/usr/bin/env python

"""
Python script to obtain GitHub Release download count and other statistics.

Based on GitHub Download Stats, modified for use.
Original Author: Alexander Gorishnyak <kefir500@gmail.com>
Link: https://github.com/kefir500/ghstats
"""

import os
import sys
import json
import time

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

__version__ = "1.2.0"
__author__ = "Alexander Gorishnyak"
__email__ = "kefir500@gmail.com"
__license__ = "MIT"


class ConnectionError(Exception):
    """
    Raised on connection error.
    """

    def __init__(self, reason=None):
        """
        :param reason: Connection error reason.
        """
        self.reason = reason if reason else "Unknown reason."

    def __str__(self):
        return str(self.reason)


class GithubError(Exception):
    """
    Generic exception raised on GitHub API HTTP error.
    """

    def __init__(self, code, message=None):
        """
        :param code: HTTP error code.
        :param message: Exception message text.
        """
        self.code = code
        self.message = message

    def __str__(self):
        return "GitHub API HTTP {0}{1}".format(self.code, (": " + self.message) if self.message else "")


class GithubRepoError(GithubError):
    """
    Raised when accessing nonexistent GitHub username, repository or release tag.
    """

    def __init__(self, message=None):
        """
        :param message: Exception message text.
        """
        self.code = 404
        self.message = message if message else "Invalid GitHub username, repository or release tag."


class GithubLimitError(GithubError):
    """
    Raised when GitHub API request limit is exceeded.
    """

    def __init__(self, message=None):
        """
        :param message: Exception message text.
        """
        self.code = 403
        self.message = message if message else "Request limit exceeded."


class GithubTokenError(GithubError):
    """
    Raised when trying to pass invalid GitHub OAuth token.
    """

    def __init__(self, message=None):
        """
        :param message: Exception message text.
        """
        self.code = 401
        self.message = message if message else "Unauthorized. Check your \"GITHUB_TOKEN\" environment variable."


class _Text:
    """
    Definitions for colored output (no ANSI colors on Windows).
    """
    if os.name != "nt":
        HEADER = "\033[1;36m"
        SUCCESS = "\033[1;32m"
        ERROR = "\033[1;31m"
        BOLD = "\033[1m"
        ITALIC = "\033[3m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"
    else:
        HEADER = SUCCESS = ERROR = BOLD = ITALIC = UNDERLINE = END = ""


def error(message):
    """
    Halt script due to critical error.
    :param message: Error text.
    """
    sys.exit(_Text.ERROR + "Error: " + message + _Text.END)


def get_env_token():
    """
    Get GitHub OAuth token from "GITHUB_TOKEN" environment variable.
    :return: GitHub OAuth token.
    """
    token = None if "GITHUB_TOKEN" not in os.environ else os.environ["GITHUB_TOKEN"]
    return token

def download_stats(user=None, repo=None, tag=None, latest=False, token=None, quiet=False):
    """
    Get download statistics from GitHub API.
    :param user: GitHub repository owner username. If empty, user will be prompted for input.
    :param repo: GitHub repository name. If empty, user will be prompted for input.
    :param tag: Release tag name. If empty, get stats for all releases.
    :param latest: If True, ignore "tag" parameter and get stats for the latest release.
    :param token: GitHub OAuth token. If empty, API request limit will be reduced.
    :param quiet: If True, print nothing.
    :return: Statistics on downloads.
    :raises GithubRepoError: When accessing nonexistent GitHub username, repository or release tag.
    :raises GithubLimitError: When GitHub API request limit is exceeded.
    :raises GithubTokenError: When trying to pass invalid GitHub API OAuth token.
    :raises ConnectionError: On connection error.
    """
    if not user:
        user = raw_input("GitHub Username: ")
    if not repo:
        repo = raw_input("GitHub Repository: ")
    if not quiet:
        #print("Downloading {0}/{1} stats...".format(user, repo))
        print("Downloading PyOS info...")
    url = "https://api.github.com/repos/{0}/{1}/releases".format(user, repo)
    url += ("" if not tag else "/tags/" + tag) if not latest else "/latest"
    headers = {} if not token else {"Authorization": "token " + token}
    request = urllib2.Request(url, headers=headers)
    start = time.time()
    try:
        response = urllib2.urlopen(request).read().decode("utf-8")
    except urllib2.HTTPError as e:
        if e.code == 404:
            raise GithubRepoError()    # Invalid GitHub username, repository or release tag.
        elif e.code == 403:
            raise GithubLimitError()   # GitHub API request limit exceeded.
        elif e.code == 401:
            raise GithubTokenError()   # Invalid GitHub OAuth token.
        else:
            raise GithubError(e.code)  # Generic GitHub API exception.
    except urllib2.URLError as e:
        raise ConnectionError(e.reason)
    stats = json.loads(response)
    if not quiet:
        end = time.time()
        print("Downloaded in {0:.3f}s".format(end - start))
    return stats


def get_release_downloads(release, quiet=False):
    """
    Get number of downloads for a single release.
    :param release: Release statistics from GitHub API.
    :param quiet: If True, print nothing.
    :return: Number of downloads for a release.
    """
    if not quiet:
        print("Latest Tag: " + release["tag_name"])
        with open("latest.txt", "w") as text_file:
            text_file.write("Latest Tag\n" + release["tag_name"])


def get_stats_downloads(stats, quiet=False):
    """
    Get number of downloads from statistics.
    :param stats: Statistics from GitHub API.
    :param quiet: If True, print nothing.
    :return: Number of downloads.
    """
    total = 0
    if isinstance(stats, dict):
        total = get_release_downloads(stats, quiet)
    else:
        for release in stats:
            total += get_release_downloads(release, quiet)
    return total

def main(user=None, repo=None, tag=None, latest=False, detail=False, token=None, quiet=False):
    """
    Get number of downloads for GitHub release(s).
    :param user: GitHub repository owner username. If empty, user will be prompted for input.
    :param repo: GitHub repository name. If empty, user will be prompted for input.
    :param tag: Release tag name. If empty, get stats for all releases.
    :param latest: If True, ignore "tag" parameter and get stats for the latest release.
    :param detail: Detailed output containing release information.
    :param token: GitHub OAuth token. If empty, API request limit will be reduced.
    :param quiet: If True, print nothing.
    :return: Number of downloads.
    """
    try:
        stats = download_stats(user, repo, tag, latest, token, quiet)
    except GithubError as e:
        error(e.message)
    except ConnectionError as e:
        error(str(e))
    else:
        total = get_stats_downloads(stats, quiet or not detail)
        # print_total(total, quiet, tag or (stats["tag_name"] if latest else None))
        return total
