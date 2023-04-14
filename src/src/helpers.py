import pynecone as pc


def navbar():
    return pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading("SinglePoint Manufacturing Inc."),
        ),
        pc.spacer(),
        pc.menu(
            pc.menu_button("Menu"),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
    )