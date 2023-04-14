import pynecone as pc

class State(pc.State):
    """The app state."""

    pass

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(contact)
app.compile()
