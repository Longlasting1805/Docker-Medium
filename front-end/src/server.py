from flask import Flask, render_template

app = Flask(__name__)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def show_books():
    # Your Container IP instead
    Books = requests.get('http://172.18.0.2:5000/books').json()  
    return render_template('show_books.html', books=Books)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')