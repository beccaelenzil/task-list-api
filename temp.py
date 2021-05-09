class Task
    #attributes

    def make_json(self):
        if self.completed_at == None:
            is_complete = False
        else:
            is_complete = True

        return {
            "task": {
                "id": 1,
                "title": "A Brand New Task",
                "description": self.description,
                "is_complete": is_complete
            }
        }

#routes
task.make_json()