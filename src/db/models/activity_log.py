from sqlalchemy import Column, Integer, String, DATETIME
from src.db.declarative_base import Base


class ActivityLogModel(Base):
    __tablename__ = "ActivityLog"
    id = Column(Integer, primary_key=True)
    time = Column(DATETIME)
    guild = Column(String)
    channel = Column(String)
    name = Column(String)
    action = Column(String)
    message = Column(String)

    def __repr__(self):
        return (
            "['%s'] guild='%s', channel='%s', name='%s', action='%s', message='%s'"
            % (
                self.time,
                self.guild,
                self.channel,
                self.name,
                self.action,
                self.message,
            )
        )
