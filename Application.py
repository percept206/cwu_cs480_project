import dearpygui.dearpygui as dpg
import retrieve as ret
import time

stock = 'NVDA'  # Stores the currently selected stock
summary_view_fields = ["52WeekHigh", "52WeekLow", "Beta", "PriceToBookRatio", "DividendPerShare", "DividendYield",
                       "MarketCapitalization", "SharesOutstanding", "EPS", "QuarterlyEarningsGrowthYOY",
                       "RevenuePerShareTTM", "RevenueTTM", 'QuarterlyRevenueGrowthYOY', "EVtoRevenue", "GrossProfitTTM",
                       "PriceToSalesRatioTTM", "EBITDA", "EVtoEBITDA", "ProfitMargin", "OperatingMarginTTM",
                       "ReturnOnEquityTTM", "PERatio", "AnalystTargetPrice"]

tooltips = [
    "Highest Price in 52 Weeks",
    "Lowest Price in 52 Weeks",
    "Measure of how volatile the stock is compared to the S&P 500 index, Higher indicates more volatility",
    "Share price / book value per share: < 1 may signal undervaluation, > 1 trading at a premium",
    "Dividend payout per share",
    "percentage of dividend payout compared to stock price relative to the year",
    "Total value of all shares outstanding",
    "total amount of shares in existence",
    "Earnings per share",
    "Quarterly Earnings compared year over year",
    "Revenue per share during the last 12 months",
    "Revenue in last 12 months",
    "Quarterly revenue compared year over year",
    "Enterprise Value / Revenue",
    "Gross Profit in last 12 months",
    "Price to Sales in last 12 months",
    "Earnings Before Income Tax Depreciation and Amortization",
    "Enterpise Value to EBITDA",
    "Profit Margin, how many cents of profit generated for each dollar of sales",
    "Operating Margin in the last 12 months",
    'Return on Equity in the last 12 months',
    "Price to Equity Ratio",
    "Analyst Target Price"
]

dpg.create_context()
dpg.create_viewport(title='Group A App', width=1080, height=720)
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
        epoch -= 3600 # adjust for DST

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



def clear_table() :
    for tag in dpg.get_item_children("summ_table")[1]:
        dpg.delete_item(tag)


#Updates summary view w/ new stock info
def update_summ(sender) :
    clear_table()

    new_values = ret.summary_view(sender)

    counter = 0
    place_field = True

    for i in range(0, 8):
        with dpg.table_row(parent="summ_table", tag=f"row_{i}"):
            for j in range(0, 6):
                if place_field and counter < 23: # populate table with fields
                    dpg.add_text(f"{summary_view_fields[counter]}", tag=f"{counter}")
                    with dpg.tooltip(parent=f"{counter}"):
                        dpg.add_text(tooltips[counter])
                    place_field = False
                elif counter < 23: # populate table with corresponding values
                    if counter == 5:
                        dpg.add_text(f"{new_values[counter]:.4%}")
                    elif counter == 9 or counter == 12:
                        dpg.add_text(f"{new_values[counter]}%")
                    elif (counter == 6 or counter == 11 or counter == 14 or counter == 16):
                        dpg.add_text(format(int(details_values[counter]), "d"))
                    else:
                        dpg.add_text(f"{new_values[counter]}")
                    place_field = True
                    counter += 1
                else:
                    dpg.add_text("")


# Ensures landing closes when stock selected
def select_stock(sender):
    dpg.configure_item("Landing", show=False)
    dpg.configure_item("Home", show=True)
    update_stock(sender)

#Switching from home to landing page
def select_landing(sender):
    dpg.configure_item("Landing", show=True)
    dpg.configure_item("Home", show=False)
    update_stock(sender)
# Updates the currently selected stock
def update_stock(sender):
    update_graph(sender)
    update_summ(sender)

#def switch()
# Opens landing page
def open_landing():
    with dpg.font_registry():
        default_font = dpg.add_font("assets\calibri.ttf", 24)

    with dpg.window(popup=True, autosize=False, no_resize=True, no_move=True,
                    pos=[0, 0], tag='Landing'):
        with dpg.table(header_row=True, borders_outerH=True, borders_innerV=True, borders_innerH=True,
                       borders_outerV=True,
                       width=int(dpg.get_viewport_client_width()),
                       height=int(dpg.get_viewport_client_height())):
            dpg.add_table_column(label='Tickers')
            dpg.add_table_column(label='Open')
            dpg.add_table_column(label='High')
            dpg.add_table_column(label='Close')
            dpg.add_table_column(label='Low')
            dpg.add_table_column(label='Volume')

            counter = 0
            place_field = True
            for i in range(len(ret.tickers)):
                with dpg.table_row():

                    current_stock = ret.tickers[int(counter/6)]
                    stock_info = ret.daily_histFromDB(current_stock)
                    for j in range(0, 6):
                        if place_field and counter < len(ret.tickers) * 6:
                            dpg.add_button(label=f"{current_stock}", callback=select_stock,
                                           height=int(dpg.get_viewport_client_height() / 20),
                                           width=int(dpg.get_viewport_client_width() / 6))

                            dpg.bind_font(default_font)
                            place_field = False
                        elif counter < 120:
                            dpg.add_text(f"{stock_info[counter % 6][0]}")
                            dpg.bind_font(default_font)
                            if counter % 6 == 5:
                                place_field = True
                        else:
                            dpg.add_text("")
                        counter += 1


with dpg.window(tag="Home", show=False):
    # create plot
    with dpg.plot(label="Candle Series (Daily)", height=400, width=-1):
        dpg.add_plot_legend()
        xaxis = dpg.add_plot_axis(dpg.mvXAxis, label="Day", time=True)
        with dpg.plot_axis(dpg.mvYAxis, label="USD", tag="candle_y"):
            dpg.add_candle_series(date_to_epoch, hist_data[1], hist_data[2], hist_data[3], hist_data[4],
                                  label="NVDA", weight=0.15, tooltip=True, time_unit=dpg.mvTimeUnit_Day,
                                  parent="candle_y", tag="candle_graph")

            dpg.fit_axis_data(dpg.top_container_stack())

        dpg.fit_axis_data(xaxis)

    # Doesn't work as intended, will try to find out how to get a proper menu
    with dpg.menu_bar():
        #button to go back to landing page
        dpg.add_button(label="Landing Page", callback=select_landing)
        with dpg.menu(label="Tickers"):
            # Loop through tickers and add them to the menu
            for ticker in ret.tickers:
                dpg.add_menu_item(label=ticker, tag=ticker, callback=update_stock)


    with dpg.table(borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True,
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
            with dpg.table_row(parent="summ_table", tag=f"row_{i}"):
                for j in range(0, 6):
                    if place_field and counter < 23: # populate table with fields
                        dpg.add_text(f"{summary_view_fields[counter]}", tag=f"{counter}")
                        with dpg.tooltip(parent=f"{counter}"):
                            dpg.add_text(tooltips[counter])
                        place_field = False
                    elif counter < 23:
                        # populate table with values
                        if counter == 5:
                            dpg.add_text(f"{details_values[counter]:.4%}")
                        elif counter == 9 or counter == 12:
                            dpg.add_text(f"{details_values[counter]}%")
                        elif (counter == 6 or counter == 11 or counter == 14 or counter == 16):
                            dpg.add_text(format(int(details_values[counter]), "d" ))
                        else:
                            dpg.add_text(f"{details_values[counter]}")
                        place_field = True
                        counter += 1
                    else:
                        dpg.add_text("")



open_landing()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Home", True)
dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()