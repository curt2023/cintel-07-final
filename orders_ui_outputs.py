"""
Purpose: Display output for Flights dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""

from shiny import ui
from shinywidgets import output_widget

def get_orders_outputs():
    return ui.panel_main(
        ui.h2("Timeline of Orders"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Orders: Charts"),
            output_widget("orders_output_widget1"),
            output_widget("orders_output_widget2"),
            ui.tags.hr(),
            ui.h3("Filtered Orders Table"),
            ui.output_text("orders_record_count_string"),
            ui.output_table("orders_filtered_table"),
            ui.tags.hr(),
        ),
    )