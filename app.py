# ============================================================
# ONLY 3 CHANGES MADE:
# 1. Added send_from_directory to imports
# 2. Added static_folder, static_url_path to Flask()
# 3. Changed last line (removed host and port)
# EVERYTHING ELSE IS 100% ORIGINAL!
# ============================================================

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, send_from_directory
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

# ✅ CHANGE 1: Added static_folder and static_url_path
app = Flask(__name__,
            static_folder='static',
            static_url_path='/static',
            template_folder='templates')

app.secret_key = 'thegrowthofsales_secret_key_2024'

# ✅ CHANGE 2: Added this static file route for Vercel
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# ============================================================
# COMPANY DATA
# ============================================================

COMPANY_INFO = {
    'name': 'The Growth of Sales',
    'tagline': 'Empowering Your Business Digitally',
    'director': 'Mr. Navneet Kumar',
    'phone': '+91 99104 23182',
    'email': 'thegrowthofsales@gmail.com',
    'address': 'Gali No. 3, Jagmal Enclave Part 2, Roshan Nagar, Faridabad – 121013, India',
    'facebook': 'https://www.facebook.com/share/1AsMXTtJb5/',
    'instagram': 'https://www.instagram.com/thegrowthofsales',
    'youtube': 'https://www.youtube.com/@thegrowthofsales',
    'linkedin': 'https://www.linkedin.com/company/thegrowthofsales',
    'year': datetime.now().year
}

SERVICES = [
    {
        'icon': 'fas fa-bullhorn',
        'title': 'Digital Marketing',
        'description': 'Result-driven digital marketing strategies to boost your brand visibility and increase sales.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-share-alt',
        'title': 'Social Media Management',
        'description': 'Professional management of all your social media platforms for consistent brand presence.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-pen-nib',
        'title': 'Content Creation',
        'description': 'High-quality, engaging content tailored to your brand voice and target audience.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-film',
        'title': 'Video Editing',
        'description': 'Professional video editing services to create compelling visual content for your brand.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-palette',
        'title': 'Graphic Designing',
        'description': 'Creative and visually stunning graphic designs for print and digital media.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-video',
        'title': 'Online Video Promotion',
        'description': 'Strategic video promotion across YouTube, Instagram, and Facebook to maximize reach.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-newspaper',
        'title': 'Daily News & Updates',
        'description': 'Daily news and market updates shared across all social media platforms.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-chart-line',
        'title': 'Market Updates',
        'description': 'Real-time market updates and insights to keep your business ahead of the competition.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-book-open',
        'title': 'Digital Magazine',
        'description': 'Professional digital magazine creation and distribution for brand storytelling.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-magazine',
        'title': 'Print Magazines',
        'description': 'High-quality print magazine production with premium design and content.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-store',
        'title': 'Stall Fabrication',
        'description': 'Complete exhibition stall design and fabrication with professional management.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-print',
        'title': 'Printing Solutions',
        'description': 'Visiting cards, brochures, banners, flex printing and all branding materials.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-briefcase',
        'title': 'Business Consultancy',
        'description': 'Strategic business consultancy including catalogues, corporate gifts, T-shirts, diaries & pens.',
        'color': '#FFD700'
    },
    {
        'icon': 'fas fa-envelope-open-text',
        'title': 'Email Marketing',
        'description': 'Targeted B2B email campaigns reaching 50,000+ professionals in the market.',
        'color': '#FFD700'
    }
]

INDUSTRIES = [
    {'icon': 'fas fa-tools', 'name': 'Hardware, Fittings & Solutions'},
    {'icon': 'fas fa-couch', 'name': 'Furniture, Wardrobes, Rugs & Carpets'},
    {'icon': 'fas fa-layer-group', 'name': 'Laminate, Ply, PB, MDF, WPC & Acrylic'},
    {'icon': 'fas fa-gem', 'name': 'Decorative Veneer & Surfaces'},
    {'icon': 'fas fa-cogs', 'name': 'Machinery'},
    {'icon': 'fas fa-border-all', 'name': 'Flooring, Ceiling & Wall Highlighters'},
    {'icon': 'fas fa-tree', 'name': 'Lumber & Timbers'},
    {'icon': 'fas fa-door-open', 'name': 'Doors & Windows (uPVC, Aluminum)'},
    {'icon': 'fas fa-star', 'name': 'Premium Interior Products'},
    {'icon': 'fas fa-bath', 'name': 'Bath, Faucets & Sanitaryware'},
    {'icon': 'fas fa-tint', 'name': 'Paint, Coatings & Adhesives'},
    {'icon': 'fas fa-lightbulb', 'name': 'Lighting & Electricals'},
    {'icon': 'fas fa-utensils', 'name': 'Kitchen, Cabinets, Counter Tops & Appliances'},
    {'icon': 'fas fa-th-large', 'name': 'Tiles, Marble & Stones'},
    {'icon': 'fas fa-building', 'name': 'HPL, ACP, Façade, Louvers & Cladding'},
]

