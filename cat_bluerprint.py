from nis import cat
from flask import Blueprint, jsonify, request, make_response
from schema import CatSchema
from models import Cat
from utils import db


cat_bp = Blueprint("cats", __name__)


@cat_bp.get("/")
def get_all_cats():
    schema = CatSchema()
    cats = Cat.get_all()

    res = schema.dump(cats, many=True)

    return make_response(jsonify(res), 200)


@cat_bp.post("/")
def store_cat():
    data = request.get_json()
    new_cat = Cat(name=data.get("name"), age=data.get("age"))
    new_cat.save()

    result = CatSchema().dump(new_cat)

    return make_response(result, 201)


@cat_bp.get("/<int:cat_id>")
def get_cat(cat_id: int):
    cat = Cat.get_by_id(cat_id)

    result = CatSchema().dump(cat)

    return make_response(result, 200)


@cat_bp.put("/<int:cat_id>")
def update_cat(cat_id: int):
    cat = Cat.get_by_id(cat_id)
    data = request.get_json()
    cat.name = data.get("name")
    cat.age = data.get("age")
    db.session.commit()

    return make_response(CatSchema().dump(cat), 200)


@cat_bp.delete("/<int:cat_id>")
def delete_cat(cat_id: int):
    cat = Cat.get_by_id(cat_id)

    cat.delete()

    return make_response("", 204)
    