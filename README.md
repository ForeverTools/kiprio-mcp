<!-- mcp-name: com.kiprio/kiprio-mcp -->
# kiprio MCP Server

[![PyPI](https://img.shields.io/pypi/v/kiprio-mcp)](https://pypi.org/project/kiprio-mcp/)
[![Downloads](https://img.shields.io/pypi/dm/kiprio-mcp)](https://pypi.org/project/kiprio-mcp/)
[![Python](https://img.shields.io/pypi/pyversions/kiprio-mcp)](https://pypi.org/project/kiprio-mcp/)
[![License](https://img.shields.io/github/license/ForeverTools/kiprio-mcp)](LICENSE)
[![MCP Compatible](https://img.shields.io/badge/MCP-compatible-blue)](https://modelcontextprotocol.io)

**23 production API tools for Claude Code, Claude Desktop, Cursor, Cline, Continue, and any [MCP](https://modelcontextprotocol.io) client** — email validation, DNS/WHOIS, SSL inspection, web scraping, NLP, and developer utilities.

No third-party API keys required. Free tier included. Powered by [kiprio.com](https://kiprio.com).

---

## Quick install

```bash
pip install kiprio-mcp
```

**Claude Code** — add to your project in one step:

```bash
claude mcp add kiprio -- kiprio-mcp
```

Or add to `~/.claude.json` / Claude Desktop / Cursor / Windsurf / Zed:

```json
{
  "mcpServers": {
    "kiprio": {
      "command": "kiprio-mcp",
      "env": {"KIPRIO_API_KEY": "your_key_here"}
    }
  }
}
```

**Cline (VS Code)** — open Cline → MCP Servers → Add Server → paste:

```json
{
  "mcpServers": {
    "kiprio": {
      "command": "kiprio-mcp",
      "env": {"KIPRIO_API_KEY": "your_key_here"}
    }
  }
}
```

**Continue.dev** — add to `~/.continue/config.json` under `mcpServers`:

```json
{
  "mcpServers": [
    {
      "name": "kiprio",
      "command": "kiprio-mcp",
      "env": {"KIPRIO_API_KEY": "your_key_here"}
    }
  ]
}
```

### Get your free API key (takes 30 seconds)

The anonymous tier is rate-limited to **30 requests/day per tool** — fine for one-off queries, but it runs out fast in any automated workflow.

**A free registered key gives you 100 req/day per tool at zero cost:**

👉 **[kiprio.com/signup](https://kiprio.com/signup?ref=kiprio-mcp)** — no credit card, no trial period.

---

## What you can do

Once connected, ask Claude naturally:

> *"Is noreply@company.io a real deliverable address?"*
> → `validate_email` checks syntax, MX records, and disposable domain lists

> *"What tech stack is stripe.com running?"*
> → `tech_stack` returns CMS, CDN, analytics, and payment providers

> *"Take a screenshot of this landing page and flag any broken layout."*
> → `screenshot_url` returns a base64 PNG Claude can analyse directly

> *"Redact all PII from this support transcript before I send it to Zendesk."*
> → `redact_text` replaces emails, phones, names, and card numbers with `[REDACTED_TYPE]`

> *"Check the SSL certificate on api.example.com — is it expiring soon?"*
> → `ssl_check` returns expiry date, issuer, and grade

---

## Building an automated agent?

kiprio tools are designed for pipelines and hooks, not just one-shot queries. Common patterns:

**Email validation before accepting signups:**
```
User submits email
→ Claude: validate_email("user@example.com")
→ If disposable/invalid → reject early, before DB write
```

**Domain monitoring hook (Claude Code slash command):**
```bash
# Add to CLAUDE.md as a custom slash command
/check-ssl  →  ssl_check on all domains in config/domains.txt
```

**Lead enrichment agent:**
```
CSV of company domains
→ Claude loops: tech_stack() + whois_lookup() + ip_lookup() per row
→ Output: enriched CSV with stack, registrar, country, hosting provider
```

**Content moderation pipeline:**
```
User-submitted text
→ sentiment_analysis() to flag negative
→ redact_text() to strip PII before logging
```

These patterns work within the free key tier (100 req/day per tool). Pro tier (1,000/day) handles larger batches.

---

## Tools

### Email & Validation
| Tool | What it does |
|------|-------------|
| `validate_email` | Syntax + MX record check + disposable domain detection |
| `validate_vat` | EU VAT number validation via VIES, returns company name |
| `validate_iban` | IBAN validation + bank details |
| `check_password_breach` | k-anonymity breach check — only a 5-char SHA1 prefix is sent |

### Network & DNS
| Tool | What it does |
|------|-------------|
| `dns_lookup` | Query A, AAAA, MX, TXT, NS, CNAME, SOA records |
| `whois_lookup` | Domain registrar, creation/expiry dates, nameservers |
| `ssl_check` | Certificate validity, expiry, issuer, SANs |
| `ip_lookup` | Geolocation + VPN/Tor/datacenter detection with threat score |

### Web & Content
| Tool | What it does |
|------|-------------|
| `readability` | Extract main article text and metadata from any URL |
| `tech_stack` | Detect CMS, framework, CDN, analytics, payments |
| `parse_og_tags` | Open Graph, Twitter Card, and meta tags from a URL |
| `screenshot_url` | Full-page or viewport screenshot → base64 PNG |
| `html_to_pdf` | Convert HTML to PDF → base64 bytes |

### Text Processing
| Tool | What it does |
|------|-------------|
| `sentiment_analysis` | positive/negative/neutral label + compound score (−1 to 1) |
| `check_grammar` | Rewrite for grammar/spelling + diff of edits; styles: concise, formal, friendly, UK-en, US-en |
| `translate_text` | Translate between languages with auto source detection |
| `summarize_text` | Extract key points (configurable sentence count) |
| `redact_text` | Replace PII with `[REDACTED_TYPE]` placeholders |

### Developer Utilities
| Tool | What it does |
|------|-------------|
| `generate_qr` | QR code → base64 PNG or SVG; custom colours and size |
| `generate_hash` | Hash string with sha256, sha512, sha1, md5, sha3_256, or blake2b |
| `generate_uuid` | Generate UUID v1, v4, or v7 |
| `parse_cron` | Parse a cron expression → next 5 run times + human description |
| `decode_jwt` | Decode JWT header + payload + expiry status (no verification) |

---

## Rate limits

| Tier | Limit | Cost |
|------|-------|------|
| Anonymous (no key) | **30 req/day/tool** | $0 |
| **Free key** | **100 req/day/tool** | **$0** — [sign up](https://kiprio.com/signup?ref=kiprio-mcp) |
| **Pro** | **1,000 req/day/tool** | **$9/mo** |
| Business | 10,000 req/day/tool | $39/mo |

**Free key vs anonymous:** Same tools, 3× the headroom, still $0. Just needs an email address.

[Get your free key at kiprio.com/signup →](https://kiprio.com/signup?ref=kiprio-mcp)

### When to upgrade to Pro

- **Batch processing** — validating 500 emails, enriching a CSV, running a link audit
- **Scheduled agents** — Claude Code hooks that fire on every commit or cron job
- **Team workspaces** — multiple developers sharing one config
- **Production scripts** — slash commands that run on every file save or PR

[Upgrade to Pro at kiprio.com →](https://kiprio.com/products/mcp-server/)

---

## Claude Code setup

```bash
pip install kiprio-mcp
claude mcp add kiprio -- kiprio-mcp
claude mcp list   # should show kiprio
```

With API key in your project `.env`:
```bash
echo "KIPRIO_API_KEY=your_key" >> .env
```

Then reference in your MCP config:
```json
{
  "mcpServers": {
    "kiprio": {
      "command": "kiprio-mcp",
      "env": {"KIPRIO_API_KEY": "${KIPRIO_API_KEY}"}
    }
  }
}
```

---

## Troubleshooting

**`kiprio-mcp: command not found`** — use the full path from your virtualenv:
```json
"command": "/path/to/venv/bin/kiprio-mcp"
```

**`429 Rate limit exceeded`** — free anonymous tier hit. Register at [kiprio.com/signup](https://kiprio.com/signup?ref=kiprio-mcp) for 100 req/day free, or [upgrade to Pro](https://kiprio.com/products/mcp-server/) for 1,000/day.

**`401/403 errors`** — API key invalid. Leave `KIPRIO_API_KEY` empty to use the anonymous tier (30 req/day).

---

## Source

[github.com/ForeverTools/kiprio-mcp](https://github.com/ForeverTools/kiprio-mcp) — MIT licence.

Maintained by [ForeverTools](https://github.com/ForeverTools). APIs powered by [kiprio.com](https://kiprio.com).
