"""
Content for the Streamlit profile app, kept separate from the UI in app.py.

Edit values here to update the site. Leave a link as "" to hide it:
the app never shows placeholder or dead links.
"""

PROFILE = {
    "name": "Laxmi Kumari",
    "brand": "LAXMI.EXE",
    "tagline": "Building Beyond Boundaries",
    "titles": ["Software Developer", "Full-Stack Engineer", "AI & Backend"],
    "role": "Development Engineer",
    "organisation": "Standard Chartered",
    "education": "B.Tech, Mechanical Engineering · IIT (BHU) Varanasi",
    "intro": [
        "I'm a **Software Developer** who enjoys turning complex requirements into clean, reliable software.",
        "I graduated from **IIT (BHU) Varanasi** with a B.Tech in Mechanical Engineering. I now work as a "
        "**Development Engineer at Standard Chartered**, building full-stack applications and data-automation tools.",
        "My focus is **backend engineering with Java and Spring Boot**, **full-stack products with React**, and "
        "**AI-driven applications**. I like working across the whole lifecycle: designing the architecture, "
        "building and debugging, testing, and shipping.",
    ],
}

LINKS = {
    "github": "https://github.com/laxmik0799",
    "linkedin": "",  # TODO: add your LinkedIn URL
    "email": "",  # TODO: add your contact email
    "repo": "https://github.com/laxmik0799/laxmi-kumari-developer-profile",
}

SKILLS = {
    "Languages": ["Java", "Python", "C++", "JavaScript", "SQL"],
    "Backend": ["Spring Boot", "REST APIs", "Spring Data JPA", "Hibernate"],
    "Frontend": ["React.js", "HTML", "CSS", "Material UI", "Streamlit"],
    "Databases": ["PostgreSQL", "H2"],
    "Tools": ["Git", "GitHub", "Azure DevOps", "VS Code", "Maven", "Swagger", "GitHub Copilot"],
    "Data & Automation": ["Pandas", "Excel automation", "Data quality automation", "Data modelling", "ETL concepts"],
}

EXPERIENCE = [
    {
        "title": "Development Engineer",
        "org": "Standard Chartered",
        "status": "Current",
        "summary": "Working on full-stack and data-automation projects, including the two featured below.",
        "points": [
            "**Full-stack development:** a banking relationship-management application built with React.js and "
            "Material UI on the front end and Java Spring Boot on the back end, connected by REST APIs and backed "
            "by H2 and PostgreSQL.",
            "**Data automation:** a Python solution that automates mapping and validation between a DTP Mapping "
            "Sheet, a Physical Data Model and the latest TDM template, with a Streamlit front end.",
        ],
    }
]

