from unicodedata import name
from django.contrib import admin
from .models import Piece, Board


class Pieces(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    list_display_links = ('id', 'name')
    search_fiealds = ('id', 'name')


class ChessBoard(admin.ModelAdmin):
    list_display = ('rows', 'columns')
    list_display_links = ('rows', 'columns')


admin.site.register(Piece, Pieces)
admin.site.register(Board, ChessBoard)
