from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID, uuid4

@dataclass
class Document:
    id: UUID
    title: str
    content: str
    created_at: datetime

    @classmethod
    def create(cls, title: str, content: str) -> "Document":
        return cls(
            id=uuid4(),
            title=title.strip(),
            content=content.strip(),
            created_at=datetime.utcnow(),
        )

@dataclass
class Chunk:
    id: UUID
    document_id: UUID
    chunk_index: int
    content: str
    created_at: datetime

    @classmethod
    def create(
        cls,
        document_id: UUID,
        chunk_index: int,
        content: str,
    ) -> "Chunk":
        return cls(
            id=uuid4(),
            document_id=document_id,
            chunk_index=chunk_index,
            content=content.strip(),
            created_at=datetime.now(timezone.utc),
        )