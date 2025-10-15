# Flask Blog 2.0 - Bootstrap Edition

A modern, responsive blog built with Flask and Bootstrap 5.

## Features

### ✨ New Bootstrap Upgrade Features
- **Multi-page website** with interactive navigation bar
- **Dynamically generated blog post pages** with full-screen hero titles
- **Fully mobile responsive** with adaptive navigation bar
- **Modern UI/UX** with smooth animations and hover effects
- **Professional typography** using Google Fonts (Playfair Display + Source Sans Pro)

### 📱 Mobile Responsive Design
- Collapsible navigation menu for mobile devices
- Responsive grid layout using Bootstrap's grid system
- Touch-friendly buttons and interactive elements
- Optimized typography for different screen sizes

### 🎨 Design Features
- Beautiful gradient hero sections
- Card-based blog post layout with hover effects
- Social media integration placeholders
- Newsletter subscription section
- Contact form with validation
- FAQ accordion section
- Smooth scrolling navigation

### 📄 Pages
- **Home**: Hero section with latest blog posts in card layout
- **Blog Posts**: Individual post pages with full-screen titles
- **About**: Personal profile with skills and statistics
- **Contact**: Contact form with FAQ section

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0
- **Fonts**: Google Fonts (Playfair Display, Source Sans Pro)
- **Styling**: Custom CSS with CSS variables

## Installation & Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure
```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   ├── base.html      # Base template with Bootstrap
│   ├── index.html     # Home page with hero section
│   ├── post.html      # Individual blog post pages
│   ├── about.html     # About page
│   └── contact.html   # Contact page
└── README.md          # This file
```

## Customization

The blog uses CSS variables for easy theming:
- `--primary-color`: Main brand color
- `--secondary-color`: Accent color
- `--accent-color`: Highlight color
- `--text-color`: Main text color
- `--light-bg`: Light background color

## Future Enhancements
- Database integration for dynamic content
- User authentication and admin panel
- Comment system
- Search functionality
- RSS feed
- SEO optimization
