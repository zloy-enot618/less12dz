from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field



app = FastAPI(title="Клуб будующего.")
templates = Jinja2Templates(directory="templates")

events = [
    {
        "id": 1,
        "title": "Создание игр",
        "seats": 5,
        "status": "Открыта"
    },
    {
        "id": 2,
        "title": "Воздушная автомагистраль",
        "seats": 0,
        "status": "Регистрация завершена"
    },
    {
        "id": 3,
        "title": "Космический беговой путь",
        "seats": 3,
        "status": "Открыта"
    },
    {
        "id": 4,
        "title": "Подземные шахты",
        "seats": 687,
        "status": "Открыта"
    }
]

class EventCreate(BaseModel):
    title: str
    seats: int = Field(ge=0) #больше или равно 0

class Event(BaseModel):
    id: int
    title: str
    seats: int
    status: str

@app.post("/api/events", response_model=Event, status_code=201)
def create_event_swagger(data_event: EventCreate):
    new_event = {
        "id": len(events) + 1,
        "title": data_event.title,
        "seats": data_event.seats,
        "status": "Открыта" if data_event.seats > 0 else "Регистрация завершена"
    }
    events.append(new_event)
    return new_event

@app.get("/api/events", response_model=list[Event])
def get_events():
    return events


@app.get("/api/events/open", response_model=list[Event])
def get_opened():
    result = []
    for event in events:
        if event["status"] == "Открыта":
            result.append(event)
    return result


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"events": events}
    )

@app.get("/events/new", response_class=HTMLResponse)
def return_add_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="new_event.html",

    )    

@app.post("/events/new")
def create_event_ui(title: str = Form(), seats: int = Form()):
    new_event = {
        "id": len(events) + 1,
        "title": title,
        "seats": seats,
        "status": "Открыта" if seats > 0 else "Регистрация завершена"
    }
    events.append(new_event)
    return RedirectResponse(
        url="/",
        status_code=303
    )

