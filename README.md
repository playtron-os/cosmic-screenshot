# cosmic-screenshot

Utility for capturing screenshots via XDG Desktop Portal

Screenshots stay at the destination returned by the portal in both interactive
and noninteractive mode. On Kora, this honors the active workspace's Captures
directory.

To override the destination for a noninteractive screenshot, pass an existing
directory with `--save-dir`:

```sh
cosmic-screenshot --interactive=false --save-dir /path/to/screenshots
```

An omitted or invalid `--save-dir` keeps the portal's destination. Interactive
screenshots always use the destination selected in the portal.
