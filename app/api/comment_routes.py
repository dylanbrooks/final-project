from flask import Blueprint, jsonify, request
from app.models import db, Comment
from flask_login import current_user, login_required
from app.forms import CommentForm

comment_routes = Blueprint("comments", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@comment_routes.route("/<int:id>")
def comments(id):
    print('AHHHHHHHHHHHHHHHHHHHHH')
    comments = Comment.query.filter(Comment.songId == id).all()
    print('Comment', comments)
    return {
        "comment": [comment.to_dict() for comment in comments]
    }


@comment_routes.route("/", methods=["POST"])
def addComment():
    print('above')
    form = CommentForm()
    print('below')
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        comment = Comment(
            comment=form.data['comment'],
            userId=form.data['userId'],
            songId=form.data['songId']
        )
        db.session.add(comment)
        db.session.commit()
        return comment.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
