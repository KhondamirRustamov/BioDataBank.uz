from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from random import randint
import pandas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'

db = SQLAlchemy(app)


class Flora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.Text)
    familyru = db.Column(db.Text)
    genus = db.Column(db.Text)
    body = db.Column(db.Text)
    rod = db.Column(db.Text)
    spec = db.Column(db.Text)
    ipni = db.Column(db.Text)
    russian = db.Column(db.Text)
    uzbek = db.Column(db.Text)
    synonim = db.Column(db.Text)
    lifestyle = db.Column(db.Text)
    area = db.Column(db.Text)
    areal = db.Column(db.Text)
    uzbekistan = db.Column(db.Text)
    endemism = db.Column(db.Text)
    status = db.Column(db.Text)
    using = db.Column(db.Text)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Flora %r>' % self.id


table = pandas.read_excel('UzFl1.xlsx')
df = pandas.DataFrame(table)
print(df['FAMILY'][0])


for i in range(4414):
    new_spec = Flora(family = df['FAMILY'][i], familyru = df['FAMILYRU'][i],
                    genus = df['GENUS'][i], body = 'FLORA',
                    rod = df['ROD'][i], spec = df['SPECIES'][i],
                    ipni = df['IPNI'][i], russian = df['RUSSIAN'][i],
                    uzbek = df['UZBEK'][i], synonim = df['SYNONIMS'][i],
                    lifestyle = df['LIFESTYLE'][i], area = df['AREA'][i],
                    areal = df['AREAL'][i], uzbekistan = df['UZBEKISTAN'][i],
                    endemism = df['ENDEMISM'][i], status = df['STATUS'][i],
                    using = df['USING'][i], comment = df['COMMENT'][i])
    try:
        db.session.add(new_spec)
        db.session.commit()
    except:
        print('Error')
