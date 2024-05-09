import matplotlib.pyplot as plt


def get_rect_area_panels_count_and_fig(panel_dim1, panel_dim2, area_dim1, area_dim2):
    panel_height = max(panel_dim1, panel_dim2)
    panel_width = min(panel_dim1, panel_dim2)
    area_height = max(area_dim1, area_dim2)
    area_width = min(area_dim1, area_dim2)

    width_panel_count = area_width // panel_width
    height_panel_count = area_height // panel_height
    rotated_panels_height_count = (area_height % panel_height) // panel_width
    rotated_panels_widtht_count = area_width // panel_height

    total_panel_count = (
        width_panel_count * height_panel_count
        + rotated_panels_height_count * rotated_panels_widtht_count
    )
    return int(total_panel_count), None
