import justpy as jp

class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home Page!", classes="text-4xl m-2")
        jp.Div(
            a=div,
            text="""
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut blandit fringilla maximus. Aliquam non nibh nis.
                    Phasellus egestas leo sit amet tellus porta vehicula. Integer molestie interdum ex, vitae luctus tortor
                    imperdiet sit amet. Nunc sollicitudin, augue at ullamcorper mollis, augue mauris vehicula mi, sed bibendum 
                    justo tellus non lectus. Duis pellentesque fermentum mi, ut luctus odio blandit vel. Sed fringilla fringilla 
                    dui at euismod. Vivamus a ipsum nec erat consequat vestibulum non ut felis. Suspendisse aliquet bibendum 
                    tristique. Vestibulum id eleifend urna, eget elementum neque. Donec rutrum imperdiet placerat.
                    Donec tristique diam sapien, a lobortis nunc imperdiet at. Nullam felis purus, gravida nec mauris nec, 
                    ultrices convallis lorem. Cras quis commodo sapien. Nullam id massa at velit cursus feugiat at vitae nunc.
                    """,
            classes="text-lg"
        )
        return wp


