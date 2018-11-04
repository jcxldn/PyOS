# Documentation

## Commands

All current commands listed in alphabetical order.

`about` - Basic information about PyOS.

`calc` - A calculator.

`clear` / `cls` - Clears the screen.

`downloader` - Downloads a file from the internet

`example` - An example program.

`exit` - Quit PyOS.

`fizzbuzz` - A fizzbuzz program.

`help` - View a list of commands.

`ls` - List the contents of your current directory.

`pwd` - List the current working directory.

`mv` - Move (rename) a file to another. 

`cp` - Copy one file to another. 

`mkdir` - Create directories. 

`sysinfo` - View system information.

`updater` - Check for updates on GitHub (requires internet access)

## Versioning
We try to follow the [Semver Standard](https://semver.org/).

This means that:

```
Given a version number MAJOR.MINOR.PATCH, increment the:

MAJOR version when you make incompatible API changes,

MINOR version when you add functionality in a backwards-compatible manner, and

PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
```

In some cases, the version in the PyOS program may read as `X.Y.Z-base-BRANCH`, and is caused because changes have been made in the branch for the upcoming  `X.Y.Z` release, but have not yet been tagged on GitHub.

An example of this would be a change in the `master` branch that has not yet been tagged, or formally released, on GitHub. Treat these releases as a pre-release. These are based of their respective branches and may be unstable, or have broken and/or missing features.

For a stable release, please use a release that is [tagged on GitHub](https://github.com/Prouser123/PyOS/releases/latest).
