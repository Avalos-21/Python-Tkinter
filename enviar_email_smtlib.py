"""
SMTP
¿Qué es y para qué sirve SMTP?
SMTP, Simple Mail Transfer Protocol por sus siglas en inglés, es un protocolo o conjunto de reglas 
de comunicación que utilizan los servidores de correo electrónico para enviar y recibir e-mails.
"""
from email.message import EmailMessage #Construir la estructura del email
import smtplib # conectar con el servidor y enviarlo
from tkinter import *
from tkinter import messagebox
#Python image Library
from PIL import ImageTk, Image
"------------INTERFAZ TKINTER------------"
ventana =Tk()
ventana.title("Envio de correos")
ventana.geometry("560x650")
ventana.resizable(0,0)
ventana.config(
    bd=10,
    bg="#F8F5F2"
)

Label(ventana, text="ENVÍO DE CORREOS",
      fg="#7A0C0C",
      font=("Georgia", 24, "bold"),
      pady=15).grid(row=0, column=0, columnspan=2)

#Imagen GMAIL
imagen_gmail = Image.open("imagen.jpg")
nueva_imagen = imagen_gmail.resize((100, 90))
render = ImageTk.PhotoImage(nueva_imagen)

label_imagen = Label(ventana, image=render)
label_imagen.image = render
label_imagen.grid(row=1, column=0, columnspan=2, pady=5)

# Variables
destinatario = StringVar(ventana)
asunto = StringVar(ventana)
otro_correo = StringVar(ventana)

correos = [
    "juliaavalos997@gmail.com",
    "marianelagarabito3@gmail.com",
    "fjcoronati@gmail.com",
    "lafortaleza246@gmail.com",
    "mfedullo@gmail.com"
]
destinatario.set(correos[0])
# Mi correo
Label(ventana, text="Mi correo:",
      fg="#7A0C0C",
      font=("Georgia", 11, "bold"),
      padx=10, pady=8).grid(row=2, column=0, sticky="w")

Label(ventana, text="juliaavalos997@gmail.com",
      fg="#333333",
      font=("Georgia", 10),
      padx=10, pady=8).grid(row=2, column=1, sticky="w")


# Destinatario
Label(ventana, text="Destinatario:",
      fg="#7A0C0C",
      font=("Georgia", 11, "bold"),
      padx=10, pady=8).grid(row=3, column=0, sticky="w")

menu_destinatario = OptionMenu(
    ventana,
    destinatario,
    *correos
)

menu_destinatario.config(
    font=("Georgia", 10),
    bg="#FFFDFC",
    fg="#333333",
    activebackground="#7A0C0C",
    activeforeground="white",
    relief="solid",
    bd=1,
    width=31
)

menu_destinatario["menu"].config(
    font=("Georgia", 10),
    bg="#FFFDFC",
    fg="#333333"
)

menu_destinatario.grid(
    row=3,
    column=1,
    padx=10,
    pady=8,
    sticky="ew"
)

Label(ventana, text="Otro correo:",
      fg="#7A0C0C",
      font=("Georgia", 11, "bold"),
      padx=10, pady=8).grid(
          row=4, column=0, sticky="w"
      )
# Otro correo
Entry(ventana,
      textvariable=otro_correo,
      width=34,
      font=("Georgia", 10),
      bg="#FFFDFC",
      fg="#333333",
      relief="solid",
      bd=1).grid(
          row=4, column=1,
          padx=10, pady=8,
          sticky="ew"
      )
# Asunto
Label(ventana, text="Asunto:",
      fg="#7A0C0C",
      font=("Georgia", 11, "bold"),
      padx=10, pady=8).grid(row=5, column=0, sticky="w")

Entry(ventana,
      textvariable=asunto,
      width=34,
      font=("Georgia", 10),
      bg="#FFFDFC",
      fg="#333333",
      relief="solid",
      bd=1).grid(
          row=5, column=1,
          padx=10, pady=8,
          sticky="ew"
      )
# Mensaje
Label(ventana, text="Mensaje:",
      fg="#7A0C0C",
      font=("Georgia", 11, "bold"),
      padx=10, pady=8).grid(row=6, column=0, sticky="nw")

mensaje = Text(ventana,
               height=6,
               width=34,
               font=("Georgia", 10),
               bg="#FFFDFC",
               fg="#333333",
               relief="solid",
               bd=1,
               padx=8,
               pady=8)
mensaje.grid(row=6, column=1, padx=10, pady=8, sticky="ew")

"------------ENVIO DE CORREO------------"
def enviar_email():
    remitente = "juliaavalos997@gmail.com"
    if not otro_correo.get().strip() and not destinatario.get():
        messagebox.showwarning(
            "Falta destinatario",
            "Seleccioná un destinatario o escribí otro correo."
        )
        return
    if not asunto.get().strip():
        messagebox.showwarning(
            "Falta asunto",
            "Escribí el asunto del correo."
        )
        return
    if not mensaje.get("1.0", "end").strip():
        messagebox.showwarning(
            "Falta mensaje",
            "Escribí el mensaje antes de enviar."
        )
        return     
    #Estrutura de email
    
    if otro_correo.get().strip():
        destinatario_final = otro_correo.get().strip()
    else:
        destinatario_final = destinatario.get()
        
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario_final
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0, 'end')))
    #Envio de email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(remitente,("kjnp euew gsqv rwtx")
)
            smtp.send_message(email)
            
            messagebox.showinfo(
                "Mensajería",
                "Correo enviado correctamente."
        )

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror(
            "Error de autenticación",
            "Gmail rechazó el acceso. Revisá la configuración de autenticación."
        )

    except Exception as error:
        messagebox.showerror(
            "Error al enviar",
            f"No se pudo enviar el correo:\n{error}"
        )
"------------BOTON------------"
boton_enviar = Button(
    ventana,
    text="✉  ENVIAR",
    command=enviar_email,
    height=2,
    width=18,
    bg="#7A0C0C",
    fg="white",
    activebackground="#5C0808",
    activeforeground="white",
    font=("Georgia", 11, "bold"),
    relief="flat",
    bd=0,
    cursor="hand2"
)

boton_enviar.grid(
    row=7,
    column=0,
    columnspan=2,
    padx=5,
    pady=18
)
ventana.mainloop()

