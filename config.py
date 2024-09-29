
import os
class Config:
    # Database settings...
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:gftiuHVFiCBXtTvrNNhpdxhGNiDDOwrr@junction.proxy.rlwy.net:32654/railway')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-string'
    
    # Email settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =  'afuya.b@gmail.com'
    MAIL_PASSWORD = 'gbgx legm mbpl eoif' 
    MAIL_DEFAULT_SENDER = 'afuya.b@gmail.com'
