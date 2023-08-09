""" 
Purpose: Provide reactive output for Flights dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

This example uses dates - arguably the most complex UI input type.
 - Consider leap years, time changes, daylight savings, etc.
 - Working with dates is often challenging. 
 - This example is a good starting point - there are many examples online.

"""
import pathlib
from shiny import render, reactive
import pandas as pd
from shiny import ui
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_orders_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("orders.xlsx")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_excel(p)

    # create new field with year as a string and month together
    original_df["year-mon"] = (
        original_df["Year"].astype(str) + "-" + original_df["Month"]
    )
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(input.ORDERS_DATE_RANGE)
    def _():
        """Reactive effect to update the filtered dataframe when inputs change.
        It doesn't need a name, because no one calls it directly."""

        # logger.info("UI inputs changed. Updating flights reactive df")

        df = original_df.copy()

        # first, drop the unnamed index column
        # axis=1 means drop a column, axis=0 means drop a row
        df = df.drop(df.columns[0], axis=1)

        # Create a new column using pd.to_datetime() method for filtering
        year_string = df["Year"].astype(str)
        month_string = df["Month"].astype(str)
        df["Date"] = pd.to_datetime(year_string + "-" + month_string)

        # Convert datetime to just the date, no time (datetime objects have both)
        df["Date"] = df["Date"].dt.date

        input_range = input.ORDERS_DATE_RANGE()
        input_min = input_range[0]
        input_max = input_range[1]
        df = df[(df["Date"] >= input_min) & (df["Date"] <= input_max)]

        # logger.debug(f"filtered flights df: {df}")
        reactive_df.set(df)

    @output
    @render.text
    def orders_record_count_string():
        # logger.debug("Triggered: flights_filter_record_count_string")
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message

    @output
    @render.table
    def orders_filtered_table():
        filtered_df = reactive_df.get()
        filtered_df.drop(columns=["Date"], inplace=True)
        return filtered_df

    @output
    @render_widget
    def orders_output_widget1():
        df = reactive_df.get()
        px_plot = px.scatter(
            df,
            x="Year",
            y="Number of Orders",
            title="Orders Scatter Chart (Plotly Express)",
            color="Month",
        )
        return px_plot

    @output
    @render_widget
    def orders_output_widget2():
        df = reactive_df.get()

        px_plot = px.line(
            df,
            x="year-mon",
            y="Number of Orders",
            title="Orders Line Chart (Plotly Express)",
            labels={"year-mon": "Year-Mon", "Number of Orders": "Orders"},
        )
        return px_plot

    # return a list of function names for use in reactive outputs
    return [
        orders_record_count_string,
        orders_filtered_table,
        orders_output_widget1,
        orders_output_widget2,
    ]