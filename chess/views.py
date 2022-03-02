from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Piece, Board
from .serializer import PieceSerializer, BoardSerializer
from .services import get_two_turns_moves, valid_coordinate_format


class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

    @action(detail=True, methods=['post'])
    def moves(self, request, pk):
        data = request.data

        if(not 'coordinate' in data):
            content = {'error': 'Object must have coordinate.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if(not Board.objects.exists()):
            content = {
                'error': 'There is not any board created.'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        coordinate = data['coordinate']
        board = Board.objects.get()

        if(not valid_coordinate_format(coordinate, board)):
            content = {
                'error': 'Coordinate must have the algebraic notation and be into the board.'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        coordinates = []
        piece = self.get_object()
        if(piece.name == 'knight'):
            coordinates = get_two_turns_moves(coordinate, board)

        return Response(coordinates)


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
