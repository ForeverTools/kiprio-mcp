# kiprio MCP Server

MCP server exposing [kiprio.com](https://kiprio.com) developer APIs as tools for Claude, Cursor, and any Model Context Protocol client.

**27 tools** covering email validation, DNS/network, web scraping, text processing, language utilities, and developer utilities.

## Install

```bash
pip install kiprio-mcp
```

Or from source:

```bash
git clone https://github.com/ForeverTools/kiprio-mcp
cd kiprio-mcp
pip install -e .
```

## Configure (Claude Desktop / Claude Code)

Add to your MCP client config (e.g. `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "kiprio": {
      "command": "kiprio-mcp",
      "env": {"KIPRIO_API_KEY": "your_key_or_leave_empty"}
    }
  }
}
```

Free tier works without a key (rate-limited). Get a key at [kiprio.com/docs](https://kiprio.com/docs/).

## Tools

**Email & validation:** `validate_email`, `validate_vat`, `validate_iban`, `check_password_breach`
**Network/DNS:** `dns_lookup`, `whois_lookup`, `ssl_check`, `ip_lookup`
**Web & content:** `readability`, `tech_stack`, `parse_og_tags`, `screenshot_url`, `html_to_pdf`
**Language:** `sentiment_analysis`, `check_grammar`, `translate_text`, `summarize_text`, `redact_text`
**Utilities:** `generate_qr`, `generate_hash`, `generate_uuid`, `parse_cron`, `decode_jwt`

Full schema is auto-discovered by your MCP client.

## License

MIT — see [LICENSE](LICENSE).

Maintained by [ForeverTools](https://github.com/ForeverTools).
