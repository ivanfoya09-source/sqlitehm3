from flask import Flask, render_template
from models import db, User, Event, Ticket

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/tickets.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql"

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    u1 = User(name="Ivan", email="ivan@gmail.com")
    u2 = User(name="Olga", email="olga@gmail.com")
    u3 = User(name="Petro", email="petro@gmail.com")
    db.session.add_all([u1, u2, u3])

    e1 = Event(title="Концерт Imagine Dragons", date="2026-03-20")
    e2 = Event(title="Театр Лесі Українки", date="2026-04-05")
    e3 = Event(title="Виставка сучасного мистецтва", date="2026-05-10")
    db.session.add_all([e1, e2, e3])
    db.session.commit()

    tickets = [
        Ticket(user_id=u1.id, event_id=e1.id, price=600),
        Ticket(user_id=u1.id, event_id=e2.id, price=400),
        Ticket(user_id=u2.id, event_id=e1.id, price=500),
        Ticket(user_id=u2.id, event_id=e3.id, price=700),
        Ticket(user_id=u3.id, event_id=e2.id, price=300),
        Ticket(user_id=u3.id, event_id=e3.id, price=550),
    ]
    db.session.add_all(tickets)
    db.session.commit()

@app.get("/")
def index():
    tickets = db.session.query(Ticket).all()
    return render_template("index.html", tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)