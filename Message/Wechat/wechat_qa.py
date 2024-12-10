# -*- encoding: utf-8 -*-
'''
@File    :   wechat.py
@Time    :   2024/12/10 18:53:06
@Author  :   chaopaoo12
@Version :   1.0
@Contact :   chaopaoo12@hotmail.com
'''

# here put the import lib
import requests

# 下面的参数自行填写
# user, strategy_id, account, code, direction, offset, price, volume, 

def send_actionnotice(strategy_id,
                      account,
                      code,
                      direction,
                      offset,
                      volume,
                      user,
                      price=None,
                      now = None):
    try:
        requests.post("http://www.yutiansut.com/signal?user_id={user}&template=xiadan_report&strategy_id={strategy_id}&realaccount={account}&code={code}&order_direction={direction}&order_offset={offset}&price={price}&volume={volume}&order_time={now}".format(user = user, strategy_id = strategy_id, account = account, code = code, direction= direction, offset= offset, price = price, volume = volume, now =now))
    except:
        pass
