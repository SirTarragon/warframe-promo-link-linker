from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    with open('promotion_codes.txt', 'r') as f:
        codes = [line.strip() for line in f]
    return render_template('redeem.html', codes=codes)

if __name__ == '__main__':
    app.run()
