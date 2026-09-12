import flet as ft
import asyncio


def main(page: ft.Page):
    page.title = "BS3D"
    page.padding = 0
    page.bgcolor = "#000000"  # Background for the empty right portion

    dimension_content = ft.Column(spacing=10)


    dimensions_container = ft.Container(
        content=dimension_content,
        opacity = 0,
        animate_opacity = 500
    )

    async def change_dimensions(e):
        selected_beam = e.control.value

        dimensions_container.opacity = 0
        dimensions_container.update()
        await asyncio.sleep(0.3)
        dimension_content.controls.clear()

        if selected_beam == "I-Beam":
            dimension_content.controls.extend(
                [
                    ft.Text(
                        "I-Beam Dimensions",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",

                    ),
                    ft.TextField(label="Height", width=260),
                    ft.TextField(label="Flange Width", width=260),
                    ft.TextField(label="Flange Thickness", width=260),
                    ft.TextField(label="Web Thickness", width=260),

                ]
            )
        elif selected_beam == "Rectangular":
            dimension_content.controls.extend(
                [
                    ft.Text(
                        "Rectangular Beam Dimensions",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.TextField(label="Width", width=260),
                    ft.TextField(label="Height", width=260),
                ]
            )
        elif selected_beam == "Circular":
            dimension_content.controls.extend(
                [
                    ft.Text(
                        "Circular Beam Dimensions",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.TextField(label="Diameter", width=260),
                ]
            )
        dimensions_container.opacity = 1
        dimensions_container.update()


    beam_type = ft.Dropdown(
        label="Select Beam Type",
        width=200,
        label_style=ft.TextStyle(color="#0F172A"),
        options=[
            ft.dropdown.Option(
                "Rectangular", style=ft.ButtonStyle(color="#0F172A")
            ),
            ft.dropdown.Option(
                "Circular", style=ft.ButtonStyle(color="#0F172A")
            ),
            ft.dropdown.Option("I-Beam", style=ft.ButtonStyle(color="#0F172A")),
        ],
        bgcolor="#FFFFFF",
        border_color="#0F172A",
        focused_border_color="#2563EB",
        border_radius=8,
        text_style=ft.TextStyle(color="#0F172A"),
        on_select = change_dimensions,



    )

    load_type = ft.Dropdown(
        label="Select Load Type",
        width=200,
        label_style=ft.TextStyle(color="#0F172A"),
        options=[
            ft.dropdown.Option(
                "POINT LOAD", style=ft.ButtonStyle(color="#0F172A")
            ),
            ft.dropdown.Option(
                "UDL", style=ft.ButtonStyle(color="#0F172A")
            ),
            ft.dropdown.Option("UVL", style=ft.ButtonStyle(color="#0F172A")),
        ],
        bgcolor="#FFFFFF",
        border_color="#0F172A",
        focused_border_color="#2563EB",
        border_radius=8,
        text_style=ft.TextStyle(color="#0F172A"),
    )

    # Left panel locked at width 300 with pure white background
    left_panel = ft.Container(
        width=250,
        bgcolor="#FFFFFF",
        padding=20,
        expand=False,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Beam Controls",
                    color="#0F172A",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    "Beam Type",
                    color="#0F172A",
                ),
                beam_type,
                dimensions_container,
                load_type
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    page.add(
        ft.Row(
            controls=[
                left_panel,
                ft.Container(expand=True),

            ],
            expand=True,
            spacing=0,
        )
    )


ft.app(target=main)
