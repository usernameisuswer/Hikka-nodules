from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Это будет наша имитация базы данных для сообщений
messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Обработка отправки сообщения
        text = request.form.get('message')
        image = request.files.get('image')
        
        if text:
            messages.append(('text', text))
        
        if image:
            # Сохраняем изображение и сохраняем имя файла
            image_filename = os.path.join('static', image.filename)
            image.save(image_filename)
            messages.append(('image', image_filename))
        
        return redirect(url_for('index'))
    
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)

# Примечание: Этот код не будет работать в текущей среде, так как требует установленного Flask и запущенного веб-сервера. Это пример того, как можно структурировать простой веб-мессенджер с возможностью отправки изображений на Python с использованием Flask.
