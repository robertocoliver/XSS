from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
  name = request.args.get('name')
  return f'Hello {name}!'

app.run(debug=True)
