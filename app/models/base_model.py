from app import db
from sqlalchemy.sql import func


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.clock_timestamp(),
                           index=True)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.clock_timestamp(),
                           onupdate=func.clock_timestamp(), index=True)
    updated_by = db.Column(db.String)
    created_by = db.Column(db.String)
