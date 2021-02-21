from aiogram import Dispatcher

from .icmp import ICMPCheckerHandler
from .ipcalc import IPCalcCommandHandler
from .minecraft import MinecraftCheckerHandler
from .start import start_cmd
from .tcp import TCPCheckerHandler
from .web import WebCheckerHandler
from .whois import WhoisCommandHandler


def setup(dp: Dispatcher):
    dp.register_message_handler(start_cmd, is_forwarded=False, commands=['start', 'help'])
    dp.register_message_handler(WebCheckerHandler().handler, is_forwarded=False, commands=['web', 'http'])
    dp.register_message_handler(WhoisCommandHandler().handler, is_forwarded=False, commands=['whois'])
    dp.register_message_handler(ICMPCheckerHandler().handler, is_forwarded=False, commands=['icmp', 'ping'])
    dp.register_message_handler(TCPCheckerHandler().handler, is_forwarded=False, commands=['tcp'])
    dp.register_message_handler(MinecraftCheckerHandler().handler, is_forwarded=False, commands=['minecraft', 'mc'])
    dp.register_message_handler(IPCalcCommandHandler().handler, is_forwarded=False, commands=['ipcalc'])
