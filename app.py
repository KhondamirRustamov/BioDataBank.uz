from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from random import randint

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


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/jamoamiz', methods=['POST', 'GET'])
def team():
    text=''
    if request.method == 'POST':
        text='Mana'
        return render_template('team.html', text=text)
    else:
        return render_template('team.html', text=text)


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/report')
def report():
    return render_template('report.html')


@app.route('/flora-uz', methods=['POST', 'GET'])
def flora():
    species = ''
    a = ''
    b = ''
    d = ''
    text = ''
    floras = Flora.query.all()

    if request.method == 'POST':
        species = "Ushbu tur O'zbekiston florasida uchramaydi"
        text = str(request.form['text'])
        method = str(request.form['metod'])
        if method == 'Tur nomi (lotin)':
            try:
                for i in floras:
                    if text.lower() in str(i.spec).lower() or text.lower() in str(i.synonim).lower():
                        a = '000'
                        species = Flora.query.get(i.id)
                        text = None, text
                        v = '+'.join(str(species.spec).split(' ')[:2])
                        r1 = str('http://www.theplantlist.org/tpl/search?q=' + v)
                        r2 = str('http://apps.kew.org/herbcat/getHomePageResults.do?homePageSearchText=' + v)
                        r3 = str('https://www.ncbi.nlm.nih.gov/search/all/?term=' + v)
                        r4 = str('https://www.gbif.org/species/search?via=data.gbif.org&dataset_key=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&q=' + v)
                        r5 = str('https://www.google.com/search?q=%22{}%22&tbm=isch'.format(v))
                        r = r1, r2, r3, r4, r5
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, d=d, r=r)

                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = None, text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d= '00'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

        elif method == 'Tur nomi (rus)':
            try:
                for i in floras:
                    if text.lower() in str(i.russian).lower():
                        a = '00'
                        species = Flora.query.get(i.id)
                        text = None, text
                        v = '+'.join(str(species.spec).split(' ')[:2])
                        r1 = str('http://www.theplantlist.org/tpl/search?q=' + v)
                        r2 = str('http://apps.kew.org/herbcat/getHomePageResults.do?homePageSearchText=' + v)
                        r3 = str('https://www.ncbi.nlm.nih.gov/search/all/?term=' + v)
                        r4 = str('https://www.gbif.org/species/search?via=data.gbif.org&dataset_key=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&q=' + v)
                        r5 = str('https://www.google.com/search?q=%22{}%22&tbm=isch'.format(v))
                        r = r1, r2, r3, r4, r5
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, d=d, r=r)
                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = None, text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d = '000'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

        elif method == "Tur nomi (o'zbek)":
            try:
                for i in floras:
                    if text.lower() in str(i.uzbek).lower():
                        a = '00'
                        species = Flora.query.get(i.id)
                        text = None, text
                        v = '+'.join(str(species.spec).split(' ')[:2])
                        r1 = str('http://www.theplantlist.org/tpl/search?q=' + v)
                        r2 = str('http://apps.kew.org/herbcat/getHomePageResults.do?homePageSearchText=' + v)
                        r3 = str('https://www.ncbi.nlm.nih.gov/search/all/?term=' + v)
                        r4 = str('https://www.gbif.org/species/search?via=data.gbif.org&dataset_key=d7dddbf4-2cf0-4f39-9b2a-bb099caae36c&q=' + v)
                        r5 = str('https://www.google.com/search?q=%22{}%22&tbm=isch'.format(v))
                        r = r1, r2, r3, r4, r5
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, d=d, r=r)
                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = None, text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d = '00'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

        elif method == "Turkum nomi (lotin)":
            try:
                for i in floras:
                    if text.lower() in str(i.genus).lower():
                        b = '00'
                        species = Flora.query.filter_by(genus=str(Flora.query.get(i.id).genus))
                        text = 'Turkum:', text
                        c = species.count()
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, c=c, d=d)
                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = 'Turkum:', text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d = '00'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

        elif method == "Turkum nomi (rus)":
            try:
                for i in floras:
                    if text.lower() == str(i.rod).lower():
                        b = '00'
                        species = Flora.query.filter_by(genus=str(Flora.query.get(i.id).genus))
                        c = species.count()
                        text = 'Turkum:', text
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, c=c, d=d)
                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = 'Turkum:', text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d = '00'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

        elif method == "Oila nomi (lotin)":
            try:
                for i in floras:
                    if text.lower() in str(i.family).lower():
                        b = '00'
                        species = Flora.query.filter_by(family=str(Flora.query.get(i.id).family))
                        text = 'Oila:', text
                        c = species.count()
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, c=c, d=d)
                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = 'Oila:', text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d = '00'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

        elif method == "Oila nomi (rus)":
            try:
                for i in floras:
                    if text.lower() in str(i.familyru).lower():
                        b = '00'
                        species = Flora.query.filter_by(family=str(Flora.query.get(i.id).family))
                        text = 'Oila:', text
                        c = species.count()
                        return render_template('flora.html', spec=species, a=a, b=b, text=text, c=c, d=d)
                    else:
                        if i.id >= 4414:
                            d = '00'
                            text = 'Oila:', text
                            return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)
            except:
                d = '00'
                return render_template('flora.html', spec=species, a=a, b=b, d=d, text=text)

    else:
        z = []
        for i in range(9):
            z1 = Flora.query.get(randint(0, 4413))
            z.append(z1)
        return render_template('flora.html', spec=species, a=a, b=b, z=z, d=d, text=text)


if __name__ == "__main__":
    app.run(debug=False)
