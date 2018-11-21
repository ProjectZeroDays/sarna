from flask_restful import Api, Resource, fields, marshal_with, abort

from sarna.core.auth import current_user
from sarna.model import Assessment


def init_app(app):
    api = Api(app)

    active_fields = {
        "name": fields.String()
    }

    assessment_fields = {
        "actives": fields.List(fields.Nested(active_fields)),
        "name": fields.String(),
        "status": fields.String()
    }

    class AssessmentResource(Resource):
        @marshal_with(Assessment.rest_fields())
        def get(self, assessment_id):
            assessment: Assessment = Assessment.query.filter_by(id=assessment_id).one()
            if not current_user.owns(assessment) and not current_user.manages(assessment.client):
                abort(403)

            return assessment

    api.add_resource(AssessmentResource, '/api/assessments/<int:assessment_id>')
