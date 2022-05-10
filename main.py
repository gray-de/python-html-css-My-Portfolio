from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/skills')
def soft_skills():
    return render_template("soft-skills.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/ru')
def main_ru():
    return render_template("index-ru.html")

@app.route('/about-ru')
def about_ru():
    return render_template("about-ru.html")

@app.route('/skills-ru')
def skills_ru():
    return render_template("soft-skills-ru.html")

@app.route('/portfolio-ru')
def portfolio_ru():
    return render_template("portfolio-ru.html")

@app.route('/contacts-ru')
def contacts_ru():
    return render_template("contacts-ru.html")

if __name__ == "__main__":
    app.run(debug=True)