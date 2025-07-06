# Virtual Master

Virtual Master is a local, open-source AI-powered Dungeon Master designed to simulate a consistent and dynamic world for tabletop RPGs like Dungeons & Dragons. The system uses local LLMs to generate content, manage story logic, and react to player decisions.

---

## Overview

The project aims to simulate a persistent world with:

- Zone and world generation
- Character and NPC creation
- Dynamic storytelling with consistent memory
- Randomized mechanics (e.g., dice rolls)
- Full offline support and reproducibility

---

## Directory Structure

```
virtual_master/
├── db/              # Database models and session config
├── engine/          # Core logic: zone, NPC, world, combat systems
├── prompts/         # Prompt templates for AI
├── main.py          # Entry point (WIP)
├── create.py        # Scripts for generating world elements
└── requirements.txt # Python dependencies
```

---

## Setup

1. Create a virtual environment

```bash
python -m venv .venv
```

2. Activate it

- Windows:
```bash
.venv\Scripts\activate
```

- Linux/macOS:
```bash
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Planned Features

- NPC dialogue generation
- Player-driven exploration
- Combat and encounter logic
- Quest and objective generation
- Inventory and spell systems
- Map and world structure via graph traversal
- Save and load full game state

---

## Requirements

- Python 3.10+
- SQLite
- Ollama (for local LLM execution)
- Optional: Stable Diffusion for image generation

---

## License

This project is released under the MIT License.