PROJECTS = {
    "Wealth Core RM": {
        "icon": "🏦",
        "category": "Full-Stack",
        "tagline": "Banking relationship-management application",
        "image": "assets/images/wealth-core-rm.png",
        "diagram": "diagrams/wealth-core-architecture.png",
        "doc": "projects/wealth-core-rm/README.md",
        "stack": ["React.js", "Material UI", "Java", "Spring Boot", "REST APIs", "H2", "PostgreSQL"],
        "problem": "Relationship managers work across many tasks: client portfolios, products, service requests, "
        "statements, advice, documents and notifications. Spreading these across disconnected tools slows them down.",
        "objective": "Bring the relationship manager's core workflows into one web application: a React interface "
        "backed by a Java Spring Boot service layer that exposes REST APIs.",
        "features": {
            "Dashboard": "Overview for the relationship manager",
            "Clients": "Client and portfolio views",
            "Products": "Product management",
            "Requests": "Service requests",
            "Statements": "Client statements",
            "Advice": "Advice workflows",
            "Downloads": "Documents and exports",
            "Notifications": "Alerts and updates",
        },
        "contributions": [
            "Worked across the stack: React.js and Material UI on the front end, Java Spring Boot on the back end",
            "REST API development and frontend–backend integration",
            "Database work with H2 and PostgreSQL",
        ],
        "workflow": """
            digraph {
              rankdir=LR; bgcolor="transparent";
              node [shape=box, style="rounded,filled", fillcolor="#0b1024", color="#8b5cf6", fontcolor="#e2e8f0", fontname="Helvetica"];
              edge [color="#22d3ee", fontcolor="#94a3b8", fontname="Helvetica", fontsize=10];
              U [label="Relationship\\nmanager", shape=ellipse, color="#22d3ee"];
              UI [label="React + MUI\\ninterface"];
              API [label="Spring Boot\\nREST API"];
              SVC [label="Business logic"];
              JPA [label="Spring Data JPA"];
              DB [label="H2 / PostgreSQL", shape=cylinder, color="#a78bfa"];
              U -> UI; UI -> API [label="REST / JSON"]; API -> SVC; SVC -> JPA; JPA -> DB;
            }
        """,
    },
    "TDM Automation": {
        "icon": "⚙️",
        "category": "Data & Automation",
        "tagline": "Automated data mapping, validation and TDM template generation",
        "image": "assets/images/tdm-automation.png",
        "diagram": "diagrams/tdm-automation-architecture.png",
        "doc": "projects/tdm-automation/README.md",
        "stack": ["Python", "Pandas", "Excel automation", "Streamlit"],
        "problem": "Maintaining a Transformational Data Model (TDM) means reconciling a DTP Mapping Sheet, a Physical "
        "Data Model (PDM) and the latest TDM template. Done by hand, cross-checking mappings, spotting discrepancies "
        "and identifying new attributes is slow, repetitive and error-prone.",
        "objective": "Automate the mapping and validation between the DTP Mapping Sheet, the PDM and the latest TDM "
        "template, and produce review-ready outputs through a simple interface.",
        "features": {
            "Excel processing": "Read and automate workbooks with Python",
            "Mapping": "Source-to-target attribute mapping",
            "Validation": "Discrepancy identification",
            "Comparison": "Proposed mappings vs existing TDM",
            "Discovery": "New attributes and pipelines",
            "TDM Buffer": "Generated automatically",
            "Reports": "Review reports and Excel outputs",
            "Interface": "Streamlit front end",
        },
        "contributions": [
            "Developed the Python automation for mapping and validation across the DTP Mapping Sheet, PDM and TDM template",
            "Implemented source-to-target mapping, validation and discrepancy identification",
            "Built the comparison against the existing TDM, including detection of new attributes and pipelines",
            "Generated the TDM Buffer, review reports and Excel outputs",
            "Developed the Streamlit front end and integrated it with the automation backend",
        ],
        "workflow": """
            digraph {
              rankdir=LR; bgcolor="transparent";
              node [shape=box, style="rounded,filled", fillcolor="#0b1024", color="#8b5cf6", fontcolor="#e2e8f0", fontname="Helvetica"];
              edge [color="#22d3ee", fontname="Helvetica"];
              A [label="DTP Mapping Sheet", color="#22d3ee"];
              B [label="Physical Data Model", color="#22d3ee"];
              C [label="Latest TDM Template", color="#22d3ee"];
              S [label="Streamlit UI", shape=ellipse, color="#22d3ee"];
              P [label="Python automation\\nmapping · validation · comparison"];
              O1 [label="TDM Buffer", color="#a78bfa"];
              O2 [label="Review reports", color="#a78bfa"];
              O3 [label="Excel outputs", color="#a78bfa"];
              A -> P; B -> P; C -> P; S -> P [label="run", fontcolor="#94a3b8", fontsize=10];
              P -> O1; P -> O2; P -> O3;
            }
        """,
    },
}

SIDE_PROJECTS = [
    {
        "name": "Cosmic Voyage",
        "summary": "Interactive 3D Solar System explorer built with React Three Fiber and GSAP.",
        "live": "https://cosmic-voyage-teal.vercel.app/",
        "code": "https://github.com/laxmik0799/cosmic-voyage",
    }
]

INTERESTS = [
    ("🧱", "Backend engineering", "Java, Spring Boot, clean architecture and maintainable APIs"),
    ("🌐", "Full-stack development", "React front ends integrated with robust backend services"),
    ("🧭", "System design", "Scalable architectures and distributed systems"),
    ("🤖", "AI-driven applications", "LLM integration and AI-powered products"),
    ("🗄️", "Data engineering", "Data quality automation, data modelling and ETL"),
]

CAREER_GOALS = [
    "Become a strong backend / software engineer",
    "Build deep expertise in Java and Spring Boot",
    "Master system design and distributed systems",
    "Develop full-stack applications independently",
    "Learn AI / LLM integration and build AI-powered products",
    "Strengthen DSA and problem-solving skills",
    "Build a strong software engineering portfolio",
    "Explore freelance software development",
]

STATS_CARDS = [
    ("profile-summary-card-output/tokyonight/0-profile-details.svg", "Profile details and contributions"),
    ("profile-summary-card-output/tokyonight/3-stats.svg", "GitHub stats"),
    ("profile-summary-card-output/tokyonight/2-most-commit-language.svg", "Most committed languages"),
]
