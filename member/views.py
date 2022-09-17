from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from userrole.permissions import *
from member.serializers import *
# Create your views here.

# class BorrowBookAPI(APIView):


class BorrowBookAPI(APIView):
    permission_classes = [MemberPermissionClass]

    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            book_name = Book.objects.get(id=request.data['book_name'])
            print(book_name)
            if book_name.book_status == "BORROWED":
                return Response({'status': 'SUCCESS', 'data': "Book not available"}, status=400)
            print(request.user.id)
            BookBorrwed.objects.create(book_name=book_name,User=request.user)
            print('not borrow')
            Book.objects.update(id=book_name.id, book_status="BORROWED")
            return Response({'status': 'SUCCESS', 'data': "BOOK BORROWED"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)

class ReturnBookAPI(APIView):
    permission_classes = [MemberPermissionClass]

    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            book_name = Book.objects.get(id=request.data['book_name'])
            ReturnBook.objects.create(book_name=book_name,user=request.user)
            Book.objects.update(id=book_name.id, book_status="AVAILABLE")
            return Response({'status': 'SUCCESS', 'data': "BOOK RETURNED"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)

class DeleteMembers(APIView):
    permission_classes = [MemberPermissionClass]

    def delete(self, request, *args, **kwargs):
        try:
            profile_id=self.request.GET['profile_id']
            member=MemberProfile.objects.get(id=profile_id)
            user=User.objects.get(username=member.name)
            roles=RolesDefine.objects.get(user=user)
            print(roles)
            roles.delete()
            member.delete()
            user.delete()

            return Response({'status': 'SUCCESS', 'data': "User Deleted"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)

