# Fast, batteries-included uv image with Python
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

# Create a workspace
WORKDIR /workspace

# Optional: speed up builds by caching uv's global cache between runs
ENV UV_CACHE_DIR=/root/.cache/uv

# Default to bash
CMD ["bash"]
