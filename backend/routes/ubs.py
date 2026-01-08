from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import model

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@router.get("/ubs/", response_model=list[schemas.UnidadeResponse])
def lista_unidades(db: Session = Depends(get_db)):
    query = db.query(model.UnidadeDeSaude)
    return query.all()
