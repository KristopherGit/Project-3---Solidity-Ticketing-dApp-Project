# concert venue generator & dictionary

# Note: Requires Version 4.14.3 to run without dedacted errors
import plotly.graph_objects as go
import numpy as np

# Venue function list
# 1.) Massey Hall - Toronto, Ontario, Canada
# i.) Massey Hall Gallery Section


def create_venue_massey_hall_main(galleryDictInput):
    # Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
    gallery = {}
    gallery = galleryDictInput

    # Instantiate each seat in a for-loop for each x,y-coord with attributes including: {x, y, name, price, bought=<boolean>, color=<#010C80>, owner_hash=address}
    # for x in range(57):
    #     for y in range(28):
    #         # Create a dictionary for the current seat
    #         seat = {
    #             'aisle': x,
    #             'row': y,
    #             'name': f'{x},{y}',
    #             # 'price': 71000000000000000,
    #             # 'bought': False,
    #             'color': '#1E90FF'
    #         }
    #         # Add the seat to the gallery dictionary
    #         gallery[seat['name']] = seat

    #########################################################

    # Create a list of scatter traces to represent the seats in the gallery
    # traces = []
    # for seat_number, seat in gallery.items():
    #     color = '#1E90FF'
    #     trace = go.Scatter(
    #         x=[seat['aisle']],
    #         y=[seat['row']],
    #         mode='markers',
    #         marker=dict(size=6, color=color),
    #         textfont=dict(
    #             size=20
    #         )
    #     )
    #     traces.append(trace)
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # to_remove_2 = [29*28+i for i in range(28)]
    # # Sort the indices in reverse order to avoid shifting
    # to_remove_2.sort(reverse=True)
    # # Remove the seats from the list
    # for index in to_remove_2:
    #     traces.pop(index)

    # to_remove_3 = [28*28+i for i in range(28)]
    # # Sort the indices in reverse order to avoid shifting
    # to_remove_3.sort(reverse=True)
    # # Remove the seats from the list
    # for index in to_remove_3:
    #     traces.pop(index)

    # to_remove_4 = [27*28+i for i in range(28)]
    # # Sort the indices in reverse order to avoid shifting
    # to_remove_4.sort(reverse=True)
    # # Remove the seats from the list
    # for index in to_remove_4:
    #     traces.pop(index)

    # seats_to_remove = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 74, 79, 80, 81, 82, 83, 84, 101, 102, 108, 109, 110, 111, 112, 129, 137, 138, 139, 140, 156, 157, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 280, 281, 308, 309, 336, 337, 364, 365, 392, 393, 394, 420, 421, 422, 448, 449, 450, 476, 477, 478, 504, 505, 506, 532, 533, 534, 560, 561, 562, 563, 588, 589, 590, 591, 616, 617, 618, 619, 644, 645, 646, 647, 672, 673, 674, 675, 700, 701, 702, 703, 728, 729, 730, 731, 756, 757, 758, 759, 784, 785, 786, 787, 812, 813, 814, 815, 840, 841,
    #                    842, 843, 868, 869, 870, 871, 896, 897, 898, 899, 924, 925, 926, 927, 952, 953, 954, 980, 981, 982, 1008, 1009, 1010, 1036, 1037, 1038, 1064, 1065, 1066, 1092, 1093, 1094, 1120, 1121, 1148, 1149, 1176, 1177, 1204, 1205, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1343, 1344, 1360, 1361, 1370, 1371, 1372, 1389, 1397, 1398, 1399, 1400, 1417, 1418, 1424, 1425, 1426, 1427, 1428, 1446, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1478, 1479, 1480, 1481, 1482, 1483, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511]

    # # Remove the seats from the gallery
    # for i in reversed(seats_to_remove):
    #     traces.pop(i)

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 60) - 8

    x = np.array(list(range(61)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#B3A301',
        text='STAGE',
        textposition='middle center',
        textfont=dict(color='white')  # set the text color to white
    )

    # Append the stage trace to the list of traces
    traces.append(stage)

    # Update stage formatting
    stage.update(fill='toself', fillcolor='#333333',
                 line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    bottom_line = go.Scatter(
        x=list(range(61)),
        y=[min(y) for i in range(61)],
        mode='lines',
        line=dict(width=2, color='#333333'),
    )

    # Append the bottom line trace to the list of traces
    traces.append(bottom_line)

    # return {
    #     'gallery': gallery,
    #     'traces' : traces
    # }
    return gallery, traces


def create_venue_massey_hall_balcony(galleryDictInput):
    # Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
    gallery = {}
    gallery = galleryDictInput

    #########################################################

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 65) - 4

    x = np.array(list(range(66)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#B3A301',
        text=['STAGE'],
        textposition='middle center',
        textfont=dict(color='white')  # set the text color to white
    )

    # Append the stage trace to the list of traces
    traces.append(stage)

    # Update stage formatting
    stage.update(fill='toself', fillcolor='#333333',
                 line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    bottom_line = go.Scatter(
        x=list(range(66)),
        y=[min(y) for i in range(66)],
        mode='lines',
        line=dict(width=2, color='#333333'),
    )

    # Append the bottom line trace to the list of traces
    traces.append(bottom_line)

    # return {
    #     'gallery': gallery,
    #     'traces' : traces
    # }
    return gallery, traces


def create_venue_massey_hall_gallery(galleryDictInput):
    #########################################################

    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 68) - 4

    x = np.array(list(range(69)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#B3A301',
        text=['STAGE'],
        textposition='middle center',
        textfont=dict(color='white')  # set the text color to white
    )

    # Append the stage trace to the list of traces
    traces.append(stage)

    # Update stage formatting
    stage.update(fill='toself', fillcolor='#333333',
                 line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    bottom_line = go.Scatter(
        x=list(range(69)),
        y=[min(y) for i in range(69)],
        mode='lines',
        line=dict(width=2, color='#333333'),
    )

    # Append the bottom line trace to the list of traces
    traces.append(bottom_line)

    # return {
    #     'gallery': gallery,
    #     'traces' : traces
    # }
    return gallery, traces


def create_venue_danforth_music_hall_main_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 41) - 4

    x = np.array(list(range(42)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#B3A301',
        text=['STAGE'],
        textposition='middle center',
        textfont=dict(color='white')  # set the text color to white
    )

    # Append the stage trace to the list of traces
    traces.append(stage)

    # Update stage formatting
    stage.update(fill='toself', fillcolor='#333333',
                 line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    bottom_line = go.Scatter(
        x=list(range(42)),
        y=[min(y) for i in range(42)],
        mode='lines',
        line=dict(width=2, color='#333333'),
    )

    # Append the bottom line trace to the list of traces
    traces.append(bottom_line)

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)
    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Danforth Music Hall Main Section - Test Function"),
                       font=dict(
                family='monospace',
                color='#B3A301'
            )
            ),
            xaxis=dict(title='X-coordinate',
                       autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            yaxis=dict(title='Y-coordinate',
                       autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            showlegend=False,
            legend=dict(itemclick="toggleothers"),
            annotations=[
                dict(
                    text='STAGE',
                    # x=center_x_value,
                    # y=-2.5,
                    # xanchor='center',
                    # yanchor='top',
                    showarrow=False,
                )
            ],
            font=dict(
                family='monospace',
                size=32,
                color='black'
            )
        )
        return layout

    layout = concert_layout(gallery)

    # Plot seating layout
    fig = go.Figure(data=traces, layout=layout)

    # Update traces/seats & add stage name
    fig.update_traces(textposition='top center',
                      hoverlabel=(dict(namelength=-1)))
    fig.update_layout(
        title={
            'text': str("Danforth Music Hall Main Section - Test Function"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        autosize=True, width=900, height=675, annotations=[
            dict(
                text="S T A G E",
                font=dict(
                    size=24,
                    family='monospace',
                    color='#B3A301'
                ),
                x=((traces[-2].x[-1] + traces[-2].x[0]) / 2),
                y=min(traces[-2].y) + 2
            )
        ], hoverlabel=dict(
            font=dict(
                size=16,
                color="#B3A301"
            )
        ))

    return gallery, traces, fig


def create_venue_elgin_theatre_orchestra_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # Create stage layout as a half moon trace figure

    # def stage_y_values(x):
    #     return 6 * np.sin(x * np.pi / 41) - 4

    # x = np.array(list(range(42)))
    # y = stage_y_values(x)

    stage = go.Scatter(
        x=[17, 17, 31, 31, 17],
        y=[35, 39, 39, 35, 35],
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#333333',
        hoverinfo='skip',  # exclude hoverinfo for this trace
        text='STAGE',
        textposition='middle center',
        textfont=dict(color='#B3A301', size=16)  # set the text color to white
    )
    traces.append(stage)

    # Add lines to separate rows for aesthetic purposes
    rowline1 = go.Scatter(
        x=[16, 16],
        y=[5, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[32, 32],
        y=[5, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['AA', 'BB', 'CC', 'DD', 'EE',
                   'FF', 'GG', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W']
    text_coords = [(17, 32), (17, 31), (17, 30), (12, 29),
                   (11, 28), (11, 27), (10, 26), (9, 25), (8, 24), (8, 23), (15, 22), (15, 21), (4, 20), (3, 19), (2, 18), (1, 17), (1, 16), (1, 15), (1, 14), (1, 13), (1, 12), (1, 11), (4, 10), (3, 9), (2, 8), (1, 7), (1, 6), (1, 5)]
    for label, coord in zip(text_labels, text_coords):
        x, y = coord
        text_trace = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=12, color='#B3A301'),
            showlegend=False,
            textposition='middle center'
        )
        traces.append(text_trace)

    # # Append the stage trace to the list of traces
    # traces.append(stage)

    # Update stage formatting
    # stage.update(fill='toself', fillcolor='#333333',
    #              line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    # bottom_line = go.Scatter(
    #     x=list(range(42)),
    #     y=[min(y) for i in range(42)],
    #     mode='lines',
    #     line=dict(width=2, color='#333333'),
    # )

    # # Append the bottom line trace to the list of traces
    # traces.append(bottom_line)

    # return {
    #     'gallery': gallery,
    #     'traces' : traces
    # }

    # Calculate midpoint of the x-range/y-range fo the 'stage' trace object

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Elgin Theatre Orchestra Section - Test Function"),
                       font=dict(
                family='monospace',
                color='#B3A301'
            )
            ),
            xaxis=dict(title='X-coordinate',
                       autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            yaxis=dict(title='Y-coordinate',
                       autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            showlegend=False,
            legend=dict(itemclick="toggleothers"),
            annotations=[
                dict(
                    text='STAGE',
                    # x=center_x_value,
                    # y=-2.5,
                    # xanchor='center',
                    # yanchor='top',
                    showarrow=False,
                )
            ],
            font=dict(
                family='monospace',
                size=32,
                color='black'
            )
        )
        return layout

    layout = concert_layout(gallery)

    # Plot seating layout
    fig = go.Figure(data=traces, layout=layout)

    # Update traces/seats & add stage name
    fig.update_traces(textposition='middle center',
                      hoverlabel=(dict(namelength=-1)))
    fig.update_layout(
        title={
            'text': str("Elgin Theatre Orchestra Section - Test Function"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        autosize=True, width=900, height=675, annotations=[
            dict(
                text="S T A G E",
                font=dict(
                    size=24,
                    family='monospace',
                    color='#B3A301'
                ),
                # x=((traces[-2].x[-1] + traces[-2].x[0]) / 2),
                # y=min(traces[-2].y) + 2
                x=(max(stage.x) - min(stage.x)) / 2 + min(stage.x),
                y=(max(stage.y) - min(stage.y)) / 2 + min(stage.y)
            )
        ], hoverlabel=dict(
            font=dict(
                size=16,
                color="#B3A301"
            )
        ))

    return gallery, traces, fig


def create_venue_elgin_theatre_mezzanine_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 41) - 4

    x = np.array(list(range(42)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#B3A301',
        text=['STAGE'],
        textposition='middle center',
        textfont=dict(color='white')  # set the text color to white
    )

    # Append the stage trace to the list of traces
    traces.append(stage)

    # Update stage formatting
    stage.update(fill='toself', fillcolor='#333333',
                 line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    bottom_line = go.Scatter(
        x=list(range(42)),
        y=[min(y) for i in range(42)],
        mode='lines',
        line=dict(width=2, color='#333333'),
    )

    # Append the bottom line trace to the list of traces
    traces.append(bottom_line)

    # return {
    #     'gallery': gallery,
    #     'traces' : traces
    # }
    return gallery, traces


def create_venue_elgin_theatre_balcony_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            )
        )
        traces.append(trace)

    #########################################################

    # Remove unnecessary traces to shape venue gallery layout

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 41) - 4

    x = np.array(list(range(42)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#B3A301',
        text=['STAGE'],
        textposition='middle center',
        textfont=dict(color='white')  # set the text color to white
    )

    # Append the stage trace to the list of traces
    traces.append(stage)

    # Update stage formatting
    stage.update(fill='toself', fillcolor='#333333',
                 line=dict(width=4, color='#333333'))

    # Add a contour line to the bottom of the half-moon stage outline
    bottom_line = go.Scatter(
        x=list(range(42)),
        y=[min(y) for i in range(42)],
        mode='lines',
        line=dict(width=2, color='#333333'),
    )

    # Append the bottom line trace to the list of traces
    traces.append(bottom_line)

    # return {
    #     'gallery': gallery,
    #     'traces' : traces
    # }
    return gallery, traces


# Dictionary to map venue names as keys to venue property function as values
# Venue dictionary for st.selectbox i.) key (venue) ii.) value (section; gallery, mezzanine, balcony, etc)
# venue_dictionary = {
#     "Massey Hall": {
#         "Massey Hall Gallery Section": create_venue_massey_hall_gallery
#     }
# }
