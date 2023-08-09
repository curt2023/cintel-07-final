""" 
Purpose: Provide reactive output for the Penguins dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib

from shiny import render, reactive
import pandas as pd
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_quantity_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("quantity.xlsx")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_excel(p)
    total_count = len(original_df)

    # Create a reactive value to hold the filtered pandas dataframe
    reactive_df = reactive.Value()

    # Create a reactive effect to set the reactive value when inputs change
    # List all the inputs that should trigger this update

    @reactive.Effect
    @reactive.event(
        input.TIME_RANGE,
        input.QUANTITY_MAX,
        input.MEDICINE_A,
        input.MEDICINE_B,
        input.MEDICINE_C,
    )
    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        This is the only way to set a reactive value (after initialization).
        It doesn't need a name, because no one calls it directly."""

        # logger.info("UI inputs changed. Updating penguins reactive df")

        df = original_df.copy()

        # Body mass is a range
        input_range = input.TIME_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        body_mass_filter = (df["time_to_complete_hrs"] >= input_min) & (
            df["time_to_complete_hrs"] <= input_max
        )
        df = df[body_mass_filter]

        # Bill length is a max number
        quantity_size_filter = df["order_size_units"] <= input.QUANTITY_MAX()
        df = df[quantity_size_filter]

        # Species is a list of checkboxes (a list of possible values)
        show_material_list = []
        if input.MEDICINE_A():
            show_material_list.append("MedicineA")
        if input.MEDICINE_B():
            show_material_list.append("MedicineB")
        if input.MEDICINE_C():
            show_material_list.append("MedicineC")
        show_material_list = show_material_list or ["MedicineA", "MedicineB", "MedicineC"]
        material_filter = df["material"].isin(show_material_list)
        df = df[material_filter]


        # logger.debug(f"filtered penguins df: {df}")
        reactive_df.set(df)

    @output
    @render.text
    def quantity_record_count_string():
        # logger.debug("Triggered: penguins_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message

    @output
    @render.table
    def quantity_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    @output
    @render_widget
    def quantity_output_widget1():
        df = reactive_df.get()
        plotly_plot = px.scatter(
            df,
            x="order_size_units",
            y="time_to_complete_hrs",
            color="material",
            title="Quantity Plot (Plotly Express))",
            labels={
                "order_size_units": "Order Size",
                "time_to_complete_hrs": "Time to Complete (hrs)",
            },
            size_max=8,
        )

        return plotly_plot

    # return a list of function names for use in reactive outputs
    return [
        quantity_record_count_string,
        quantity_filtered_table,
        quantity_output_widget1,
    ]
