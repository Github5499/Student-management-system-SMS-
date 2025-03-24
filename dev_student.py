from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineIconListItem,TwoLineIconListItem,TwoLineAvatarIconListItem,ThreeLineAvatarIconListItem,IconLeftWidget, IconRightWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.tab import MDTabsBase
#from kivymd.uix.separator import MDSeparator
from kivymd.uix.button import MDRaisedButton,MDFloatingActionButton,MDIconButton,MDRectangleFlatIconButton, MDFillRoundFlatIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
import time
import threading
import socket
import random
import json
import os
from kivymd.uix.pickers import MDDatePicker
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window
from jnius import autoclass
import inspect
import asyncio
import kivymd 
from kivymd.utils import asynckivy
from kivy.config import Config
from kivymd.toast import toast
Config.set('kivy', 'keyboard_mode', 'multi')
#import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton


KV='''
MDNavigationLayout:  
    MDScreenManager:
        id:sm
        MDScreen:
            name:'MainScreen'

            MDBottomNavigation:
                id: btab
                panel_color:0.2647,0.4922,0.6765,1
                text_color_normal:0,0,0,1
                text_color_active:0,0,0,1
                radius:[0,0,0,0]
                selected_color_background:app.theme_cls.primary_color
                
                MDBottomNavigationItem:
                    name: 'homescreen'
                    text: 'Students'
                    icon: 'account-school'
                    
                    MDScreenManager:
                        id:home_screenmanager
                        MDScreen:
                            name: 'home_menu_screen'
                            MDBoxLayout:
                                orientation: 'vertical'
                                MDCard:
                                    orientation:'vertical'
                                    size_hint:1,None
                                    height:self.minimum_height
                                    radius:[0,0,0,0]
                                    padding: [20,10,20,10]
                                    md_bg_color:app.theme_cls.primary_color
                                    
                                    MDCard:
                                        orientation:'horizontal'
                                        size_hint:1,None
                                        height:self.minimum_height
                                        radius:[40,40,40,40]
                                        padding: [0,0,0,0]
                                        md_bg_color:0.2647,0.4922,0.6765,1
                                        MDTextField :
                                            hint_text:'Search students'
                                            icon_left: 'magnify'
                                            mode:'round'
                                            md_bg_color_normal: [0,0,1,1]
                                            theme_text_color:'Custom'
                                            text_color:0,0,0,1
                                            text_color_normal:0,0,0,1
                                            text_color_focus:0,0,0,1
                                            hint_text_color_normal:0,0,0,1
                                            icon_left_color_normal :0,0,0,1
                                            icon_left_color_focus:0,0,0,1
                                            fill_color_normal: 0,0,1,0
                                            fill_color_focus:0,0,1,0
                                            line_color_normal:0,0,1,0
                                            line_color_focus:0,0,1,0
                                            pos_hint:{'center_x':0.5,'center_y':0.5}
                                            on_text_validate:app.search_student(self.text)
                                        
                                        MDIconButton:
                                            icon: 'microphone-outline'
                                            theme_icon_color:'Custom'
                                            icon_color:0,0,0,1
                                        
                                        MDIconButton:
                                            icon:'dots-vertical'
                                            theme_icon_color:'Custom'
                                            icon_color: 0,0,0,1
                                            on_release:nav_bar.set_state('open')
                                        
                                    
                                MDCard :
                                    orientatio : 'vertical'
                                    radius:[0]
                                    padding: [0,10,0,0]
                                    spacing:10
                                    md_bg_color:app.theme_cls.primary_color
                                    MDScrollView:
                                        effect_cls:'ScrollEffect'
                                        adaptive_height:True
                                        MDCard:
                                            id: homelst
                                            orientation: 'vertical'
                                            spacing:20
                                            padding:[26,10,26,10]
                                            radius:[0]
                                            elevation:0
                                            size_hint:1,None
                                            md_bg_color:0.7,0,0,0
                                            height:self.minimum_height
                                MDRelativeLayout:
                                    size_hint:1,0.0001
                                    md_bg_color:1,0,0,0
                                    MDCard:
                                        orientation: 'vertical'
                                        padding:[0,0,0,60]
                                        pos_hint:{'center_x':0.80}
                                        md_bg_color:0,0,0,0
                                        size_hint:None,None
                                        width:'10sp'
                                        height:'10sp'
                                        MDFloatingActionButton:
                                            icon : 'account-plus'
                                            md_bg_color:0.2647,0.4922,0.6765,1
                                            elevation:1.4
                                            _no_ripple_effect:True
                                            on_press:home_screenmanager.current='home_addmission_screen'
                                


                        MDScreen:
                            name: 'home_addmission_screen'
                            on_enter: student_2.scroll_y=1
                            MDBoxLayout:
                                orientation: 'vertical'
                                MDBoxLayout:
                                    orientation : 'vertical'
                                    MDTopAppBar :
                                        title: 'Candidate Information '
                                        md_bg_color:0.2647,0.4922,0.6765,1
                                        left_action_items: [["arrow-left", lambda x:app.addmission_screen()]]
                                        right_action_items: [["window-close", lambda x:app.cancel_confirmation()],["check-all", lambda x:app.submit_form()]]
                                        
                                    MDScrollView:
                                        id: student_2
                                        effect_cls:'ScrollEffect'
                                        adaptive_height:True
                                        MDCard:
                                            orientation: 'vertical'
                                            spacing:30
                                            padding:[40,10,10,10]
                                            radius:[0]
                                            size_hint:1,None
                                            height:self.minimum_height
                                            md_bg_color:app.theme_cls.primary_color
                                            MDLabel :
                                                text:'~Persnal, Academic, Residential~'
                                                adaptive_size:True
                                                font_size:'25sp'
                                                theme_text_color:'Custom'
                                                text_color:0.2647,0.4922,0.6765,1
                                            MDTextField:
                                                id: first_name
                                                mode:'rectangle'
                                                do_space:False
                                                hint_text:'First Name'
                                                icon_left:'account'
                                                max_text_length:8
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                error_color: 1,0,0,1
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                            MDTextField:
                                                id: last_name
                                                hint_text:'Last Name'
                                                icon_left:'account-circle'
                                                max_text_length:8
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                error_color: 1,0,0,1
                                                mode:'rectangle'
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                            MDTextField:
                                                id: father_name
                                                hint_text:'Father Name'
                                                icon_left:'human-male'
                                                max_text_length:16
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                error_color: 1,0,0,1
                                                mode:'rectangle'
                                                #pos_hint:{'center_x':0.5,'center_y':0.5}
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                            MDTextField:
                                                id: mother_name
                                                hint_text:'Mother Name'
                                                icon_left:'human-female'
                                                max_text_length:16
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                error_color: 1,0,0,1
                                                mode:'rectangle'
                                               # pos_hint:{'center_x':0.5,'center_y':0.5}
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                            MDBoxLayout:
                                                orientation :'horizontal'
                                                size_hint:0.9,None
                                                height:self.minimum_height
                                                spacing: 10
                                                md_bg_color:0,0,0,0.0
                                                #pos_hint:{'center_x':0.5,'center_y':0.5}
                                                MDTextField:
                                                    id:dob
                                                    mode: 'rectangle'
                                                    icon_left: 'calendar-account'
                                                    hint_text:'Date Of Birth' 
                                                    font_size:'23sp'
                                                    readonly:True
                                                    helper_text:'click on the calendar icon to set up DOB'
                                                    helper_text_mode: 'persistent'
                                                    #theme_text_color:'ContrastParentBavkground'
                                                    helper_text_color_normal:0,0,0.01,1
                                                    hint_text_color_normal:0,0,0,1
                                                    hint_text_color_focus:0,0,0,1
                                                    text_color_normal:0,0,0,1
                                                    text_color_focus:0,0,0,1
                                                    icon_left_color_normal:0,0,0,1
                                                    icon_left_color_focus:0,0,0,1
                                                    line_color_normal:0,0,0,1
                                                    line_color_focus:0,0,0,1
                                                    md_bg_color:1,0,0,1
                                                MDIconButton:
                                                    icon:'calendar-month'
                                                    theme_icon_color:'Custom'
                                                    icon_color:0,0,0,1
                                                    on_release:app.dob()
                                                    pos_hint:{'center_x':0.5,'center_y':0.5}
                                            
                                            MDTextField :
                                                id:aadhaar
                                                icon_left:'id-card'
                                                mode: 'rectangle'
                                                hint_text:'Aadhaar number'
                                                helper_text:'Please fill correct number '
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                input_filter:'int'
                                                #pos_hint:{'center_x':0.5,'center_y':0.5}
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                            
                                            MDTextField :
                                                id: phone
                                                icon_left:'phone'
                                                mode: 'rectangle'
                                                hint_text:'phone number'
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                input_filter:'int'
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                                
                                            MDTextField :
                                                id: address 
                                                icon_left:'home-map-marker'
                                                mode: 'rectangle'
                                                hint_text:'Full Address'
                                                size_hint_x:0.9
                                                font_size:'24sp'
                                                hint_text_color_normal:0,0,0,1
                                                hint_text_color_focus:0,0,0,1
                                                text_color_normal:0,0,0,1
                                                text_color_focus:0,0,0,1
                                                icon_left_color_normal:0,0,0,1
                                                icon_left_color_focus:0,0,0,1
                                                line_color_normal:0,0,0,1
                                                line_color_focus:0,0,0,1
                                                md_bg_color:1,0,0,1
                                                
                                            MDCard :
                                                padding: [0,0,0,0]
                                                orientation :'vertical'
                                                size_hint:1,None
                                                height:self.minimum_height
                                                spacing: 30
                                                md_bg_color:0,0,0,0
                                                MDCard:
                                                    padding: [0,0,0,0]
                                                    orientation :'vertical'
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    spacing: 10
                                                    md_bg_color:0,0,0,0
                                                    MDBoxLayout:
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 10
                                                        md_bg_color:0,0,0,0.0
                                                        MDLabel:
                                                            text:'Gender :'
                                                            adaptive_size:True
                                                            font_size:'23sp'
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                                            pos_hint:{'center_x':0.5,'center_y':0.5}
                                                    MDCard :
                                                        padding: [56,0,0,0]
                                                        orientation :'vertical'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 10
                                                        md_bg_color:0,0,0,0
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'gender'
                                                                adaptive_size:True
                                                                active:True
                                                                on_active: app.gender='male'
                                                            MDLabel:
                                                                text:'Male'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                        MDCard :
                                                            padding: [00,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'gender'
                                                                adaptive_size:True
                                                                on_active: app.gender='female'
                                                            MDLabel:
                                                                text:'Female'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'gender'
                                                                adaptive_size:True
                                                                on_active: app.gender='other'
                                                            MDLabel:
                                                                text:'Other'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                MDCard:
                                                    padding: [0,0,0,0]
                                                    orientation :'vertical'
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    spacing: 10
                                                    md_bg_color:0,0,0,0
                                                    MDBoxLayout:
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 10
                                                        MDLabel:
                                                            text:'Nationality :'
                                                            adaptive_size:True
                                                            font_size:'23sp'
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                                            pos_hint:{'center_x':0.5,'center_y':0.5}
                                                    MDCard :
                                                        padding: [56,0,0,0]
                                                        orientation :'vertical'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 10
                                                        md_bg_color:0,0,0,0
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'natinality'
                                                                adaptive_size:True
                                                                active:True
                                                                on_active: app.natinality='indian'
                                                            MDLabel:
                                                                text:'Indian'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'natinality'
                                                                adaptive_size:True
                                                                on_active: app.natinality='other'
                                                            MDLabel:
                                                                text:'Other'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                MDCard:
                                                    padding: [0,0,0,0]
                                                    orientation :'vertical'
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    spacing: 10
                                                    md_bg_color:0,0,0,0
                                                    MDBoxLayout:
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 10
                                                        MDLabel:
                                                            text:'Catagory :'
                                                            adaptive_size:True
                                                            font_size:'23sp'
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                                            pos_hint:{'center_x':0.5,'center_y':0.5}
                                                    MDCard :
                                                        padding: [56,0,0,0]
                                                        orientation :'vertical'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 10
                                                        md_bg_color:0,0,0,0
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'catagory'
                                                                adaptive_size:True
                                                                on_active: app.catagory='OBC'
                                                            MDLabel:
                                                                text:'OBC'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'catagory'
                                                                adaptive_size:True
                                                                on_active: app.catagory='SC/NT'
                                                            MDLabel:
                                                                text:'SC/NT'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                        MDCard :
                                                            padding: [0,0,0,0]
                                                            orientation :'horizontal'
                                                            size_hint:1,None
                                                            height:self.minimum_height
                                                            spacing: 10
                                                            md_bg_color:0,0,0,0
                                                            MDCheckbox:
                                                                group: 'catagory'
                                                                adaptive_size:True
                                                                active:True
                                                                on_active: app.catagory='open'
                                                            MDLabel:
                                                                text:'open'
                                                                adaptive_size:True
                                                                theme_text_color:'Custom'
                                                                text_color:0,0,0,1
                                                
                                            MDCard:
                                                orientation :'horizontal'
                                                size_hint:None,None
                                                height:'55sp'
                                                width:'150sp'
                                                padding :[0]
                                                spacing:10
                                                elevation :0
                                                md_bg_color:1,0.5,0.7,0
                                                MDLabel:
                                                    text:'Class :'
                                                    font_size:'23sp'
                                                    adaptive_size:True
                                                    theme_text_color:'Custom'
                                                    text_color:0,0,0,1
                                                    pos_hint:{'center_x':0.5,'center_y':0.5}
                                                MDCard:
                                                    padding: [10]
                                                    spacing: 8
                                                    orientation: 'horizontal'
                                                    size_hint:None,None
                                                    height: self.minimum_height
                                                    width: '150sp'
                                                    md_bg_color:0,0,0,0
                                                    pos_hint:{'center_x':0.5,'center_y':0.5}
                                                    MDCard :
                                                        padding: [0,0,0,0]
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 4
                                                        md_bg_color:0,0,0,0
                                                        MDCheckbox:
                                                            group: 'class'
                                                            adaptive_size:True
                                                            active:True
                                                            on_active: app._class='11th'
                                                        MDLabel:
                                                            text:'11th'
                                                            adaptive_size:True
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                                    MDCard :
                                                        padding: [0,0,0,0]
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 4
                                                        md_bg_color:0,0,0,0
                                                        MDCheckbox:
                                                            group: 'class'
                                                            adaptive_size:True
                                                            on_active: app._class='12th'
                                                        MDLabel:
                                                            text:'12th'
                                                            adaptive_size:True
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                            MDCard:
                                                orientation :'horizontal'
                                                size_hint:1,None
                                                height:'55sp'
                                                padding :[0]
                                                spacing:10
                                                elevation :0
                                                md_bg_color:1,0.5,0.7,0
                                                MDLabel:
                                                    text:'Stream :'
                                                    font_size:'23sp'
                                                    adaptive_size:True
                                                    theme_text_color:'Custom'
                                                    text_color:0,0,0,1
                                                    pos_hint:{'center_x':0.5,'center_y':0.5}
                                                MDCard:
                                                    padding: [10]
                                                    spacing: 9
                                                    orientation: 'horizontal'
                                                    size_hint:None,None
                                                    height: self.minimum_height
                                                    width: '350sp'
                                                    md_bg_color:0,0,0,0
                                                    pos_hint:{'center_x':0.5,'center_y':0.5}
                                                    MDCard :
                                                        padding: [0,0,0,0]
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 5
                                                        md_bg_color:0,0,0,0
                                                        MDCheckbox:
                                                            group: 'stream'
                                                            adaptive_size:True
                                                            active:True
                                                            on_active: app.stream='science'
                                                        MDLabel:
                                                            text:'Science'
                                                            adaptive_size:True
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                                    MDCard :
                                                        padding: [0,0,0,0]
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 5
                                                        md_bg_color:0,0,0,0
                                                        MDCheckbox:
                                                            group: 'stream'
                                                            adaptive_size:True
                                                            on_active: app.stream='commerce'
                                                        MDLabel:
                                                            text:'Commerce'
                                                            adaptive_size:True
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                                                    MDCard :
                                                        padding: [0,0,0,0]
                                                        orientation :'horizontal'
                                                        size_hint:1,None
                                                        height:self.minimum_height
                                                        spacing: 5
                                                        md_bg_color:0,0,0,0
                                                        MDCheckbox:
                                                            group: 'stream'
                                                            adaptive_size:True
                                                            on_active: app.stream='arts'
                                                        MDLabel:
                                                            text:'Arts'
                                                            adaptive_size:True
                                                            theme_text_color:'Custom'
                                                            text_color:0,0,0,1
                        MDScreen:
                            name: 'home_information_screen'
                            on_enter: student.scroll_y=1
                            MDBoxLayout:
                                orientation: 'vertical'
                                MDBoxLayout:
                                    orientation : 'vertical'
                                    md_bg_color:app.theme_cls.primary_color
                                    MDTopAppBar :
                                        id: heading
                                        title: 'student details'
                                        md_bg_color:0.2647,0.4922,0.6765,1
                                        left_action_items: [["window-close", lambda x:app.addmission_screen()]]
                                        right_action_items: [["account-edit", lambda x :app.correction()], ["trash-can", lambda x:app.del_student()]]
                                        
                                    MDScrollView:
                                        id: student
                                        effect_cls:'ScrollEffect'
                                        adaptive_height:True
                                        MDCard:
                                            orientation: 'vertical'
                                            spacing:0
                                            padding:[40,10,40,10]
                                            radius:[0]
                                            size_hint:1,None
                                            height:self.minimum_height
                                            md_bg_color:app.theme_cls.primary_color
                                            MDCard:
                                                orientation: 'vertical'
                                                spacing:0
                                                padding:[4,4,2,2]
                                                radius:[0]
                                                size_hint:1,None
                                                height:self.minimum_height
                                                md_bg_color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Name : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_name
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Father : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_father_name
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Mother Name : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_mother_name
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Date of Birth: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_dob
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Gender: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_gender
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Nationality : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_nationality
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Catagory: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_catagory
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Aadhaar : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_aadhaar
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Registration No: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_rgtn_no
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                        
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Registration Date: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_rgtn_date
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Class : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_class
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Roll No : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_roll_no
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Subjects: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_subjects
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Phone : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_phone
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Address : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: student_address
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                        MDScreen:
                            name: 'home_correction_screen'
                            on_enter: crr_student.scroll_y=1
                            MDBoxLayout:
                                orientation : 'vertical'
                                MDBoxLayout :
                                    orientation :'vertical' 
                                    md_bg_color:app.theme_cls.primary_color
                                    MDTopAppBar :
                                        id: heading_crr
                                        title: 'update details'
                                        md_bg_color:0.2647,0.4922,0.6765,1
                                        left_action_items: [["window-close", lambda x:app.addmission_screen()]]
                                        right_action_items: [["check-bold", lambda x: app.lam()]]
                                            
                                    MDScrollView:
                                        id: crr_student
                                        effect_cls:'ScrollEffect'
                                        adaptive_height:True
                                        MDCard:
                                            orientation: 'vertical'
                                            spacing:0
                                            padding:[40,10,40,10]
                                            radius:[0]
                                            size_hint:1,None
                                            height:self.minimum_height
                                            md_bg_color:app.theme_cls.primary_color
                                            MDCard:
                                                orientation: 'vertical'
                                                spacing:0
                                                padding:[4,4,2,2]
                                                radius:[0]
                                                size_hint:1,None
                                                height:self.minimum_height
                                                md_bg_color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'First Name : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_first_name
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Last Name : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_last_name
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Father : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_father_name
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Mother Name : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_mother_name
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Date of Birth: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_dob
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDIconButton:
                                                        icon:'calendar-month'
                                                        theme_icon_color:'Custom'
                                                        icon_color:0,0,0,1
                                                        pos_hint:{'center_y':0.5}
                                                        on_release:app.dob()
                                                        pos_hint:{'center_x':0.5,'center_y':0.5}
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Gender: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        pos_hint:{'center_y':0.5}
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_gender
                                                        text:'' 
                                                        adaptive_size:True
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Nationality : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_nationality
                                                        text:''
                                                        pos_hint:{'center_y':0.5}
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Catagory: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_catagory
                                                        text:'' 
                                                        adaptive_size:True
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Aadhaar : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_aadhaar
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        max_text_length:16
                                                        input_type:'number'
                                                        input_filter:'int'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Registration No: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_rgtn_no
                                                        text:'' 
                                                        pos_hint:{'center_y':0.5}
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                        
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Registration Date: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        pos_hint:{'center_y':0.5}
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_rgtn_date
                                                        text:'' 
                                                        pos_hint:{'center_y':0.5}
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Class : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_class
                                                        text:'' 
                                                        adaptive_size:True
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Stream : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_stream
                                                        text:'' 
                                                        pos_hint:{'center_y':0.5}
                                                        adaptive_size:True
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Roll No : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        pos_hint:{'center_y':0.5}
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_roll_no
                                                        text:'' 
                                                        adaptive_size:True
                                                        padding :[0]
                                                        pos_hint:{'center_y':0.5}
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                        
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                    
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Core Subjects: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_core_subjects
                                                        text:''
                                                        adaptive_size:True
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Optional Subjects: ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDLabel:
                                                        id: crr_student_optional_subjects
                                                        text:''
                                                        adaptive_size:True
                                                        size_hint_x: None
                                                        width: 300
                                                        pos_hint:{'center_y':0.5}
                                                        text_size: self.width, None
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Phone : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        pos_hint:{'center_y':0.5}
                                                        font_size: '20sp'
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_phone
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        max_text_length:10
                                                        input_type:'number'
                                                        input_filter:'int'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color
                                                MDSeparator :
                                                    color: 0,0,0,1
                                                MDCard:
                                                    orientation: 'horizontal'
                                                    spacing:30
                                                    padding:[10,10,10,10]
                                                    radius:[0]
                                                    size_hint:1,None
                                                    height:self.minimum_height
                                                    md_bg_color:app.theme_cls.primary_color
                                                    MDLabel:
                                                        text:'Address : ' 
                                                        adaptive_size:True
                                                        font_name:'SourceSansPro-SemiBold.ttf'
                                                        font_size: '20sp'
                                                        pos_hint:{'center_y':0.5}
                                                        padding :[0]
                                                        theme_text_color:'Custom'
                                                        text_color: 0,0,0,1
                                                    MDTextField:
                                                        id: crr_student_address
                                                        icon_right:'square-edit-outline'
                                                        size_hint_x:0.9
                                                        font_size:'24sp'
                                                        pos_hint:{'center_y':0.5}
                                                        hint_text_color_focus:0,0,0,1
                                                        text_color_normal:0,0,0,1
                                                        text_color_focus:0,0,0,1
                                                        icon_right_color_normal:0,0,0,1
                                                        icon_right_color_focus:0,0,0,1
                                                        line_color_normal: app.theme_cls.primary_color
                                                        line_color_focus: app.theme_cls.primary_color

                MDBottomNavigationItem:
                    name: 'members'
                    text: 'Members'
                    icon: 'account-group'
                    MDBoxLayout:
                        orientation: 'vertical'


                MDBottomNavigationItem:
                    name: 'documents'
                    text: 'Documents'
                    icon: 'folder-multiple'
                    MDBoxLayout:
                        orientation: 'vertical'


    MDNavigationDrawer:
        id:nav_bar
        swipe_distance:50
        orientation :'vertical'
        md_bg_color:app.theme_cls.primary_color
        MDNavigationDrawerHeader:
            title: "Header title"
            title_color: "#4a4939"
            text: "Header text"
            spacing: "4dp"
            padding: "12dp", 0, 0, "56dp"
        MDBoxLayout:
            orientation: 'vertical'
            MDIconButton:
                icon:'star'
                pos_hint:{'center_x':0.5,'center_y':0.5}
                on_release:app.theme_cls.theme_style = "Light" 
                    
'''


