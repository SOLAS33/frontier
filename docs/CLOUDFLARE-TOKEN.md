# Cloudflare token for the scheduled deploy

The 3-hourly job in `.github/workflows/live.yml` refreshes data and rebuilds the sites. It can only publish them when the
repository has a real `CF_API_TOKEN` secret. This is the one key the series needs now.

## Create a token just for Frontier (recommended)

1. Open https://dash.cloudflare.com/profile/api-tokens and choose **Create Token**.
2. Next to **Edit Cloudflare Workers** choose **Use template**.
3. Under **Permissions** keep what the template adds, then add one more row: **Zone, DNS, Edit**.
4. Under **Account Resources** choose the account that owns the `frontier` Worker. Under **Zone Resources** choose
   **Include, Specific zone, solas33.com**.
5. Choose **Continue to summary**, then **Create Token**. Copy the value now. Cloudflare shows it once.

## Put it on the repository

In PowerShell on the founder PC:

    gh secret set CF_API_TOKEN --repo SOLAS33/frontier

Paste the token when prompted (the characters are hidden) and press Enter. Then run the job:

    gh workflow run live --repo SOLAS33/frontier
    gh run list --repo SOLAS33/frontier --limit 3

A green run with a "Deploy to Cloudflare" step means it worked. The variable `CF_ACCOUNT_ID` is already set.

## If you would rather reuse the existing token

`solas-github-deploy` is shown once at creation. If the value is saved, run `store-cf-token.ps1` and then
`set-cf-token.ps1 frontier`. Do not use **Roll** on that token unless you re-run `set-cf-token.ps1` for every site
repository afterwards, because rolling it invalidates the old value everywhere.
