import asyncio
import flet as ft


def main(page: ft.Page):
    page.title = "BS3D"
    page.padding = 0
    page.bgcolor = "#000000"

    dimension_content = ft.Column(spacing=10)

    dimensions_container = ft.Container(
        content=dimension_content, opacity=0, animate_opacity=500
    )

    load_content = ft.Column(spacing=10)

    # Removed fixed height to let container adjust dynamically to content size
    load_container = ft.Container(
        content=load_content,
        border=ft.Border.all(1, "#000000"),
        padding=10,
        width=220,
        height=None,
        bgcolor= ft.Colors.BLUE_300,
        opacity=0,
        animate_opacity=500,
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
                    ft.TextField(label="Height", width=260, color="#0F172A"),
                    ft.TextField(
                        label="Flange Width", width=260, color="#0F172A"
                    ),
                    ft.TextField(
                        label="Flange Thickness", width=260, color="#0F172A"
                    ),
                    ft.TextField(
                        label="Web Thickness", width=260, color="#0F172A"
                    ),
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
                    ft.TextField(label="Width", width=260, color="#0F172A"),
                    ft.TextField(label="Height", width=260, color="#0F172A"),
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
                    ft.TextField(label="Diameter", width=260, color="#0F172A"),
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
        on_select=change_dimensions,
    )

    # Callback action for the Confirm Button
    async def confirm_load(e):
        load_data = {}
        # Iterate over inputs in load_content and extract non-empty field values
        for control in load_content.controls:
            if isinstance(control, ft.TextField):
                load_data[control.label] = control.value

        print("Confirmed Load Data:", load_data)

        # Visual feedback: Briefly flash border green on confirmation
        load_container.border = ft.Border.all(2, "#22C55E")
        load_container.update()
        await asyncio.sleep(0.4)
        load_container.border = ft.Border.all(1, "#000000")
        load_container.update()

    async def change_load(e):
        selected_load = e.control.value

        load_container.opacity = 0
        load_container.update()

        await asyncio.sleep(0.3)
        load_content.controls.clear()

        if selected_load == "POINT LOAD":
            load_content.controls.extend(
                [
                    ft.Text(
                        "Point Load Parameters",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.TextField(
                        label="Load Magnitude (kN)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                    ft.TextField(
                        label="Load Position (m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                ]
            )

        elif selected_load == "UDL":
            load_content.controls.extend(
                [
                    ft.Text(
                        "UDL Parameters",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.TextField(
                        label="Load Intensity (kN/m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                    ft.TextField(
                        label="Start Position (m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                    ft.TextField(
                        label="End Position (m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                ]
            )

        elif selected_load == "UVL":
            load_content.controls.extend(
                [
                    ft.Text(
                        "UVL Parameters",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.TextField(
                        label="Start Intensity (kN/m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                    ft.TextField(
                        label="End Intensity (kN/m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                    ft.TextField(
                        label="Start Position (m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                    ft.TextField(
                        label="End Position (m)",
                        width=200,
                        color="#0F172A",
                        keyboard_type=ft.KeyboardType.NUMBER,
                    ),
                ]
            )

        # Add Confirm Button at the bottom of the dynamic load fields
        if selected_load:
            load_content.controls.append(
                ft.ElevatedButton(
                    "Confirm Load",
                    on_click=confirm_load,
                    bgcolor="#0F172A",
                    color="#FFFFFF",
                    width=200,
                )
            )

        load_container.opacity = 1
        load_container.update()

    load_type = ft.Dropdown(
        label="Select Load Type",
        width=200,
        label_style=ft.TextStyle(color="#0F172A"),
        options=[
            ft.dropdown.Option(
                "POINT LOAD", style=ft.ButtonStyle(color="#0F172A")
            ),
            ft.dropdown.Option("UDL", style=ft.ButtonStyle(color="#0F172A")),
            ft.dropdown.Option("UVL", style=ft.ButtonStyle(color="#0F172A")),
        ],
        bgcolor="#FFFFFF",
        border_color="#0F172A",
        focused_border_color="#2563EB",
        border_radius=8,
        text_style=ft.TextStyle(color="#0F172A"),
        on_select=change_load,
    )

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
                ft.Text("Load Type", color="#0F172A"),
                load_type,
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    page.add(
        ft.Row(
            controls=[
                left_panel,

                ft.Container(
                    expand=True,
                ),

                ft.Column(
                    controls=[
                        load_container,
                    ],
                    tight=True,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
            ],
            expand=True,
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )




ft.app(target=main)