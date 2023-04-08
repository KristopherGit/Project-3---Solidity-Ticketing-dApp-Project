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
        )
    )

    return gallery, traces, fig


def create_venue_massey_hall_balcony(galleryDictInput):
    # Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
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
        )
    )

    return gallery, traces, fig


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


# Dictionary to map venue names as keys to venue property function as values
# Venue dictionary for st.selectbox i.) key (venue) ii.) value (section; gallery, mezzanine, balcony, etc)
# venue_dictionary = {
#     "Massey Hall": {
#         "Massey Hall Gallery Section": create_venue_massey_hall_gallery
#     }
# }
