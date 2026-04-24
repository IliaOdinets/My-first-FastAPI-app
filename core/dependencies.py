from typing import Annotated

from fastapi import Depends, HTTPException, status

async def get_note_or_404(note_id: str) -> dict:
    from main import notes
    note = notes.get(note_id)
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )
    return note

NoteIDDep = Annotated[str, Depends(get_note_or_404)]