# -*- coding: utf-8 -*-
"""app.py"""
from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)

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
      <meta name="google-site-verification" content="LBIuqR4BpR4-ddCXsmny00Hrrmg9jWSqd4gL_Bpbl_A" />
      <title>Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
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
           mentorship, and technology-driven learning by leveraging research and feasible evidence based intervention. Join us as we transform rural education and build
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

@app.route("/about")
def about():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>About Us</title>
    </head>
    <body>
      <h2>About Connecting Dreams Initiative Kenya</h2>
      <p>Connecting Dreams Initiative Kenya is part of a global initiative focused on enabling sustainable development through student-led community projects. Our chapter is dedicated to improving digital literacy and access to education in rural areas of Kenya.</p>
      <img src="{{ url_for('static', filename='pic1.jpg') }}" alt="Team Activity" style="width: 300px;">
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/projects")
def projects():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Our Projects</title>
    </head>
    <body>
      <h2>Our Projects</h2>
      <p>We have initiated several projects focused on education and empowerment, including:</p>
      <ul>
        <li>Digital Literacy Workshops</li>
        <li>Mentorship Programs</li>
        <li>Community Outreach Events</li>
      </ul>
      <img src="{{ url_for('static', filename='pic2.jpg') }}" alt="Workshop" style="width: 300px;">
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        thank_you = """
        <!DOCTYPE html>
        <html lang="en">
        <head><meta charset="UTF-8"><title>Thank You</title></head>
        <body>
          <h2>Thank you for getting in touch!</h2>
          <p>We appreciate your message and will respond shortly.</p>
          <p><a href="/">Back to Home</a></p>
        </body>
        </html>
        """
        return render_template_string(thank_you)

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Contact Us</title>
    </head>
    <body>
      <h2>Contact Us</h2>
      <form action="/contact" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Send">
      </form>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
