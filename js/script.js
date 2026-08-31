document.addEventListener('DOMContentLoaded', function () {
    // 1. Dictionary Translasi (Bahasa Indonesia & English)
    const translations = {
        id: {
            nav_home: "Beranda",
            nav_project: "Project",
            nav_sertifikat: "Sertifikat",
            nav_profile: "Tentang Saya",
            hero_badge: '<i class="fa-solid fa-brain"></i> AI & MLOps Specialist | Ex-Intern Kemenkeu RI',
            hero_greeting: 'Halo, Saya <br><span>Dzulfikri Adjmal</span>',
            hero_lead: 'Mahasiswa Informatika UPN "Veteran" Jakarta (IPK 3.90/4.00) spesialisasi <strong>Machine Learning, AI, dan MLOps</strong>. Berpengalaman merancang end-to-end ML pipelines, mengintegrasikan LLM dengan <strong>Model Context Protocol (MCP)</strong>, serta berkontribusi nyata pada efisiensi sistem di Kementerian Keuangan RI.',
            btn_projects: '<i class="fa-solid fa-rocket"></i> Lihat Project',
            btn_cv: '<i class="fa-solid fa-arrow-up-right-from-square"></i> Preview CV (Resume)',
            btn_contact: '<i class="fa-solid fa-user"></i> Kontak & Bio',
            metric_gpa_label: "IPK UPNVJ (GPA)",
            metric_projects_label: "Proyek AI & Software",
            metric_certs_label: "Sertifikasi Resmi",
            project_title: "Project Unggulan",
            project_subtitle: "Kumpulan proyek terbaik di bidang AI Agent (MCP), RAG System, MLOps, IoT, Web Development, dan DevOps.",
            filter_all: "Semua Proyek",
            filter_ai: "AI & LLM / MCP",
            filter_devops: "MLOps & DevOps",
            filter_iot: "IoT",
            filter_web: "Web & Backend",
            detail_project: 'Detail Project <i class="fa-solid fa-arrow-right"></i>',
            cert_title: "Sertifikasi Profesional (Dicoding)",
            cert_subtitle: "Koleksi sertifikat kelulusan resmi di bidang Generative AI, Machine Learning, Deep Learning, MLOps, DevOps, & Cloud Computing.",
            profile_title: "Tentang Saya",
            profile_subtitle: "Latar belakang pendidikan, statistik, dan kontak profesional.",
            bio_heading: "Biodata & Pendidikan",
            bio_univ_label: "Universitas",
            bio_major_label: "Program Studi",
            bio_major_val: "S1 Informatika (Computer Science)",
            bio_gpa_label: "IPK / GPA",
            bio_exp_label: "Pengalaman",
            bio_exp_val: "Ex-Data Science Intern @ Kementerian Keuangan RI",
            skills_heading: "Keahlian Utama (Technical Skills)",
            
            // Descriptions
            desc_pdf: "Pipeline ekstraksi teks dokumen PDF dan transkripsi audio berbasis Python untuk memperkaya knowledge base chatbot KMS Chat di Kementerian Keuangan Learning Center.",
            desc_hydro_backend: "Layanan Backend API berbasis Python FastAPI untuk menerima telemetry data sensor IoT (suhu, kelembaban, pH, TDS), validasi Pydantic, migrasi Alembic, serta manajemen database time-series di TimescaleDB.",
            desc_hydro_mcp: "Server Model Context Protocol (MCP) untuk sistem hidroponik pintar. Memungkinkan LLM Agent memanggil tool otomatis untuk memantau data sensor.",
            desc_nexo: "Ekosistem AI Discord terpadu (WebHook Gateway dan Agent Orchestrator). Mengintegrasikan Model Context Protocol (MCP) untuk pemanggilan tool eksternal secara dinamis dan automated zero-downtime deployment melalui integrasi dengan WebHook Portainer.",
            desc_rag: "Sistem Retrieval-Augmented Generation (RAG) menggunakan fine-tuned Large Language Model (LLM) untuk menjawab pertanyaan berbasis konteks dokumen hukum secara presisi.",
            desc_mlops: "Arsitektur pipeline machine learning menggunakan TensorFlow Extended (TFX) dan Apache Beam (Data Ingestion, Validation, Transformation, serta model serving dengan Railway).",
            desc_constructify: "Proyek UAS mata kuliah Pemrograman Web: platform e-commerce pengadaan bahan bangunan dengan katalog produk dan manajemen pemesanan."
        },
        en: {
            nav_home: "Home",
            nav_project: "Projects",
            nav_sertifikat: "Certificates",
            nav_profile: "About Me",
            hero_badge: '<i class="fa-solid fa-brain"></i> AI & MLOps Specialist | Ex-Intern Ministry of Finance RI',
            hero_greeting: 'Hi, I\'m <br><span>Dzulfikri Adjmal</span>',
            hero_lead: 'Undergraduate Computer Science student at UPN Veteran Jakarta (GPA 3.90/4.00), specializing in <strong>Machine Learning, AI, and MLOps</strong>. Experienced in designing end-to-end ML pipelines, integrating LLMs with <strong>Model Context Protocol (MCP)</strong>, and driving system cost efficiency at the Ministry of Finance RI.',
            btn_projects: '<i class="fa-solid fa-rocket"></i> View Projects',
            btn_cv: '<i class="fa-solid fa-arrow-up-right-from-square"></i> Preview CV (Resume)',
            btn_contact: '<i class="fa-solid fa-user"></i> Contact & Bio',
            metric_gpa_label: "UPNVJ GPA",
            metric_projects_label: "AI & Software Projects",
            metric_certs_label: "Verified Certifications",
            project_title: "Featured Projects",
            project_subtitle: "Collection of top projects in AI Agents (MCP), RAG Systems, MLOps, IoT, Web Development, & DevOps.",
            filter_all: "All Projects",
            filter_ai: "AI & LLM / MCP",
            filter_devops: "MLOps & DevOps",
            filter_iot: "IoT",
            filter_web: "Web & Backend",
            detail_project: 'View Project <i class="fa-solid fa-arrow-right"></i>',
            cert_title: "Professional Certifications (Dicoding)",
            cert_subtitle: "Official completion certificates in Generative AI, Machine Learning, Deep Learning, MLOps, DevOps, & Cloud Computing.",
            profile_title: "About Me",
            profile_subtitle: "Educational background, statistics, and professional contact info.",
            bio_heading: "Bio & Education",
            bio_univ_label: "University",
            bio_major_label: "Major",
            bio_major_val: "B.S. in Computer Science (Informatika)",
            bio_gpa_label: "GPA",
            bio_exp_label: "Experience",
            bio_exp_val: "Ex-Data Science Intern @ Ministry of Finance RI",
            skills_heading: "Technical Skills",
            
            // Descriptions
            desc_pdf: "Python-based text extraction pipeline and automatic audio transcription to enrich the knowledge base for the KMS Chat chatbot at the Ministry of Finance Learning Center.",
            desc_hydro_backend: "Python FastAPI Backend API service for ingesting IoT sensor telemetry data (temperature, humidity, pH, TDS), Pydantic validation, Alembic migrations, and time-series database management in TimescaleDB.",
            desc_hydro_mcp: "Model Context Protocol (MCP) server for smart hydroponics. Enables LLM Agents to dynamically invoke tools to monitor sensor data.",
            desc_nexo: "Unified Discord AI ecosystem (Nexo Orchestrator & Pigeon Webhook). Integrates Model Context Protocol (MCP) for dynamic tool invocation and automated zero-downtime Docker CI/CD deployment.",
            desc_rag: "Retrieval-Augmented Generation (RAG) system utilizing a custom fine-tuned LLM to provide context-aware responses based on specific legal document bases.",
            desc_mlops: "End-to-end machine learning pipeline architecture using TensorFlow Extended (TFX) and Apache Beam (Data Ingestion, Validation, Transformation, and model serving with Railway).",
            desc_constructify: "Web Programming Course Final Project: an e-commerce platform for building materials procurement with product catalogs and order management."
        }
    };

    // 2. Language Switcher Logic
    let currentLang = localStorage.getItem('pref-lang') || 'id';

    function setLanguage(lang) {
        currentLang = lang;
        localStorage.setItem('pref-lang', lang);

        const langIdSpan = document.getElementById('lang-id');
        const langEnSpan = document.getElementById('lang-en');

        if (langIdSpan && langEnSpan) {
            if (lang === 'id') {
                langIdSpan.classList.add('active-lang');
                langEnSpan.classList.remove('active-lang');
            } else {
                langEnSpan.classList.add('active-lang');
                langIdSpan.classList.remove('active-lang');
            }
        }

        // Translate all elements with data-i18n
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                el.innerHTML = translations[lang][key];
            }
        });
    }

    const langToggleBtn = document.getElementById('lang-toggle');
    if (langToggleBtn) {
        langToggleBtn.addEventListener('click', function () {
            const newLang = currentLang === 'id' ? 'en' : 'id';
            setLanguage(newLang);
        });
    }

    // Initialize Language
    setLanguage(currentLang);

    // 3. Navbar Scroll Effect & Active Section Highlight
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('nav.nav-list ul li a');
    const sections = document.querySelectorAll('section');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }

        let currentSection = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    });

    // 4. Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navList = document.getElementById('nav-list');

    if (mobileMenuBtn && navList) {
        mobileMenuBtn.addEventListener('click', function () {
            navList.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (navList.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navList.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            });
        });
    }

    // 5. Interactive Project Filtering
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const filterValue = this.getAttribute('data-filter');

            projectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                
                if (filterValue === 'all' || cardCategory.includes(filterValue)) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 250);
                }
            });
        });
    });

    // 6. Dynamic Copyright Year
    const copyrightElement = document.querySelector('.copyright');
    if (copyrightElement) {
        const currentYear = new Date().getFullYear();
        copyrightElement.innerHTML = `&copy; ${currentYear} Dzulfikri Adjmal. All Rights Reserved.`;
    }
});
