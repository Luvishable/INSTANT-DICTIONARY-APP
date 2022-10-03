import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
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

    @staticmethod
    def move_drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True


