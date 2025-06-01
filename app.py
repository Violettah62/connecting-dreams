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
        <p>Our mission is to empower rural students in Kenya through comprehensive digital literacy,
           mentorship, and technology-driven learning by leveraging research and feasible evidence-based intervention. Join us as we transform rural education and build
           brighter futures together.</p>
        <img src="{{ url_for('static', filename='pic6.jpg') }}" alt="engaging session" style="width: 50%;">
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# About page
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
        <p>The Connecting Dreams Initiative (CDI) is a grassroots youth-led movement that champions inclusive education, digital equity, and community empowerment in underserved regions of Kenya. Our programs blend data-driven research, grassroots leadership, and youth mentorship to close opportunity gaps in rural education.</p>

        <p>Founded in 2023 by passionate university students and young professionals, CDI works closely with schools, parents, and policymakers to co-create innovative learning solutions that reflect local realities.</p>

        <p>Our values are grounded in equity, integrity, sustainability, and a deep belief that every dream can thrive with the right support.</p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Projects page (already implemented previously)
@app.route("/projects")
def projects():
    # [Keep the full existing content with url_for('static', filename='pic1.jpg') as previously shared]
    # For brevity, omitted here since you have it already and confirmed it's okay.
    return render_template_string("{{ Full projects page HTML here }}")  # Replace with your full projects HTML.

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
