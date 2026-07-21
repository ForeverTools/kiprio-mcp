# kiprio-mcp — Glama evaluation Dockerfile.
# Installs from PyPI (same binary users install) and starts the MCP server over stdio.
# Glama builds this image and verifies tools/list responds correctly.
FROM python:3.11-slim

# Install from PyPI — matches the production package users install via pip/uvx.
RUN pip install --no-cache-dir "kiprio-mcp==0.3.3"

# Free tier works without a key; clients can override at runtime.
ENV KIPRIO_API_KEY=""

# kiprio-mcp speaks MCP over stdio (FastMCP.run()). Glama introspects via the protocol.
ENTRYPOINT ["kiprio-mcp"]
