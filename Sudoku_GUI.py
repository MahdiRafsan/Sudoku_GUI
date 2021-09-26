from Sudoku_Solver import is_valid_num, is_empty
import pygame
pygame.init()
pygame.font.init()

width, height = 600, 650
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 150, 0)
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont("comicsans", 40)
font_game_ins = pygame.font.SysFont("timesnewroman", 20)
font_disp = pygame.font.SysFont("timesnewroman", 40)

def draw_grid():
    '''
    draw the sudoku board
    '''
    for i in range(10):
        if i % 3 == 0:
            thick = 5
        else:
            thick = 2
        
        # horizontal lines (x changes, y constant)
        pygame.draw.line(screen, black, (30, 30 + 60 * i), (570, 30 + 60 * i), thick)
        
        # vertical lines (x constant, y changes)
        pygame.draw.line(screen, black, (30 + 60 * i, 30), (30 + 60 * i, 570), thick)

def draw_box(x, y):
    '''
    draw box around the selected cell on the sudoku grid
    '''
    if  0 <= x <= 8 and  0 <= y <= 8:  
        for i in range(2):
            
            # horizontal lines
            pygame.draw.line(screen, orange, (30 + x * 60, 30 + (y + i) * 60), (30 + x * 60 + 60, 30 + (y + i) * 60), 5)
            
            # vertical lines
            pygame.draw.line(screen, orange, (30 + (x + i) * 60, 30 + y * 60), (30 + (x + i) * 60, 30 + y * 60 + 60), 5)  
     
def print_num(grid):
    '''
    print numbers on the sudoku board
    '''
   
    for i in range(9):
        for j in range(9):
            if grid[j][i] != 0:   # grid[j][i] = grid[row][column]
                
            # rect → left, top, width, height
                pygame.draw.rect(screen, (0, 200, 210), (30 + 60 * i, 30 + 60 * j, 60, 60))
                text = font.render(str(grid[j][i]), 1, black)
                
                # values choosen depending on the window size
                screen.blit(text, (30 + 60 * i + 22, 30 + 60 * j + 18))
            
def solve(grid):
    ''' 
    function to solve the board
    '''
    row, col = is_empty(grid)
    
    if row == None:
        return True
    pygame.event.pump()   
    for num in range(1, 10):
        if is_valid_num(grid, num, row, col):
            grid[row][col] = num
                
            screen.fill((255, 255, 255))
            print_num(grid)
            draw_grid()
            
            pygame.display.update()
            pygame.time.delay(100)
            
            if solve(grid):
                return True
            
            grid[row][col] = 0
            
            screen.fill((255, 255, 255))
            print_num(grid)
            draw_grid()
            
            pygame.display.update()
            pygame.time.delay(100)   
    return False 

def game_instructions():
    '''
    shows instructions for the user
    '''
    text_clr = font_game_ins.render("Press C to clear the board and R to reset the board", 1, black)
    text_solve = font_game_ins.render("Press Enter to solve the board automatically", 1, black)
    screen.blit(text_clr, (20, 590))
    screen.blit(text_solve, (20, 620))
    
def wrong_num():
    ''' 
    displays error message
    '''
    text = font_disp.render("WRONG ENTRY!!!", True, (255, 0, 0))
    screen.blit(text, (145, 590))
    
def solve_text():
    text = font_disp.render("SOLVED SUCCESSFULLY!!", True, (0, 255, 0))
    screen.blit(text, (60, 590))
    
def clear(grid):
    '''
    clears the grid
    '''
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                grid[i][j] = 0
                
def main():    
    
    x, y = 0, 0          # mouse position
    value = 0            # value entered by user on board
    running = True       # to check game loop
    auto_solve = False   # to check auto solving
    wrong_value = False  # flag to print error message for entering wrong value 
    result = False       # flag to print text on solving board
    game_ins = False     # flag to print instructions on resetting the board
    grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    
    while running:
        
        pygame.display.set_caption("Sudoku Solver")
        screen.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: 
                    x += 1
                if event.key == pygame.K_LEFT:
                    x -= 1
                if event.key == pygame.K_UP:
                    y -= 1
                if event.key == pygame.K_DOWN:
                    y += 1
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    value = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    value = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    value = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    value = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    value = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    value = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    value = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    value = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    value = 9
                if event.key == pygame.K_RETURN:
                    auto_solve = True
                if event.key == pygame.K_c:
                    clear(grid)
                if event.key == pygame.K_r:
                    auto_solve = False
                    wrong_value = False
                    result = False
                    game_ins = True
                    grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]]
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos() 
                
                # ensuring orange box is drawn within the grid
                # since a offset of 30 pixels is used
                clicked = ((x - 30) // 60, (y - 30) // 60)
                x, y = clicked
              
                
        if auto_solve:
            if solve(grid):
                result = True
            auto_solve = False
        
        # y, x → row, col
        if value != 0 and grid[y][x] == 0:
            if is_valid_num(grid, value, y, x):
                grid[y][x] = value
            else:
                grid[y][x] = 0
                wrong_value = True
            value = 0
        
        if result:
            solve_text()
       
        if wrong_value and not result and not game_ins:
            wrong_num()
        print_num(grid)
        draw_grid()
        draw_box(x,y)
        
        if not wrong_value and not result or game_ins: 
            game_instructions()
            game_ins = False
        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()