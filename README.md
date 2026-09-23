# Telegram Translator Bot 🌐

Bot Telegram në Python që **përkthen çdo mesazh** që merr në 5 gjuhë: anglisht 🇬🇧, spanjisht 🇪🇸, arabisht 🇮🇶, kinezisht 🇨🇳 dhe turqisht 🇹🇷.

## Si funksionon
Përdoruesi i dërgon botit një tekst dhe boti kthen përkthimet në të 5 gjuhët, në formatin:

```
▫️ Translated for : `teksti`
▫️🇬🇧 English : `...`
▫️🇪🇸 Spanish : `...`
▫️🇮🇶 Arabic : `...`
▫️🇨🇳 Chinese : `...`
▫️🇹🇷 Turkish : `...`
```

## Si ekzekutohet versioni real
1. Instalo libraritë: `pip install pyTelegramBotAPI googletrans==4.0.0-rc1`
2. Krijo një bot me [@BotFather](https://t.me/BotFather) në Telegram dhe merr **token-in**
3. Vendose token-in në `original/bot.py` (tek `telebot.TeleBot("...")`)
4. Ekzekuto: `python original/bot.py`

> ⚠️ Mos e ndaj token-in e botit me askënd.

## Demo në browser
Dosja `demo/` përmban një **simulim**: përdor një fjalor të vogël të integruar për fjalë të zakonshme (jo Google Translate të vërtetë). Versioni real përdor Google Translate API.

---
Krijuar nga **Erion Nezha** — © 2026 Të gjitha të drejtat e rezervuara
