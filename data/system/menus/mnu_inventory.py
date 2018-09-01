import pygame
from data.dta_constants import *
from data.system.sys_window import *
class Mnu_Inventory:
    def __init__(self):
        self.font = pygame.font.SysFont(FONT_15[0],FONT_15[1],1)
        self.displays = {
            "Stats" : None,
            "Equipment" : None,
            "Invetory" : None,
            "Combat" : None,
            "Talent" : None
        }
        self.canvas = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.canvas_alpha = INVENTORY_ALPHA
        self.windows = {
            "Stats" : Sys_Window(WINDOWS["Stats"][0],WINDOWS["Stats"][1]),
            "Status" : Sys_Window(WINDOWS["Status"][0],WINDOWS["Status"][1])
        }

    def status_win_render(self, surface, system):
        # Acortadores:
        actor = system.player.actor
        status = system.player.stats["Status"]

        self.windows["Status"].box_render()
        x, y = 280, 0
        label_render = self.font.render("| Status |",False,COLORS["White"],COLORS["Black"])
        self.windows["Status"].canvas.blit(label_render,(x,y))
        x, y = 20, 15
        text = status["Health"]["Label"]+": "+str(actor.health_points)+"/"+str(status["Health"]["Points"])
        text_render = self.font.render(text,False,COLORS["Yellow"],COLORS["Black"])
        self.windows["Status"].canvas.blit(text_render,(x,y))
        x, y = 120, 15
        text = "Hit -> "+str(actor.hit_points)
        text_render = self.font.render(text,False,COLORS["Yellow"],COLORS["Black"])
        self.windows["Status"].canvas.blit(text_render,(x,y))
        x, y = 200, 15
        text = "Def -> "+str(actor.defense_points)
        text_render = self.font.render(text,False,COLORS["Yellow"],COLORS["Black"])
        self.windows["Status"].canvas.blit(text_render,(x,y))
        
        self.windows["Status"].render(surface)

    def stats_win_render(self, surface, system):
        self.windows["Stats"].box_render()
        x, y = 20, 0
        current_stat = 0
        label_render = self.font.render("| Attribute |",False,COLORS["White"],COLORS["Black"])
        label_height = label_render.get_height()
        self.windows["Stats"].canvas.blit(label_render,(x,y+label_height*current_stat))
        for stat in system.player.stats["Attribute"]:
            label = system.player.stats["Attribute"][stat]
            label_render = self.font.render(label["Label"],False,COLORS["Yellow"])
            points_render = self.font.render("-> "+str(label["Points"]),False,COLORS["Yellow"])
            label_height = label_render.get_height()
            current_stat += 1
            self.windows["Stats"].canvas.blit(label_render,(x,y+label_height*current_stat))
            self.windows["Stats"].canvas.blit(points_render,(x+35,y+label_height*current_stat))
        self.windows["Stats"].render(surface)
    # def stats_render(self, system):
    #     x, y = 100, 50
    #     current_stat = 0
    #     label_render = self.font.render("Attribute",False,self.font_color)
    #     label_height = label_render.get_height()
    #     self.canvas.blit(label_render,(x,y+label_height*current_stat))
    #     for stat in system.player.stats["Attribute"]:
    #         label_render = self.font.render(stat,False,self.font_color)
    #         label_height = label_render.get_height()
    #         current_stat += 1
    #         self.canvas.blit(label_render,(x,y+label_height*current_stat))
            

    def all_render(self, surface, system):
        # self.canvas.fill(BACKGROUND_COLOR)
        self.status_win_render(surface,system)
        self.stats_win_render(surface,system)
        # self.canvas.set_alpha(self.canvas_alpha)