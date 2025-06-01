# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="description" content="Empowering rural students in Kenya through digital literacy, mentorship, and technology through research and verified data.">
      <meta name="keywords" content="Connecting Dreams Initiative, Kenya, digital literacy, student empowerment">
      <meta name="author" content="Connecting Dreams Initiative">
      <title>Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; background: #f0f8ff; margin: 0; padding: 0; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>Connecting Dreams Initiative</h1>
        <p>Every Dream Can Thrive</p>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Welcome</h2>
        <p>Our mission is to empower rural students in Kenya through comprehensive digital literacy, mentorship, and technology-driven learning by leveraging research and feasible evidence-based intervention. Join us as we transform rural education and build brighter futures together.</p>
        <img src="{{ url_for('static', filename='pic6.jpg') }}" alt="engaging session" style="width: 50%;">
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# About page (original content)
@app.route("/about")
def about():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>About Us - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; background: #f0f8ff; margin: 0; padding: 0; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>About Us</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Who We Are</h2>
        <p>Connecting Dreams Initiative (CDI) Kenya is a grassroots organization passionate about bridging the opportunity divide in rural Kenya. We focus on empowering students through Digital Literacy, Mentorship, and Research & Evaluation programs that are contextualized, inclusive, and evidence-based.</p>
        <p>Our team is composed of young professionals and university students who believe in the power of youth-driven change. Since our inception, we’ve impacted hundreds of students across multiple counties, building capacity and hope one school at a time.</p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Projects page
@app.route("/projects")
def projects():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Projects - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; background: #f0f8ff; margin: 0; padding: 0; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        img { max-width: 100%; border-radius: 10px; margin-top: 10px; }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>Our Projects</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>1. Digital Literacy</h2>
        <p>We equip students with essential 21st-century digital skills by conducting interactive training sessions in rural schools. Our curriculum includes computer basics, internet navigation, and responsible digital citizenship.</p>
        <img src="{{ url_for('static', filename='pic1.jpg') }}" alt="Digital Literacy Program">

        <h2>2. Mentorship</h2>
        <p>We run mentorship programs connecting university student volunteers and professionals with high school learners. These sessions focus on academic excellence, career awareness, self-confidence, and goal-setting.</p>
        <img src="{{ url_for('static', filename='pic2.jpg') }}" alt="Mentorship Session">

        <h2>3. Research & Evaluation</h2>
        <p>We conduct research to understand the real challenges facing learners in rural Kenya. Our data informs evidence-based interventions and helps measure the impact of our programs.</p>
        <img src="{{ url_for('static', filename='pic3.jpg') }}" alt="Research and Community Evaluation">
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Contact page
@app.route("/contact")
def contact():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Contact Us - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; background: #f0f8ff; margin: 0; padding: 0; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>Contact Us</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Get in Touch</h2>
        <p><strong>Email:</strong> <a href="mailto:malafuthwahir3@gmail.com">malafuthwahir3@gmail.com</a></p>
        <p><strong>WhatsApp:</strong> <a href="https://wa.me/19099648648" target="_blank">+1 (909) 964-8648</a></p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
