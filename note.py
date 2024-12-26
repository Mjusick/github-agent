from langchain_core.tools import tool

@tool
def note_tool(note):
    """
    Saves a note to a file.

    Args:
        note (str): The note to save.
    """
    with open("note.txt", "a") as f:
        f.write(note + "\n")