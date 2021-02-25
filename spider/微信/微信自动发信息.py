import win32clipboard as w
import win32con
import win32api
import win32gui
import time
import random

#把文字放入剪贴板
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
    w.CloseClipboard()

#模拟ctrl+V
def ctrlV():
    win32api.keybd_event(17,0,0,0) #ctrl
    win32api.keybd_event(86,0,0,0) #V
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)#释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

#模拟alt+s
def altS():
    win32api.keybd_event(18,0,0,0)
    win32api.keybd_event(83,0,0,0)
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
# 模拟enter
def enter():
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
#模拟单击
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#移动鼠标的位置
def movePos(x,y):
    win32api.SetCursorPos((x,y))

if __name__=="__main__":
    name_list = ['认真你就输了', '沐雷', 'c- 。', '我是聂聂聂聂sir', '渣渣翔', '沐雨', '群主', 'D啊、💥', '沐电', '天⃰宥⃰～', '大白', '赫拉利', 'llb',
                 '苏。', '聂聂六', '刘家大少爷', '老阎', '洪源骏', '日日锐', 'Mr.humor', 'DAO', 'Run', '木皆', '六筒', '◆丶小双〃 ﹏', '彭文达', '日全十',
                 '何以慰相思', '日全六', '旋转的烤鸡', '渣渣绪', '.', 'magicHu', '小菜鸟', '梓', '梵空', '牧人之上', '沐风','@_@嘟', 'Toby', '沐火', '沐维',
                 '渣渣弗', 'Eli', '🐋🦈🇾⃰🇺⃰ 洋⃰', '粉条', '无敌天才蛋', 'W', '城南花已开。', '江山如画', '陈伯亮']
    call_list = ['炮友', '老哥', '老铁', '基友', '兄弟', 'LSP', '富豪','老板','3秒先生']
    content_list = ['过年回不去了，可咋整？', '今天买鸡赚了没？', '最近喝茶没有？', '过年发了什么物资？', '年底年终奖多少？', '你们老家需要核酸检测吗？','玩过双飞没有，刺激吗？','一般啪啪你能做多久？',
                    '最近有B日吗？','兰兰的熊大吗？' ]
    while 1 > 0:
        #获取鼠标当前位置
        #hwnd=win32gui.FindWindow("MozillaWindowClass",None)
        hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
        win32gui.ShowWindow(hwnd,win32con.SW_SHOW)
        win32gui.MoveWindow(hwnd,0,0,1000,700,True)
        time.sleep(0.01)
        #1.移动鼠标到通讯录位置，单击打开通讯录
        movePos(28,147)
        click()
        #2.移动鼠标到搜索框，单击，输入要搜索的名字
        movePos(148,35)
        click()
        setText('相亲相爱')
        ctrlV()
        time.sleep(1) #别问我为什么要停1秒，问就是给微信一个反应的时间，他反应慢反应不过来，其他位置暂停的原因同样
        enter()
        time.sleep(1)
        choice_name_list = random.choice(name_list)
        choice_call_list = random.choice(call_list)
        choice_content_list = random.choice(content_list)
        #3.复制要发送的消息，发送
        setText(str(choice_call_list) + ',' + str(choice_name_list) + '你好啊！' + str(choice_content_list))
        ctrlV()
        altS()
