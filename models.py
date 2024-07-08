import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from sqlalchemy.sql import func

db = SQLAlchemy()

class YoutubeTranscription(db.Model):
    __tablename__ = 'youtube_transcription'
    id = db.Column(db.String, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    contenido_transcription = db.Column(db.Text, nullable=False)
    contenido_html = db.Column(db.Text)
    fecha_inicio = db.Column(db.DateTime(timezone=True))
    fecha_final = db.Column(db.DateTime(timezone=True), server_default=func.now())
    uri = db.Column(db.String)
    imagen = db.Column(db.Text)
    meta_description = db.Column(db.String(100))