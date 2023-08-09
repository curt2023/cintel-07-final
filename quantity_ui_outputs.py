"""
Purpose: Display output for Penguins dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_quantity_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Quantity: Charts"),
            output_widget("quantity_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Quantity Table"),
            ui.output_text("quantity_record_count_string"),
            ui.output_table("quantity_filtered_table"),
            ui.tags.hr(),
        ),
    )
