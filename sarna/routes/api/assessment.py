from flask_restful import Resource, abort, marshal_with, Api

from sarna.core.auth import current_user
from sarna.model import Assessment


def init_api(api: Api):
    api.add_resource(AssessmentResource, '/assessments/<int:assessment_id>')


class AssessmentResource(Resource):
    @marshal_with(Assessment.rest_fields())
    def get(self, assessment_id):
        assessment: Assessment = Assessment.query.filter_by(id=assessment_id).one()
        if not current_user.owns(assessment) and not current_user.manages(assessment.client):
            abort(403)

        return assessment
