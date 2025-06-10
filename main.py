from flask import Flask, request, render_template

app = Flask(__name__)

def read_ps():
    with open("ps.txt", "r", encoding="utf-8") as f:
        return f.readline().strip()

def read_st():
    with open("st.txt", "r", encoding="utf-8") as f:
        return f.readline().strip()

def change(inp):
    with open("st.txt", "w", encoding="utf-8") as f:
        f.write(inp)

@app.route("/")
def home():
    if read_st() == '1':
        return render_template('index.html', status="선생님께서 계십니다.")
    else:
        return render_template('index.html', status="선생님께서 안 계십니다.")

@app.route("/submit", methods=["POST"])
def submit():
    password = request.form['p']
    if password == read_ps():
        if read_st() == '1':
            change('0')
        else:
            change('1')

    if read_st() == '1':
        return render_template('index.html', status="선생님께서 계십니다.")
    else:
        return render_template('index.html', status="선생님께서 안 계십니다.")

if __name__ == '__main__':
    app.run(debug=True)
