# 🚀 Entorno Profesional de Desarrollo con IA (WSL + Docker + Python + OpenAI)

## 📌 Objetivo

Configurar un entorno profesional para:

- Desarrollo backend (Python)
- Desarrollo general (Node.js)
- Uso de IA (OpenAI)
- Contenedores (Docker)
- VS Code conectado a Linux (WSL)

---

# 🧱 1. Instalación de WSL (Windows Subsystem for Linux)

## 📌 Comando (PowerShell como administrador)

```powershell
wsl --install
📖 Explicación
Instala WSL2
Instala Ubuntu automáticamente
Permite correr Linux dentro de Windows
Verificar instalación
wsl -l -v
🔄 2. Reset completo (opcional)
Eliminar distribuciones
wsl --unregister Ubuntu
wsl --unregister docker-desktop
wsl --unregister docker-desktop-data
Verificar limpieza
wsl -l -v
🐧 3. Configuración inicial de Ubuntu
sudo apt update && sudo apt upgrade -y
🐳 4. Instalación de Docker en WSL
sudo apt install -y docker.io
Habilitar Docker
sudo systemctl enable docker
sudo systemctl start docker
Evitar usar sudo
sudo usermod -aG docker $USER
exit

(Reabrir Ubuntu después)

Verificar Docker
docker run hello-world
Prueba avanzada
docker run -it ubuntu bash
ls
exit
📁 5. Crear workspace de desarrollo
cd ~
mkdir -p workspace/dev-test
cd workspace/dev-test
⚠️ IMPORTANTE

❌ NO trabajar en:

/mnt/c/

✅ Trabajar en:

/home/usuario/
🟢 6. Instalación de Node.js (nvm)
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
Instalar Node
nvm install --lts
nvm use --lts
Verificar
node -v
npm -v
🐍 7. Instalación de Python
sudo apt install -y python3 python3-pip python3-venv
🧪 8. Crear entorno virtual
cd ~/workspace/dev-test
mkdir python-backend
cd python-backend

python3 -m venv .venv
source .venv/bin/activate
Verificar entorno
which python
which pip
📦 9. Actualizar pip
pip install --upgrade pip setuptools wheel
💻 10. Configurar VS Code con WSL
Abrir proyecto
cd ~/workspace/dev-test/python-backend
code .
En VS Code
Ctrl + Shift + P → Python: Select Interpreter

Seleccionar:

.venv/bin/python
📦 11. Instalar librerías IA
pip install openai python-dotenv
🔐 12. Variables de entorno
Crear archivo
nano .env

Contenido:

OPENAI_API_KEY=tu_api_key
Exportar variables (opcional)
export $(grep -v '^#' .env | xargs)
🚫 .gitignore
nano .gitignore

Contenido:

.venv/
.env
__pycache__/
📁 13. Estructura del proyecto
mkdir -p app/services
touch app/__init__.py
touch app/main.py
touch app/services/__init__.py
touch app/services/openai_service.py
🤖 14. Código OpenAI
Servicio
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text
Main
from dotenv import load_dotenv
from app.services.openai_service import ask_openai

load_dotenv()

def main():
    prompt = "Explícame qué es una API REST en una frase"

    print("\n--- OpenAI ---")
    print(ask_openai(prompt))

if __name__ == "__main__":
    main()
▶️ 15. Ejecutar aplicación
python -m app.main
🧪 16. Test rápido de OpenAI (sin app)
export $(grep -v '^#' .env | xargs)

python - <<'PY'
from openai import OpenAI
client = OpenAI()
r = client.responses.create(
    model="gpt-5",
    input="Responde solo: OpenAI OK"
)
print(r.output_text)
PY
🧠 Arquitectura final
main.py → service → OpenAI API
🔥 Conceptos clave
Separación de responsabilidades
Uso de .env
Modularidad
Ejecución con -m
Entorno aislado (venv)
Desarrollo en Linux real (WSL)
🚀 Estado final

✔ WSL configurado
✔ Docker funcionando
✔ Node con nvm
✔ Python con venv
✔ VS Code conectado a WSL
✔ OpenAI funcionando

🔜 Próximos pasos
FastAPI
endpoints REST
múltiples modelos (OpenAI + Claude)
Dockerización
despliegue
🧠 Conclusión

Este entorno replica un stack profesional usado en:

startups
fintech
equipos de IA
backend moderno

---

# 💬 Si quieres siguiente nivel

Puedo darte la **versión extendida del MD** con:

- FastAPI
- Dockerfile
- arquitectura limpia
- API real `/ask`

Solo dime:

👉 **“agrega backend con FastAPI al md”** 🚀


📌 1. DOCUMENTACIÓN GIT (LISTA PARA TU MD)

Puedes copiar esto directo a tu documentación:

# 🔧 Configuración de Git y GitHub en WSL

## 📌 Objetivo

Configurar Git dentro de WSL para:

- trabajar en proyectos Linux
- colaborar con otros desarrolladores
- usar GitHub de forma segura (SSH)

---

# 🧱 1. Verificar instalación de Git

```bash
git --version
Instalar si no existe
sudo apt install -y git
⚙️ 2. Configurar identidad de usuario
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
Verificar configuración
git config --list
🔐 3. Configurar acceso a GitHub (SSH)
Generar clave SSH
ssh-keygen -t ed25519 -C "tu@email.com"

Presionar Enter → Enter → Enter

Mostrar clave pública
cat ~/.ssh/id_ed25519.pub
Agregar clave en GitHub
Ir a GitHub
Settings
SSH and GPG Keys
New SSH Key
Pegar clave
Probar conexión
ssh -T git@github.com

Resultado esperado:

Hi username! Youve successfully authenticated
📁 4. Inicializar repositorio
cd ~/workspace/dev-test/python-backend

git init
git add .
git commit -m "Initial commit"
🔗 5. Conectar con GitHub
git remote add origin git@github.com:tu-usuario/tu-repo.git
git branch -M main
git push -u origin main
🔄 6. Flujo básico de trabajo
git add .
git commit -m "mensaje"
git push
🚫 Buenas prácticas
.gitignore obligatorio
.venv/
.env
__pycache__/
⚠️ Reglas importantes
No subir API keys
No subir entornos virtuales
Usar SSH en lugar de HTTPS
Trabajar siempre desde WSL (no Windows)
🧠 Conceptos clave
git init: inicia repositorio
git add: prepara archivos
git commit: guarda cambios
git push: sube cambios a GitHub
git remote: conecta con repositorio remoto
🚀 Resultado final

✔ Proyecto versionado
✔ Conectado a GitHub
✔ Listo para colaboración