if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    ActivityInfo = autoclass('android.content.pm.ActivityInfo')
    
    # Function to lock the orientation
    @run_on_ui_thread
    def lock_orientation():
        activity = PythonActivity.mActivity
        activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT)  # Portrait mode
        # For landscape, use ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE

    #PythonActivity = autoclass('org.kivy.android.PythonActivity')
    View = autoclass('android.view.View')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    ActivityInfo = autoclass('android.content.pm.ActivityInfo')

    @run_on_ui_thread
    def hide_navigation_bar():
        # Gets the current Android activity and decor view
        activity = PythonActivity.mActivity
        decor_view = activity.getWindow().getDecorView()
        # Hides the navigation and status bar
        decor_view.setSystemUiVisibility(
            View.SYSTEM_UI_FLAG_LAYOUT_STABLE
            | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_FULLSCREEN
            | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
        )

             

    # NOTIFICATION ON DEVICE
    @run_on_ui_thread
    def notification( hadding, mssg):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Context = autoclass('android.content.Context')
        NotificationManager = autoclass('android.app.NotificationManager')
        NotificationChannel = autoclass('android.app.NotificationChannel')
        NotificationBuilder = autoclass('android.app.Notification$Builder')

        activity = PythonActivity.mActivity
        notification_service = activity.getSystemService(Context.NOTIFICATION_SERVICE)

        # Android 8.0+ requires a Notification Channel
        channel_id = "my_channel_id"
        if notification_service.getNotificationChannel(channel_id) is None:
            channel = NotificationChannel(channel_id, "My Channel", NotificationManager.IMPORTANCE_DEFAULT)
            notification_service.createNotificationChannel(channel)

        # Create the notification
        notification = NotificationBuilder(activity, channel_id)
        notification.setContentTitle(hadding)
        notification.setContentText(mssg)
        notification.setSmallIcon(activity.getApplicationInfo().icon)

        # Send the notification
        notification_service.notify(1, notification.build())


