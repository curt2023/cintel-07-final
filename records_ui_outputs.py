"""
Purpose: Display output for MT Cars dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_records_outputs():
    return ui.panel_main(
        ui.h2("Data Panel"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Records: Charts"),
            output_widget("records_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Records Table"),
            ui.output_text("records_record_count_string"),
            ui.output_table("records_filtered_table"),
            ui.tags.hr(),
        ),
    )
