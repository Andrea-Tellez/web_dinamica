#Modificacion 
import web

urls = (
    "/", "Index",
    "/webpy", "Webpy",
    "/javascript", "Javascript"
)

app = web.application(urls, globals())
render = web.template.render("templates/", base="layout")

class Index:
    def GET (self):
        return render.index()

class Webpy:
    def GET (self):
        resultado = 0
        return render.webpy(resultado)

    def POST(self):
        form = web.input()#obtiene los datos del formulario
        num1 = int(form.num1)#convierte a entero
        num2 = int(form.num2)#convierte a entero
        resultado = num1 + num2 #realiza la suma
        return render.webpy(resultado)#retornona resultado

class Javascript:
    def GET(self):
        return render.javascript()

if __name__ == "__main__":
    app.run()