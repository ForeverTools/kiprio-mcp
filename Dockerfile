# kiprio-mcp — MCP server for kiprio.com developer APIs.
# Glama builds this image, starts the container, and verifies the server responds to
# MCP introspection (tools/list) over stdio. No ports/HTTP needed — MCP is stdio here.
FROM python:3.11-slim

WORKDIR /app

# Install the package (pulls deps: mcp>=1.0.0, httpx>=0.27.0) + the `kiprio-mcp` entrypoint.
COPY pyproject.toml README.md LICENSE kiprio_mcp.py /app/
RUN pip install --no-cache-dir .

# Free tier works without a key; clients can override at runtime.
ENV KIPRIO_API_KEY=""

# kiprio-mcp speaks MCP over stdio (mcp.run()). Glama introspects via the protocol.
ENTRYPOINT ["kiprio-mcp"]
