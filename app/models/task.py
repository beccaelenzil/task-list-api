from flask import current_app
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime)

    def make_json(self):
        if not self.completed_at:
            is_complete = False
        else:
            is_complete = self.completed_at

        return {
            "title": self.title,
            "description": self.description,
            "is_complete": is_complete
        }
