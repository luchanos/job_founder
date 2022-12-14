from datetime import datetime
from datetime import timedelta
from typing import Optional

from core.config import settings
from jose import jwt


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


print(create_access_token({"sub": "n.luchanos@gmail.com"}))

# TOKEN = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuLmx1Y2hhbm9zQGdtYWlsLmNvbSIsImV4cCI6MTY3MTA1NDk3NX0.AQNjbTdq8Ndmo4pKrCvU2q0a3c_l85NAOpPq5mdhqDQ
