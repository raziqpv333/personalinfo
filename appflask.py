from flask import Flask, render_template,url_for,request,redirect
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')




@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        
        print(f"Message from {name} ({email}): {message}")

        return redirect(url_for('thank_you'))

    return render_template('contact.html')

app.run()


