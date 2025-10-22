from flask import render_template, Blueprint

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/carbon_app')
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

@carbon_app.route('/carbon_app/new_entry')
def new_entry():
    return render_template('carbon_app/new_entry.html', title='new_entry')

@carbon_app.route('/carbon_app/new_entry/car')
def new_entry_car():
    return render_template('carbon_app/new_entry_car.html', title='new_entry_car')

@carbon_app.route('/carbon_app/new_entry/plane')
def new_entry_plane():
    return render_template('carbon_app/new_entry_plane.html', title='new_entry_plane')

@carbon_app.route('/carbon_app/new_entry/bus')
def new_entry_bus():
    return render_template('carbon_app/new_entry_bus.html', title='new_entry_bus')

@carbon_app.route('/carbon_app/new_entry/train')
def new_entry_train():
    return render_template('carbon_app/new_entry_train.html', title='new_entry_train')

@carbon_app.route('/carbon_app/new_entry/ferry')
def new_entry_ferry():
    return render_template('carbon_app/new_entry_ferry.html', title='new_entry_ferry')

@carbon_app.route('/carbon_app/new_entry/motorbike')
def new_entry_motorbike():
    return render_template('carbon_app/new_entry_motorbike.html', title='new_entry_motorbike')

@carbon_app.route('/carbon_app/new_entry/bicycle')
def new_entry_bicycle():
    return render_template('carbon_app/new_entry_bicycle.html', title='new_entry_bicycle')

@carbon_app.route('/carbon_app/new_entry/walk')
def new_entry_walk():
    return render_template('carbon_app/new_entry_walk.html', title='new_entry_walk')

@carbon_app.route('/carbon_app/new_entry/electric-scooter')
def new_entry_electric_scooter():
    return render_template('carbon_app/new_entry_electricscooter.html', title='new_entry_electricscooter')

@carbon_app.route('/carbon_app/your_data')
def your_data():
    return render_template('carbon_app/your_data.html', title='your_data')
    
