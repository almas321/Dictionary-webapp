import justpy as jp

class About:
    # Quasar page as the
    # page that has the visuals.So
    # its responsible for the HTML part and the
    # CSS part.What the user is seeing
    # and the about
    # page is more concerned about handling
    # the URL, handling the routing. So
    # we want to make the connection between the
    # routing and the actual visual page, the
    # actual Quasar page. Therefore
    # for about we also need a path variable.

    path="/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is About page",classes="text-4xl m-2")
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

# this class is going to be used when the user visits the URL path.
# So your domain .com/about. In that case, that is when we want to instaniate the class.
# Otherwise we don't need to instaniate the class.
# If nobody is asking for an instance of this class, we don't need to do that.
# Therefore, we cannot use that way of instantiating the class.

# jp.Route(About.path, About.serve)

# jp.justpy(port=8001)





