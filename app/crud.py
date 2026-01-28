from sqlalchemy.orm import Session
from . import models, schemas


def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        is_completed=False,
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all_todos(db: Session):
    return db.query(models.Todo).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def update_todo(db: Session, todo: models.Todo, updates: schemas.TodoUpdate):
    update_data = updates.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: models.Todo):
    db.delete(todo)
    db.commit()
