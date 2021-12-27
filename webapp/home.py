import justpy as jp
from webapp import layout
class Home:
    path = "/home"

    @classmethod
    def serve(cls,self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")

        container = jp.QPageContainer(a=lay)
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



