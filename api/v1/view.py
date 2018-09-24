from flask import Blueprint, jsonify
import logging

post_bp = Blueprint('post_v1', __name__)
logger = logging.getLogger('posts')

@post_bp.route('/', methods=['GET'])
def posts():
    return jsonify({'post':"first_post"}), 200