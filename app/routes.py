from flask import Flask, render_template,request, jsonify,redirect,url_for
from flask_bootstrap import Bootstrap
from forms import StarterForm
from vim import Vim
from vim_proxy import VimProxy

app = Flask(__name__)      
Bootstrap(app)
app.config.from_object('config')
text = "The quick brown fox jumps over the lazy dog." 
expected_text = "The lazy dog jumps over the quick brown fox." 

vim = Vim()
vimProxy = VimProxy(vim,text)

@app.route('/wrong_answer', methods = ['GET','POST'])
def wrong_answer():

    if request.method == 'POST':
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('wrong_answer.html',puzzle_text=text)


@app.route('/wow', methods = ['GET','POST'])
def wow():

    if request.method == 'POST':
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('wow.html',puzzle_text=text)


@app.route('/home', methods = ['GET','POST'])
def home():

    if request.method == 'POST':
        if 'TryAgain' in request.form:
            vimProxy.Reset()
            return render_template('home.html',puzzle_text=text)

        puzzle_text = request.form.get('Puzzle',None)
        password_text = request.form.get('Password',None)
        if (puzzle_text == expected_text and len(password_text)<=12):
            return redirect(url_for('wow'))
        return redirect(url_for('wrong_answer'))#,length=len(password_text))

    if request.method == 'GET':
        vimProxy.Reset()
        return render_template('home.html',puzzle_text=text)

@app.route('/load_ajax',methods=['GET','POST'])
def load_ajax():

    key = request.json
    if request.method == 'POST':

        result = vimProxy.FeedKeys(key)
        print("Keys Sent: {}; Result: {}".format(result['sent'],result['buffer']))
        return jsonify(result)

    return jsonify(key)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
