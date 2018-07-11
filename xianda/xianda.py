from flask import Flask, render_template, redirect, url_for, session, request
from extends import db
import config
from forms import ArticleForm
from models import User, Message, Article
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():

    page = request.args.get('page', default=1, type=int)
    pagination = Article.query.paginate(
        page=page,
        per_page=5,
        error_out=False
    )
    return render_template('index.html', pagination=pagination)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/thinking')
def thinking():
    page = request.args.get('page', default=1, type=int)
    pagination = Article.query.paginate(
        page=page,
        per_page=5,
        error_out=False
    )
    return render_template('think.html', pagination=pagination)


@app.route('/learning')
def learning():
    page = request.args.get('page', default=1, type=int)
    pagination = Article.query.paginate(
        page=page,
        per_page=5,
        error_out=False
    )
    return render_template('learn.html', pagination=pagination)


@app.route('/index/<int:article_id>/detail')
def detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('detail.html', article=article)


@app.route('/message', methods=['POST', 'GET'])
def message():
    if request.method == 'GET':
        page = request.args.get('page', default=1, type=int)
        pagination = Message.query.paginate(
            page=page,
            per_page=10,
            error_out=False
        )
        return render_template('message.html', pagination=pagination)
    else:
        name = request.form.get('name')
        msg = request.form.get('msg')
        m = Message(name=name, message=msg)
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('message'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('name')
        password1 = request.form.get('pwd1')
        password2 = request.form.get('pwd2')
        user1 = User.query.filter(User.username == username).first()
        if user1:
            return '昵称已被占用'
        elif password1 != password2:
            return '密码不一致'
        else:
            user1 = User(username=username, password=password1)
            db.session.add(user1)
            db.session.commit()
            return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('name')
        password = request.form.get('pwd')
        user2 = User.query.filter(User.username == username).first()
        if user2:
            if user2.password == password:
                session['user_id'] = user2.id
                session['user_name'] = user2.username
                return redirect(url_for('admin'))
            else:
                return '密码错误'
        else:
            return '昵称未注册'


@app.route('/logout')
@login_required
def logout():
    session.pop('user_id')
    return redirect(url_for('index'))


@app.route('/admin')
@login_required
def admin():
    page = request.args.get('page', default=1, type=int)
    pagination = Article.query.paginate(
        page=page,
        per_page=15,
        error_out=False
    )
    return render_template('admin/admin.html', pagination=pagination)


@app.route('/article')
@login_required
def article():
    page = request.args.get('page', default=1, type=int)
    pagination = Article.query.paginate(
        page=page,
        per_page=15,
        error_out=False
    )
    return render_template('admin/article.html', pagination=pagination)


@app.route('/admin/user')
@login_required
def user():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=15,
        error_out=False
    )
    return render_template('admin/user.html', pagination=pagination)


@app.route('/admin/user/<int:user_id>/delete')
@login_required
def del_user(user_id):
    d_user = User.query.get_or_404(user_id)
    db.session.delete(d_user)
    db.session.commit()
    return redirect(url_for('user'))


@app.route('/admin/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        form.create_article()
        return redirect(url_for('article'))
    return render_template('admin/add_article.html', form=form)


@app.route('/admin/<int:article_id>/edit_article', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article1 = Article.query.get_or_404(article_id)
    form = ArticleForm(obj=article1)
    if form.validate_on_submit():
        form.update_article(article1)
        return redirect(url_for('article'))
    return render_template('admin/edit_article.html', form=form, article=article1)


@app.route('/admin/<int:article_id>/delete')
@login_required
def del_article(article_id):
    d_article = Article.query.get_or_404(article_id)
    db.session.delete(d_article)
    db.session.commit()
    return redirect(url_for('article'))


if __name__ == '__main__':
    app.run()
