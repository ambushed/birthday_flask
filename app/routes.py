from flask import Flask, render_template,request, jsonify
from forms import StarterForm
from neovim import attach

app = Flask(__name__)      
app.config.from_object('config')
nvim = attach('child', argv=["/bin/env","nvim","--embed"])
buffer = nvim.current.buffer
text = 'The quick brown fox jumps over the lazy dog.' 
buffer[0] = text  

@app.route('/')
def home():
    captions = {'login':'Login: '}
    return render_template('login.html',title='Present for Nelly',captions=captions)

@app.route('/load_ajax',methods=['GET','POST'])
def load_ajax():
    key = request.json
    if request.method == 'POST':

        #nvim.command("/whole")
        nvim.feedkeys(key)
        #print(buffer[0])

        app.logger.debug("{}".format(key))
        return jsonify(key)
    return jsonify(key)

@app.route('/starter', methods = ['GET','POST'])
def starter():
    form = StarterForm(text)

    if request.method == 'POST':
        return 'Form posted!'

    if request.method == 'GET':
        return render_template('starter.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
