import dearpygui.dearpygui as dpg
import window.appConstants as Constants


def start():
    """
    Starts the Application. Does the prior setup.
    Then starts the login sequence into the camera...
    When successful will show other windows
    """
    show_exec_view()


def show_exec_view():
    """
    Shows the execution view to the user.
    This shall be the main window of the application.
    The user will see info of the camera and the status.
    The user will be able to execute single commands and see their results.
    """
    dpg.create_context()
    dpg.create_viewport(title="Panasonic Controller", small_icon=Constants.PATH_TO_ICON,
                        large_icon=Constants.PATH_TO_ICON, resizable=False)
    # Creating main window
    with dpg.window(tag="exec_window", autosize=True, no_resize=True) as exec_window:
        # Creating top bar
        with dpg.group(horizontal=True, horizontal_spacing=400):
            # Creating camera info panel
            with dpg.group():
                dpg.add_text("Camera Info")
            # Creating mode button
            with dpg.group():
                dpg.add_button(label="Execution Mode")
            # Creating status panel
            with dpg.group():
                dpg.add_text("Camera Status")
        # Creating list and stream field
        with dpg.group(horizontal=True):
            # Creating command list
            with dpg.group():
                dpg.add_listbox()
            # Creating streaming window
            with dpg.group():
                # TODO: remove palceholder
                # create plot
                with dpg.plot(label="Line Series", height=400, width=400):
                    # optionally create legend
                    dpg.add_plot_legend()

                    # REQUIRED: create x and y axes
                    dpg.add_plot_axis(dpg.mvXAxis, label="x")
                    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

                    # series belong to a y axis
                    dpg.add_line_series([1, 2, 3, 4], [1, 2, 3, 4], label="0.5 + 0.5 * sin(x)", parent="y_axis")
    # Finishing up
    dpg.set_primary_window("exec_window", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
