from flask import jsonify
from app.obe import obe


@obe.route('/mkdir', methods=['GET'])
def obe_mkdir():
    return jsonify({'message': 'Directory created successfully'}), 200
