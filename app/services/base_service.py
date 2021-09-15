from app import db


class BaseService(object):
    model = None

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def save_changes(data, auto_commit=True):
        db.session.add(data)
        if auto_commit:
           db.session.commit()

    @classmethod
    def get_details(self, **kwargs):
        return self.model.query.filter_by(**kwargs).first()

    @staticmethod
    def commit_changes():
        db.session.commit()

    @staticmethod
    def delete(obj, auto_commit=True):
        db.session.delete(obj)
        if auto_commit:
            db.session.commit()

