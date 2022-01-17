import justpy as jp
import definition
from webapp import layout
import requests
class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.", classes="text-lg")

        input_div=jp.Div(a=div, classes="grid grid-cols-2")



        output= jp.Div(a=div, classes="m=2 p=2 text-lg border-2 border-black h-40")

        # jp.Button(a=input_div, text="Get Definition", classes="border-2 border-black",
        #           click=cls.get_definition, op=output, inputbox=input_box)
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",
                             classes="m-2 bg-gray-100 border-2 border-gray-200 "
                                     "rounded w-54 focus:bg:white focus:outline-none "
                                     "focus:border-black py-2 px-4", op=output)

        input_box.on('input', cls.get_definition)


        return wp


    @staticmethod
    def get_definition(widget, msg):
        # # widget.op.text= widget.inputbox.value
        # defined= definition.Defintion(widget.value).get()

        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = req.json()
        widget.op.text = " ".join(data["definition"])
