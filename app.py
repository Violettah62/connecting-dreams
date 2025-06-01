# -*- coding: utf-8 -*-
"""app.py"""
from flask import Flask, render_template_string, request, url_for
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    image_url = url_for('static', filename='pic6.jpg')
    html = f"""
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
        body {{ font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }}
        header {{ background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }}
        nav {{ text-align: center; margin: 20px; }}
        nav a {{ margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }}
        section {{ margin: 20px; padding: 20px; background: white; border-radius: 8px;
                   box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        footer {{ text-align: center; padding: 10px; background: #00008b; color: white; }}
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
           brighter futures together.<br>
           <img src="{image_url}" alt="engaging session" style="width: 50%;">
           </p>
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
    pic1 = url_for('static', filename='pic1.jpg')
    pic2 = url_for('static', filename='pic2.jpg')
    pic3 = url_for('static', filename='pic3.jpg')
    pic4 = url_for('static', filename='pic4.jpg')
    html = f"""
    <!-- unchanged head and nav -->
    ...
    <p><b>Project 1: Tree Planting and Environmental Education</b><br>
    ...
    <img src="{pic1}" alt="Tree planting" style="width: 45%;">
    <img src="{pic2}" alt="Tree planting" style="width: 45%;"><br>
    <img src="{pic3}" alt="Tree planting" style="width: 45%;">
    <img src="{pic4}" alt="Tree planting" style="width: 45%;">
    ...
    """
    return render_template_string(html)

