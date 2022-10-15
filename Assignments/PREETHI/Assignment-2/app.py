from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def home_page():
       return render_template('home.html')

@app.route('/sign')
def sign_in():
      return render_template('sign.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')





if __name__=='__main__':
    app.run(host="0.0.0.0" , port=5000 ,debug=True)

# docker build -t akhil.