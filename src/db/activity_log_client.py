from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from src.db.models.activity_log import ActivityLogModel
from src.db.declarative_base import Base


class ActivityLogClient:
    def __init__(self):
        try:
            # Path for docker
            engine = create_engine("sqlite:////sharedvolume/activity_log.db")
            Base.metadata.create_all(engine)

        except OperationalError:
            # Path for regular run
            engine = create_engine("sqlite:///activity_log.db")
            Base.metadata.create_all(engine)

        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session: Session = Session()

    @contextmanager
    def session_manager(self):
        try:
            yield self.session
            self.session.flush()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def add_row(self, action):
        with self.session_manager() as session:
            new_row = ActivityLogModel(
                time=datetime.now(),
                guild=action.guild,
                channel=action.channel,
                name=action.name,
                action=action.action,
                message=action.message,
            )
            session.add(new_row)

    def get_rows(self, limit=20, offset=0, _filter=None):
        with self.session_manager() as session:
            if _filter is None:
                rows = (
                    session.query(ActivityLogModel)
                    .order_by(ActivityLogModel.id.desc())
                    .offset(offset)
                    .limit(limit)
                )
            else:
                rows = (
                    session.query(ActivityLogModel)
                    .filter(_filter)
                    .order_by(ActivityLogModel.id.desc())
                    .offset(offset)
                    .limit(limit)
                )

            out = [str(r) + "\n" for r in rows]
            return "".join(out)
