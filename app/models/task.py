from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'))

    def to_json(self):
        if self.completed_at:
            completed = True
        else:
            completed = False

        return {
            "id": self.task_id,
            "title": self.title,
            "goal_id": self.goal_id,
            "description": self.description,
            "is_complete": completed,
        }