class SMS :
    def __init__(self):
        self.__student=[]
        self.__all_11th_s=0
        self.__11th_science_s=0
        self.__11th_commerce_s=0
        self.__11th_arts_s=0
        self.__all_12th_s=0
        self.__12th_science_s=0
        self.__12th_commerce_s=0
        self.__12th_arts_s=0
        self.__all_s=0
        self.__rgtn_no=0
        self.__roll_no=0
        #try :
    def update_file(self):#the method for updating file
        self.__all_11th_s=0
        self.__11th_science_s=0
        self.__11th_commerce_s=0
        self.__11th_arts_s=0
        self.__all_12th_s=0
        self.__12th_science_s=0
        self.__12th_commerce_s=0
        self.__12th_arts_s=0
        self.__all_s=0
        self.__rgtn_no=0
        try:
            with open('database.json', 'r') as file :
                data=json.load(file)
            for i in data:
                if i['class']=='11th':
                    self.__all_11th_s+=1
                    if i['stream']=='science':
                        self.__11th_science_s+=1
                    elif i['stream']=='commerce':
                        self.__11th_commerce_s+=1
                    else:
                        self.__11th_arts_s+=1             
                else:
                    self.__all_12th_s+=1
                    if i['stream']=='science':
                        self.__12th_science_s+=1
                    elif i['stream']=='commerce':
                        self.__12th_commerce_s+=1
                    else:
                        self.__12th_arts_s+1
        except :
            self.__rgtn_no=1
            print('no student available(update_file)')

        self.__all_s=self.__all_11th_s+self.__all_12th_s
        self.__rgtn_no=self.__all_s+1
 
        register={
                'all_11th_s':self.__all_11th_s,
                '11th_science_s':self.__11th_science_s,
                '11th_commerce_s':self.__11th_commerce_s,
                '11th_arts_s':self.__11th_arts_s,
                'all_12th_s':self.__all_12th_s,
                '12th_science_s':self.__12th_science_s,
                '2th_commerce_s':self.__12th_commerce_s,
                '12th_arts_s':self.__12th_arts_s,
                'all_s':self.__all_s,
            }
        with open('ragister.json','w') as pg:
            json.dump(register, pg, indent=4)
    
    def get_rgtn(self):# it is  gives registration number for students 
        self.update_file()
        return self.__rgtn_no
    
    def get_roll_no(self,stream, _class): #this method update the self.__roll_no and return it 
        self.update_file()
        self.__roll_no=1
        try :
            with open('database.json','r') as file:
                list=json.load(file)
            if _class=='11th':
                if stream=='science':
                    self.__roll_no=self.__11th_science_s+1
                elif stream=='commerce':
                    core_subject=['accountancy','business Studies','economics','english']
                    self.__roll_no=self.__11th_commerce_s+1
                else:
                    self.__roll_no=self.__11th_arts_s+1
                    core_subject=['history','political science', 'geography', 'socialogy','psychology', 'economics','english']
            else:
                if stream=='science':
                    self.__roll_no=self.__12th_science_s+1
                elif stream=='commerce':
                    self.__roll_no=self.__12th_commerce_s+1
                else:
                    self.__roll_no=self.__12th_arts_s+1
            return f'{self.__roll_no}'
        except :
            return f'{self.__roll_no}'
        
    def addmission(self,first_name='student default',last_name='candidate last name',father_name='student father',mother_name='student mother',dob='25-08-2007', gender='male', nationality='indian', catagory='open', aadhaar='1234567890',_class='11th', stream='science', phone='9360544302', address='kurankhed'):#this is the main method to admit student in college
        core_subject=[]
        optional_subject=[]
        if stream=='science':
            core_subject=['P,C,M,B']
            optional_subject=['computer science','information technology','graphics engineering']
        elif stream=='commerce':
            core_subject=['A,B, E, E']
            optional_subject=['mathematics', 'informatics practices','entrepreneurship','physical education']
        else:
            core_subject=['H, P, G,S, P, E,E']
            optional_subject=['hindi','physical education', 'fine arts', 'home science']
        self.update_file()
        self.get_roll_no(stream, _class)
        t=time.localtime()
        f_time=time.strftime('%Y-%m-%d %H:%M:%S',t)
        new_student={
                'first name': first_name,
                'last name' : last_name,
                'father name' : father_name,
                'mother name' : mother_name,
                'rgtn no':self.__rgtn_no,
                'dob': dob,
                'gender': gender,
                'nationality': nationality,
                'catagory': catagory,
                'aadhaar' : aadhaar,
                'class': _class,
                'roll no': self.__roll_no,
                'stream': stream,
                'core subject': core_subject,
                'optional subject': optional_subject,
                'phone': phone,
                'address': address,
                'time' : f_time
                }
        try :
            with open('database.json', 'r') as file:
                list=json.load(file)
                
            list.append(new_student)
            
            with open('database.json','w') as f:
                json.dump(list, f, indent=4)
            toast        ('student details loaded in file successfully.')
            self.update_file()
        except :
            self.update_file()
            lst=[]
            lst.append(new_student)
            with open('database.json','w') as f:
                    json.dump(lst, f, indent=4)
            self.update_file()
            toast(f'Student {first_name} {last_name} admitted successfully')
        return notification(' Congratulation!',f'Student {first_name} {last_name} admitted successfully')
        

    def correction(self,rgtn_no):#this is the method to correction in student details 
        pass


    def leave(self,rgtn_no='',aadhaar='962331667212'):#this is a method to delete a student from collage 
        toast(f'stufent with Registration No: {rgtn_no} has been deleted.')
        try:
            with open('database.json', 'r') as file :
                data=json.load(file)
        except :
            MDDialog(title='No available student.'). open()
        try :
            new_data=[i for i in data if i['rgtn no']!=rgtn_no]
            with open('database.json', 'w') as new_file:
                json.dump(new_data, new_file, indent=4)
                notification('Leaved',f'the student with Registration number {rgtn_no} has  leaved successfully.')
        except Exception as e :
            MDDialog(title=f'error in leave method {e}')
        #self.home_list()
 
    def all_student(self):# it is return all students list available in the college 
        try :
            with open('database.json','r') as file:
                data=json.load(file)
            return data
        except :
            return 'No students available.'
    
    
        
