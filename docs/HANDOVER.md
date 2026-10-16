# Handover: the deploy token, and how to send information to Claude

Written 16 October 2026. Everything below is a link, a command or a folder. Nothing here needs a secret pasted into chat.

## 1. Links

| What | Link |
|---|---|
| The live series (hub) | https://frontier.solas33.com/ |
| Code (public) | https://github.com/SOLAS33/frontier |
| Scheduled job and runs | https://github.com/SOLAS33/frontier/actions/workflows/live.yml |
| Repository secrets (where the token goes) | https://github.com/SOLAS33/frontier/settings/secrets/actions |
| Repository variables | https://github.com/SOLAS33/frontier/settings/variables/actions |
| Create a Cloudflare token | https://dash.cloudflare.com/profile/api-tokens |
| Send a correction or a source | https://github.com/SOLAS33/frontier/issues/new/choose |
| Solas33 products page | https://solas33.com/products |
| Local clone | C:\Users\damcdonagh\Repos\frontier |

## 2. The API token (CF_API_TOKEN)

State on 16 October 2026: the secret **CF_API_TOKEN already exists on the repository and holds the placeholder `set-me`.** The workflow
detects the placeholder, skips the deploy step and says so in its log, so a forgotten edit cannot publish anything wrong. Until you
replace it, Claude deploys by hand from the founder PC with wrangler, and the live data on the pages goes stale between those deploys.

**To replace it (about two minutes):**

1. Open https://dash.cloudflare.com/profile/api-tokens and choose **Create Token**.
2. Next to **Edit Cloudflare Workers** choose **Use template**. Under permissions add one row: **Zone, DNS, Edit**.
   Account resources: the account that owns the `frontier` Worker. Zone resources: **Include, Specific zone, solas33.com**.
3. Choose **Continue to summary**, then **Create Token**, and copy the value. Cloudflare shows it once.
4. Open https://github.com/SOLAS33/frontier/settings/secrets/actions, click the **pencil next to CF_API_TOKEN**, paste the value, save.
   Edit that one name only. Do not create a new secret.
5. Check it. In PowerShell:

       gh workflow run live --repo SOLAS33/frontier
       gh run list --repo SOLAS33/frontier --limit 3
       python tools/verify_all.py

   A green run whose log says `token length: 40 characters` (a real token is about 40) and shows a **Deploy to Cloudflare** step
   means it worked. `verify_all.py` then checks all fourteen live sites.

**If you would rather reuse the existing Solas33 deploy token (`solas-github-deploy`):** run `store-cf-token.ps1` once in your own
terminal (it asks for the value and stores it encrypted for this PC and user), then `set-cf-token.ps1 frontier`. The files are
in `C:\Users\damcdonagh\.solas33\` and the encrypted value is not there yet. Do not use **Roll** on that token unless you re-run
`set-cf-token.ps1` for every site repository afterwards.

**Other secrets and variables (names only):** `SEC_CONTACT_EMAIL` (set, hello@solas33.com), `CF_ACCOUNT_ID` (variable, set),
`BREVO_API_KEY` (not requested yet; it is for the weekly digest and will be asked for together with anything else at the end).

## 3. Sending information to Claude

Claude has no inbox of its own. It reads what is in the repository and what you say in a session. Use any of these.

**A. A file in the inbox folder (best for documents, figures, screenshots, notes).**

1. Put the file in `C:\Users\damcdonagh\Repos\frontier\inbox\`. Name it `site-topic.ext`, for example `fusion-cfs-update.pdf`.
2. Optional, so it is saved with the project history. The repository is public, so only commit what you are happy to publish. Private files go in `inbox\private\`, which git ignores:

       cd C:\Users\damcdonagh\Repos\frontier
       git add inbox
       git commit -m "Inbox: fusion update"
       git push

3. Tell Claude at the start of a session: "read the inbox". Claude reads every file, checks each claim against its source,
   changes the site only for claims it can source, and moves processed files to `inbox/done/` with a one-line note.

**B. A GitHub issue (best for a correction or a source for one claim).** Use https://github.com/SOLAS33/frontier/issues/new/choose.
There are two forms: **Correction** (a fact on a page is wrong) and **Source or new information** (a link or document Claude should use).
Give the page address, the sentence, and the link that supports the change. Claude will read open issues on request:
"read the open issues".

**C. In the session.** Paste a link or a file path and say which site it is for. Claude fetches the page, checks it, and applies
the sourcing rule in `docs/SOURCING.md`.

**What makes an input useful:** a primary source (filing, regulator, agency, paper) beats a news report. A date and a number beat an
opinion. Anything marked as a target or a company claim stays labelled that way.

## 4. Checks you can run yourself

    cd C:\Users\damcdonagh\Repos\frontier
    python tools/verify_all.py              # all live sites: page, hub link, sitemap, live.json age, feed
    python tools/verify_all.py --links      # also tests every reference link (slow)
    python build.py quantum --check-links   # one site, its reference links
    python tools/voice_lint.py dist/quantum/index.html
    python -m pytest -q tests

## 5. Deploying by hand until the token is set

    cd C:\Users\damcdonagh\Repos\frontier
    python build.py <slug>                  # one site, or run for each slug in config.toml
    node "%TEMP%\wr\node_modules\wrangler\bin\wrangler.js" deploy

If `%TEMP%\wr` is missing: make a temporary folder, run `npm i wrangler@4` in it, and call its `node_modules/wrangler/bin/wrangler.js`
the same way. Wrangler uses the logged-in Cloudflare account (`wrangler login`).
