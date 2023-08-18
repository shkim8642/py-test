# conftest.py

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings
from .models import User

db_engine = create_engine(settings.POSTGRES_DSN)
session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

@pytest.fixture
def create_user():
    user = User(
        nickname="test",
        email="test@test.com",
        password="1q2w3e4r",
    )
    db = session()
    db.add(user)
    db.commit()