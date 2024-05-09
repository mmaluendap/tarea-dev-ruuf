import matplotlib.pyplot as plt


def get_rect_area_panels_count_and_fig(panel_dim1, panel_dim2, area_dim1, area_dim2):
    panel_height = max(panel_dim1, panel_dim2)
    panel_width = min(panel_dim1, panel_dim2)
    area_height = max(area_dim1, area_dim2)
    area_width = min(area_dim1, area_dim2)

    x_panel_count = area_width // panel_width
    y_panel_count = area_height // panel_height
    rotated_panels_y_count = (area_height % panel_height) // panel_width
    rotated_panels_x_count = area_width // panel_height

    total_panel_count = (
        x_panel_count * y_panel_count + rotated_panels_y_count * rotated_panels_x_count
    )

    return int(total_panel_count), None
