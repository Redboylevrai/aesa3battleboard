import flet as ft
from flet_core import icons


class AppBar(ft.AppBar):
    def __init__(self):
        super().__init__(

        leading=ft.IconButton(icons.POST_ADD),

        title=ft.Text("AESA III Battleboard"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,

        actions=[
            ft.Container(
                content=ft.Badge(
                    content=ft.Icon(icons.PLAY_CIRCLE_OUTLINED),
                    text="12",
                    ),
                width=100,
                alignment=ft.alignment.center_left
            ),

            ft.IconButton(icons.FOLDER_OPEN),
            ft.IconButton(icons.SAVE),
            ft.IconButton(icons.UNDO),
            ft.IconButton(icons.REDO),
            ft.IconButton(icons.REPLAY),
            ]
        )

def main(page: ft.Page):
    page.appbar = AppBar()

    page.bottom_appbar = ft.BottomAppBar(
        #bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.Container(expand=True),
                ft.ElevatedButton(icon=icons.DONE, text="OK", icon_color=ft.colors.GREEN_ACCENT),
                ft.ElevatedButton(icon=icons.FORWARD, text="GO"),
                ft.Container(expand=True),
            ]
        )
    )

    page.add(
        ft.DataTable(
            width=1200,
            bgcolor="yellow",
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.BorderSide(3, "blue"),
            horizontal_lines=ft.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[
                ft.DataColumn(
                    ft.Text("Column 1"),
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
                ft.DataColumn(
                    ft.Text("Column 2"),
                    tooltip="This is a second column",
                    numeric=True,
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
            ],
            rows=[
                ft.DataRow(
                    [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                ),
                ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
            ],
        ),
    )


ft.app(main)
