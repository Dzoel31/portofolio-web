import os
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def create_circular_avatar(image_path, size=(240, 240)):
    """Creates a high-resolution circular cropped avatar keeping 100% natural authentic colors."""
    img = Image.open(image_path).convert("RGBA")
    img = img.resize(size, Image.Resampling.LANCZOS)
    
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    
    circular_img = Image.new("RGBA", size, (255, 255, 255, 0))
    circular_img.paste(img, (0, 0), mask=mask)
    
    # Refined border
    draw_border = ImageDraw.Draw(circular_img)
    draw_border.ellipse((1, 1, size[0]-2, size[1]-2), outline=(203, 213, 225, 255), width=3)
    
    temp_path = "temp_avatar.png"
    circular_img.save(temp_path, "PNG")
    return temp_path

def generate_pdf():
    pdf_path = "Portofolio_Dzulfikri_Adjmal.pdf"
    
    # 2 Pages Balanced Layout (Margins 32 pt)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=32,
        rightMargin=32,
        topMargin=32,
        bottomMargin=32
    )
    
    # Typography Styles
    name_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a')
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#334155')
    )
    
    lead_style = ParagraphStyle(
        'LeadText',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155')
    )
    
    contact_style = ParagraphStyle(
        'ContactText',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#64748b')
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=4,
        spaceAfter=3
    )
    
    card_title_style = ParagraphStyle(
        'CardTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=colors.HexColor('#0f172a')
    )
    
    card_badge_style = ParagraphStyle(
        'CardBadge',
        fontName='Helvetica-Bold',
        fontSize=6.8,
        leading=8.5,
        textColor=colors.HexColor('#475569')
    )
    
    card_desc_style = ParagraphStyle(
        'CardDesc',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )
    
    card_metric_style = ParagraphStyle(
        'CardMetric',
        fontName='Helvetica-Oblique',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor('#0f172a')
    )

    story = []
    
    # =========================================================================
    # PAGE 1: HEADER + FEATURED PROJECTS + EDUCATION
    # =========================================================================
    
    # 1. Header (Authentic Color Photo + Bio)
    avatar_path = create_circular_avatar("img/profile.jpg", size=(200, 200))
    avatar_img = RLImage(avatar_path, width=72, height=72)
    
    header_left = [
        Paragraph("<b>Dzulfikri Adjmal</b>", name_style),
        Spacer(1, 2),
        Paragraph("AI & Software Engineer Specialist &nbsp;|&nbsp; Ex-Intern Kementerian Keuangan RI", subtitle_style),
        Spacer(1, 4),
        Paragraph(
            "Mahasiswa Informatika UPN \"Veteran\" Jakarta (<b>IPK 3.90 / 4.00</b>) spesialisasi <b>Machine Learning, Agentic AI, dan MLOps</b>. "
            "Berpengalaman merancang end-to-end ML pipelines (TFX, Apache Beam), integrasi LLM dengan <b>Model Context Protocol (MCP)</b>, "
            "serta membangun sistem ekstraksi dokumen cerdas di Kementerian Keuangan RI.",
            lead_style
        ),
        Spacer(1, 4),
        Paragraph("✉ dzulfikriadjmal@gmail.com &nbsp;|&nbsp; 🔗 linkedin.com/in/dzulfikriadjmal &nbsp;|&nbsp; 💻 github.com/Dzoel31 &nbsp;|&nbsp; 🌐 dzoel31.github.io/portofolio-web", contact_style)
    ]
    
    header_table = Table([[header_left, avatar_img]], colWidths=[445, 85])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#e2e8f0'), spaceBefore=3, spaceAfter=6))
    
    # 2. Featured Projects (6 Major Projects)
    story.append(Paragraph("PROYEK REKAYASA UNGGULAN (ENGINEERING PROJECTS)", section_heading))
    story.append(Spacer(1, 2))
    
    projects = [
        {
            "title": "PDF & Audio Extractor Pipeline",
            "tags": "MAGANG KEMENKEU • NLP • PYTHON • PYTORCH",
            "desc": "Pipeline ekstraksi teks dokumen PDF dan transkripsi audio berbasis Python untuk memperkaya knowledge base chatbot KMS Chat di Kementerian Keuangan Learning Center.",
            "metric": "Mar - Jul 2025"
        },
        {
            "title": "Smart Hydroponic - IoT & Backend API",
            "tags": "FASTAPI • POSTGRESQL • TIMESCALEDB • DOCKER",
            "desc": "Layanan Backend API berbasis Python FastAPI untuk menerima telemetry data sensor IoT (suhu, kelembaban, pH, TDS), validasi Pydantic, dan time-series database TimescaleDB.",
            "metric": "Aug 2026"
        },
        {
            "title": "Smart Hydroponic - MCP Integration",
            "tags": "MCP PROTOCOL • MCP SERVER • AI TOOLING",
            "desc": "Server Model Context Protocol (MCP) untuk sistem hidroponik pintar. Memungkinkan LLM Agent memanggil tool otomatis untuk memantau data sensor.",
            "metric": "Aug 2026"
        },
        {
            "title": "KSM AIoT Bot Ecosystem (Nexo)",
            "tags": "MCP PROTOCOL • LLM AGENT • DOCKER & CI/CD",
            "desc": "Ekosistem AI Discord terpadu (WebHook Gateway dan Agent Orchestrator). Mengintegrasikan Model Context Protocol (MCP) untuk pemanggilan tool eksternal dan deployment Portainer.",
            "metric": "Jan - Feb 2026"
        },
        {
            "title": "Generative AI & Legal RAG System",
            "tags": "RAG SYSTEM • LANGCHAIN • VECTOR DB • LLM",
            "desc": "Sistem Retrieval-Augmented Generation (RAG) menggunakan fine-tuned LLM untuk menjawab pertanyaan berbasis konteks dokumen hukum perundang-undangan secara presisi.",
            "metric": "Jun 2026"
        },
        {
            "title": "MLOps & Machine Learning Pipeline",
            "tags": "MLOPS • TFX & APACHE BEAM • PROMETHEUS",
            "desc": "Arsitektur pipeline machine learning end-to-end menggunakan TensorFlow Extended (TFX) dan Apache Beam untuk Data Ingestion, Validation, Transformasi, serta model serving dengan Railway.",
            "metric": "Oct 2025"
        }
    ]
    
    project_cards = []
    for p in projects:
        card_content = [
            Paragraph(f"<b>{p['title']}</b>", card_title_style),
            Paragraph(f"<code>{p['tags']}</code>", card_badge_style),
            Spacer(1, 2),
            Paragraph(p['desc'], card_desc_style),
            Spacer(1, 2),
            Paragraph(p['metric'], card_metric_style)
        ]
        card_table = Table([[card_content]], colWidths=[258])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
            ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 7),
            ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ]))
        project_cards.append(card_table)
    
    project_grid_data = [
        [project_cards[0], project_cards[1]],
        [project_cards[2], project_cards[3]],
        [project_cards[4], project_cards[5]]
    ]
    project_grid = Table(project_grid_data, colWidths=[265, 265])
    project_grid.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(project_grid)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#e2e8f0'), spaceBefore=2, spaceAfter=5))
    
    # 3. Education & Key Experience (Compact Bento at bottom of Page 1)
    story.append(Paragraph("PENDIDIKAN & PENGALAMAN KERJA (EDUCATION & EXPERIENCE)", section_heading))
    story.append(Spacer(1, 2))
    
    edu_card = [
        Paragraph("<b>Universitas Pembangunan Nasional \"Veteran\" Jakarta</b>", card_title_style),
        Paragraph("S1 Informatika (Computer Science) &nbsp;|&nbsp; <b>IPK / GPA: 3.90 / 4.00</b>", card_desc_style),
        Paragraph("• Fokus Keahlian: Machine Learning, Artificial Intelligence, Big Data, & Software Engineering", card_desc_style)
    ]
    exp_card = [
        Paragraph("<b>Kementerian Keuangan RI (Pusintek / KLC)</b>", card_title_style),
        Paragraph("Data Science & AI Engineer Intern &nbsp;|&nbsp; Mar 2025 - Jul 2025", card_desc_style),
        Paragraph("• Merancang Pipeline Ekstraksi KMS Chat & benchmark performa knowledge base.", card_desc_style)
    ]
    
    edu_t = Table([[edu_card]], colWidths=[258])
    edu_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    exp_t = Table([[exp_card]], colWidths=[258])
    exp_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    
    page1_bottom = Table([[edu_t, exp_t]], colWidths=[265, 265])
    page1_bottom.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(page1_bottom)
    
    # =========================================================================
    # PAGE 2: PROFESSIONAL CERTIFICATIONS + DEEP TECHNICAL SKILLS TAXONOMY
    # =========================================================================
    story.append(PageBreak())
    
    story.append(Paragraph("SERTIFIKASI PROFESIONAL RESMI (OFFICIAL CERTIFICATIONS)", section_heading))
    story.append(Paragraph("Sertifikasi kompetensi terverifikasi industri yang diterbitkan oleh Dicoding Indonesia.", lead_style))
    story.append(Spacer(1, 4))
    
    certifications = [
        ("Pengembangan Generative AI Berbasis LLM", "Dicoding Indonesia • Arsitektur Transformer, RAG Systems, Fine-Tuning LLM (PEFT/QLoRA), Agentic AI Workflows (ReAct, CrewAI)"),
        ("Belajar Fundamental Deep Learning", "Dicoding Indonesia • Neural Networks dengan TensorFlow & Keras, NLP & Text Classification, Computer Vision, RNN & LSTM"),
        ("Machine Learning Operations (MLOps)", "Dicoding Indonesia • Automated ML Pipelines (TFX, Apache Beam), Data Ingestion & Validation, Model Serving Cloud REST API"),
        ("Machine Learning Terapan", "Dicoding Indonesia • Machine Learning System Design, Predictive Analytics, Recommendation Systems (Content-Based & Collaborative)"),
        ("Belajar Implementasi CI/CD dengan Jenkins", "Dicoding Indonesia • Continuous Integration & Automated Testing, Zero-Downtime Deployment, Infrastructure Monitoring, DevSecOps"),
        ("Prompt Engineering untuk Developer", "Dicoding Indonesia • Fundamental LLM Prompting, Chain-of-Thought, Few-Shot Prompting, Structured Output Optimization"),
        ("Belajar Analisis Data dengan Python", "Dicoding Indonesia • Descriptive Statistics, Data Cleansing & Wrangling, Exploratory Data Analysis (EDA) & Data Visualization"),
        ("Belajar Dasar AWS Cloud", "Dicoding Indonesia • Cloud Computing Fundamentals, Amazon EC2, S3, DynamoDB, VPC Networking, CloudWatch & Identity Management (IAM)")
    ]
    
    cert_cells = []
    for c_title, c_desc in certifications:
        c_content = [
            Paragraph(f"<b>{c_title}</b>", card_title_style),
            Paragraph(c_desc, card_desc_style)
        ]
        c_table = Table([[c_content]], colWidths=[258])
        c_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ffffff')),
            ('BOX', (0, 0), (-1, -1), 0.6, colors.HexColor('#e2e8f0')),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 7),
            ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ]))
        cert_cells.append(c_table)
        
    cert_grid_data = [
        [cert_cells[0], cert_cells[1]],
        [cert_cells[2], cert_cells[3]],
        [cert_cells[4], cert_cells[5]],
        [cert_cells[6], cert_cells[7]]
    ]
    cert_grid = Table(cert_grid_data, colWidths=[265, 265])
    cert_grid.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(cert_grid)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#e2e8f0'), spaceBefore=4, spaceAfter=8))
    
    # 5. Comprehensive Technical Skills Matrix
    story.append(Paragraph("TAKSONOMI KEAHLIAN TEKNIS (TECHNICAL SKILLS MATRIX)", section_heading))
    story.append(Spacer(1, 3))
    
    skill_categories = [
        ("Artificial Intelligence & LLM", "Machine Learning, Deep Learning, Large Language Models (LLM), RAG Systems, Model Context Protocol (MCP), LLM Inference (llama.cpp), LangChain, Hugging Face, PyTorch, TensorFlow, Scikit-Learn, Pandas, NumPy"),
        ("Backend & System Engineering", "Python (FastAPI, Flask, Asyncio, Pydantic, SQLAlchemy, Alembic), PostgreSQL, TimescaleDB (Time-series), MySQL, SQLite, PHP (Blade, OOP), RESTful API Design & High-Concurrency Architecture"),
        ("MLOps, DevOps & Cloud", "TensorFlow Extended (TFX), Apache Beam, Docker, Docker Compose, Jenkins CI/CD, Portainer (Webhook Auto-deploy), Prometheus, AWS Cloud Computing (EC2, S3, VPC), Linux / Bash Scripting, Git / GitHub"),
        ("IoT & Web Technologies", "ESP32 Firmware, IoT Telemetry Sensors (Suhu, pH, TDS, Kelembaban), HTML5, CSS3, JavaScript, Vue.js, Real-time Webhooks & Discord Bot APIs")
    ]
    
    skill_tables = []
    for cat_title, cat_skills in skill_categories:
        s_box = [
            Paragraph(f"<b>{cat_title}</b>", card_title_style),
            Spacer(1, 1),
            Paragraph(cat_skills, card_desc_style)
        ]
        s_table = Table([[s_box]], colWidths=[258])
        s_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
            ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        skill_tables.append(s_table)
        
    skills_grid_data = [
        [skill_tables[0], skill_tables[1]],
        [skill_tables[2], skill_tables[3]]
    ]
    skills_grid = Table(skills_grid_data, colWidths=[265, 265])
    skills_grid.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(skills_grid)
    story.append(Spacer(1, 6))
    
    footer_text = Paragraph("<font color='#64748b'>Dokumen Portofolio Resmi &bull; Dzulfikri Adjmal &bull; https://dzoel31.github.io/portofolio-web</font>", ParagraphStyle('Foot', fontName='Helvetica', fontSize=7.5, alignment=TA_CENTER))
    story.append(footer_text)
    
    # Build Document
    doc.build(story)
    
    # Clean up temp avatar
    if os.path.exists("temp_avatar.png"):
        os.remove("temp_avatar.png")
        
    print(f"Successfully generated {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
