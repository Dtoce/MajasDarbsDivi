from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
#  return render_template('index.html')
  return render_template('atminasspele.html')

@app.route('/atminasspele')
def spele():
  return render_template('atminasspele.html')


app.run(host='0.0.0.0', port=8020)
