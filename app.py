
# -*- coding: utf-8 -*-
"""app.py"""
from flask import Flask, render_template_string, request

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
      <meta name="google-site-verification" content="LBIuqR4BpR4-ddCXsmny00Hrrmg9jWSqd4gL_Bpbl_A" />
      <title>Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px;
                   box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
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
      <title>About - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px;
                   box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
      </style>
    </head>
    <body>
      <header>
        <h1>About Connecting Dreams Initiative</h1>
      </header>
      <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/projects">Projects</a> |
        <a href="/contact">Contact</a>
      </nav>
      <section>
        <h2>Our Journey</h2>
        <p>At Connecting Dreams Initiative, we believe that every student—regardless of background—deserves the opportunity to thrive in a digital, connected world.

Rooted in the rural communities of Western Kenya, our mission is to transform education by providing holistic support to high school students through academic mentorship, emotional guidance, community engagement, and digital empowerment.



What We Do
We work hand-in-hand with students, parents, teachers, and local leaders to bridge the educational gap in underserved areas. Our approach includes:

Personalized Mentorship: Supporting students not just academically, but emotionally and socially, through a strong network of mentors and peer leaders.

Community-Driven Research: Gathering local insights to create affordable, practical solutions for education challenges in rural Kenya.

Digital Literacy & Technology Integration: Equipping students with essential tech skills, then empowering them to teach others—building a sustainable cycle of peer learning.



Our Vision
We’re building more than just schools—we’re building self-sustaining, tech-enabled learning ecosystems. We’re introducing students to the worlds of coding, data science, and robotics in the near future.

Our future plans include:

Student-led coding and innovation clubs

Solar-powered tech hubs for continuous access to learning tools

Annual innovation challenges to solve real-world community problems

Mobile literacy units to train parents in digital skills and support at-home learning

Why It Matters
The digital divide remains one of the biggest barriers to education equity. In a world where opportunity is increasingly linked to technology, rural students can’t be left behind. That’s why we’re committed to providing tools, training, and mentorship to help them succeed—not just in school, but in life.

We also aim to work closely with the Ministry of Education and local authorities to influence national curriculum reforms and advocate for inclusive, tech-forward education policies.

Join Us
Whether you're a donor, educator, tech partner, or passionate volunteer—there’s a place for you in this movement.

Together, we can turn dreams into tangible futures and ensure that hope, talent, and innovation are never limited by geography.</p>
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
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px;
                   box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
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
        <h2>All Projects</h2>
        <p><b>Project 1: Tree Planting and Environmental Education</b><br>
<b>Timeline:</b> November 26 – January 15, 2024 <br>
 <b>Location:</b> Holy Family Musembe Secondary School <br>
 <b>Status:</b> Completed <br>
This project engaged over twenty students enrolled in the program in planting trees at Holy Family Musembe Secondary School. The goal was to instill environmental stewardship while offering practical, hands-on learning. Over 500 trees were planted during the December  school break through January, incorporating nature-based education into the students’ learning experience.
<br><b>Outcomes:</b>
<ul>
<li> Educated students on tree care and environmental conservation </li>

<li> Strengthened student collaboration and holiday engagement </li>

<li> Enhanced the school’s environment and promoted community pride </li>
</ul>

<b>Future Engagement:</b>
 Plans are underway to replicate this model in neighboring schools and to integrate it with climate education workshops, further promoting sustainability.
<img src="pictures/pic 1.jpg" alt="tree planting"style="width: 45%; height: auto;">
<img src="pictures/pic 2.jpg" alt="tree planting"style="width: 45%; height: auto;"> <br>
<img src="pictures/pic 3.jpg" alt="tree planting"style="width: 45%; height: auto;">
<img src="pictures/pic 4.jpg" alt="tree planting"style="width: 45%; height: auto;">

 <br> <br> <br>
<b>Project 2: Competency-Based Curriculum (CBC) Research and Advocacy</b><br>
<b>Timeline:</b> December 2024 – March 2025<br>
 <b>Location:</b> Musembe Village and Lugari Sub-County Schools<br>
 <b>Status:</b> Completed<br>
This study investigated the challenges faced by low-income families, teachers, and students under Kenya’s CBC. Using a comparative framework with education systems in Finland and the U.S., the research examined the real-world impact of CBC on rural communities and developed practical, community-informed policy recommendations.
<br><b>Outcomes:</b>
<ul>
<li>Highlighted socio-economic, infrastructural, and administrative barriers to CBC implementation</li>

<li>Documented adaptive strategies by families and teachers</li>

<li>Provided actionable recommendations on equity, funding, teacher training, and parental engagement</li>

<li>Presented findings to local stakeholders and educational policymakers</li>
</ul>

<b>Future Engagement:</b>
 The research will inform advocacy efforts to influence CBC implementation policies, guide new mentorship and infrastructure programs, and support the case for inclusive education reform in partnership with county governments and national education bodies.
<br> <br> <br>
<b>Project 3: Bridging the Digital Divide</b><br>
<b>Timeline:</b> May 2025 – Ongoing<br>
 <b>Location:</b> Musembe Secondary, Angayu High, and Mbajo Secondary Schools<br>
 <b>Status:</b> In Progress <br>
This ongoing project aims to address the critical lack of digital resources in rural schools. Through the deployment of 20 desktop computers and 3 Starlink satellite internet units, students and teachers are gaining access to digital tools for education. The program includes structured digital literacy training for students, teachers, and parents. It also incorporates peer-led learning, and socio-emotional mentorship supported by partner organizations.
<br><b>Outcomes (To Date):</b>
<ul>
<li>Digital literacy curriculum developed and deployed</li>

<li>Over 40 peer mentors trained across three schools</li>

<li>Starlink satellite internet installed, improving online access</li>

<li>Collaborations with KenSAP  and Shamiri Institute.</li>
</ul>

<b>Future Engagement:</b>
<ul>
<li>Introduction of coding and innovation clubs</li>

<li>Integration of gamified learning and AI-based educational tools</li>

<li>Launch of mobile digital literacy units for parents</li>

<li>Long-term policy collaboration with the Ministry of Education for national scaling.</li>
</ul>
</p>
      </section>
      <footer>
        <p>&copy; 2025 Connecting Dreams Initiative</p>
      </footer>
    </body>
    </html>
    """
    return render_template_string(html)

# Contact page
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
      <title>Contact - Connecting Dreams Initiative</title>
      <style>
        body { font-family: "Times New Roman", serif; margin: 0; padding: 0; background: #f0f8ff; }
        header { background: linear-gradient(to bottom, #add8e6, #00008b); color: white; padding: 20px; text-align: center; }
        nav { text-align: center; margin: 20px; }
        nav a { margin: 0 15px; text-decoration: none; color: #00008b; font-size: 18px; }
        section { margin: 20px; padding: 20px; background: white; border-radius: 8px;
                   box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        footer { text-align: center; padding: 10px; background: #00008b; color: white; }
        form { max-width: 600px; margin: auto; }
        input, textarea, button { width: 100%; padding: 10px; margin: 5px 0; }
        button { background: #00008b; color: white; border: none; cursor: pointer; }
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
        <form method="post">
          <input type="text" name="name" placeholder="Your Name" required>
          <input type="email" name="email" placeholder="Your Email" required>
          <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
          <button type="submit">Submit</button>
        </form>
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
