<div style="display: flex; justify-content: center; align-items: center;">
  <img
    src="https://docs.arcade.dev/images/logo/arcade-logo.png"
    style="width: 300px;"
  >
</div>
<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px;">
  <img src="https://img.shields.io/github/v/release/spartee/arcade_memory" alt="GitHub release" style="margin: 0 2px;">
  <img src="https://img.shields.io/badge/python-3.10%2C3.11%2C3.12%2C3.13%2C3.14-blue.svg" alt="Python version" style="margin: 0 2px;">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License" style="margin: 0 2px;">
  <img src="https://img.shields.io/pypi/v/arcade_memory" alt="PyPI version" style="margin: 0 2px;">
</div>
<div style="display: flex; justify-content: center; align-items: center;">
  <a href="https://github.com/spartee/arcade-llm-memory" target="_blank">
    <img src="https://img.shields.io/github/stars/spartee/arcade-llm-memory" alt="GitHub stars" style="margin: 0 2px;">
  </a>
  <a href="https://github.com/spartee/arcade-llm-memory/fork" target="_blank">
    <img src="https://img.shields.io/github/forks/spartee/arcade-llm-memory" alt="GitHub forks" style="margin: 0 2px;">
  </a>
</div>

<br>
<br>

# Arcade Memory Toolkit

Arcade Memory Toolkit is a toolkit for managing semantic memory of LLM apps through a collection of tools.

## Features

-   Storage and retrieval of semantic memories with vector embeddings
-   Support for OpenAI and Anthropic embeddings
-   Redis and RedisVL used for vector storage

## Install

Install this toolkit using pip:

```bash
pip install arcade_memory
```

## Available Tools

| Tool Name | Description |
| --------- | ----------- |
| Memory.StoreSummarizedInformation      | Store summarized information in Redis along with its vector embedding.        |
| Memory.SearchSummarizedInformation      | Query stored summaries in Redis by embedding similarity to the given query. |
