# kiprio MCP Server

[![PyPI](https://img.shields.io/pypi/v/kiprio-mcp)](https://pypi.org/project/kiprio-mcp/)
[![Python](https://img.shields.io/pypi/pyversions/kiprio-mcp)](https://pypi.org/project/kiprio-mcp/)
[![License](https://img.shields.io/github/license/ForeverTools/kiprio-mcp)](LICENSE)

**23 production APIs in one MCP package** — email validation, DNS/WHOIS, SSL inspection, web scraping, NLP, and developer utilities — usable by Claude, Cursor, Windsurf, and any [Model Context Protocol](https://modelcontextprotocol.io) client.

No third-party API keys required. Free tier included.

---

## Quick install

```bash
pip install kiprio-mcp
```

Add to your MCP client config:

```json
{
  "mcpServers": {
    "kiprio": {
      "command": "kiprio-mcp",
      "env": {"KIPRIO_API_KEY": ""}
    }
  }
}
```

**Claude Code** — run once in your project:

```bash
claude mcp add kiprio -- kiprio-mcp
```

Free tier works without a key. Get a free key for higher limits at [kiprio.com/docs](https://kiprio.com/docs/).

---

## What you can do

Once connected, ask Claude things like:

> *"Is noreply@company.io a real email address?"*
> → `validate_email` checks syntax, MX records, and disposable domain lists

> *"What tech stack is stripe.com running?"*
> → `tech_stack` returns CMS, CDN, analytics, and payment providers

> *"Take a screenshot of this URL and describe what you see."*
> → `screenshot_url` returns a base64 PNG Claude can analyse visually

> *"Redact all personal information from this support transcript."*
> → `redact_text` replaces emails, phones, names, and card numbers with `[REDACTED_TYPE]`

> *"Is this EU VAT number valid? GB123456789"*
> → `validate_vat` verifies via VIES and returns the registered company name

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
| Free (no key) | 30 requests/day/tool | $0 |
| Free (with key) | 100 requests/day/tool | $0 |
| Pro | 1,000 requests/day/tool | from $9/mo |
| Business | 10,000 requests/day/tool | from $39/mo |

Get a free key and manage usage at [kiprio.com/docs](https://kiprio.com/docs/).

---

## Claude Code setup

```bash
# Install and register in one step
pip install kiprio-mcp
claude mcp add kiprio -- kiprio-mcp

# Verify it's connected
claude mcp list
```

Or add `KIPRIO_API_KEY=your_key` to a `.env` and reference it in your MCP config.

---

## Troubleshooting

**`kiprio-mcp: command not found`** — your virtualenv's `bin/` isn't on PATH. Use the full path:
```json
"command": "/path/to/venv/bin/kiprio-mcp"
```

**`429 Rate limit exceeded`** — you've hit the free tier daily cap. Get a free key at [kiprio.com/docs](https://kiprio.com/docs/) to raise the limit to 100/day, or upgrade to Pro.

**`401/403 errors`** — your API key is invalid. Leave `KIPRIO_API_KEY` empty to use the anonymous free tier.

---

## Source

[github.com/ForeverTools/kiprio-mcp](https://github.com/ForeverTools/kiprio-mcp) — MIT licence.

Maintained by [ForeverTools](https://github.com/ForeverTools). APIs powered by [kiprio.com](https://kiprio.com).
