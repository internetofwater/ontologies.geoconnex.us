# Copyright 2026 Lincoln Institute of Land Policy
# SPDX-License-Identifier: MIT

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_NO_DEV=1

COPY ./loader/pyproject.toml ./loader/uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project

COPY ./loader/ ./
COPY ./*.ttl ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

CMD ["python", "/app/main.py"]