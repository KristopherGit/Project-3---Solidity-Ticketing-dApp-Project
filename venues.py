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

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'  # medium/sky-blue (standard basic blue)
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################
    # create list of alphabetical row text labels & their coordinates

    text_labels = ['100', '104', '106', '101', '103', '105', '102', 'A', 'B', 'C', 'D', 'E',
                   'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'SRO', 'A', 'B', 'C', 'D', 'SRO', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F']
    text_coords = [(7, 9), (14, 21), (4, 1), (56, 1), (49, 21), (7, 33), (53, 33), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6),
                   (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (10, 14), (15, 16), (17, 19), (17, 20), (17, 21), (18, 22), (19, 23), (20, 24), (6, 3), (5, 3), (4, 3), (3, 3), (1, 3), (54, 3), (55, 3), (56, 3), (57, 3), (59, 3), (45, 19), (46, 20), (45, 21), (45, 22), (44, 23), (44, 24), (8, 22), (6, 22), (5, 23), (4, 24), (3, 25), (3, 27), (52, 22), (54, 22), (55, 23), (56, 24), (56, 26), (56, 28)]
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

    # Add row lines to venue layout
    rowline1 = go.Scatter(
        x=[30, 30],
        y=[2, 16],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[8, 8],
        y=[1, 8],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    rowline3 = go.Scatter(
        x=[8, 8],
        y=[10, 17],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    arrow_2 = go.Scatter(
        x=[9],
        y=[1],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_2)

    arrow_3 = go.Scatter(
        x=[9],
        y=[17],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_3)

    rowline4 = go.Scatter(
        x=[8, 9],
        y=[17, 17],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    rowline5 = go.Scatter(
        x=[8, 9],
        y=[1, 1],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

    rowline6 = go.Scatter(
        x=[16, 16],
        y=[18, 25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline6)

    arrow_4 = go.Scatter(
        x=[17],
        y=[18],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_4)

    rowline7 = go.Scatter(
        x=[16, 17],
        y=[18, 18],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline7)

    arrow_5 = go.Scatter(
        x=[17],
        y=[25],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_5)

    rowline8 = go.Scatter(
        x=[16, 17],
        y=[25, 25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline8)

    rowline9 = go.Scatter(
        x=[47, 47],
        y=[18, 25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline9)

    arrow_6 = go.Scatter(
        x=[46],
        y=[25],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_6)

    arrow_7 = go.Scatter(
        x=[46],
        y=[18],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_7)

    rowline10 = go.Scatter(
        x=[46, 47],
        y=[18, 18],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline10)

    rowline11 = go.Scatter(
        x=[46, 47],
        y=[25, 25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline11)

    # Create stage layout as a half moon trace figure
    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 60) - 6

    x = np.array(list(range(61)))
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
        x=list(range(61)),
        y=[min(y) for i in range(61)],
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
            title=dict(text=str("Massey Hall Main"),
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
            'text': str("Massey Hall Main"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        autosize=False, width=900, height=625, annotations=[
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
        ),
        margin=dict(
            l=20,  # adjust the left margin
            r=20,  # adjust the right margin
            t=30,  # adjust the title margin
            b=20,  # adjust the bottom margin
        ),
        paper_bgcolor='#000000',  # super dark grey, almost black
        plot_bgcolor='#000000'  # super dark grey almost black
    )

    return gallery, traces, fig


def create_venue_massey_hall_balcony(galleryDictInput):
    # Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################
    # create list of alphabetical row text labels & their coordinates

    text_labels = ['209', '208', '208', '207 SRO', '207', '206', '204', '205', '203', 'SRO 203', '202', '202', '201', 'A', 'B', 'C', 'D', 'E',
                   'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    text_coords = [(11, 7), (11, 17), (0, 28), (-1, 43), (15, 29), (26, 29), (40, 29), (33, 47), (51, 29), (67, 43), (66, 28), (55, 17), (55, 7), (8, 4), (7, 2), (6, 2),
                   (5, 2), (4, 3), (3, 5), (2, 6), (8, 22), (7, 22), (6, 22), (5, 22), (4, 22), (3, 22), (2, 21), (9, 24), (8, 24), (7, 24), (6, 24), (5, 24), (4, 24), (3, 24), (18, 32), (18, 33), (18, 34), (18, 35), (18, 36), (18, 37), (18, 38), (18, 39), (15, 40), (14, 41), (33, 31), (33, 32), (33, 33), (33, 34), (33, 35), (33, 36), (33, 37), (33, 38), (48, 32), (48, 33), (48, 34), (48, 35), (48, 36), (48, 37), (48, 38), (48, 39), (49, 40), (52, 41), (57, 24), (58, 24), (59, 24), (60, 24), (61, 24), (62, 24), (63, 26), (58, 22), (59, 22), (60, 22), (61, 22), (62, 22), (63, 22), (64, 22), (58, 4), (59, 2), (60, 1), (61, 2), (62, 3), (63, 4), (64, 5)]
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

    # Sec 209 line
    rowline1 = go.Scatter(
        x=[9, 9],
        y=[2, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    # Sec 209 arrow 1
    arrow_1 = go.Scatter(
        x=[8],
        y=[2],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_1)

    rowline2 = go.Scatter(
        x=[8, 9],
        y=[2, 2],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # Sec 209 arrow 2
    arrow_2 = go.Scatter(
        x=[8],
        y=[12],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_2)

    rowline3 = go.Scatter(
        x=[8, 9],
        y=[12, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    # Sec 208 line
    rowline4 = go.Scatter(
        x=[9, 9],
        y=[13, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    # Sec 208 arrow 3
    arrow_3 = go.Scatter(
        x=[8],
        y=[13],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_3)

    rowline5 = go.Scatter(
        x=[8, 9],
        y=[13, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

    # Sec 208 arrow 4
    arrow_4 = go.Scatter(
        x=[8],
        y=[23],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_4)

    rowline6 = go.Scatter(
        x=[8, 9],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline6)

    # Sec 208 b line
    rowline7 = go.Scatter(
        x=[2, 2],
        y=[23, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline7)

    # Sec 208 arrow 5
    arrow_5 = go.Scatter(
        x=[3],
        y=[23],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_5)

    rowline8 = go.Scatter(
        x=[2, 3],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline8)

    # Sec 208 arrow 6
    arrow_6 = go.Scatter(
        x=[3],
        y=[34],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_6)

    rowline9 = go.Scatter(
        x=[2, 3],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline9)

    # Sec 206 line
    rowline10 = go.Scatter(
        x=[20, 32],
        y=[30, 30],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline10)

    # Sec 206 arrow up
    arrow_7 = go.Scatter(
        x=[32],
        y=[31],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_7)

    rowline11 = go.Scatter(
        x=[32, 32],
        y=[30, 31],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline11)

    # Sec 206 arrow up
    arrow_8 = go.Scatter(
        x=[20],
        y=[31],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_8)

    rowline12 = go.Scatter(
        x=[20, 20],
        y=[30, 31],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline12)

    # Sec 204 line
    rowline13 = go.Scatter(
        x=[34, 46],
        y=[30, 30],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline13)

    # Sec 206 arrow up
    arrow_9 = go.Scatter(
        x=[34],
        y=[31],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_9)

    # Sec 206 arrow up
    arrow_10 = go.Scatter(
        x=[46],
        y=[31],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_10)

    # Sec 204 vertical short line
    rowline14 = go.Scatter(
        x=[34, 34],
        y=[30, 31],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline14)

    # Sec 204 vertical short line
    rowline15 = go.Scatter(
        x=[46, 46],
        y=[30, 31],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline15)

    # Sec 205 line
    rowline16 = go.Scatter(
        x=[19, 47],
        y=[46, 46],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline16)

    # Sec 205 arrow up
    arrow_11 = go.Scatter(
        x=[19],
        y=[45],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-down', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_11)

    # Sec 205 vertical short line
    rowline17 = go.Scatter(
        x=[19, 19],
        y=[46, 45],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline17)

    # Sec 205 arrow up
    arrow_12 = go.Scatter(
        x=[47],
        y=[45],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-down', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_12)

    # Sec 205 vertical short line
    rowline18 = go.Scatter(
        x=[47, 47],
        y=[46, 45],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline18)

    # Sec 202 line
    rowline19 = go.Scatter(
        x=[64, 64],
        y=[24, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline19)

    # Sec 202 arrow left
    arrow_13 = go.Scatter(
        x=[63],
        y=[24],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_13)

    # Sec 202 horizontal short line
    rowline19 = go.Scatter(
        x=[63, 64],
        y=[24, 24],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline19)

    # Sec 202 arrow left
    arrow_14 = go.Scatter(
        x=[63],
        y=[34],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_14)

    # Sec 202 horizontal short line
    rowline20 = go.Scatter(
        x=[63, 64],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline20)

    # Sec 202 line B
    rowline21 = go.Scatter(
        x=[57, 57],
        y=[13, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline21)

    # Sec 202 arrow RIGHT B
    arrow_15 = go.Scatter(
        x=[58],
        y=[13],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_15)

    # Sec 202 horizontal short line
    rowline22 = go.Scatter(
        x=[57, 58],
        y=[13, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline22)

    # Sec 202 arrow RIGHT B
    arrow_16 = go.Scatter(
        x=[58],
        y=[23],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_16)

    # Sec 202 horizontal short line
    rowline23 = go.Scatter(
        x=[57, 58],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline23)

    # Sec 201 line
    rowline24 = go.Scatter(
        x=[57, 57],
        y=[1, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline24)

    # Sec 201 arrow RIGHT
    arrow_17 = go.Scatter(
        x=[58],
        y=[1],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_17)

    # Sec 201 horizontal short line
    rowline25 = go.Scatter(
        x=[57, 58],
        y=[1, 1],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline25)

    # Sec 201 arrow RIGHT
    arrow_18 = go.Scatter(
        x=[58],
        y=[12],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_18)

    # Sec 201 horizontal short line
    rowline26 = go.Scatter(
        x=[57, 58],
        y=[12, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline26)

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 65) - 3

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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)
    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Massey Hall Balcony"),
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
            'text': str("Massey Hall Balcony"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        autosize=False, width=900, height=625, annotations=[
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
        ),
        margin=dict(
            l=20,  # adjust the left margin
            r=20,  # adjust the right margin
            t=30,  # adjust the title margin
            b=20,  # adjust the bottom margin
        ),
        paper_bgcolor='#000000',  # super dark grey, almost black
        plot_bgcolor='#000000'
    )

    return gallery, traces, fig


def create_venue_massey_hall_gallery(galleryDictInput):
    #########################################################

    # Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################
    # create list of alphabetical row text labels & their coordinates

    text_labels = ['311', '310', '309', '308', '307', '305', '306', '304', '303', '302', '301', 'A', 'B', 'C', 'D', 'E',
                   'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'A', 'B', 'C', 'D', 'E', 'F', 'G',                      'A', 'B', 'C', 'D', 'E', 'F', 'G',                      'A', 'B', 'C', 'D', 'E', 'F', 'G']
    text_coords = [(11, 7), (11, 17), (-2, 31), (-2, 43), (26, 33), (42, 33), (34, 51), (70, 43), (70, 31), (57, 17), (57, 7), (7, 1), (6, 0), (5, 1), (4, 2), (3, 2), (2, 2), (1, 2), (7, 24), (6, 23), (5, 24), (4, 24), (3, 24), (2, 23), (1, 23), (7, 25), (6, 25), (5, 25), (4, 25), (3, 25), (2, 25), (1, 25), (7, 37), (6, 38), (5, 39), (4, 40), (3, 41), (2, 42), (1, 43),
                   (34, 37), (34, 38), (34, 39), (34, 40), (34, 43), (34, 44), (34, 45), (34, 46), (34, 47), (34, 49), (61, 37), (62, 38), (63, 39), (64, 40), (65, 41), (66, 42), (67, 43),                      (61, 24), (62, 23), (63, 24), (64, 24), (65, 24), (66, 23), (67, 23),                 (61, 1), (62, 0), (63, 1), (64, 2), (65, 2), (66, 2), (67, 2)]
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

    # Sec 311 line
    rowline1 = go.Scatter(
        x=[9, 9],
        y=[2, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    # Sec 311 arrow 1
    arrow_1 = go.Scatter(
        x=[8],
        y=[2],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_1)

    rowline2 = go.Scatter(
        x=[8, 9],
        y=[2, 2],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # Sec 311 arrow 2
    arrow_2 = go.Scatter(
        x=[8],
        y=[12],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_2)

    rowline3 = go.Scatter(
        x=[8, 9],
        y=[12, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    # Sec 310 line
    rowline4 = go.Scatter(
        x=[9, 9],
        y=[13, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    # Sec 310 arrow 3
    arrow_3 = go.Scatter(
        x=[8],
        y=[13],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_3)

    rowline5 = go.Scatter(
        x=[8, 9],
        y=[13, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

    # Sec 310 arrow 4
    arrow_4 = go.Scatter(
        x=[8],
        y=[23],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_4)

    rowline6 = go.Scatter(
        x=[8, 9],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline6)

    # Sec 309 b line
    rowline7 = go.Scatter(
        x=[0, 0],
        y=[24, 39],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline7)

    # Sec 309 arrow 5
    arrow_5 = go.Scatter(
        x=[1],
        y=[24],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_5)

    rowline8 = go.Scatter(
        x=[0, 1],
        y=[24, 24],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline8)

    # Sec 309 arrow 6
    arrow_6 = go.Scatter(
        x=[1],
        y=[39],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_6)

    rowline9 = go.Scatter(
        x=[0, 1],
        y=[39, 39],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline9)

    # Sec 307 line
    rowline10 = go.Scatter(
        x=[20, 32],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline10)

    # Sec 206 arrow up
    arrow_7 = go.Scatter(
        x=[32],
        y=[35],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_7)

    rowline11 = go.Scatter(
        x=[32, 32],
        y=[34, 35],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline11)

    # Sec 307 arrow up
    arrow_8 = go.Scatter(
        x=[20],
        y=[35],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_8)

    rowline12 = go.Scatter(
        x=[20, 20],
        y=[34, 35],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline12)

    # Sec 305 line
    rowline13 = go.Scatter(
        x=[36, 48],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline13)

    # Sec 305 arrow up
    arrow_9 = go.Scatter(
        x=[36],
        y=[35],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_9)

    # Sec 305 arrow up
    arrow_10 = go.Scatter(
        x=[48],
        y=[35],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_10)

    # Sec 305 vertical short line
    rowline14 = go.Scatter(
        x=[36, 36],
        y=[34, 35],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline14)

    # Sec 305 vertical short line
    rowline15 = go.Scatter(
        x=[48, 48],
        y=[34, 35],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline15)

    # Sec 306 line
    rowline16 = go.Scatter(
        x=[18, 50],
        y=[50, 50],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline16)

    # Sec 306 arrow down
    arrow_11 = go.Scatter(
        x=[18],
        y=[49],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-down', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_11)

    # Sec 306 vertical short line
    rowline17 = go.Scatter(
        x=[18, 18],
        y=[49, 50],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline17)

    # Sec 306 arrow down
    arrow_12 = go.Scatter(
        x=[50],
        y=[49],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-down', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_12)

    # Sec 306 vertical short line
    rowline18 = go.Scatter(
        x=[50, 50],
        y=[49, 50],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline18)

    # Sec 303 line
    rowline19 = go.Scatter(
        x=[68, 68],
        y=[24, 38],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline19)

    # Sec 303 arrow left
    arrow_13 = go.Scatter(
        x=[67],
        y=[24],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_13)

    # Sec 303 horizontal short line
    rowline19 = go.Scatter(
        x=[67, 68],
        y=[24, 24],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline19)

    # Sec 303 arrow left
    arrow_14 = go.Scatter(
        x=[67],
        y=[38],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_14)

    # Sec 303 horizontal short line
    rowline20 = go.Scatter(
        x=[67, 68],
        y=[38, 38],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline20)

    # Sec 302 line B
    rowline21 = go.Scatter(
        x=[59, 59],
        y=[13, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline21)

    # Sec 302 arrow RIGHT B
    arrow_15 = go.Scatter(
        x=[60],
        y=[13],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_15)

    # Sec 302 horizontal short line
    rowline22 = go.Scatter(
        x=[59, 60],
        y=[13, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline22)

    # Sec 302 arrow RIGHT B
    arrow_16 = go.Scatter(
        x=[60],
        y=[23],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_16)

    # Sec 302 horizontal short line
    rowline23 = go.Scatter(
        x=[59, 60],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline23)

    # Sec 301 line
    rowline24 = go.Scatter(
        x=[59, 59],
        y=[1, 11],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline24)

    # Sec 301 arrow RIGHT
    arrow_17 = go.Scatter(
        x=[60],
        y=[1],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_17)

    # Sec 201 horizontal short line
    rowline25 = go.Scatter(
        x=[59, 60],
        y=[1, 1],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline25)

    # Sec 201 arrow RIGHT
    arrow_18 = go.Scatter(
        x=[60],
        y=[11],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_18)

    # Sec 201 horizontal short line
    rowline26 = go.Scatter(
        x=[59, 60],
        y=[11, 11],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline26)

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 67) - 3

    x = np.array(list(range(68)))
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
        x=list(range(68)),
        y=[min(y) for i in range(68)],
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
            title=dict(text=str("Massey Hall Gallery"),
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
            'text': str("Massey Hall Gallery"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        autosize=False, width=900, height=625, annotations=[
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
        ),
        margin=dict(
            l=20,  # adjust the left margin
            r=20,  # adjust the right margin
            t=30,  # adjust the title margin
            b=20,  # adjust the bottom margin
        )
    )

    return gallery, traces, fig


def create_venue_danforth_music_hall_main_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################
    # create list of alphabetical row text labels & their coordinates

    text_labels = ['UU', 'TT', 'SS', 'RR', 'PP',
                   'OO', 'NN', 'MM', 'LL', 'KK', 'JJ', 'HH', 'GG', 'FF', 'GA']
    text_coords = [(0, 49), (0, 48), (0, 47), (0, 46),
                   (0, 45), (0, 44), (0, 43), (0, 42), (0, 41), (0, 40), (0, 39), (0, 35), (0, 34), (0, 33), (0, 19)]
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

    # Add row lines to venue layout
    rowline1 = go.Scatter(
        x=[3, 38],
        y=[31, 31],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[2, 39],
        y=[37, 37],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    rowline3 = go.Scatter(
        x=[12, 12],
        y=[6, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    rowline4 = go.Scatter(
        x=[13, 13],
        y=[6, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    rowline5 = go.Scatter(
        x=[28, 28],
        y=[6, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

    rowline6 = go.Scatter(
        x=[29, 29],
        y=[6, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline6)

    arrow_1 = go.Scatter(
        x=[2],
        y=[30],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_1)

    arrow_2 = go.Scatter(
        x=[2, 2],
        y=[5, 5],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_2)

    rowline7 = go.Scatter(
        x=[1, 1],
        y=[5, 30],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline7)

    rowline8 = go.Scatter(
        x=[1, 2],
        y=[5, 5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline8)

    rowline9 = go.Scatter(
        x=[1, 2],
        y=[30, 30],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline9)

    rowline10 = go.Scatter(
        x=[13, 13],
        y=[39, 47],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline10)

    rowline11 = go.Scatter(
        x=[14, 14],
        y=[39, 47],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline11)

    rowline12 = go.Scatter(
        x=[27, 27],
        y=[39, 47],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline12)

    rowline13 = go.Scatter(
        x=[28, 28],
        y=[39, 47],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline13)

    # Create stage layout as a half moon trace figure
    def stage_y_values(x):
        return 6 * np.sin(x * np.pi / 41) - 2

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

    # Create mixing both trace object
    x = [18, 18, 27, 27, 19, 19, 18]
    y = [28, 29, 29, 26, 26, 28, 28]

    mixing_both = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line=dict(width=2, color='#333333'),
        fillcolor='#333333',
        fill='toself'
    )

    # Append mixing both to the list of traces
    traces.append(mixing_both)

    # Calculate center of the trapezoid mixing both trace object
    center_x = sum(x)/len(x) + 2
    center_y = sum(y)/len(y) - 1
    text_label = 'Mixing Position'

    mixing_position_label = go.Scatter(
        x=[center_x],
        y=[center_y],
        mode='text',
        text=text_label,
        textfont=dict(size=14, color='#B3A301'),
        showlegend=False
    )

    # Append mixing both label to the list of traces
    traces.append(mixing_position_label)

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
                       range=[-2, 43], showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            yaxis=dict(title='Y-coordinate',
                       range=[-2, 50], showgrid=None, gridcolor=None, showticklabels=False, visible=False),
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
            'text': str("Danforth Music Hall Main Section"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        autosize=False, width=900, height=625, annotations=[
            dict(
                text="S T A G E",
                font=dict(
                    size=24,
                    family='monospace',
                    color='#B3A301'
                ),
                x=((traces[-3].x[-1] + traces[-3].x[0]) / 2),
                y=min(traces[-3].y) + 2
            )
        ], hoverlabel=dict(
            font=dict(
                size=16,
                color="#B3A301"
            )
        ),
        margin=dict(
            l=20,  # adjust the left margin
            r=20,  # adjust the right margin
            t=30,  # adjust the title margin
            b=20,  # adjust the bottom margin
        )
    )

    return gallery, traces, fig


def create_venue_elgin_theatre_orchestra_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

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

    # Add lines to separate rows for aesthetic purposes on venue floor
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

    rowline3 = go.Scatter(
        x=[17, 31],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    rowline4 = go.Scatter(
        x=[5, 14],
        y=[21, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    rowline5 = go.Scatter(
        x=[34, 43],
        y=[21, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

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
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[16, 16],
        y=[5, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[32, 32],
        y=[5, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    rowline3 = go.Scatter(
        x=[17, 31],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    text_coords = [(4, 12), (3, 11), (3, 10), (1, 9),
                   (1, 8), (1, 7), (1, 6), (1, 5)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Elgin Theatre Mezzanine Section"),
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
            'text': str("Elgin Theatre Mezzanine Section"),
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


def create_venue_elgin_theatre_balcony_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[10, 10],
        y=[5, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[11, 11],
        y=[5, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    rowline3 = go.Scatter(
        x=[24, 24],
        y=[5, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    rowline4 = go.Scatter(
        x=[37, 37],
        y=[5, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    rowline5 = go.Scatter(
        x=[38, 38],
        y=[5, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S']
    text_coords = [(-1, 13), (-1, 12), (-1, 11), (-1, 10),
                   (-1, 9), (-1, 8), (-1, 7), (-1, 6), (-1, 5)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Elgin Theatre Balcony Section"),
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
            'text': str("Elgin Theatre Balcony Section"),
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


def create_venue_winter_garden_theatre_orchestra_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[15, 15, 30, 30, 15],
        y=[33, 37, 37, 33, 33],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[14, 14],
        y=[12, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[31, 31],
        y=[12, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    rowline3 = go.Scatter(
        x=[8, 13],
        y=[22, 22],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    rowline4 = go.Scatter(
        x=[32, 37],
        y=[22, 22],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline4)

    rowline5 = go.Scatter(
        x=[0, 6],
        y=[32, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline5)

    rowline6 = go.Scatter(
        x=[0, 0],
        y=[23, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline6)

    rowline7 = go.Scatter(
        x=[0, 6],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline7)

    rowline8 = go.Scatter(
        x=[3, 3],
        y=[23, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline8)

    rowline9 = go.Scatter(
        x=[6, 6],
        y=[23, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline9)

    rowline10 = go.Scatter(
        x=[1, 1],
        y=[8, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline10)

    rowline11 = go.Scatter(
        x=[1, 4],
        y=[21, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline11)

    rowline12 = go.Scatter(
        x=[4, 4],
        y=[8, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline12)

    rowline13 = go.Scatter(
        x=[1, 4],
        y=[8, 8],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline13)

    rowline14 = go.Scatter(
        x=[39, 45],
        y=[32, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline14)

    rowline15 = go.Scatter(
        x=[39, 45],
        y=[32, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline15)

    rowline16 = go.Scatter(
        x=[39, 39],
        y=[23, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline16)

    rowline17 = go.Scatter(
        x=[39, 45],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline17)

    rowline18 = go.Scatter(
        x=[39, 45],
        y=[23, 23],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline18)

    rowline18 = go.Scatter(
        x=[45, 45],
        y=[23, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline18)

    rowline19 = go.Scatter(
        x=[42, 42],
        y=[23, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline19)

    rowline20 = go.Scatter(
        x=[41, 44],
        y=[21, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline20)

    rowline21 = go.Scatter(
        x=[41, 44],
        y=[21, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline21)

    rowline22 = go.Scatter(
        x=[41, 41],
        y=[8, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline22)

    rowline23 = go.Scatter(
        x=[41, 44],
        y=[8, 8],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline23)

    rowline24 = go.Scatter(
        x=[44, 44],
        y=[8, 21],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline24)

    rowline25 = go.Scatter(
        x=[15, 30],
        y=[32, 32],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline25)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U']
    text_coords = [(14, 30), (11, 29), (10, 28), (9, 27),
                   (9, 26), (8, 25), (10, 24), (7, 23), (7, 22), (5, 21), (5, 20), (5, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14), (5, 13), (8, 12)]
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

    # create label list & coordinates with zip() for the upbox & lowbox box sections
    text_labels_2 = ['UPBOX', 'LOWBOX', 'LOWBOX', 'UPBOX', 'LOWBOX', 'LOWBOX']
    text_coords_2 = [(43, 33), (39, 33), (3, 33), (0, 33), (1, 22), (41, 22)]
    for label, coord in zip(text_labels_2, text_coords_2):
        x, y = coord
        text_trace_2 = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=12, color='#B3A301'),
            showlegend=False,
            textposition='middle right'
        )
        traces.append(text_trace_2)

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Winter Garden Theatre Balcony Section"),
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
            'text': str("Winter Garden Theatre Balcony Section"),
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


def create_venue_winter_garden_theatre_mezzanine_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[19, 19, 34, 34, 19],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[18, 18],
        y=[10, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[35, 35],
        y=[10, 13],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    rowline3 = go.Scatter(
        x=[19, 34],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline3)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['A', 'B', 'C', 'D']
    text_coords = [(5, 13), (4, 12), (3, 11), (2, 10)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Winter Garden Theatre Mezzanine Section"),
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
            'text': str("Elgin Theatre Balcony Section"),
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


def create_venue_winter_garden_theatre_balcony_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[19, 19, 34, 34, 19],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[26, 26],
        y=[7, 15],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[19, 34],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['E', 'F', 'G', 'H', 'J', 'K', 'L']
    text_coords = [(2, 15), (2, 14), (3, 13), (3, 12),
                   (3, 9), (3, 8), (5, 7)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Winter Garden Theatre Balcony Section"),
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
            'text': str("Winter Garden Theatre Balcony Section"),
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


def create_venue_horseshoe_tavern_main_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[19, 19, 34, 34, 19],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[26, 26],
        y=[7, 15],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[19, 34],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['E', 'F', 'G', 'H', 'J', 'K', 'L']
    text_coords = [(2, 15), (2, 14), (3, 13), (3, 12),
                   (3, 9), (3, 8), (5, 7)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Horseshoe Tavern Main Section"),
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
            'text': str("Horseshoe Tavern Main Section"),
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


def create_venue_el_mocambo_the_starlight_room_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[19, 19, 34, 34, 19],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[26, 26],
        y=[7, 15],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[19, 34],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['E', 'F', 'G', 'H', 'J', 'K', 'L']
    text_coords = [(2, 15), (2, 14), (3, 13), (3, 12),
                   (3, 9), (3, 8), (5, 7)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("el Mocambo The Starlight Room Section"),
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
            'text': str("el Mocambo The Starlight Room Section"),
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


def create_venue_el_mocambo_under_the_neon_palms_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[19, 19, 34, 34, 19],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[26, 26],
        y=[7, 15],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[19, 34],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['E', 'F', 'G', 'H', 'J', 'K', 'L']
    text_coords = [(2, 15), (2, 14), (3, 13), (3, 12),
                   (3, 9), (3, 8), (5, 7)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("el Mocambo Under the Neon Palms Section"),
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
            'text': str("el Mocambo Under the Neon Palms Section"),
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


def create_venue_the_velvet_underground_main_section(galleryDictInput):
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=6, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    stage = go.Scatter(
        x=[19, 19, 34, 34, 19],
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

    # Add lines to separate rows for aesthetic purposes on venue floor
    rowline1 = go.Scatter(
        x=[26, 26],
        y=[7, 15],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline1)

    rowline2 = go.Scatter(
        x=[19, 34],
        y=[34, 34],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline2)

    # create list of alphabetical row text labels & their coordinates
    text_labels = ['E', 'F', 'G', 'H', 'J', 'K', 'L']
    text_coords = [(2, 15), (2, 14), (3, 13), (3, 12),
                   (3, 9), (3, 8), (5, 7)]
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

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("The Velvet Underground Main Section"),
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
            'text': str("The Velvet Underground Main Section"),
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


def create_venue_meridian_arts_centre_george_weston_main_section(galleryDictInput):

    # Meridian Arts Centre George Weston Main Section
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=5, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    # Create stage layout as a half moon trace figure

    def stage_y_values(x):
        return 5 * np.sin((x+0.5) * np.pi / 26) + 18.75

    x = np.array(list(range(26)))
    y = stage_y_values(x)

    stage = go.Scatter(
        x=x + 12,
        y=y,
        mode='lines',
        fill='toself',
        line=dict(width=3, color='#333333'),
        fillcolor='#333333',
        hoverinfo='skip',  # exclude hoverinfo for this trace
        textfont=dict(color='#B3A301', size=16)  # set the text color to white
    )
    traces.append(stage)

    # Add trapezoid object below to create the complete stage trace object for the Merdiain Arts Centre - George Weston theatre section
    stage_trapezoid_x_coord = [12, 19, 30, 37, 12]
    stage_trapezoid_y_coord = [19, 14, 14, 19, 19]

    stage_trapezoid = go.Scatter(
        x=stage_trapezoid_x_coord,
        y=stage_trapezoid_y_coord,
        mode='lines',
        fill='toself',
        line=dict(width=3, color='#333333'),
        fillcolor='#333333',
        text='STAGE',
        textposition='middle center',
        hoverinfo='skip',  # exclude hoverinfo for this trace
        textfont=dict(color='#B3A301', size=16)  # set the text color to white
    )
    traces.append(stage_trapezoid)

    # Create coordinates for the trapezoid boundary to outline the C-LOGE section
    trapezoid_c_loge_x = [12, 37, 41, 8, 12]  # x-coord
    trapezoid_c_loge_y = [13, 13, 9, 9, 13]  # y-coord

    # Create trapezoid for C-LOGE section
    trapezoid_c_loge = go.Scatter(
        x=trapezoid_c_loge_x,
        y=trapezoid_c_loge_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.3
        ),
    )

    # Add C-LOGE trapezoid to traces list
    traces.append(trapezoid_c_loge)

    # Create coordinates for the trapezoid boundary to outline the R-LOGE section
    trapezoid_r_loge_x = [3, 8, 10.5, 7, 3]  # x-coord
    trapezoid_r_loge_y = [28, 12, 14, 28, 28]  # y-coord

    # Create trapezoid for C-LOGE section
    trapezoid_r_loge = go.Scatter(
        x=trapezoid_r_loge_x,
        y=trapezoid_r_loge_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.3
        ),
    )

    # Add C-LOGE trapezoid to traces list
    traces.append(trapezoid_r_loge)

    # Create coordinates for the trapezoid boundary to outline the L-LOGE section
    trapezoid_l_loge_x = [38.5, 41, 46, 42, 38.5]  # x-coord
    trapezoid_l_loge_y = [14, 12, 28, 28, 14]  # y-coord

    # Create trapezoid for L-LOGE section
    trapezoid_l_loge = go.Scatter(
        x=trapezoid_l_loge_x,
        y=trapezoid_l_loge_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.3
        ),
    )

    # Add L-LOGE trapezoid to traces list
    traces.append(trapezoid_l_loge)

    # Create coordinates for the trapezoid boundary to outline the R-ORCH section
    trapezoid_r_orch_x = [16, 11.5, 11.5, 17.5, 17.5, 16]  # x-coord
    trapezoid_r_orch_y = [44, 41, 26.5, 26.5, 44, 44]  # y-coord

    # Create trapezoid for R-ORCH section
    trapezoid_r_orch = go.Scatter(
        x=trapezoid_r_orch_x,
        y=trapezoid_r_orch_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.2
        ),
    )

    # Add R-ORCH trapezoid to traces list
    traces.append(trapezoid_r_orch)

    # Create coordinates for the trapezoid boundary to outline the L-ORCH section
    trapezoid_l_orch_x = [31.5, 37.5, 37.5, 33, 31.5, 31.5]  # x-coord
    trapezoid_l_orch_y = [26.5, 26.5, 41, 44, 44, 26.5]  # y-coord

    # Create trapezoid for L-ORCH section
    trapezoid_l_orch = go.Scatter(
        x=trapezoid_l_orch_x,
        y=trapezoid_l_orch_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.2
        ),
    )

    # Add L-ORCH trapezoid to traces list
    traces.append(trapezoid_l_orch)

    # Create coordinates for the trapezoid boundary to outline the C-ORCH section
    trapezoid_c_orch_x = [18.5, 24, 25, 30.5, 30.5, 18.5, 18.5]  # x-coord
    trapezoid_c_orch_y = [25.75, 26.5, 26.5,
                          25.75, 44.5, 44.5, 25.75]  # y-coord

    # Create trapezoid for C-ORCH section
    trapezoid_c_orch = go.Scatter(
        x=trapezoid_c_orch_x,
        y=trapezoid_c_orch_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.05
        ),
    )

    # Add C-ORCH trapezoid to traces list
    traces.append(trapezoid_c_orch)

    # Create coordinates for the trapezoid boundary to outline the C-TERR section
    trapezoid_c_terr_x = [18.5, 18.5, 30.5, 30.5, 18.5]  # x-coord
    trapezoid_c_terr_y = [52, 44.5, 44.5, 52, 52]  # y-coord

    # Create trapezoid for C-TERR section
    trapezoid_c_terr = go.Scatter(
        x=trapezoid_c_terr_x,
        y=trapezoid_c_terr_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.05
        ),
    )

    # Add R-TERR trapezoid to traces list
    traces.append(trapezoid_c_terr)

    # Create coordinates for the trapezoid boundary to outline the R-TERR section
    trapezoid_r_terr_x = [9, 7.5, 14, 17.5, 17.5, 11, 9]  # x-coord
    trapezoid_r_terr_y = [40.5, 44, 52, 52, 44.5, 43.5, 40.5]  # y-coord

    # Create trapezoid for R-TERR section
    trapezoid_r_terr = go.Scatter(
        x=trapezoid_r_terr_x,
        y=trapezoid_r_terr_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.4
        ),
    )

    # Add R-TERR trapezoid to traces list
    traces.append(trapezoid_r_terr)

    # Create coordinates for the trapezoid boundary to outline the L-TERR section
    trapezoid_l_terr_x = [40, 41.5, 35, 31.5, 31.5, 38, 40]  # x-coord
    trapezoid_l_terr_y = [40.5, 44, 52, 52, 44.5, 43.5, 40.5]  # y-coord

    # Create trapezoid for L-TERR section
    trapezoid_l_terr = go.Scatter(
        x=trapezoid_l_terr_x,
        y=trapezoid_l_terr_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.4
        ),
    )

    # Add L-TERR trapezoid to traces list
    traces.append(trapezoid_l_terr)

    # Create coordinates for the trapezoid boundary to outline the DRESS section
    trapezoid_dress_x = [11, 38, 43, 46, 44,
                         40, 36, 13, 9, 5, 3, 6, 11]  # x-coord
    trapezoid_dress_y = [54, 54, 48, 48, 54, 62,
                         72, 72, 62, 54, 48, 48, 54]  # y-coord

    # Create trapezoid for DRESS section
    trapezoid_dress = go.Scatter(
        x=trapezoid_dress_x,
        y=trapezoid_dress_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.35
        ),
    )

    # Add DRESS trapezoid to traces list
    traces.append(trapezoid_dress)

    # Create coordinates for the trapezoid boundary to outline the L-PART section
    trapezoid_l_part_x = [38.65, 40.35, 40.35, 38.65, 38.65]  # x-coord
    trapezoid_l_part_y = [22.5, 22.5, 39.5, 39.5, 22.5]  # y-coord

    # Create trapezoid for L-PART section
    trapezoid_l_part = go.Scatter(
        x=trapezoid_l_part_x,
        y=trapezoid_l_part_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.2
        ),
    )

    # Add L-PART trapezoid to traces list
    traces.append(trapezoid_l_part)

    # Create coordinates for the trapezoid boundary to outline the R-PART section
    trapezoid_l_part_x = [10.5, 8.65, 8.65, 10.5, 10.5]  # x-coord
    trapezoid_l_part_y = [22.5, 22.5, 39.5, 39.5, 22.5]  # y-coord

    # Create trapezoid for R-PART section
    trapezoid_l_part = go.Scatter(
        x=trapezoid_l_part_x,
        y=trapezoid_l_part_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.2
        ),
    )

    # Add R-PART trapezoid to traces list
    traces.append(trapezoid_l_part)

    # Create coordinates for the trapezoid boundary to outline the L-DC section
    trapezoid_l_dc_x = [43.75, 46.25, 46.25, 43.75, 43.75]  # x-coord
    trapezoid_l_dc_y = [28.75, 28.75, 46.25, 46.25, 28.75]  # y-coord

    # Create trapezoid for L-DC section
    trapezoid_l_dc = go.Scatter(
        x=trapezoid_l_dc_x,
        y=trapezoid_l_dc_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.2
        ),
    )

    # Add L-DC trapezoid to traces list
    traces.append(trapezoid_l_dc)

    # Create coordinates for the trapezoid boundary to outline the R-DC section
    trapezoid_r_dc_x = [2.75, 5.25, 5.25, 2.75, 2.75]  # x-coord
    trapezoid_r_dc_y = [28.75, 28.75, 46.25, 46.25, 28.75]  # y-coord

    # Create trapezoid for R-DC section
    trapezoid_r_dc = go.Scatter(
        x=trapezoid_r_dc_x,
        y=trapezoid_r_dc_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=0.5,
            shape='spline',
            smoothing=0.2
        ),
    )

    # Add R-DC trapezoid to traces list
    traces.append(trapezoid_r_dc)

    # Fill seat gaps for the middle continuity gap for the DRESS section
    trace_gap_filler = go.Scatter(
        x=[24, 24, 24, 24, 24],
        y=[56, 58, 60, 62, 64],
        mode='markers',
        marker=dict(size=6, color='#1E90FF'),
        hoverinfo='none'
    )
    traces.append(trace_gap_filler)

    # create list of alphabetical row text labels & their coordinates for DRESS section
    text_labels_dress = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    text_coords_dress = [(4, 50), (6, 54), (9, 59), (10, 62),
                         (14, 64), (16, 66), (16, 68), (14, 70)]

    for label, coord in zip(text_labels_dress, text_coords_dress):
        x, y = coord
        text_trace_dress = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=11, color='#B3A301', family='arial'),
            showlegend=False,
            textposition='middle center'
        )
        traces.append(text_trace_dress)

    # create list of alphabetical row text labels & their coordinates for C-ORCH section
    text_labels_c_orch = ['A', 'B', 'C', 'D', 'E',
                          'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T']
    text_coords_c_orch = [(18, 27), (18, 28), (18, 29),
                          (18, 30), (18, 31), (18, 32), (18, 33), (18, 34), (18, 35), (18, 36), (18, 37), (18, 38), (18, 39), (18, 40), (18, 41), (18, 42), (18, 43), (18, 44)]

    # create C-ORCH text trace objects and append to the master traces list
    for label, coord in zip(text_labels_c_orch, text_coords_c_orch):
        x, y = coord
        text_trace_c_orch = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=11, color='#B3A301', family='arial'),
            showlegend=False,
            textposition='middle center'
        )
        traces.append(text_trace_c_orch)

    # create list of alphabetical row text labels & their coordinates for C-TERR section
    # Note: 'ZZ' label added even though it's not part of C-TERR for simplicity
    text_labels_c_terr = ['U', 'V', 'W', 'X', 'Y', 'Z', 'ZZ']
    text_coords_c_terr = [(18, 45), (18, 46), (18, 47),
                          (18, 48), (18, 49), (18, 50)]

    # create C-TERR text trace objects and append to the master traces list
    for label, coord in zip(text_labels_c_terr, text_coords_c_terr):
        x, y = coord
        text_trace_c_terr = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=11, color='#B3A301', family='arial'),
            showlegend=False,
            textposition='middle center'
        )
        traces.append(text_trace_c_terr)

    # create left line for C-LOGE venue section label
    rowline_c_loge_left = go.Scatter(
        x=[8, 22],
        y=[7, 7],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_loge_left)

    # create right line for C-LOGE venue section label
    rowline_c_loge_right = go.Scatter(
        x=[26, 41],
        y=[7, 7],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_loge_right)

    rowline_c_loge_vertical_left = go.Scatter(
        x=[8, 8],
        y=[7, 8],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_loge_vertical_left)

    rowline_c_loge_vertical_right = go.Scatter(
        x=[41, 41],
        y=[7, 8],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_loge_vertical_right)

    arrow_c_loge_left = go.Scatter(
        x=[8],
        y=[8],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_loge_left)

    arrow_c_loge_right = go.Scatter(
        x=[41],
        y=[8],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_loge_right)

    # create left diagonal line for R-LOGE venue section label
    rowline_r_loge_left = go.Scatter(
        x=[1, 3],
        y=[28, 22],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_loge_left)

    # create right diagonal line for R-LOGE venue section label
    rowline_r_loge_right = go.Scatter(
        x=[4.25, 6.25],
        y=[18, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_loge_right)

    # create horizontal line connecting main line with top right arrow for R-LOGE
    rowline_r_loge_vertical_left = go.Scatter(
        x=[1, 2],
        y=[28, 28],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_loge_vertical_left)

    # create horizontal line connecting main line with bottom right arrow for R-LOGE
    rowline_r_loge_vertical_right = go.Scatter(
        x=[6.25, 7.25],
        y=[12, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_loge_vertical_right)

    # create top right-facing arrow for R-LOGE
    arrow_r_loge_top = go.Scatter(
        x=[2],
        y=[28],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_r_loge_top)

    # create a bottom right-facing arrow for R-LOGE
    arrow_r_loge_bottom = go.Scatter(
        x=[7.25],
        y=[12],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_r_loge_bottom)

    # create top vertical line for R-DC venue section label
    rowline_r_dc_top = go.Scatter(
        x=[1, 1],
        y=[46, 39.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_dc_top)

    # create bottom vertical line for R-DC venue section label
    rowline_r_dc_bottom = go.Scatter(
        x=[1, 1],
        y=[35.5, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_dc_bottom)

    # create horizontal line connecting main line with top right arrow for R-DC
    rowline_r_dc_vertical_left = go.Scatter(
        x=[1, 2],
        y=[46, 46],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_dc_vertical_left)

    # create horizontal line connecting main line with bottom right arrow for R-DC
    rowline_r_dc_vertical_right = go.Scatter(
        x=[1, 2],
        y=[29, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_dc_vertical_right)

    # create top right-facing arrow for R-DC
    arrow_r_dc_top = go.Scatter(
        x=[2],
        y=[46],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_r_dc_top)

    # create a bottom right-facing arrow for R-DC
    arrow_r_dc_bottom = go.Scatter(
        x=[2],
        y=[29],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_r_dc_bottom)

    # create top diagonal line for DRESS venue section label
    rowline_dress_top = go.Scatter(
        x=[7.33, 12],
        y=[61.82, 72],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_dress_top)

    # create bottom vertical line for DRESS venue section label
    rowline_dress_bottom = go.Scatter(
        x=[5.67, 1],
        y=[58.21, 48],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_dress_bottom)

    # create horizontal line connecting main line with top right arrow for DRESS
    rowline_dress_horizontal_top = go.Scatter(
        x=[12, 12.5],
        y=[72, 72],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_dress_horizontal_top)

    # create horizontal line connecting main line with bottom right arrow for DRESS
    rowline_dress_horizontal_bottom = go.Scatter(
        x=[1, 2],
        y=[48, 48],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_dress_horizontal_bottom)

    # create top right-facing arrow for DRESS
    arrow_dress_top = go.Scatter(
        x=[12.5],
        y=[72],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_dress_top)

    # create a bottom right-facing arrow for DRESS
    arrow_dress_bottom = go.Scatter(
        x=[2],
        y=[48],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-right', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_dress_bottom)

    # create left diagonal line for L-LOGE venue section label
    rowline_l_loge_left = go.Scatter(
        x=[48, 46],
        y=[28, 22],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_loge_left)

    # create right diagonal line for L-LOGE venue section label
    rowline_l_loge_right = go.Scatter(
        x=[44.75, 42.75],
        y=[18, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_loge_right)

    # create horizontal line connecting main line with top right arrow for L-LOGE
    rowline_l_loge_horizontal_left = go.Scatter(
        x=[47, 48],
        y=[28, 28],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_loge_horizontal_left)

    # create horizontal line connecting main line with bottom right arrow for L-LOGE
    rowline_l_loge_horizontal_right = go.Scatter(
        x=[42.75, 41.75],
        y=[12, 12],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_loge_horizontal_right)

    # create top left-facing arrow for L-LOGE
    arrow_l_loge_top = go.Scatter(
        x=[47],
        y=[28],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_l_loge_top)

    # create a bottom left-facing arrow for L-LOGE
    arrow_l_loge_bottom = go.Scatter(
        x=[41.75],
        y=[12],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_l_loge_bottom)

    # create top vertical line for L-DC venue section label
    rowline_l_dc_top = go.Scatter(
        x=[48, 48],
        y=[46, 39.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_dc_top)

    # create bottom vertical line for L-DC venue section label
    rowline_l_dc_bottom = go.Scatter(
        x=[48, 48],
        y=[35.5, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_dc_bottom)

    # create horizontal line connecting main line with top right arrow for L-DC
    rowline_l_dc_vertical_left = go.Scatter(
        x=[48, 47],
        y=[46, 46],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_dc_vertical_left)

    # create horizontal line connecting main line with bottom right arrow for L-DC
    rowline_l_dc_vertical_right = go.Scatter(
        x=[48, 47],
        y=[29, 29],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_dc_vertical_right)

    # create top left-facing arrow for L-DC
    arrow_l_dc_top = go.Scatter(
        x=[47],
        y=[46],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_l_dc_top)

    # create a bottom left-facing arrow for L-DC
    arrow_l_dc_bottom = go.Scatter(
        x=[47],
        y=[29],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-left', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_l_dc_bottom)

    # create left line for C-TERR venue section label
    rowline_c_terr_left = go.Scatter(
        x=[18.5, 22.5],
        y=[53.5, 53.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_terr_left)

    # create right line for C-TERR venue section label
    rowline_c_terr_right = go.Scatter(
        x=[26.5, 30.5],
        y=[53.5, 53.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_terr_right)

    rowline_c_terr_vertical_left = go.Scatter(
        x=[18.5, 18.5],
        y=[53.5, 52.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_terr_vertical_left)

    rowline_c_terr_vertical_right = go.Scatter(
        x=[30.5, 30.5],
        y=[53.5, 52.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_terr_vertical_right)

    arrow_c_terr_left = go.Scatter(
        x=[18.5],
        y=[52.5],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-down', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_terr_left)

    arrow_c_terr_right = go.Scatter(
        x=[30.5],
        y=[52.5],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-down', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_terr_right)

    # create left line for C-ORCH venue section label
    rowline_c_orch_left = go.Scatter(
        x=[18.5, 22.5],
        y=[24.5, 24.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_orch_left)

    # create right line for C-ORCH venue section label
    rowline_c_orch_right = go.Scatter(
        x=[26.5, 30.5],
        y=[24.5, 24.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_orch_right)

    rowline_c_orch_vertical_left = go.Scatter(
        x=[18.5, 18.5],
        y=[24.75, 24.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_orch_vertical_left)

    rowline_c_orch_vertical_right = go.Scatter(
        x=[30.5, 30.5],
        y=[24.75, 24.5],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_orch_vertical_right)

    arrow_c_orch_left = go.Scatter(
        x=[18.5],
        y=[25],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_orch_left)

    arrow_c_orch_right = go.Scatter(
        x=[30.5],
        y=[25],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_orch_right)

    # create left line for R-ORCH venue section label
    rowline_r_orch_left = go.Scatter(
        x=[11.5, 12.5],
        y=[25.25, 25.25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_orch_left)

    # create right line for R-ORCH venue section label
    rowline_r_orch_right = go.Scatter(
        x=[16.5, 17.5],
        y=[25.25, 25.25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_r_orch_right)

    rowline_c_orch_vertical_left = go.Scatter(
        x=[11.5, 11.5],
        y=[25.25, 25.75],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_orch_vertical_left)

    rowline_c_orch_vertical_right = go.Scatter(
        x=[17.5, 17.5],
        y=[25.25, 25.75],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_c_orch_vertical_right)

    arrow_c_orch_left = go.Scatter(
        x=[11.5],
        y=[25.75],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_orch_left)

    arrow_c_orch_right = go.Scatter(
        x=[17.5],
        y=[25.75],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_c_orch_right)

    # create left line for L-ORCH venue section label
    rowline_l_orch_left = go.Scatter(
        x=[31.5, 32.5],
        y=[25.25, 25.25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_orch_left)

    # create right line for L-ORCH venue section label
    rowline_l_orch_right = go.Scatter(
        x=[36.5, 37.5],
        y=[25.25, 25.25],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_orch_right)

    rowline_l_orch_vertical_left = go.Scatter(
        x=[31.5, 31.5],
        y=[25.25, 25.75],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_orch_vertical_left)

    rowline_l_orch_vertical_right = go.Scatter(
        x=[37.5, 37.5],
        y=[25.25, 25.75],
        mode='lines',
        line=dict(
            color='gray',
            width=1
        ),
    )

    traces.append(rowline_l_orch_vertical_right)

    arrow_l_orch_left = go.Scatter(
        x=[31.5],
        y=[25.75],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_l_orch_left)

    arrow_l_orch_right = go.Scatter(
        x=[37.5],
        y=[25.75],
        mode='lines+markers+text',
        name='Arrow',
        line=dict(width=1, color='#333333'),
        marker=dict(symbol='triangle-up', size=10, color='#333333'),
        hoverinfo=None
    )

    traces.append(arrow_l_orch_right)

    # create list of alphabetical section labels
    text_section_labels = ['C-LOGE', 'R-LOGE',
                           'R-DC', 'DRESS', 'L-LOGE', 'L-DC', 'C-TERR', 'C-ORCH', 'R-ORCH', 'L-ORCH']
    text_section_coords = [(24, 7), (2.625, 20), (1, 37),
                           (6.49, 60), (46.375, 20), (48, 37), (24.5, 53.5), (24.5, 24.5), (14.5, 25.25), (34.5, 25.25)]

    # create section label text trace objects and append to the master traces list
    for label, coord in zip(text_section_labels, text_section_coords):
        x, y = coord
        text_section_traces = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=14, color='#B3A301', family='arial'),
            showlegend=False,
            textposition='middle center'
        )
        traces.append(text_section_traces)

    # create list of numerical row text labels & their coordinates for L, R & C-TERR sections
    # text_labels_num_terr = ['114', '115', '116', '117', '118', '119', '120', '121', '122']
    # text_coords_num_terr = [(41, 46), (40, 47), (39, 49),
    #                         (38, 50), (37, 51), (36, 52), (35, 53), (34, 53), (33, 53)]

    # # create C-TERR text trace objects and append to the master traces list
    # for label, coord in zip(text_labels_num_terr, text_coords_num_terr):
    #     x, y = coord
    #     text_trace_num_terr = go.Scatter(
    #         x=[x],
    #         y=[y],
    #         mode='text',
    #         text=label,
    #         textfont=dict(size=11, color='#B3A301'),
    #         showlegend=False,
    #         textposition='middle center',
    #         # textangle=90
    #     )
    #     traces.append(text_trace_num_terr)

    # Create a layout for the plot
    # @st.cache(allow_output_mutation=True)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("Meridian Arts Centre George Weston Main Section"),
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
                    text=' STAGE',
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
            'text': str("Meridian Arts Centre George Weston Main Section"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        # autosize=True, width=900, height=675, annotations=[
        autosize=True, width=950, height=1200, annotations=[
            dict(
                text="S T A G E",
                font=dict(
                    size=40,
                    family='arial',
                    color='#B3A301'  # '#B3A301' olive-gold
                ),
                # x=((traces[-2].x[-1] + traces[-2].x[0]) / 2),
                # y=min(traces[-2].y) + 2
                x=(max(stage_trapezoid.x) - min(stage_trapezoid.x)) / \
                2 + min(stage_trapezoid.x),
                y=(max(stage_trapezoid.y) - min(stage_trapezoid.y)) / \
                2 + min(stage_trapezoid.y) + 2
            )
        ], hoverlabel=dict(
            font=dict(
                size=16,
                color="#B3A301"
            )
        ))

    # create list of numerical row text labels & their coordinates for L, R & C-TERR sections
    text_labels_num_terr = ['114', '115', '116',
                            '117', '118', '119', '120', '121', '122', '123', '125', '126', '127', '128',
                            '129', '130', '131', '132', '132', '133', '134', '135', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147']
    text_coords_num_terr = [(41, 46), (40, 47), (39, 49),
                            (38, 50), (37, 51), (36, 52), (35, 53.35), (34, 53.35),
                            (33, 53.35), (32, 53.35), (30, 51.25), (29, 51.25),
                            (28, 51.25), (27, 51.25), (26, 51.25), (25, 51.25),
                            (24, 51.25), (23, 51.25), (22,
                                                       51.25), (21, 51.25), (20, 51.25),
                            (19, 51.25), (17, 53.35), (16, 53.35), (15, 53.35), (14, 53.35), (13, 52), (12, 51), (11, 50), (10, 49), (9, 47), (8, 46)]

    # add numerical text labels as 'add_annotation' in order to get textangle function to display seat row numbers vertically (90deg rotation)
    # note: cannot rotate via traces directly, must use 'add_annotation' function to fig
    for label, coord in zip(text_labels_num_terr, text_coords_num_terr):
        x, y = coord
        print("label: ", label)
        print("coord: ", coord)
        fig.add_annotation(text=label, x=x,
                           y=y, showarrow=False, textangle=90, font=dict(size=12, color='#B3A301', family='arial'))

    # create list of numerical row text labels & their coordinates for DRESS section
    text_labels_num_terr = ['212', '213', '214', '215', '216',
                            '217', '218', '219', '220', '221',
                            '222', '223', '224', '225', '226',
                            '227', '228', '229', '230', '231',
                            '232', '233', '234', '235', '236',
                            '237', '238', '239', '240']
    text_coords_num_terr = [(44, 51.5), (43, 52.5), (42, 55.5), (41, 56.5), (40, 57.5),
                            (39, 60.5), (38, 63.5), (36,
                                                     63.5), (35, 63.5), (34, 71.5),
                            (33, 71.5), (32, 71.5), (31,
                                                     71.5), (30, 71.5), (29, 71.5),
                            (28, 71.5), (27, 71.5), (26,
                                                     71.5), (25, 71.5), (24, 71.5),
                            (23, 71.5), (22, 71.5), (21,
                                                     71.5), (20, 71.5), (19, 71.5),
                            (18, 71.5), (17, 71.5), (16, 71.5), (15, 71.5)]

    # add numerical text labels as 'add_annotation' in order to get textangle function to display seat row numbers vertically (90deg rotation)
    # note: cannot rotate via traces directly, must use 'add_annotation' function to fig
    for label, coord in zip(text_labels_num_terr, text_coords_num_terr):
        x, y = coord
        print("label: ", label)
        print("coord: ", coord)
        fig.add_annotation(text=label, x=x,
                           y=y, showarrow=False, textangle=90, font=dict(size=12, color='#B3A301'))

    return gallery, traces, fig


def create_venue_history_main_section(galleryDictInput):
    # History Main Section
    gallery = {}
    gallery = galleryDictInput

    # Create a list of scatter traces to represent the seats in the gallery
    traces = []
    for seat_number, seat in gallery.items():
        price = seat['price']['CAD']
        color = '#1E90FF'
        trace = go.Scatter(
            x=[seat['x']],
            y=[seat['y']],
            mode='markers',
            name=seat['name'],
            hovertext=[f"{seat['name']}<br>$ {seat['price']['CAD']} CAD"],
            hovertemplate='%{hovertext}<extra></extra>',
            marker=dict(size=5, color=color),
            textfont=dict(
                size=16
            ),
            customdata=[price]
        )
        traces.append(trace)

    #########################################################

    # Create rectangle stage trace object

    # Create stage layout as a half moon trace figure

    # def stage_y_values(x):
    #     return 5 * np.sin((x+0.5) * np.pi / 26) + 18.75

    # x = np.array(list(range(26)))
    # y = stage_y_values(x)

    # stage = go.Scatter(
    #     x=x + 12,
    #     y=y,
    #     mode='lines',
    #     fill='toself',
    #     line=dict(width=3, color='#333333'),
    #     fillcolor='#333333',
    #     hoverinfo='skip',  # exclude hoverinfo for this trace
    #     textfont=dict(color='#B3A301', size=16)  # set the text color to white
    # )
    # traces.append(stage)

    stage = go.Scatter(
        x=[1, -5, -5, 1, 1],
        y=[31, 31, 6, 6, 31],
        mode='lines',
        fill='toself',
        line=dict(width=4, color='#333333'),
        fillcolor='#333333',
        hoverinfo='skip',  # exclude hoverinfo for this trace
        text='STAGE',
        textposition='middle center',
        # set the text color to white
        textfont=dict(color='#B3A301', size=16, family='arial')
    )
    traces.append(stage)

    # Add trapezoid object below to create the complete stage trace object for the Merdiain Arts Centre - George Weston theatre section
    # mezz_row_x_coord = [1.85, 2.77, 7.55]
    # mezz_row_y_coord = [22.85, 22.5, 20.5]

    # mezz_row_structure = go.Scatter(
    #     x=mezz_row_x_coord,
    #     y=mezz_row_y_coord,
    #     mode='lines',
    #     fill='toself',
    #     line=dict(width=3, color='#333333'),
    #     fillcolor='#333333',
    #     text='STAGE',
    #     textposition='middle center',
    #     hoverinfo='skip',  # exclude hoverinfo for this trace
    #     textfont=dict(color='#B3A301', size=16)  # set the text color to white
    # )
    # traces.append(mezz_row_structure)

    # Create coordinates for the trapezoid boundary to outline the C-LOGE section
    # mezz_row_x_coord = [1.85, 7.55, 28.7, 32.29, 1.85]
    # mezz_row_y_coord = [22.85, 20.5, 11.75, 6.53, 22.85]

    # mezz_row_x_coord = [22.75, 20.5, 21.24, 22.17, 23.09, 23.99,
    #                     24.87, 25.74, 26.58, 27.41, 28.21, 28.7, 32.29, 31.5, 30.69, 29.86, 29.02, 28.16, 27.29, 26.39, 25.5, 24.58, 23.65, 22.75]
    # mezz_row_y_coord = [1.44, 7.55,  7.78, 8.13, 8.52, 8.95,
    #                     9.41, 9.90, 10.43, 10.98, 11.57, 11.75, 6.53, 6.04, 5.45, 4.90, 4.37, 3.87, 3.39, 2.95, 2.53, 2.14, 1.77, 1.44]

    # mezz_row_x_coord = [1, 7, 28, 32, 1]
    # mezz_row_y_coord = [22, 20, 11, 6, 22]

    # Create trapezoid for C-LOGE section
    # mezz_row_structure = go.Scatter(
    #     x=mezz_row_x_coord,
    #     y=mezz_row_y_coord,
    #     mode='lines',
    #     line=dict(
    #         color='darkgray',
    #         width=0.5,
    #         shape='spline',
    #         smoothing=1
    #     ),
    # )

    # # Add C-LOGE trapezoid to traces list
    # traces.append(mezz_row_structure)

    # Add row lines to venue layout
    rowline1 = go.Scatter(
        x=[22.77, 20.53785],
        y=[1.2405, 7.66416],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline1)

    # Add row lines to venue layout
    rowline2 = go.Scatter(
        x=[28.64035, 32.29],
        y=[12.16, 6.40],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline2)

    # Create an arc to border the MEZZ seats
    mezz_outer_border_1_center = (12.25, 32.15)
    mezz_outer_border_1_radius = 32.65

    # Define start and end angle of the arc
    mezz_outer_border_1_start_angle = -94.85
    mezz_outer_border_1_end_angle = 30

    # Generate array of angles within the specified range
    angles = np.linspace(np.deg2rad(mezz_outer_border_1_start_angle),
                         np.deg2rad(mezz_outer_border_1_end_angle), num=100)

    # Caclulate the x & y coordinates of the arc
    x = mezz_outer_border_1_center[0] + \
        mezz_outer_border_1_radius * np.cos(angles)
    y = mezz_outer_border_1_center[1] + \
        mezz_outer_border_1_radius * np.sin(angles)

    # Create a scatter trace
    mezz_outer_border_1 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line_color='darkgray',
        line=dict(
            color='darkgray',
            width=1.5
        )
    )
    traces.append(mezz_outer_border_1)

    # Create an arc to border the MEZZ seats
    mezz_inner_border_1_center = (12.25, 32.15)
    mezz_inner_border_1_radius = 31.65

    # Define start and end angle of the arc
    mezz_inner_border_1_start_angle = -71.2
    mezz_inner_border_1_end_angle = 30

    # Generate array of angles within the specified range
    angles = np.linspace(np.deg2rad(mezz_inner_border_1_start_angle),
                         np.deg2rad(mezz_inner_border_1_end_angle), num=100)

    # Caclulate the x & y coordinates of the arc
    x = mezz_inner_border_1_center[0] + \
        mezz_inner_border_1_radius * np.cos(angles)
    y = mezz_inner_border_1_center[1] + \
        mezz_inner_border_1_radius * np.sin(angles)

    # Create a scatter trace
    mezz_inner_border_1 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line_color='darkgray',
        line=dict(
            color='darkgray',
            width=1.25
        )
    )
    traces.append(mezz_inner_border_1)

    # Create an arc to border the MEZZ seats
    sbox_inner_border_1_center = (12.25, 32.15)
    sbox_inner_border_1_radius = 25.85

    # Define start and end angle of the arc
    sbox_inner_border_1_start_angle = -71.3
    sbox_inner_border_1_end_angle = -50.65

    # Generate array of angles within the specified range
    angles = np.linspace(np.deg2rad(sbox_inner_border_1_start_angle),
                         np.deg2rad(sbox_inner_border_1_end_angle), num=100)

    # Caclulate the x & y coordinates of the arc
    x = sbox_inner_border_1_center[0] + \
        sbox_inner_border_1_radius * np.cos(angles)
    y = sbox_inner_border_1_center[1] + \
        sbox_inner_border_1_radius * np.sin(angles)

    # Create a scatter trace
    sbox_inner_border_1 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line_color='darkgray',
        line=dict(
            color='darkgray',
            width=1.25
        )
    )
    traces.append(sbox_inner_border_1)

    # Create an arc to border the MEZZ seats
    bottom_curve_border_1_center = (12.25, 32.15)
    bottom_curve_border_1_radius = 36.75

    # Define start and end angle of the arc
    bottom_curve_border_1_start_angle = -94.35
    bottom_curve_border_1_end_angle = -11.325

    # Generate array of angles within the specified range
    angles = np.linspace(np.deg2rad(bottom_curve_border_1_start_angle),
                         np.deg2rad(bottom_curve_border_1_end_angle), num=100)

    # Caclulate the x & y coordinates of the arc
    x = bottom_curve_border_1_center[0] + \
        bottom_curve_border_1_radius * np.cos(angles)
    y = bottom_curve_border_1_center[1] + \
        bottom_curve_border_1_radius * np.sin(angles)

    # Create a scatter trace
    bottom_curve_border_1 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line_color='darkgray',
        line=dict(
            color='darkgray',
            width=1.5
        )
    )
    traces.append(bottom_curve_border_1)

    # Add the connecting vertical line to connect the inner MEZZ border structure to thw outer MEZZ structural section
    rowline3 = go.Scatter(
        x=[9.489, 9.489],
        y=[-0.383, -4.494],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline3)

    # Mezzanine Standing Room Only Structure Section

    # Diagonal line creating corner structure of the standing room only structure section
    rowline4 = go.Scatter(
        x=[29.7215, 30.75],
        y=[-0.1812, -2.25],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline4)

    # Horizontal bottom line of the Mezzanine Standing Room Only Structure Section

    rowline5 = go.Scatter(
        x=[30.75, 52.00],
        y=[-2.25, -2.25],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline5)

    # Vertical right most border line of the Mezzanine Standing Room Only Structure Section

    rowline6 = go.Scatter(
        x=[52.00, 52.00],
        y=[-2.25, 50.525],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline6)

    # Create an outer arc to border the BOX203 & BOX204 sections
    outer_box203_box204_curve_border_1_center = (12.25, 32.15)
    outer_box203_box204_curve_border_1_radius = 37.75

    # Define start and end angle of the arc
    outer_box203_box204_curve_border_1_start_angle = -11.25
    outer_box203_box204_curve_border_1_end_angle = 6.75

    # Generate array of angles within the specified range
    angles = np.linspace(np.deg2rad(outer_box203_box204_curve_border_1_start_angle),
                         np.deg2rad(outer_box203_box204_curve_border_1_end_angle), num=100)

    # Caclulate the x & y coordinates of the arc
    x = outer_box203_box204_curve_border_1_center[0] + \
        outer_box203_box204_curve_border_1_radius * np.cos(angles)
    y = outer_box203_box204_curve_border_1_center[1] + \
        outer_box203_box204_curve_border_1_radius * np.sin(angles)

    # Create a scatter trace
    outer_box203_box204_curve_border_1 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line_color='darkgray',
        line=dict(
            color='darkgray',
            width=1.5
        )
    )
    traces.append(outer_box203_box204_curve_border_1)

    # Horizontal line separating the Box 203 & Box 204 sections

    rowline7 = go.Scatter(
        x=[43.86, 49.95795],
        y=[30.65, 30.36],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline7)

    # Horizontal line separating the Box 203 & Box 204 sections

    rowline8 = go.Scatter(
        x=[44.231, 49.27464],
        y=[25.58, 24.78534],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline8)

    # Diagonal top line separating the Box 202 & Box 203 sections

    rowline9 = go.Scatter(
        x=[44.80, 49.7833],
        y=[35.85, 36.58704],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline9)

    # Create an arc to border the MEZZ seats
    upper_curve_border_1_center = (12.25, 32.15)
    upper_curve_border_1_radius = 36.75

    # Define start and end angle of the arc
    upper_curve_border_1_start_angle = 6.75
    upper_curve_border_1_end_angle = 30

    # Generate array of angles within the specified range
    angles = np.linspace(np.deg2rad(upper_curve_border_1_start_angle),
                         np.deg2rad(upper_curve_border_1_end_angle), num=100)

    # Caclulate the x & y coordinates of the arc
    x = upper_curve_border_1_center[0] + \
        upper_curve_border_1_radius * np.cos(angles)
    y = upper_curve_border_1_center[1] + \
        upper_curve_border_1_radius * np.sin(angles)

    # Create a scatter trace
    upper_curve_border_1 = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line_color='darkgray',
        line=dict(
            color='darkgray',
            width=1.5
        )
    )
    traces.append(upper_curve_border_1)

    # Diagonal upper most top line containing Box 201

    rowline10 = go.Scatter(
        x=[39.6957, 44.07643],
        y=[47.975, 50.525],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline10)

    # Horizontal upper most top cap border line of the Mezzanine Standing Room Only Structure Section connecting to the Box 201 section

    rowline11 = go.Scatter(
        x=[44.07643, 52.00],
        y=[50.525, 50.525],
        mode='lines',
        line=dict(
            color='gray',
            width=1.5
        ),
    )

    traces.append(rowline11)

    # Create coordinates for the trapezoid boundary to outline the R-LOGE section
    top_mezz_standing_room_only_x = [
        39.6957, 22.20, 22.20, 33.4, 33.4, 42.4, 42.4, 39.6957]  # x-coord
    top_mezz_standing_room_only_y = [
        47.975, 47.975, 53.475, 53.475, 52, 52, 49.5571129, 47.975]  # y-coord

    # Create trapezoid for C-LOGE section
    top_mezz_standing = go.Scatter(
        x=top_mezz_standing_room_only_x,
        y=top_mezz_standing_room_only_y,
        mode='lines',
        line=dict(
            color='darkgray',
            width=1.5,
            shape='spline',
            smoothing=0
        ),
    )

    # Add C-LOGE trapezoid to traces list
    traces.append(top_mezz_standing)

    # create list of alphabetical section labels
    text_section_labels = []
    text_section_coords = []

    # create section label text trace objects and append to the master traces list
    for label, coord in zip(text_section_labels, text_section_coords):
        x, y = coord
        text_section_traces = go.Scatter(
            x=[x],
            y=[y],
            mode='text',
            text=label,
            textfont=dict(size=14, color='#B3A301', family='arial'),
            showlegend=False,
            textposition='middle center'
        )
        traces.append(text_section_traces)

    def concert_layout(gallery):
        largest_x_value = max(seat['x'] for seat in gallery.values())
        center_x_value = largest_x_value/2
        layout = go.Layout(
            title=dict(text=str("History Main Section"),
                       font=dict(
                family='monospace',
                color='#B3A301'
            )
            ),
            xaxis=dict(title='X-coordinate', range=[-10, 60],
                       autorange=False, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            yaxis=dict(title='Y-coordinate', range=[-10, 60],
                       autorange=False, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
            showlegend=False,
            legend=dict(itemclick="toggleothers"),
            annotations=[
                dict(
                    text=' STAGE',
                    showarrow=False,
                )
            ],
            font=dict(
                family='monospace',
                size=32,
                color='black'
            ),
            images=[
                dict(
                    source="/Image_Data/history_2.png",
                    xref="x",
                    yref="y",
                    x=0,
                    y=50,
                    sizex=50,
                    sizey=50,
                    sizing="contain",
                    opacity=1,
                    layer="below"
                )
            ]
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
            'text': str("History Main Section"),
            'font': {'family': 'monospace', 'color': '#B3A301'}
        },
        title_font=dict(
            family='monospace',
            size=18,
            color='#B3A301'
        ),
        # autosize=True, width=900, height=675, annotations=[
        autosize=False, width=950, height=950, annotations=[
            dict(
                text="",
                font=dict(
                    size=40,
                    family='arial',
                    color='#B3A301'  # '#B3A301' olive-gold
                )
                # # x=((traces[-2].x[-1] + traces[-2].x[0]) / 2),
                # # y=min(traces[-2].y) + 2
                # x=(max(stage_trapezoid.x) - min(stage_trapezoid.x)) / \
                # 2 + min(stage_trapezoid.x),
                # y=(max(stage_trapezoid.y) - min(stage_trapezoid.y)) / \
                # 2 + min(stage_trapezoid.y) + 2
            )
        ], hoverlabel=dict(
            font=dict(
                size=16,
                color="#B3A301"
            )
        )
    )

    # create list of numerical row text labels & their coordinates for L, R & C-TERR sections
    stage_text_label = ['S T A G E']
    stage_text_coord = [(-2, 18.5)]

    # add numerical text labels as 'add_annotation' in order to get textangle function to display seat row numbers vertically (90deg rotation)
    # note: cannot rotate via traces directly, must use 'add_annotation' function to fig
    for label, coord in zip(stage_text_label, stage_text_coord):
        x, y = coord
        print("label: ", label)
        print("coord: ", coord)
        fig.add_annotation(text=label, x=x,
                           y=y, showarrow=False, textangle=270, font=dict(size=40, color='#B3A301', family='arial'))

    # create list of numerical row text labels & their coordinates for DRESS section
    mezz_text_label = ['MEZZANINE', 'STANDING ROOM', 'ONLY']
    mezz_text_coord = [(45, 4), (45, 2), (45, 0)]

    # add numerical text labels as 'add_annotation' in order to get textangle function to display seat row numbers vertically (90deg rotation)
    # note: cannot rotate via traces directly, must use 'add_annotation' function to fig
    for label, coord in zip(mezz_text_label, mezz_text_coord):
        x, y = coord
        print("label: ", label)
        print("coord: ", coord)
        fig.add_annotation(text=label, x=x,
                           y=y, showarrow=False, textangle=0, font=dict(size=16, color='#B3A301', family='arial'))

    # create list of numerical row text labels & their coordinates for L, R & C-TERR sections
    top_mezzanine_text_label = ['MEZZANINE', 'STANDING ROOM', 'ONLY']
    top_mezzanine_text_coord = [(27.8, 51.725), (27.8, 50.725), (27.8, 49.725)]

    # add numerical text labels as 'add_annotation' in order to get textangle function to display seat row numbers vertically (90deg rotation)
    # note: cannot rotate via traces directly, must use 'add_annotation' function to fig
    for label, coord in zip(top_mezzanine_text_label, top_mezzanine_text_coord):
        x, y = coord
        print("label: ", label)
        print("coord: ", coord)
        fig.add_annotation(text=label, x=x,
                           y=y, showarrow=False, textangle=0, font=dict(size=11, color='#B3A301', family='arial'))

    fig.update_layout(images=[
        dict(
            source="Image_Data/history_2.png",
            xref="x",
            yref="y",
            x=0,
            y=50,
            sizex=50,
            sizey=50,
            sizing="stretch",
            opacity=1,
            layer="above"
        )
    ])

    return gallery, traces, fig
# Dictionary to map venue names as keys to venue property function as values
# Venue dictionary for st.selectbox i.) key (venue) ii.) value (section; gallery, mezzanine, balcony, etc)
# venue_dictionary = {
#     "Massey Hall": {
#         "Massey Hall Gallery Section": create_venue_massey_hall_gallery
#     }
# }
