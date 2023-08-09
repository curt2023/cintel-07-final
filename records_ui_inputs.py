"""
Purpose: Provide user interaction options for MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui


def get_records_inputs():
    return ui.panel_sidebar(
        ui.h2("Batch Record Interaction"),
        ui.tags.hr(),
        ui.input_slider("ERRORS_PER_RECORD_RANGE", "Number of Errors in a Record", min=0, max=65, value=[0, 65],),
        ui.input_checkbox("DEPARTMENT_TYPE", "Aerobes", value=True),
        ui.input_checkbox("DEPARTMENT_TYPE", "Anerobes", value=True),
        ui.input_checkbox("DEPARTMENT_TYPE", "EUCS", value=True),
        ui.input_checkbox("DEPARTMENT_TYPE", "ROW", value=True),

        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Records Table"),
            ui.tags.p("Description of Fields in Table"),
            ui.tags.ul(
                ui.tags.li("Department"),
                ui.tags.li("Errors"),
                ui.tags.li("Material"),
                ui.tags.li("Employee"),
            ),
        
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )

