from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    number = request.form['number']
    base = request.form['base']

    # Simple logic: convert decimal to another base
    try:
        number_int = int(number)
        if base == 'binary':
            result = bin(number_int)[2:]
        elif base == 'hex':
            result = hex(number_int)[2:]
        elif base == 'octal':
            result = oct(number_int)[2:]
        else:
            result = str(number_int)
    except ValueError:
        result = "Invalid input"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
