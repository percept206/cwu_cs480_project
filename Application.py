import dearpygui.dearpygui as dpg
import retrieve as ret
import time


dpg.create_context()

hist_data = ret.daily_hist('NVDA')

hist_data[0].reverse()
hist_data[1].reverse()
hist_data[2].reverse()
hist_data[3].reverse()
hist_data[4].reverse()
hist_data[5].reverse()

date_to_epoch = []

DAY_OFFSET = -25200 # offset to fix date formatting

for x in hist_data[0]:
    date_to_epoch.append(int(time.mktime(time.strptime(x, "%Y-%m-%d"))) + DAY_OFFSET)
print(date_to_epoch)

def open_det_view():
    with dpg.window(label="Detailed View", popup=True, autosize=False, no_resize=True, no_move=True,
                    pos=[int(dpg.get_viewport_client_width()/4), int(dpg.get_viewport_client_height()/4)]):
        with dpg.table(header_row=True, borders_outerH=True, borders_innerV=True, borders_innerH=True,
                       borders_outerV=True,
                       width=int(dpg.get_viewport_client_width()/2), height=int(dpg.get_viewport_client_height()/2)):

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()

            # add_table_next_column will jump to the next row
            # once it reaches the end of the columns
            # table next column use slot 1
            for i in range(0, 4):
                with dpg.table_row():
                    for j in range(0, 3):
                        dpg.add_text(f"Row{i} Column{j}")

with dpg.window(tag="Home"):
    # create plot
    with dpg.plot(label="Candle Series (Daily)", height=400, width=-1):

        dpg.add_plot_legend()
        xaxis = dpg.add_plot_axis(dpg.mvXAxis, label="Day", time=True)
        with dpg.plot_axis(dpg.mvYAxis, label="USD"):

            dpg.add_candle_series(date_to_epoch, hist_data[1], hist_data[2], hist_data[3], hist_data[4],
            label="NVDA", weight=0.3,tooltip=True, time_unit=dpg.mvTimeUnit_Day)

            dpg.fit_axis_data(dpg.top_container_stack())

        dpg.fit_axis_data(xaxis)

    #dpg.add_menu_bar()
    #dpg.add_same_line()
    dpg.add_button(label="Detailed View", callback=open_det_view, height=40, width=100)

    with dpg.table(header_row=True, borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):

        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 4):
            with dpg.table_row():
                for j in range(0, 3):
                    dpg.add_text(f"Row{i} Column{j}")

dpg.create_viewport(title='Group A App', width=1080, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Home", True)
dpg.start_dearpygui()
dpg.destroy_context()