from flask import Flask, render_template, request, redirect, url_for
import todo_app.data.session_items as session

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        items = session.get_items()
        return render_template('index.html', myitems=items)

@app.route('/new-item', methods=['POST']) 
def new_item():
    if request.form.get('title'):
        title = request.form.get('title')
        session.add_item(title)
    return redirect('/')

@app.route('/delete-item', methods=['POST']) 
def delete_item():
    if request.form.get('del_id'):
        del_id = int(request.form.get('del_id')) 
        session.delete_item(del_id -1)
    return redirect('/')

@app.route('/update-item', methods=['POST']) 
def update_item():
    if request.form.get('com_id'):
        com_item = session.get_item(request.form.get('com_id'))
        com_item['status'] = 'Complete'
        session.save_item(com_item)
    return redirect('/')

if __name__ == '__main__':
    app.run()
