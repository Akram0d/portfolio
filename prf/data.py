"""All portfolio content lives here. Edit this file to update the site."""

PROFILE = {
    "name": "Akram Odeh",
    "full_name": "Akram Mohammad Odeh",
    "title": "Software engineer building AI tools and backend systems",
    "bio": (
        "I'm a software engineer from Palestine with a BA in Computer Science from "
        "An-Najah National University. I currently lead technical support at Jawwal "
        "and build AI tools for the team. Before that, I worked on backend systems as "
        "an intern at Jaffa.Net Software."
    ),
    "location": "Nablus, Palestine",
    "resume": "media/Resume.pdf",
    "links": [
        {"label": "LinkedIn", "url": "https://www.linkedin.com/in/akram-odeh-a46877316/", "icon": "fa-brands fa-linkedin"},
        {"label": "GitHub", "url": "https://github.com/Akram0d", "icon": "fa-brands fa-github"},
        {"label": "Facebook", "url": "https://www.facebook.com/abochloe", "icon": "fa-brands fa-facebook"},
    ],
}

# TODO: replace the highlights below with your real, specific achievements.
EXPERIENCE = [
    {
        "role": "Technical Support Manager & AI Developer",
        "company": "Jawwal",
        "place": "Nablus",
        "start": "Mar 2026",
        "end": "Present",
        "current": True,
        "highlights": [
            "Lead the technical support team and own escalated issues.",
            "Build AI-powered tools that speed up and automate support work.",
        ],
    },
    {
        "role": "Technical Support Specialist",
        "company": "Jawwal",
        "place": "Nablus",
        "start": "Nov 2025",
        "end": "Mar 2026",
        "current": False,
        "highlights": [
            "Diagnosed and resolved technical issues for customers and internal teams.",
        ],
    },
    {
        "role": "Backend Developer Intern",
        "company": "Jaffa.Net Software",
        "place": "Ramallah",
        "start": "Feb 2025",
        "end": "Jun 2025",
        "current": False,
        "highlights": [
            "Worked with the software team on backend development tasks.",
        ],
    },
]

SKILLS = [
    {"group": "Python and AI", "items": ["Django", "TensorFlow", "REST APIs", "Pandas", "NumPy"]},
    {"group": "Web development", "items": ["Angular", "TypeScript", "RxJS", "Bootstrap", "Tailwind"]},
    {"group": "Java and backend", "items": ["Java", "Spring Boot", "Hibernate", "REST APIs"]},
    {"group": "Databases", "items": ["SQL", "PostGIS", "Supabase"]},
    {"group": "Tools", "items": ["Git", "Postman", "Figma"]},
    {"group": "Other languages", "items": ["C", "C++", "Assembly (x86, MIPS)"]},
    {"group": "Languages spoken", "items": ["Arabic (native)", "English (fluent, IELTS 9)"]},
]

EDUCATION = [
    {"years": "2025", "title": "AI Programming with Python and TensorFlow Nanodegree",
     "where": "Online, sponsored by Palestine Launchpad and Google"},
    {"years": "2021 to 2024", "title": "BA in Computer Science",
     "where": "An-Najah National University, Nablus"},
    {"years": "2018 to 2019", "title": "Kotlin Programming Course",
     "where": "Palestinian Ministry of Education"},
    {"years": "2017 to 2020", "title": "High School",
     "where": "Kafr Thulth Secondary Boys School, Qalqilya"},
    {"years": "2016 to 2018", "title": "English Access Microscholarship Program",
     "where": "American Consulate program, Qalqilya"},
]

PROJECTS = [
    {
        "title": "GeeksHub",
        "subtitle": "Graduation project",
        "image": "media/geekshub.webp",
        "tech": ["Django", "Angular"],
        "tags": "web",
        "featured": True,
        "description": (
            "A platform that connects job candidates with recruiters. Includes user "
            "authentication, resource sharing, AI-powered training modules, and "
            "candidate-to-opportunity matching."
        ),
        "demo_video": "media/demo.mp4",
    },
    {
        "title": "InForm",
        "subtitle": "Gym management platform",
        "image": "media/inform.webp",
        "tech": ["Spring Boot", "Angular"],
        "tags": "web ai backend",
        "featured": True,
        "description": (
            "A web platform for a gym manager with exercises, nutrition plans, and "
            "messaging. Adds role management, personal plans, and a trained AI "
            "assistant for fitness questions."
        ),
        "code": "https://github.com/Akram0d/InForm",
    },
    {
        "title": "Worker Service Platform",
        "subtitle": "Services marketplace",
        "image": "media/workP.webp",
        "tech": ["Django", "Bootstrap"],
        "tags": "web",
        "featured": True,
        "description": (
            "Users register to find or offer services. Includes authentication, "
            "role-based access, and searchable contact listings."
        ),
        "code": "https://github.com/Akram0d/Worker-Service",
    },
    {
        "title": "Class Booking System",
        "subtitle": "Backend API",
        "image": "media/classbooking.webp",
        "tech": ["Spring Boot", "MySQL"],
        "tags": "backend",
        "featured": False,
        "description": (
            "A backend for booking classes with teachers. Role-based access for "
            "students and teachers, REST APIs, and MySQL persistence."
        ),
        "code": "https://github.com/Akram0d/ClassBooking",
    },
    {
        "title": "Flower Image Classifier",
        "subtitle": "Udacity nanodegree project",
        "image": "media/flower.webp",
        "tech": ["Python", "TensorFlow"],
        "tags": "ai",
        "featured": False,
        "description": (
            "An image classifier that identifies flower species from photos, built "
            "with Python and TensorFlow."
        ),
        "code": "https://github.com/Akram0d/Image-Classifier",
    },
]
