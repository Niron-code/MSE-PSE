from django.http import HttpResponse


def welcome(request, name):
    """
    A simple Django view that takes a name from the URL
    and returns a personalized welcome message.
    """
    return HttpResponse(f"""
    <html>
    <head>
        <title>Welcome to Django</title>
    </head>
    <body style="background-color: #9ff24b">
        <h1 style="color: #4bf2f2">
            Welcome {name} to Django!
        </h1>
    </body>
    </html>
    """)