
import setting
import discord
from discord import Option
from discord.ext import commands
import os
import subprocess

TOKEN = setting.TOKEN

bot = discord.Bot()
GUILD_IDS = [1165893761621049414]  # ← BOTのいるサーバーのIDを入れます



@bot.event
async def on_ready():
    print(f"Bot名:{bot.user} On ready!!")


@bot.slash_command(description="コマンドを実行する", guild_ids=GUILD_IDS)
async def t(ctx,arg):
    await ctx.respond(str(arg))
    print(arg)
    powershell_command = arg

    result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True)
    pwd = str('\n'.join(subprocess.run(['powershell', '-Command', "pwd"], capture_output=True, text=True).stdout.strip().split('\n')[2:]))
    if result.returncode == 0:

        output_lines = result.stdout.strip().split('\n')[0:]  # 不要な行を削除
        output_text = '\n'.join(output_lines)
        s = output_text.translate(str.maketrans({"`":"\'"}))

        if len(str(output_text)) == 0:
            pwd = str('\n'.join(subprocess.run(['powershell', '-Command', "pwd"], capture_output=True, text=True).stdout.strip().split('\n')[2:]))
            await ctx.send(pwd+"  >")

        elif len(str(output_text)) < 1980:
            await ctx.send("```"+str(output_text)+"```")
            pwd = str('\n'.join(subprocess.run(['powershell', '-Command', "pwd"], capture_output=True, text=True).stdout.strip().split('\n')[2:]))
            await ctx.send(pwd+"  >")
        else:
            await ctx.send("```"+str(output_text)[0:1980]+".........```")
            pwd = str('\n'.join(subprocess.run(['powershell', '-Command', "pwd"], capture_output=True, text=True).stdout.strip().split('\n')[2:]))
            await ctx.send(pwd+"  >")
    else:
        await ctx.send("実行中にエラーが発生しました")
        pwd = str('\n'.join(subprocess.run(['powershell', '-Command', "pwd"], capture_output=True, text=True).stdout.strip().split('\n')[2:]))
        await ctx.send(pwd+"  >")

bot.run(TOKEN)