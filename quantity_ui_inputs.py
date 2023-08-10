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
        ui.h2("Management Input"),
        ui.tags.hr(),
        ui.input_slider(
            "TIME_RANGE",
            "Time to complete (hrs)",
            min=1,
            max=10,
            value=[2, 6],
        ),
        ui.input_numeric("QUANTITY_MAX", "Order Size", value=43000.0),
        ui.input_checkbox("MEDICINE_A", "MedicineA", value=True),
        ui.input_checkbox("MEDICINE_B", "MedicineB", value=True),
        ui.input_checkbox("MEDICINE_C", "MedicineC", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
