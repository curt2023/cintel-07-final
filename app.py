"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python with 
interactive charts from HoloViews Bokeh and Plotly Express.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
from shiny import App, ui
import shinyswatch
from shiny import App, ui, render


from quantity_server import get_quantity_server_functions
from quantity_ui_inputs import get_quantity_inputs
from quantity_ui_outputs import get_quantity_outputs


from orders_server import get_orders_server_functions
from orders_ui_inputs import get_orders_inputs
from orders_ui_outputs import get_orders_outputs
from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.spacelab(),
    ui.nav(
        "Home",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("User Information"),
                ui.tags.hr(),
                ui.input_text("name_input", "Enter your name", placeholder="Your Name"),
                ui.input_text(
                    "color_input",
                    "Enter your department",
                    placeholder="Department"
                ),
                ui.tags.hr(),
            ),
            ui.panel_main(
                ui.h2("Daily Production Reminders"),
                ui.tags.hr(),
                ui.tags.ul(
                    ui.tags.li(
                        "Review all errors and corrections needed during shift change."
                    ),
                    ui.tags.li(
                        "Review and sign all completed records before leaving for the day."
                    ),
                    ui.tags.li(
                        "Sumbit and saftey suggestions."
                    ),
                ),
                ui.tags.hr(),
                ui.h2("Operator Information"),
                ui.tags.hr(),
                ui.output_text_verbatim("welcome_output"),
                ui.output_text_verbatim("cars_output"),
                ui.output_text_verbatim("color_output"),
                ui.tags.hr(),
            ),
        ),
    ),
    ui.nav(
        "Orders",
        ui.layout_sidebar(
            get_orders_inputs(),
            get_orders_outputs(),
        ),
    ),

    ui.nav(
        "Material Breakdown",
        ui.layout_sidebar(
            get_quantity_inputs(),
            get_quantity_outputs(),
        ),
    ),
   
    ui.nav(ui.a("About", href="https://github.com/curt2023")),
    ui.nav(ui.a("GitHub", href="https://github.com/curt2023/cintel-07-final")),
    ui.nav(ui.a("App", href="https://curt2023.shinyapps.io/cintel-07-final/")),
    ui.nav(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.nav(ui.a("Widgets", href="https://shiny.rstudio.com/py/docs/ipywidgets.html")),
    title=ui.h1("Hyde Labs Production Dashboard"),
)


def server(input, output, session):
    """Define functions to create UI outputs."""
    @output
    @render.text
    def welcome_output():
        user = input.name_input()
        welcome_string = f"{user} is viewing operational reports. "
        return welcome_string

    @output
    @render.text
    def color_output():
        answer = input.color_input()
        count = len(answer)
        language_string = f"Your department is {answer}."
        return language_string
    
    logger.info("Starting server...")
    get_orders_server_functions(input, output, session)
    get_quantity_server_functions(input, output, session)



# app = App(app_ui, server, debug=True)
app = App(app_ui, server)
