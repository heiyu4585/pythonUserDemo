from flask import Flask,request,jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker,DeclarativeBase
from sqlalchemy import Column, Integer, String, Text, DateTime, func


engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/userDemo?charset=utf8")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="用户名")
    gender = Column(String(120), default="", comment="性别")

db_session = scoped_session(
    sessionmaker(
        autoflush=False,
        bind=engine
    )
)

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_user_list", methods=["GET"])
def get_user_list():
    page_index = request.args.get('pageIndex')
    page_size = request.args.get('pageSize')

    users = db_session.query(User).limit(int(page_size)).offset((int(page_index) - 1) * int(page_size))
    user_total = db_session.query(User).count()
    user_list = []
    for user in users:
        user_dict = {
            'id': user.id,
            'name': user.name,
            'gender': user.gender
        }
        user_list.append(user_dict)

    return jsonify({
        "data":user_list,
        "status":200,
        "total":user_total
    })

@app.route("/add_user",methods=["POST"])
def add_user():
    request_data = request.get_json()
    u = User(name=request_data.get("name"), gender=request_data.get("gender"))
    db_session.add(u)
    db_session.commit()
    return "success"

@app.route("/edit_user",methods=["POST"])
def edit_user():
    request_data = request.get_json()

    targetId=request_data.get("id");

    record = db_session.query(User).filter_by(id=targetId).first()
    if record:
        record.name = request_data.get("name");
        record.gender = request_data.get("gender");
        db_session.commit()
    return "success"