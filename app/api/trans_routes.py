from flask import Blueprint, jsonify, request
from app.models import db, Artist, Song, Translation
from flask_login import current_user, login_required
from app.forms import TransForm

translation_routes = Blueprint("translations", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages

@translation_routes.route("/<int:id>")
def translations(id):
    print('AHHHHHHHHHHHHHHHHHHHHH')
    translations = Translation.query.filter(Translation.songId == id).all()
    print('Translation', translations)
    return {
        "translation": [translation.to_dict() for translation in translations]
    }


@translation_routes.route("/", methods=["POST"])
def addTranslation():
    print('above')
    form = TransForm()
    print('below')
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        trans = Translation(
            translation=form.data['translation'],
            startIndex=form.data['startIndex'],
            stopIndex=form.data['stopIndex'],
            userId=form.data['userId'],
            songId=form.data['songId']
        )
        db.session.add(trans)
        db.session.commit()
        return trans.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
