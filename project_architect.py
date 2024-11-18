from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all() 

class ProjectResource(Resource):
    def get(self, project_id=None, user_id=None):
        if project_id:
            project = Project.query.get(project_id)
            if not project:
                return {'message': 'Project not found'}, 404
            return jsonify({'id': project.id, 'title': project.title, 'description': project.description, 'user_id': project.user_id})

        if user_id:
            projects = Project.query.filter_by(user_id=user_id).all()
            return jsonify([{'id': proj.id, 'title': proj.title, 'description': proj.description} for proj in projects])

        projects = Project.query.all()
        return jsonify([{'id': proj.id, 'title': proj.title, 'description': proj.description} for proj in projects])

    def post(self):
        data = request.get_json()
        new_project = Project(title=data['title'], description=data['description'], user_id=data['user_id'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created', 'id': new_project.id}), 201

    def put(self, project_id):
        data = request.get_json()
        project = Project.query.get(project_id)
        if not project:
            return {'message': 'Project not found'}, 404

        project.title = data['title']
        project.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Project updated'})

    def delete(self, project_id):
        project = Project.query.get(project_id)
        if not project:
            return {'message': 'Project not found'}, 404

        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted'})

class SearchResource(Resource):
    def get(self):
        query = request.args.get('q')
        projects = Project.query.filter(Project.title.contains(query) | Project.description.contains(query)).all()
        return jsonify([{'id': proj.id, 'title': proj.title, 'description': proj.description} for proj in projects])

# Роуты
api.add_resource(ProjectResource, '/projects', '/projects/<int:project_id>', '/projects/user/<int:user_id>')
api.add_resource(SearchResource, '/search')

if __name__ == '__main__':
    app.run(debug=True)