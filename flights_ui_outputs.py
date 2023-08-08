"""
Purpose: Display output for Flights dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""

from shiny import ui
from shinywidgets import output_widget


#def get_flights_outputs():
    #return ui.panel_main(
        #ui.h2("Main Panel with Reactive Output"),
        #ui.tags.hr(),
        #ui.tags.section(
           # ui.h3("Filtered Flights: Charts"),
            #output_widget("flights_output_widget1"),
            #output_widget("flights_output_widget2"),
            #ui.tags.hr(),
            #ui.h3("Filtered Flights Table"),
            #ui.output_text("flights_record_count_string"),
            #ui.output_table("flights_filtered_table"),
            #ui.tags.hr(),
       # ),
   # )
def get_orders_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered orders: Charts"),
            output_widget("orders_output_widget1"),
            output_widget("orders_output_widget2"),
            ui.tags.hr(),
            ui.h3("Filtered Orders Table"),
            ui.output_text("orders_record_count_string"),
            ui.output_table("orders_filtered_table"),
            ui.tags.hr(),
        ),
    )
