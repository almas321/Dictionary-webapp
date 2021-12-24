import justpy as jp

class Home:
    path = "/home"

    @classmethod
    def serve(cls,self):
        wp = jp.QuasarPage(tailwind=True)

        layout=jp.QLayout(a=wp,view="hHh lpR fFf" )
        header=jp.QHeader(a=layout)
        toolbar=jp.QToolbar(a=header)



        drawer=jp.QDrawer(a=layout, show_if_above=True, v_model="left",
               bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes="fit" )
        qlist= jp.QList(a=scroller)

        jp.A(a=qlist, text="Home", href="/home", classes="p-2 m-2 text-lg text-blue-400 hover:text-blue-700")
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes="p-2 m-2 text-lg text-blue-400 hover:text-blue-700")
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes="p-2 m-2 text-lg text-blue-400 hover:text-blue-700")
        jp.Br(a=qlist)


        jp.QButton(a=toolbar, dense=True, flat=True, round=True,
                  icon="menu", click=cls.move_drawer, drawer=drawer)

        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")


        container=jp.QPageContainer(a=layout)


        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is Home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                is simply dummy text of the printing
                 and typesetting industry.
                  Lorem Ipsum has been the industry's 
                  standard dummy text ever since the 
                  1500s, when an unknown printer took
                   a galley of type and scrambled it 
                   to make a type specimen book.
                    It has survived not only five 
                    centuries, but also the leap
                    is simply dummy text of the printing
                 and typesetting industry.
                  Lorem Ipsum has been the industry's 
                  standard dummy text ever since the 
                  1500s, when an unknown printer took
                   a galley of type and scrambled it 
                   to make a type specimen book.
                    It has survived not only five 
                    centuries, but also the leap
                """, classes="text-lg")
        return wp


    @staticmethod
    def move_drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value=False
        else:
            widget.drawer.value = True
