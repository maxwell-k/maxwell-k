---
title: Using GoLand on Fedora Silverblue
cover_image: https://raw.githubusercontent.com/maxwell-k/blog/master/295829/cover_image.JPG
tags: go,tooling,jetbrains,fedora
published: true
---

I could find very little information online about running [JetBrains GoLand] on Fedora Silverblue. I hope this post will change that. I have tested the instructions below with the latest version, `2020.1` — [released yesterday] — and the previous version `2019.3.4` both on [Fedora Silverblue] 30.

Using Fedora Silverblue as a desktop operating system means that “every installation is identical to every other installation of the same version”. I am a very happy Fedora Silverblue user; last year I gave [a talk] explaining why.

# Why GoLand?

I normally try to use open source rather than proprietary software wherever possible. I am a long term [vim] user. Saying that, I also actively try to stay open minded about technology. In the end, I decided to try out GoLand because:

- it was widely endorsed at [Belfast Gophers]
- a lot of people I respect from [SoCraTes UK](https://socratesuk.org) are JetBrains fans
- a recent coding test / interview involved pairing with a developer using another JetBrains product; a bit of exposure to JetBrains can only help in that sort of situation
- I've already got a licence, from a Legacy Code Retreat event in 2019; the first year of a GoLand licence [normally costs] £149.00.

# Installation process

On Fedora Silverblue the [root filesystem] is immutable although certain mutable directories are made available from `/var`. On another system I would install into `/opt`, to follow the [Filesystem Hierarchy Standard]. On Fedora Silverblue `/opt` is a symbolic link to `/var/opt` so I'll install there. I also add a link to the `PATH`; `/usr/local/bin` is writable via `/var/usrlocal` which is mounted at `/usr/local`.

```sh
version=2020.1
sudo mkdir /var/opt/goland
cd /var/opt/goland
sudo chown "$LOGNAME:$LOGNAME" .
curl -OL https://download.jetbrains.com/go/goland-$version.tar.gz
curl -O https://download.jetbrains.com/go/goland-$version.tar.gz.sha256
sha256sum -c goland-$version.tar.gz.sha256
tar xf goland-$version.tar.gz
cd GoLand-$version/bin
sudo ln -s "$PWD/goland.sh" /var/usrlocal/bin
```

`Alt-F2` then `goland.sh⏎` should start GoLand!

Next up activate your licence. Then use the UI to download an SDK ( File → Settings → GOROOT ); this happens in the background. I chose 1.13.8 to match the [current version in Alpine Linux edge]. After that I was all set; I started working through “The Hitchhiker's Guide to GoLand”.

## Debugging

If you have an issue it might help to see messages printed to a terminal; instead at the same terminal as above try: `./goland.sh⏎`. At first I was connected via SSH without `$DISPLAY` set properly.

# Why did this need a blog post?

Fedora Silverblue is an immutable desktop operating system. The recommended methods for running GUI software include Flatpaks and or other containers using [toolbox] or even [Podman] directly. It is also possible to layer or install traditionally packaged applications with `rpm-ostree` but that introduces differences between one system and the next.

My early research didn't show a straight forward answer. The possibilities I came across included: an [unofficial container], the official [snap that JetBrains publish] or even using [an AppImage]. [No Flatpak is available]. Snaps are more common on Ubuntu, on Fedora Silverblue the background service would have to be installed first: either inside a container or as a layer with `rpm-ostree`.

I should probably have jumped into trying this out practically more quickly. The JetBrains [installation guide] doesn't give much detail about this approach, but the files are clearly linked from the JetBrains [Linux download page].

This isn't the perfect installation method but a set of compromises; one disadvantage is that it doesn't provide a launcher. While I knew there would be compromises, I wanted to:

1. Avoid changing the base Fedora Silverblue system with `rpm-ostree`
2. Avoid a complicated setup that includes manually installed dependencies
3. Use a supported, official method

In the end I didn't have to compromise on these three points. The process of writing out and ordering the potential compromises for someone else to follow helped me to prioritise the order in which I investigated options.

---

Installing GoLand under Fedora Silverblue was easier than I expected. I wonder what other surprises I will find now I have GoLand up and running.

[a talk]: https://github.com/maxwell-k/20191023-Belfast-Linux-User-Group-Silverblue-talk
[an appimage]: https://github.com/AppImage/pkg2appimage/blob/master/recipes/GoLand
[belfast gophers]: https://www.meetup.com/Belfast-Gophers/
[current version in alpine linux edge]: https://pkgs.alpinelinux.org/package/edge/community/x86_64/go
[fedora silverblue]: https://docs.fedoraproject.org/en-US/fedora-silverblue/
[filesystem hierarchy standard]: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
[installation guide]: https://www.jetbrains.com/help/go/installation-guide.html
[jetbrains goland]: https://www.jetbrains.com/go/
[linux download page]: https://www.jetbrains.com/go/download/#section=linux
[no flatpak is available]: https://youtrack.jetbrains.com/issue/GO-7441
[normally costs]: https://www.jetbrains.com/store/?fromNavMenu#commercial?billing=yearly
[podman]: https://github.com/containers/libpod
[released yesterday]: https://www.jetbrains.com/go/download/other.html
[root filesystem]: https://docs.fedoraproject.org/en-US/fedora-silverblue/technical-information/#filesystem-layout
[snap that jetbrains publish]: https://snapcraft.io/goland
[toolbox]: https://github.com/containers/toolbox
[unofficial container]: https://hub.docker.com/r/rycus86/goland/
[vim]: https://www.vim.org
[xdg specification]: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html

<!-- vim: set filetype=markdown.gfm.frontmatter : -->
