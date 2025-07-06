from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class ZoneConnection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    from_zone_id: int = Field(foreign_key="zone.id")
    to_zone_id: int = Field(foreign_key="zone.id")

    from_zone: Optional["Zone"] = Relationship(back_populates="connections_from", sa_relationship_kwargs={"foreign_keys": "[ZoneConnection.from_zone_id]"})
    to_zone: Optional["Zone"] = Relationship(back_populates="connections_to", sa_relationship_kwargs={"foreign_keys": "[ZoneConnection.to_zone_id]"})

class Zone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    parent_zone_id: Optional[int] = Field(default=None, foreign_key="zone.id")

    # Relazioni
    connections_from: List[ZoneConnection] = Relationship(back_populates="from_zone", sa_relationship_kwargs={"foreign_keys": "[ZoneConnection.from_zone_id]"})
    connections_to: List[ZoneConnection] = Relationship(back_populates="to_zone", sa_relationship_kwargs={"foreign_keys": "[ZoneConnection.to_zone_id]"})

class NPC(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    appearance: str
    personality: str
    occupation: str
    zone_id: int = Field(foreign_key="zone.id")