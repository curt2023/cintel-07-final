"""
Purpose: Provide user interaction options for the Penguins dataset.

 - Choose checkboxes when the options are independent of each other.
 - Choose radio buttons when a set of options are mutually exclusive.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""

from shiny import ui


def get_quantity_inputs():
    return ui.panel_sidebar(
        ui.h2("Quantity Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "TIME_RANGE",
            "Time to complete (hrs)",
            min=2700,
            max=6300,
            value=[2700, 6300],
        ),
        ui.input_numeric("QUANTITY_MAX", "Order Size", value=20000.0),
        ui.input_checkbox("PENGUIN_SPECIES_Adelie", "Adelie", value=True),
        ui.input_checkbox("PENGUIN_SPECIES_Chinstrap", "Chinstrap", value=True),
        ui.input_checkbox("PENGUIN_SPECIES_Gentoo", "Gentoo", value=True),
        ui.input_radio_buttons(
            "PENGUIN_GENDER",
            "Select Genders",
            {"a": "All (includes missing values)", "f": "Female", "m": "Male"},
            selected="a",
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
