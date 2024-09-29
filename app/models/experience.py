from .. import db

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'role': self.role,
            'duration': self.duration,
            'description': self.description
        }
