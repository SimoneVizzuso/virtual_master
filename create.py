import argparse
from engine.characters.npc_generator import generate_npc_in_zone

def handle_create_npc(args):
    zone_name = args.zone
    npc = generate_npc_in_zone(zone_name)
    if npc:
        print("✅ NPC created:")
        print(f"Name: {npc.name}")
        print(f"Appearance: {npc.appearance}")
        print(f"Personality: {npc.personality}")
        print(f"Occupation: {npc.occupation}")
    else:
        print("⚠️ Failed to generate NPC.")

def main():
    parser = argparse.ArgumentParser(description="Virtual Master CLI content generator.")
    subparsers = parser.add_subparsers(dest="command")

    # create.py npc "Riftel"
    npc_parser = subparsers.add_parser("npc", help="Generate an NPC for a given zone")
    npc_parser.add_argument("zone", type=str, help="Zone name where the NPC will be located")
    npc_parser.set_defaults(func=handle_create_npc)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
