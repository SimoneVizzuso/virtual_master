from sqlmodel import select
from db.session import get_session
from db.models import NPC

def create_npc(name: str, appearance: str, personality: str, occupation: str, zone_id: int):
    with get_session() as session:
        existing = session.exec(select(NPC).where(NPC.name == name)).first()
        if existing:
            print(f"NPC '{name}' già esistente.")
            return existing
        new_npc = NPC(
            name=name,
            appearance=appearance,
            personality=personality,
            occupation=occupation,
            zone_id=zone_id
        )
        session.add(new_npc)
        session.commit()
        session.refresh(new_npc)
        print(f"NPC '{name}' creato.")
        return new_npc

def get_npcs_in_zone(zone_id: int):
    with get_session() as session:
        return session.exec(select(NPC).where(NPC.zone_id == zone_id)).all()

def get_npc(name: str):
    with get_session() as session:
        return session.exec(select(NPC).where(NPC.name == name)).first()