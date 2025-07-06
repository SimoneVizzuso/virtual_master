from sqlmodel import select
from db.session import get_session
from db.models import Zone, ZoneConnection

def create_zone(name: str, description: str):
    with get_session() as session:
        existing = session.exec(select(Zone).where(Zone.name == name)).first()
        if existing:
            print(f"Zona '{name}' già esistente.")
            return existing
        new_zone = Zone(name=name, description=description)
        session.add(new_zone)
        session.commit()
        session.refresh(new_zone)
        print(f"Zona '{name}' creata.")
        return new_zone

def connect_zones(from_zone_name: str, to_zone_name: str):
    with get_session() as session:
        from_zone = session.exec(select(Zone).where(Zone.name == from_zone_name)).first()
        to_zone = session.exec(select(Zone).where(Zone.name == to_zone_name)).first()
        if not from_zone or not to_zone:
            print("Una delle zone non esiste.")
            return
        existing = session.exec(
            select(ZoneConnection).where(
                ZoneConnection.from_zone_id == from_zone.id,
                ZoneConnection.to_zone_id == to_zone.id
            )
        ).first()
        if existing:
            print("Connessione già esistente.")
            return
        connection = ZoneConnection(from_zone_id=from_zone.id, to_zone_id=to_zone.id)
        session.add(connection)
        session.commit()
        print(f"Connessione creata: {from_zone.name} → {to_zone.name}")

def get_zone(name: str):
    with get_session() as session:
        return session.exec(select(Zone).where(Zone.name == name)).first()

def list_connections(zone_name: str):
    with get_session() as session:
        zone = session.exec(select(Zone).where(Zone.name == zone_name)).first()
        if not zone:
            print(f"Nessuna zona trovata con nome: {zone_name}")
            return []
        connections = session.exec(
            select(ZoneConnection).where(ZoneConnection.from_zone_id == zone.id)
        ).all()
        result = []
        for conn in connections:
            target = session.exec(select(Zone).where(Zone.id == conn.to_zone_id)).first()
            if target:
                result.append(target.name)
        return result