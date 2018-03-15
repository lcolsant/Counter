from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def root():
    
    if 'counter' in session:
        session['counter']+=1
    else:
        session['counter'] = 1
    
    print 'root route was viewed, counter is:',session['counter']
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    session['counter']+=1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter']=0    #reset counter to zero, will become 1, once redirected
    return redirect('/')

app.run(debug=True)