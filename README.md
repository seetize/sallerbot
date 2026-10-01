# Telegram sales bot

Бот использует Telegram polling и OpenAI-compatible `/chat/completions` endpoint. Состояния диалога и последние сообщения сохраняются в SQLite (`bot.db`). Для анализа фото используется `OPENAI_VISION_MODEL` (сейчас `gemini-2.5-flash`), затем `OPENAI_VISION_FALLBACK_MODEL` и `OPENAI_VISION_SECOND_FALLBACK_MODEL`; endpoint должен поддерживать мультимодальные запросы OpenAI.

После `/start` бот спрашивает о занятости и свободном времени. Пользователь может выбрать более мягкий или прямой тон и открыть отдельный раздел «Безопасность». После пяти минут тишины бот отправляет одно короткое сообщение по контексту; `/stop_followups` отключает такие сообщения, повторный `/start` включает их снова.

При явном интересе к оплате бот показывает сопровождение по скриншотам или текстовую инструкцию и даёт выбрать Telegram Wallet, Bybit или Binance. Инструкции сейчас текстовые. Реальные или сгенерированные изображения экранов бирж не используются: для точных шагов нужны проверенные материалы, иначе изображение может показать неправильные элементы интерфейса.

Для инструкции Bybit сохраните присланную памятку как `assets/bybit/bybit-guide.png`, затем выполните `py -3 scripts/split_bybit_guide.py`. Бот будет отправлять шаги `bybit-step-1.png` ... `bybit-step-6.png` с кнопкой перехода к следующему шагу.

## Запуск в PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
python bot.py
```

В `.env` укажите `TELEGRAM_BOT_TOKEN`, `OPENAI_API_KEY`, модель и реальный `PAYMENT_ADDRESS`.
Не публикуйте `.env` и не отправляйте токен в чат или репозиторий. После публикации токена в переписке его следует перевыпустить через BotFather.
