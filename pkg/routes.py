from flask import render_template, jsonify, json
from pkg.models import GDP_Percap, By_Edu, By_Housing, By_Income
from pkg.dashboard import app

 # let's define out '/go-to-dashboard' route here:
@app.server.route('/go-to-dashboard/')
def dashboard():
    return app.index()

# # created routes for the appropriate HTML Templates
# @app.server.route('/users')
# def users_index():
#     all_users = db.session.query(User).all()
#     all_users_dicts = [user.to_dict() for user in all_users]
#     return render_template('users.html', users=all_users_dicts)

# @app.server.route('/users/<int:id>')
# def user_show_by_id(id):
#     user = User.query.filter(User.id == id).first().to_dict()
#     return render_template('user_show.html', user=user)

# @app.server.route('/users/<name>')
# def user_show_by_name(name):
#     user = User.query.filter(User.username.like(name)).first().to_dict()
#     return render_template('user_show.html', user=user)
