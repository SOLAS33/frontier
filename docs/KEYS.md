# Keys and secrets, in one list

Nothing is requested until every site is ready. Then these go in together.

| Name | Where | Used for | Status |
|---|---|---|---|
| CF_API_TOKEN | repo secret | Lets the 3-hourly workflow redeploy. Create it as in CLOUDFLARE-TOKEN.md | placeholder |
| CF_ACCOUNT_ID | repo variable | Cloudflare account | set |
| SEC_CONTACT_EMAIL | repo secret | Contact in the SEC User-Agent (fair access) | set to hello@solas33.com |
| BREVO_API_KEY | repo secret | Weekly digest email (not wired yet) | not requested |
| FRONTIER_INDEXABLE | repo variable | Not needed: indexing is on in config.toml | not used |

Contact addresses used on the pages: hello@solas33.com (primary), dmcdtkofc@outlook.com (alternate). Both are in config.toml.
