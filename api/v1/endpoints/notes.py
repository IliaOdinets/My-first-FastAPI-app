from fastapi import APIRouter, Depends, HTTPException, status
from schemas.note import NoteInDB, NoteCreate
from core.dependencies import get_note_or_404
from main import notes

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/notes/", tags=["Notes"], response_model=list[NoteInDB])
def get_all_notes() -> list[NoteInDB]:
        return list(notes.values())

@router.get("/notes/{note_id}", response_model=NoteInDB)
def get_note(note: dict = Depends(get_note_or_404))
    return note

@router.post("/notes/", tags=["Notes"], response_model=NoteInDB, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate) -> NoteInDB:
    note_id = str(len(notes) + 1)
    new_note = NoteInDB(id=note_id, **note.model_dump())
    notes[note_id] = new_note
    return new_note

@router.put("/notes/{note_id}", tags=["Notes"], response_model=NoteInDB)
def update_note(note_id: str, note_update:NoteCreate) -> NoteInDB:
    if note_id not in notes:
         raise HTTPException(status_code=404, detail="Note not found")
    updated = NoteInDB(id=note_id, **note_update.model_dump())
    notes[note_id] = updated
    return updated 

@router.delete("/notes/{note_id}", tags=["Notes"], status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: str) -> None:
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]