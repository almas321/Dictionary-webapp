import justpy as jp

class Home:
    path = "/home"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
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


