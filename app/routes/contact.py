from flask import Blueprint, request, jsonify
from flask_mail import Message
from app import mail

bp = Blueprint('contact', __name__)

@bp.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Create the email message
    msg = Message(
        subject=f"New message from {name}",
        sender=email,
        recipients=["afuyaah@gmail.com"], 
        body=f"Message from {name} ({email}):\n\n{message}"
    )

    try:
        # Send the email
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
