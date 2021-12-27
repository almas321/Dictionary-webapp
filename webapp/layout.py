import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_model="left",
                            bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)

        jp.A(a=qlist, text="Home", href="/home", classes="p-2 m-2 text-lg text-blue-400 hover:text-blue-700")
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes="p-2 m-2 text-lg text-blue-400 hover:text-blue-700")
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes="p-2 m-2 text-lg text-blue-400 hover:text-blue-700")
        jp.Br(a=qlist)

        jp.QButton(a=toolbar, dense=True, flat=True, round=True,
                   icon="menu", click=self.move_drawer, drawer=drawer)

        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")



    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True