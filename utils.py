import matplotlib.pyplot as plt
import numpy as np


def get_rect_area_panels_count_and_fig(panel_dim1, panel_dim2, area_dim1, area_dim2):
    panel_height = min(panel_dim1, panel_dim2)
    panel_width = max(panel_dim1, panel_dim2)
    area_height = min(area_dim1, area_dim2)
    area_width = max(area_dim1, area_dim2)

    x_panel_count = int(area_width // panel_width)
    y_panel_count = int(area_height // panel_height)
    rotated_panels_y_count = int(area_height // panel_width)
    rotated_panels_x_count = int(area_width % panel_width) // panel_height

    total_panel_count = (
        x_panel_count * y_panel_count + rotated_panels_y_count * rotated_panels_x_count
    )

    fig = get_panels_layout_fig(
        area_width,
        area_height,
        panel_width,
        panel_height,
        x_panel_count,
        y_panel_count,
        rotated_panels_x_count,
        rotated_panels_y_count,
    )
    return int(total_panel_count), fig


def get_panels_layout_fig(
    area_width,
    area_height,
    panel_width,
    panel_height,
    x_panel_count,
    y_panel_count,
    rotated_panels_x_count,
    rotated_panels_y_count,
):
    panels_rightmost_x = x_panel_count * panel_width
    fig, ax = plt.subplots()
    for x in np.arange(0, (x_panel_count + 1) * panel_width, step=panel_width):
        ax.plot([x, x], [0, y_panel_count * panel_height], 'b')
    for y in np.arange(0, (y_panel_count + 1) * panel_height, step=panel_height):
        ax.plot([0, panels_rightmost_x], [y, y], 'b')
    for x in np.arange(
        0, (rotated_panels_x_count + 1) * panel_height, step=panel_height
    ):
        ax.plot(
            [panels_rightmost_x + x, panels_rightmost_x + x],
            [0, rotated_panels_y_count * panel_width],
            'b',
        )
    for y in np.arange(0, (rotated_panels_y_count + 1) * panel_width, step=panel_width):
        ax.plot(
            [
                panels_rightmost_x,
                panels_rightmost_x + rotated_panels_x_count * panel_height,
            ],
            [y, y],
            'b',
        )

    ax.set_xlim(0, area_width)
    ax.set_ylim(0, area_height)
    ax.set_aspect('equal', adjustable='box')
    ax.tick_params(axis='both', which='both', length=0)

    return fig
