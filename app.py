#!/usr/bin/env python3
import datetime
import logging
import connexion
from flask import Flask, request
from connexion import NoContent

import orm
from orm import student

db_session = None


def get_students():
    q = db_session.query(orm.student)
    return [p.dump() for p in q]


# def get_student(student_id):
#     student = db_session.query(orm.student).filter(orm.student.id == student_id).one_or_none()
#     return student.dump() if student is not None else ('Not found', 404)

def post_student():
    logging.info('Creating new student...')
    #student['name'] = connexion.request
    #db_session.add(orm.student(**student))
    #db_session.commit()
    print(connexion.request.body)
    return NoContent, (200 if student is not None else 201)

# def put_student(student_id, student):
#     p = db_session.query(orm.student).filter(orm.student.id == student_id).one_or_none()
#     student['id'] = student_id
#     if p is not None:
#         logging.info('Updating students %s..', student_id)
#         p.update(orm.student(**student))
#     else:
#         logging.info('Creating new student %s..', student_id)
#         student['created'] = datetime.datetime.utcnow()
#         db_session.add(orm.student(**student))
#         db_session.commit()
#     return NoContent, (200 if p is not None else 201)

# def delete_student(student_id):
#     student = db_session.query(orm.student).filter(orm.student.id == student_id).one_or_none()
#     if student is not None:
#         logging.info('Deleting student %s..', student_id)
#         db_session.query(orm.student).filter(orm.student.id == student_id).delete()
#         db_session.commit()
#         return NoContent, 204
#     else:
#         return NoContent, 404

logging.basicConfig(level=logging.INFO)
db_session = orm.init_db('sqlite:///:memory:')
app = connexion.FlaskApp(__name__)
app.add_api('openapi.yaml')


application = app.app

@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
   app.run(port=8081, use_reloader=False, threaded=False, debug=True)