class Main_Screen(Screen):
    pass

class myapp(MDApp, SMS):
    first_name='default f_name'
    last_name='default l_name'
    father_name='default father_n'
    mother_name='default mother_n'
    dob='25-08-2007'
    gender='male'
    nationality='indian'
    catagory='open'
    aadhaar='694882001639'
    _class='11th'
    stream='science'
    address='katipurna'
    phone='9022821262'
    dialog=None
    dict={
        'name': [],
        'rgtn': [],
        'tm': []
        }
    current_screen=None
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue='100'
        self.theme_cls.theme_style = "Dark"
        if platform == 'android':
            hide_navigation_bar()
          #  lock_orientation() implement a button for setting orientation in future      
        return Builder.load_string(KV)
    
    def on_start(self):
        self.home_list()
    
    def submit_form(self):
        self.dialog=MDDialog(
        title='Comfirmation',
        text=f'Roll Number: {self.get_roll_no(self.stream, self._class)}\nRegisteration Number: {self.get_rgtn()}',
        buttons=[
        
            MDFillRoundFlatIconButton(icon='arrow-left', text='Back',on_release=lambda x:self.dialog.dismiss()),
            MDFillRoundFlatIconButton(icon='check', text='Done',on_release=lambda x:(self.confirm(),self.dialog.dismiss()))
            
                ]
        )
        self.dialog.open()

    def confirm(self):
        self.addmission(f'{self.root.ids.first_name.text}',f'{self.root.ids.last_name.text}',f'{self.root.ids.father_name.text}',f'{self.root.ids.mother_name.text}',f'{self.root.ids.dob.text}',f'{self.gender}', f'{self.nationality}',f'{self.catagory}',f'{self.root.ids.aadhaar.text}',f'{self._class}',f'{self.stream}', f'{self.root.ids.phone.text}',f'{self.root.ids.address.text}')
        t=time.localtime()
        f_time=time.strftime('%Y-%m-%d %H:%M:%S',t)
        rgtn= int(self.get_rgtn())-1
        self.func2(self.root.ids.first_name.text,rgtn, f_time)
        self.root.ids.first_name.text=''
        self.root.ids.last_name.text=''
        self.root.ids.father_name.text=''
        self.root.ids.mother_name.text=''
        self.root.ids.dob.text=''
        self.gender='male'
        self.nationality='indian'
        self.catagory='open'
        self.root.ids.aadhaar.text=''
        self._class='11th'
        self.root.ids.phone.text=''
        self.root.ids.address.text=''
        
    def cancel(self):
        self.root.ids.first_name.text=''
        self.root.ids.last_name.text=''
        self.root.ids.father_name.text=''
        self.root.ids.mother_name.text=''
        self.root.ids.dob.text=''
        self.gender='male'
        self.nationality='indian'
        self.catagory='open'
        self.root.ids.aadhaar.text=''
        self._class='11th'
        self.root.ids.phone.text=''
        self.root.ids.address.text=''
        self.root.ids.home_screenmanager.current='home_menu_screen'
    
    def cancel_confirmation(self):
        self.dialog=MDDialog(
        
        title='Are your sure?',
        text=f'If you cancel addmission, the form will be reset!!',
        buttons=[
        
            MDFillRoundFlatIconButton(icon='arrow-left', text='Back',on_release=lambda x:self.dialog.dismiss()),
            MDFillRoundFlatIconButton(icon='cancel', text='Cancel',on_release=lambda x:(self.cancel(),self.dialog.dismiss()))
            
                ]
        )
        self.dialog.open()

   
    def on_date_selected(self, instance, value, date_range):
        self.root.ids.dob.text = f"{value}"
        self.root.ids.crr_student_dob.text = f"{value}"
    
    def dob(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def home_list(self):
        async def home_list():
            try :
                self.root.ids.homelst.clear_widgets()
                with open('database.json','r') as file:
                    data=json.load(file)
                for i in data:
                    name=i['first name']
                    rgtn=i['rgtn no']
                    tm=i['time']
                    await asynckivy.sleep(0)
                    self.func2(name, rgtn, tm)
            except :
                MDDialog(title='Empty File',text='No student available in database file.').open()
        asynckivy.start(home_list())
                
    def func2(self, name, rgtn, tm):
        string=f'''
MDCard:
    id: {rgtn}
    orientation: 'horizontal'
    spacing:20
    md_bg_color:0,0,0,0
    size_hint:1,None
    height:self.minimum_height
    FitImage:
        source:'dp.jpg'
        size_hint:None,None
        size:80,80
        radius:[90]
        pos_hint:{{'center_x':0.5,'center_y':0.5}}
    MDCard :
        orientation: 'vertical'
        adaptive_size:True
        spacing:2
        padding:[5]
        radius:[10]
        elevation :0
        height:self.minimum_height
        pos_hint: {{'center_y':0.5}}
        md_bg_color:0,0,0,0
        MDLabel:
            text:'{name}' 
            adaptive_size:True
            font_name:'SourceSansPro-SemiBold.ttf'
            font_size: '20sp'
            padding :[0]
            theme_text_color:'Custom'
            text_color: 0,0,0,1
        MDLabel:
            text:'{rgtn}' 
            adaptive_size:True
            font_size:'12sp'
            padding :[0]
            theme_text_color:'Custom'
            text_color:0.2647,0.4922,0.6765,1
        MDLabel:
            text:'{tm}' 
            adaptive_size:True
            font_size:'12sp'
            padding :[0]
            theme_text_color:'Custom'
            text_color:0.2647,0.4922,0.6765,1
    MDRelativeLayout:
        MDIconButton:
            icon:'chevron-right'
            theme_icon_color: 'Custom'
            icon_color:0,0,0,1
            pos_hint:{{'center_x':0.9,'center_y':0.5}}
            on_release:
                app.crrent_screen={rgtn}
                app.all_info({rgtn})

       
    '''
        sp='''
MDSeparator:
    md_bg_color:0.2647,0.4922,0.6765,0.1
'''
        
        dp=Builder.load_string(sp)
        wgd=Builder.load_string(string)
        self.root.ids.homelst.add_widget(wgd) 
        self.root.ids.homelst.add_widget(dp)


    def all_info(self, rgtn):
        data=self.all_student()
        self.current_screen=rgtn
        for i in data :
            if i['rgtn no']==rgtn :
                self.root.ids.student_name.text=f"{i['first name']} {i['last name']}"
                self.root.ids.student_father_name.text=i['father name']
                self.root.ids.student_mother_name.text=i['mother name']
                self.root.ids.student_dob.text=i['dob']
                self.root.ids.student_gender.text=i['gender']
                self.root.ids.student_catagory.text=i['catagory']
                self.root.ids.student_nationality.text=i['nationality']
                self.root.ids.student_aadhaar.text=f"{i['aadhaar']}"
                self.root.ids.student_class.text=f"{i['class']} {i['stream']}"
                self.root.ids.student_rgtn_no.text=f"{i['rgtn no']}"
                self.root.ids.student_roll_no.text=f"{i['roll no']}"
                self.root.ids.student_subjects.text=f"{i['core subject']}"
                self.root.ids.student_phone.text=f"{i['phone']}"
                self.root.ids.student_address.text=i['address']
                self.root.ids.student_rgtn_date.text=f"{i['time']}"
                self.root.ids.home_screenmanager.current='home_information_screen'
            elif i['rgtn no']==rgtn :
                pass
    
    def del_student(self):
        self.dialog=MDDialog(
        
        title='Delete student Record',
        text=f'If you want to delete student record click on the deleted button. on clicking the Student record will be deleted permenently!!',
        buttons=[
        
            MDFillRoundFlatIconButton(icon='arrow-left', text='Back',on_release=lambda x:self.dialog.dismiss() ),
            MDFillRoundFlatIconButton(icon='delete-forever', text='Delete',on_release=lambda x:(self.del_student2(),self.dialog.dismiss()))
            
                ]
        )
        self.dialog.open()
        
        
    def del_student2(self):
        self.root.ids.home_screenmanager.current='home_menu_screen'
        self.leave(rgtn_no=self.current_screen)
        self.home_list()
        
    def correction(self):
        self.root.ids.home_screenmanager.current='home_correction_screen'
        data=self.all_student()
        rgtn=self.current_screen
        for i in data :
            if i['rgtn no']==rgtn :
                self.root.ids.crr_student_first_name.text=f"{i['first name']}"
                self.root.ids.crr_student_last_name.text=f"{i['last name']}"
                self.root.ids.crr_student_father_name.text=i['father name']
                self.root.ids.crr_student_mother_name.text=i['mother name']
                self.root.ids.crr_student_dob.text=i['dob']
                self.root.ids.crr_student_gender.text=i['gender']
                self.root.ids.crr_student_catagory.text=i['catagory']
                self.root.ids.crr_student_nationality.text=i['nationality']
                self.root.ids.crr_student_aadhaar.text=f"{i['aadhaar']}"
                self.root.ids.crr_student_class.text=f"{i['class']}"
                self.root.ids.crr_student_stream.text=f"{i['stream']}"
                self.root.ids.crr_student_rgtn_no.text=f"{i['rgtn no']}"
                self.root.ids.crr_student_roll_no.text=f"{i['roll no']}"
                self.root.ids.crr_student_core_subjects.text=f"{i['core subject']}"
                self.root.ids.crr_student_optional_subjects.text=f"{i['optional subject']}"
                self.root.ids.crr_student_phone.text=f"{i['phone']}"
                self.root.ids.crr_student_address.text=i['address']
                self.root.ids.crr_student_rgtn_date.text=f"{i['time']}"
            else :
                pass
    
    def lam(self):
        self.dialog=MDDialog(
        
        title='Update Student',
        text=f"Please check the details first, if you want to update click on the Update Button",
        buttons=[
        
            MDFillRoundFlatIconButton(icon='arrow-left', text='Back',on_release=lambda x:self.dialog.dismiss()),
            MDFillRoundFlatIconButton(icon='update', text='Update',on_release=lambda x:(self.lam2(),self.dialog.dismiss()))
            
                ]
        )
        self.dialog.open()
    def lam2(self):
        with open('database.json', 'r') as fl :
            data=json.load(fl)
            for i,val in enumerate(data) :
                if val['rgtn no']==self.current_screen :
                    new_data={
                        'first name': self.root.ids.crr_student_first_name.text,
                        'last name' : self.root.ids.crr_student_last_name.text,
                        'father name' : self.root.ids.crr_student_father_name.text,
                        'mother name' : self.root.ids.crr_student_mother_name.text,
                        'rgtn no': int(self.root.ids.crr_student_rgtn_no.text),
                        'dob': self.root.ids.crr_student_dob.text,
                        'gender': self.root.ids.crr_student_gender.text,
                        'nationality': self.root.ids.crr_student_nationality.text,
                        'catagory': self.root.ids.crr_student_catagory.text,
                        'aadhaar' : self.root.ids.crr_student_aadhaar.text,
                        'class': self.root.ids.crr_student_class.text,
                        'roll no': int(self.root.ids.crr_student_roll_no.text),
                        'stream': self.root.ids.crr_student_stream.text,
                        'core subject': self.root.ids.crr_student_core_subjects.text,
                        'optional subject': self.root.ids.crr_student_optional_subjects.text,
                        'phone': self.root.ids.crr_student_phone.text,
                        'address': self.root.ids.crr_student_address.text,
                        'time' : self.root.ids.crr_student_rgtn_date.text
                        }
                    data[i]=new_data
                    with open('database.json', 'w') as fil :
                        json.dump(data, fil, indent=4)
                    notification('Update',f'the student with Registration number {self.current_screen} has  updated successfully.')
                    toast('please restart the app to refresh list')
                    self.root.ids.home_screenmanager.current='home_menu_screen'
    
    def search_student(self, TEXT):
        if TEXT.isdigit():
            self.all_info(int(TEXT))
        else:
            toast('This is not a valid registration number!')
    
    def addmission_screen(self):
        self.root.ids.home_screenmanager.current='home_menu_screen'
    
    def home_screen(self):
        pass
    
    def correction_screen(self):
        pass
    
    def leaving_screen(self):
        pass

myapp().run()