from flask import Flask, render_template, request, redirect, url_for
import todo_app.data.session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        items = session.get_items()
        return render_template('index.html', myitems=items)
    elif request.method == 'POST':
        #Add new item
        if request.form.get('title'):
            title = request.form.get('title')
            session.add_item(title)
        #Delete item
        if request.form.get('del_id'):
            del_id = int(request.form.get('del_id')) if request.form.get('del_id') else 0
            session.delete_item(del_id -1)
        #Update item
        if request.form.get('com_id'):
            com_item = session.get_item(request.form.get('com_id'))
            com_item['status'] = 'Complete'
            session.save_item(com_item)
        #Populate table with current items
        items = session.get_items()
        #Show website
        return render_template('index.html', myitems=items)


if __name__ == '__main__':
    app.run()