CLIENTS = [
    'Architects', 'Interior Designers', 'Dealers', 'Distributors',
    'Buying & Selling Agents', 'Showroom Owners', 'OEMs', 'Manufacturers',
    'Consultants', 'Builders & Developers', 'Civil Engineers',
    'PMCs & Contracting Firms', 'Facade & Roofing Consultants', 'Importers',
    'Machinery Buyers', 'Furniture Designers', 'Government Departments',
    'Green Building Professionals', 'Lighting Consultants', 'MEP Consultants',
    'Product Designers', 'Project Managers', 'Procurement Heads',
    'Structural Engineers', 'Raw Material Buyers', 'Product Specifiers'
]

TESTIMONIALS = [
    {
        'text': 'The Growth of Sales has completely transformed our online presence. Their digital marketing strategies and consistent promotions helped us reach the right audience and significantly improve our brand visibility.',
        'author': 'Rajesh Kumar',
        'position': 'CEO, Interior Solutions'
    },
    {
        'text': 'We are very impressed with their professionalism and creativity. From social media management to video production, everything is handled perfectly.',
        'author': 'Priya Sharma',
        'position': 'Director, Furniture World'
    },
    {
        'text': 'Their email marketing and B2B promotions provided us with excellent market exposure. We started receiving quality leads within a short period.',
        'author': 'Amit Verma',
        'position': 'MD, Hardware Hub'
    },
    {
        'text': 'The team is extremely supportive and always goes the extra mile. Their daily updates and promotional activities keep our brand active and engaging.',
        'author': 'Sunita Agarwal',
        'position': 'Owner, Decor Studio'
    },
    {
        'text': 'We collaborated with them for exhibition stall setup and the execution was flawless. From manpower to complete management, everything was well organized.',
        'author': 'Vikram Singh',
        'position': 'GM, Building Materials Co.'
    },
    {
        'text': 'Highly recommended for any business looking to grow. The Growth of Sales truly understands what a brand needs to succeed.',
        'author': 'Neha Gupta',
        'position': 'Founder, Design Interiors'
    }
]

EXHIBITION_SERVICES = [
    {'icon': 'fas fa-shield-alt', 'name': 'Security Services'},
    {'icon': 'fas fa-hard-hat', 'name': 'Manpower Support'},
    {'icon': 'fas fa-broom', 'name': 'Housekeeping'},
    {'icon': 'fas fa-user-tie', 'name': 'Hostess Services'},
    {'icon': 'fas fa-utensils', 'name': 'Catering'},
    {'icon': 'fas fa-chair', 'name': 'Carpet & Furniture Setup'},
    {'icon': 'fas fa-microphone', 'name': 'Conference Setup'},
    {'icon': 'fas fa-volume-up', 'name': 'Audio & Video Solutions'},
]

STATS = [
    {'number': '500+', 'label': 'Happy Clients', 'icon': 'fas fa-users'},
    {'number': '50K+', 'label': 'Email Campaigns', 'icon': 'fas fa-envelope'},
    {'number': '1000+', 'label': 'Projects Completed', 'icon': 'fas fa-check-circle'},
    {'number': '5+', 'label': 'Years Experience', 'icon': 'fas fa-calendar-alt'},
]

# ============================================================
# ROUTES
# ============================================================

@app.route('/')
def index():
    return render_template('index.html',
                           company=COMPANY_INFO,
                           services=SERVICES[:6],
                           stats=STATS,
                           testimonials=TESTIMONIALS[:3],
                           industries=INDUSTRIES[:8])

@app.route('/about')
def about():
    return render_template('about.html',
                           company=COMPANY_INFO,
                           stats=STATS,
                           exhibition_services=EXHIBITION_SERVICES)

@app.route('/services')
def services():
    return render_template('services.html',
                           company=COMPANY_INFO,
                           services=SERVICES)

@app.route('/industries')
def industries():
    return render_template('industries.html',
                           company=COMPANY_INFO,
                           industries=INDUSTRIES,
                           clients=CLIENTS)

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html',
                           company=COMPANY_INFO,
                           testimonials=TESTIMONIALS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        # Validation
        errors = []
        if not name:
            errors.append('Name is required.')
        if not email or '@' not in email:
            errors.append('Valid email is required.')
        if not message:
            errors.append('Message is required.')

        if errors:
            return jsonify({'status': 'error', 'errors': errors}), 400

        return jsonify({
            'status': 'success',
            'message': f'Thank you {name}! We will contact you shortly.'
        })

    return render_template('contact.html', company=COMPANY_INFO)

# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', company=COMPANY_INFO), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('404.html', company=COMPANY_INFO), 500

# ============================================================
# LOGO ROUTE
# ============================================================

@app.route('/logo')
def serve_logo():
    """Serve logo directly - useful for debugging"""
    logo_path = os.path.join(app.static_folder, 'images', 'logo.png')
    if os.path.exists(logo_path):
        return app.send_static_file('images/logo.png')
    else:
        images_dir = os.path.join(app.static_folder, 'images')
        if os.path.exists(images_dir):
            files = os.listdir(images_dir)
            return f"Logo not found. Files in static/images/: {files}"
        return "static/images/ folder does not exist!"

# ============================================================
# RUN
# ============================================================

# ✅ CHANGE 3: Removed host='0.0.0.0', port=5000
if __name__ == '__main__':
    app.run(debug=True)