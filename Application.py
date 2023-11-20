import dearpygui.dearpygui as dpg
import retrieve as ret
import time

stock = 'NVDA'  # Stores the currently selected stock
summary_view_fields = ["52WeekHigh", "52WeekLow", "Beta", "PriceToBookRatio", "DividendPerShare", "DividendYield",
                       "MarketCapitalization", "SharesOutstanding", "EPS", "QuarterlyEarningsGrowthYOY",
                       "RevenuePerShareTTM", "RevenueTTM", 'QuarterlyRevenueGrowthYOY', "EVtoRevenue", "GrossProfitTTM",
                       "PriceToSalesRatioTTM", "EBITDA", "EVtoEBITDA", "ProfitMargin", "OperatingMarginTTM",
                       "ReturnOnEquityTTM", "PERatio", "AnalystTargetPrice"]

dpg.create_context()

hist_data = ret.daily_hist(stock)
hist_data[0].reverse()
hist_data[1].reverse()
hist_data[2].reverse()
hist_data[3].reverse()
hist_data[4].reverse()
hist_data[5].reverse()

date_to_epoch = []

details_values = ret.summary_view(stock)

DAY_OFFSET = -25200  # Offset to fix date formatting

for x in hist_data[0]:

    epoch = int(time.mktime(time.strptime(x, "%Y-%m-%d"))) + DAY_OFFSET
    if epoch > 1699142400:
        epoch -= 3600

    date_to_epoch.append(epoch)


# Updates graph w/ new stock info
def update_graph(sender):
    u_hist_data = ret.daily_hist(sender)
    u_hist_data[0].reverse()
    u_hist_data[1].reverse()
    u_hist_data[2].reverse()
    u_hist_data[3].reverse()
    u_hist_data[4].reverse()
    u_hist_data[5].reverse()
    u_date_to_epoch = []
    for l in u_hist_data[0]:
        u_date_to_epoch.append(int(time.mktime(time.strptime(l, "%Y-%m-%d"))) + DAY_OFFSET)
    dpg.configure_item("candle_graph", dates=u_date_to_epoch, opens=u_hist_data[1], closes=u_hist_data[2],
                       lows=u_hist_data[3], highs=u_hist_data[4], label=sender)


'''
#Updates summary view w/ new stock info
def update_summ() {

}
'''


# Updates the currently selected stock
def update_stock(sender):
    update_graph(sender)
    # update_summ()


# Opens detailed view
'''def open_landing():
    with dpg.window(popup=True, autosize=False, no_resize=True, no_move=True,
                    pos=[int(dpg.get_viewport_client_width() / 4), int(dpg.get_viewport_client_height() / 4)]):
        with dpg.table(header_row=False, borders_outerH=True, borders_innerV=True, borders_innerH=True,
                       borders_outerV=True,
                       width=int(dpg.get_viewport_client_width() / 2),
                       height=int(dpg.get_viewport_client_height() / 2)):
            for x in range(6):
                dpg.add_table_column()

            counter = 0
            place_field = True
            for i in range(len(ret.tickers)):
                with dpg.table_row():
                    current_stock = ret.tickers[int(counter/6)]
                    stock_info = ret.daily_hist(current_stock)
                    for j in range(0, 6):
                        if place_field and counter < len(ret.tickers) * 6:
                            dpg.add_button(label=f"{current_stock}", callback=update_stock)
                            place_field = False
                        elif counter < 120:
                            dpg.add_text(f"{stock_info[counter % 6][0]}")
                            if counter % 6 == 5:
                                place_field = True
                        else:
                            dpg.add_text("")
                        counter += 1
'''

with dpg.window(tag="Home"):
    # create plot
    with dpg.plot(label="Candle Series (Daily)", height=400, width=-1):
        xaxis = dpg.add_plot_axis(dpg.mvXAxis, label="Day", time=True)
        with dpg.plot_axis(dpg.mvYAxis, label="USD", tag="candle_y"):
            dpg.add_candle_series(date_to_epoch, hist_data[1], hist_data[2], hist_data[3], hist_data[4],
                                  label="NVDA", weight=0.2, tooltip=True, time_unit=dpg.mvTimeUnit_Day,
                                  parent="candle_y", tag="candle_graph")

            dpg.fit_axis_data(dpg.top_container_stack())

        dpg.fit_axis_data(xaxis)

    # Doesn't work as intended, will try to find out how to get a proper menu
    with dpg.menu_bar():
        with dpg.menu(label="Tickers"):
            # Loop through tickers and add them to the menu
            for ticker in ret.tickers:
                dpg.add_menu_item(label=ticker, tag=ticker, callback=update_stock)

    with dpg.table(header_row=True, borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True,
                   tag="summ_table"):
        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        for x in range(6):
            dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        counter = 0
        place_field = True
        for i in range(0, 8):
            with dpg.table_row():
                for j in range(0, 6):
                    if place_field and counter < 23:
                        dpg.add_text(f"{summary_view_fields[counter]}")
                        place_field = False
                    elif counter < 23:
                        # amount of valid fields
                        dpg.add_text(f"{details_values[counter]}")
                        place_field = True
                        counter += 1
                    else:
                        dpg.add_text("")


dpg.create_viewport(title='Group A App', width=1080, height=720)
#open_landing()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Home", True)
dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
