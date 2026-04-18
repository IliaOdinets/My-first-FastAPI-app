from fastapi import FastAPI

app = FastAPI(title="My first API")
notes = {}

@app.get("/")
def read_root():
    return {"message": "FastApi is working"}

@app.get("/notes/",)
def get_all_notes():
        return notes

@app.get("/notes/{notes_id}")
def get_note(notes_id: str):
    return enumerate(notes.get(notes_id, None), start= 1)

@app.post("/notes/")
def create_note(key: str, note: list[str]):
    notes[key] = note
    return note

@app.put("/notes/{notes_id}")
def update_note(notes_id: str, new_note: list[str]):
    if notes.get(notes_id):
        notes[notes_id] = new_note
        return new_note
    return {"message": "Note not found"}

@app.delete("/notes/{notes_id}")
def delete_note(notes_id: str):
    if notes.get(notes_id):
        del notes[notes_id]
        return {"message": "note is deleted"}
    return {"message": "Note not found"}