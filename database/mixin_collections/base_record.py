from database.database_session import session, Base

from sqlalchemy_mixins.serialize import SerializeMixin
from sqlalchemy_mixins.repr import ReprMixin
from sqlalchemy_mixins.smartquery import SmartQueryMixin
from sqlalchemy_mixins.activerecord import ActiveRecordMixin
from sqlalchemy import func, Column, TIMESTAMP


class AlchemyMixin(
    Base, ActiveRecordMixin, ReprMixin, SmartQueryMixin, SerializeMixin
):
    __abstract__ = True
    __repr__ = ReprMixin.__repr__

    created_at = Column(
        "created_at",
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at = Column(
        "updated_at",
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

AlchemyMixin.set_session(session)
