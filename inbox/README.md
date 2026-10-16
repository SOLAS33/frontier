# Inbox

Drop information here for Claude to use on the Frontier sites: documents, figures, screenshots, notes, links.

- Name each file `site-topic.ext`, for example `fusion-cfs-update.pdf` or `orbit-launch-count.txt`.
- A text file can simply list links, one per line, with a note on which claim each supports.
- Commit and push if you want it kept: `git add inbox`, `git commit -m "Inbox: ..."`, `git push`.
- Then tell Claude: "read the inbox".

Claude checks each claim against its source (see `docs/SOURCING.md`), updates a site only for claims it can source, and moves processed files
to `inbox/done/` with a one-line note. This repository is public, so anything you commit is published. Commit only information you are happy to publish. For private files put them in `inbox/private/`, which git ignores, and tell Claude the file name. Never put passwords, keys or tokens in any of these folders.
