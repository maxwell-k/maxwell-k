---
title: Actionable output from Ansible 2.11
cover_image: https://raw.githubusercontent.com/maxwell-k/blog/master/293991/cover_image.JPG
tags: ansible,devops,git,intro
published: true
---

```sh
ANSIBLE_DISPLAY_SKIPPED_HOSTS=no ANSIBLE_DISPLAY_OK_HOSTS=no \
    ansible-playbook -i, site.yaml
```

---

Though there is more to say than that. This is my first blog on <https://dev.to> and I've ideas and drafts for many more. I was really encouraged by [Miguel Grinberg]'s [talk] at [PyCon Limerick]. I am pleased to have put a post out into the world.

I am a big fan of Ansible and have found the community, especially the documentation team, very welcoming. I've been using Ansible since around version 2.4 which was [released in 2017]. The current version is 2.9.

Ansible 2.7 deprecated a feature for limiting the output of the `ansible-playbook` command line interface (CLI). It is scheduled to be removed in 2.11. This post explains a little context and how to switch over to the new approach.

As you may know, deprecation is a process for removing features from software; in Ansible deprecation follows [a policy]. This process gives users warnings and an opportunity to move away from the deprecated feature before anything relying on it breaks.

---

Simplifying a little, an Ansible playbook runs a series of tasks against a host. By default the `ansible-playbook` CLI reports back the status from each task. This can be reported as:

1. OK: completed successfully and nothing was changed
2. Changed: completed successfully with changes
3. Failed: the task did not complete . Skipped: the task was not run, likely because of a `when:` clause

Ansible will report a task as unreachable if it cannot contact the host. Further [ignored] and [rescued] relate to bespoke error handling.

Quickly identifying tasks with a changed status is a helpful filter. It is particularly effective if you write [idempotent] playbooks. Failed tasks are also of interest.

If you are tracking configuration as code, for example as Ansible playbooks in a git repository, this filtering makes it easier to marry the system changes reported by Ansible and the configuration changes in git.

Before Ansible 2.7 the recommended way to filter output to only show tasks with a changed or failed status was the [actionable] plugin. In Ansible 2.11 that plugin will be removed.

The current approach is to set two options and use the [default output plugin]. The two commands below show the old and new approach:

```sh
ANSIBLE_STDOUT_CALLBACK=actionable ansible-playbook -i, site.yaml
ANSIBLE_DISPLAY_SKIPPED_HOSTS=no ANSIBLE_DISPLAY_OK_HOSTS=no \
    ansible-playbook -i, site.yaml
```

There are many different ways to set these options; either [in configuration files] or environment variables. The change is the same regardless: instead of overriding the [default callback plugin for standard out], `stdout_callback=actionable`, instead set two options on the default callback: `display_skipped_hosts=no` and `display_ok_hosts=no`.

For more detail about the background to this change, take a look at the GitHub [pull request] and [commit] implementing the deprecation.

[a policy]: https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#deprecation-cycle
[actionable]: https://docs.ansible.com/ansible/latest/plugins/callback/actionable.html
[commit]: https://github.com/ansible/ansible/commit/9c5d40ff152a8a94dc226735ce43593ebbb10104
[default callback plugin for standard out]: https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-stdout-callback
[default output plugin]: https://docs.ansible.com/ansible/latest/plugins/callback/default.html
[idempotent]: https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-idempotency
[ignored]: https://docs.ansible.com/ansible/latest/user_guide/playbooks_error_handling.html#ignoring-failed-commands
[in configuration files]: https://docs.ansible.com/ansible/latest/plugins/callback.html
[miguel grinberg]: https://blog.miguelgrinberg.com
[pull request]: https://github.com/ansible/ansible/pull/41058
[pycon limerick]: https://python.ie/pycon-limerick-2020/
[released in 2017]: https://pypi.org/project/ansible/#history
[rescued]: https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html#block-error-handling
[talk]: https://github.com/PyConLimerick/Limerick2020/blob/master/Abstracts/09_Grinsberg_Miguel_Python_Community_Engagement.md

<!-- vim: set ft=markdown.gfm.frontmatter : -->
