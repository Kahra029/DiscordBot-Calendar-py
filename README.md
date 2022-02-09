# sample-calendar-discordbot

https://zenn.dev/kahra/articles/538e51cb9b33f6 こちらの記事を書くにあたり作成しました。

`config.json`と`credentials.json`を設定する必要があります。

## 設定
### config.json
`  "discord":{
    "token":"DISCORD BOT TOKEN",
    "webhook":"WEBHOOK URL"
  },`
  
`token` [Botアカウント作成](https://discordpy.readthedocs.io/ja/latest/discord.html)に従ってBotを作成後、トークンを取得。使用するDiscordサーバーにBotを入れることも忘れずに。
  
`webhook` [webhook](https://discord.com/developers/docs/resources/webhook)URLを作成し置換する。
  
 ` "calendar":{
     "id": "CALENDAR ID",
     "calendar_url":"CALENDAR URL"
   },`
   
 `id`, `calendar_url` [記事](https://zenn.dev/kahra/articles/8cb29a55ed392b)に従ってセットアップを行う。
  

## コマンド一覧
### イベント追加
`!eventadd YYYY/mm/DD HH:mm タイトル 関連URL` 1時間のイベントを追加

`!eventadd-long YYYY/mm/DD YYYY/mm/DD タイトル 関連URL` 終日のイベントを追加
### イベント確認
`!eventlist` 一週間分のイベントを表示する
### イベント削除
`!eventdelete イベントID`
