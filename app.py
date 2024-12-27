from flask import Flask, render_template, request

frutas = []
registro = []

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def principal():
   if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
   return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
   #notas = {"Fulano":5.0, "Bltrano":7.4, "Aluno":7.0}
   if request.method == "POST":
      if request.form.get("aluno") and request.form.get("nota"):
        registro.append({"aluno": request.form.get("aluno"),"nota": request.form.get("nota")})
   
   return render_template("sobre.html", registro = registro)

if __name__ == '__main__':
    app.run(debug=True)
