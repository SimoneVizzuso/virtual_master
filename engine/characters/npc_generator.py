import json
import re
import subprocess
import yaml
from pathlib import Path

from engine.characters.npc_manager import create_npc
from engine.world.zone_manager import get_zone

PROMPT_FILE = Path("prompts/templates.yaml")

def load_prompt(template_name: str, **kwargs) -> str:
    with open("prompts/templates.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    template = data[template_name]
    if isinstance(template, dict) and "template" in template:
        template = template["template"]
    return template.format(**kwargs)


def extract_json(text: str) -> str | None:
    match = re.search(r'\{.*}', text, re.DOTALL)
    return match.group(0) if match else None

def query_ollama(prompt: str, model: str = "qwen3:8b") -> str:
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

def generate_npc_in_zone(zone_name: str, model: str = "qwen3:8b"):
    zone = get_zone(zone_name)
    if not zone:
        print(f"Zone '{zone_name}' not found.")
        return None

    prompt = load_prompt("npc_generation", zone_name=zone.name)
    raw_output = query_ollama(prompt, model=model)

    json_str = extract_json(raw_output)
    if not json_str:
        print("No JSON found in model output. Raw output:")
        print(raw_output)
        return None

    try:
        npc_data = json.loads(json_str)
    except json.JSONDecodeError:
        print("Failed to parse JSON. Raw string:")
        print(json_str)
        return None

    npc = create_npc(
        name=npc_data["name"],
        appearance=npc_data["appearance"],
        personality=npc_data["personality"],
        occupation=npc_data["occupation"],
        zone_id=zone.id
    )
    return npc
