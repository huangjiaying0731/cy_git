import simpleguitk as simplegui
import random

baymax = simplegui.load_image('https://img2020.cnblogs.com/blog/2145917/202010/2145917-20201017214651584-1156775001.jpg')

width = 500
height = width + 100
# 定义图像块的边长
image_size = width / 3
# 定义图像块的坐标列表
all_coordinates = [[image_size * 0.5, image_size * 0.5], [image_size * 1.5, image_size * 0.5],
                   [image_size * 2.5, image_size * 0.5], [image_size * 0.5, image_size * 1.5],
                   [image_size * 1.5, image_size * 1.5], [image_size * 2.5, image_size * 1.5],
                   [image_size * 0.5, image_size * 2.5], [image_size * 1.5, image_size * 2.5],
                   None
                   ]

# 棋盘的行列
ROWS = 3
COLS = 3

# 棋盘步数
steps = 0

# 保存所有图像块的列表
board = [[None, None, None], [None, None, None], [None, None, None]]


# 定义一个图像块的类
class Square:

    def __init__(self, coordinate):
        self.center = coordinate

    def draw(self, canvas, board_pos):
        canvas.draw_image(baymax, self.center, [image_size, image_size],
                          [(board_pos[1] + 0.5) * image_size, (board_pos[0] + 0.5) * image_size]
                          , [image_size, image_size])


def init_board():
    """对每个小方格，创建方块对象"""

    # 随机打乱列表
    random.shuffle(all_coordinates)

    # 填充并且拼接图版
    for i in range(ROWS):
        for j in range(COLS):
            idx = i * ROWS + j
            square_center = all_coordinates[idx]
            if square_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(square_center)


def play_game():
    """重置游戏"""
    global steps
    steps = 0
    init_board()

    
def draw(canvas):
    """画界面上的元素"""

    # 画下方图片
    canvas.draw_image(baymax, [width / 2, height / 2], [width, height], [50, width + 50], [98, 98])
    # 画下方步数
    canvas.draw_text("步数: " + str(steps), [300, 580], 22, 'white')
    # 绘制游戏界面各元素
    
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                board[i][j].draw(canvas, [i, j])

def draw_intro(canvas):
    #画游戏介绍的主要内容#
    canvas.draw_text("玩家需在最短的时间最少的步",[30,100],10,'black')
    canvas.draw_text("数内使九个小方框组成一个完整的图片",[30,120],10,'black')

def draw_win(canvas):
    #画游戏成功后的内容#
    canvas.draw_text("您赢得了这次游戏",[30,100],20,'black')
   
def mouse_click(pos):
    """鼠标点击事件"""
    global steps
    # r为行数，c为列数
    r = int(pos[1] // image_size)
    c = int(pos[0] // image_size)
    if r < 3 and c < 3:
        # 点击到空白位置
        if board[r][c] is None:
            return
        else:
            # 依次检查当前图像位置的上下左右是否有空位置
            current_square = board[r][c]
            # 判断上面
            if r - 1 >= 0 and board[r - 1][c] is None:
                board[r][c] = None
                board[r - 1][c] = current_square
                steps += 1
            # 判断下面
            elif r + 1 <= 2 and board[r + 1][c] is None:
                board[r][c] = None
                board[r + 1][c] = current_square
                steps += 1
            # 判断在左边
            elif c - 1 >= 0 and board[r][c - 1] is None:
                board[r][c] = None
                board[r][c - 1] = current_square
                steps += 1
            # 判断在右边
            elif c + 1 <= 2 and board[r][c + 1] is None:
                board[r][c] = None
                board[r][c + 1] = current_square
                steps += 1


def end_game():
    #关闭游戏界面#
    exit()

def intro_game():
    #设置游戏介绍的框架#
    frame=simplegui.create_frame('华容道',300,300)
    frame.set_canvas_background('white')
    frame.set_draw_handler(draw_intro)
    frame.add_button('主菜单', main_game, 100)
    frame.start()
    
def main_game():
    #设置主菜单的框架#
    frame=simplegui.create_frame('华容道',-100,-100)
    frame.set_canvas_background('black')
    frame.add_button('开始游戏', play_game, 100)
    frame.add_button('游戏介绍', intro_game, 100)
    frame.add_button('结束游戏', end_game, 100)
    frame.start()

def win_game():
    #设置游戏成功的框架#
    frame=simplegui.create_frame('华容道',300,300)
    frame.set_canvas_background('white')
    frame.set_draw_handler(draw_win)
    frame.add_button('主菜单', main_game, 100)
    frame.add_button('结束游戏', end_game, 100)
    frame.start()

#主要开始游戏的框架构建#
frame=simplegui.create_frame('拼图', width,height)
frame.set_canvas_background('black')
# 绘制界面
frame.set_draw_handler(draw)
# 创建窗口，绑定事件，设置大小
frame.add_button('重新开始', play_game, 100)
frame.add_button('游戏成功', win_game, 100)
frame.add_button('主菜单', main_game, 100)
# 注册鼠标事件
frame.set_mouseclick_handler(mouse_click)
# 初始化游戏
play_game()
# 启动框架
frame.start()
