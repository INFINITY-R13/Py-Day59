from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts data
blog_posts = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'subtitle': 'A beginner\'s guide to web development',
        'author': 'John Doe',
        'date': 'March 15, 2024',
        'content': '''
        Flask is a lightweight and flexible web framework for Python. It's perfect for beginners 
        who want to learn web development without getting overwhelmed by complex features.
        
        In this post, we'll explore the basics of Flask and build our first web application.
        Flask follows the principle of "micro-framework" which means it provides the core
        functionality while allowing developers to choose their own tools and libraries.
        '''
    },
    {
        'id': 2,
        'title': 'Understanding Jinja Templates',
        'subtitle': 'Dynamic content made easy',
        'author': 'Jane Smith',
        'date': 'March 20, 2024',
        'content': '''
        Jinja is a powerful templating engine that comes built-in with Flask. It allows you
        to create dynamic HTML pages by embedding Python-like expressions in your templates.
        
        With Jinja, you can use variables, loops, conditionals, and filters to create
        sophisticated web pages without repeating code. This makes your application
        more maintainable and scalable.
        '''
    },
    {
        'id': 3,
        'title': 'Building RESTful APIs',
        'subtitle': 'Creating web services with Flask',
        'author': 'Mike Johnson',
        'date': 'March 25, 2024',
        'content': '''
        REST (Representational State Transfer) is an architectural style for designing
        web services. Flask makes it easy to build RESTful APIs that can be consumed
        by various clients including web browsers, mobile apps, and other services.
        
        In this tutorial, we'll learn how to create endpoints that handle different
        HTTP methods and return JSON responses.
        '''
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in blog_posts if post['id'] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', post=post, posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)