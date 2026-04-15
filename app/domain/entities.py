from dataclasses import dataclass
from datetime import datetime
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