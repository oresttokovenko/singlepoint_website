import pynecone as pc
from .helpers import navbar

# background_image = pc.image(src="src/assets/landing_background.jpg", width="100px", height="auto")

background_style = {
    "background_size": "cover",
    "background_repeat": "no-repeat",
    "background_image": "src/assets/landing_background.jpg",
}

class State(pc.State):
    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            # navbar(),
            # pc.divider(),
            pc.heading("Singlepoint Manufacturing Inc.", font_size="2em"),
            pc.text("Carving precision into every piece - one mill at a time"),
            spacing="1.5em",
            font_size="2em",
            # background_image='src/assets/landing_background.jpg',
            # background_position="center",
            # background_size="cover",
            # background_repeat="no-repeat",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
