import profile
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from librarian.models import *
from userrole.permissions import *
from librarian.serializers import *
from member.models import MemberProfile
# Create your views here.


class GetAllBooks(APIView):
    def get(self, request, *args, **kwargs):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response({'status': 'SUCCESS', 'data': serializer.data}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class AddBooks(APIView):
    permission_classes = [LibrarianPermissionClass]

    def post(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'SUCCESS', 'data': "Book Added"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class UpdateBook(APIView):
    permission_classes = [LibrarianPermissionClass]

    def get_object(self, book_id):
        return Book.objects.get(id=book_id)

    def patch(self, request, *args, **kwargs):

        try:

            serializer = BookSerializer(self.get_object(
                request.GET['book_id']), data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'SUCCESS', 'data': "Book Updated"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class DeleteBooks(APIView):
    permission_classes = [LibrarianPermissionClass]

    def delete(self, request, *args, **kwargs):
        try:
            book_id = request.GET['book_id']
            books = Book.objects.get(id=book_id)

            books.delete()

            return Response({'status': 'SUCCESS', 'data': "Book Delete"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class GetAllMembers(APIView):
    permission_classes = [LibrarianPermissionClass]

    def get(self, request, *args, **kwargs):
        try:
            member_profile = MemberProfile.objects.all()
            serializer = MemberSerializer(member_profile, many=True)
            return Response({'status': 'SUCCESS', 'data': serializer.data}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class AddMembers(APIView):
    permission_classes = [LibrarianPermissionClass]

    def post(self, request, *args, **kwargs):
        try:
            name = request.data['name']
            password = request.data['password']
            user = User.objects.create_user(username=name, password=password)
            user.set_password(password)
            user.save()
            serializer = MemberSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            RolesDefine.objects.create(
                user=user, role=RolesToAccess.objects.get(id=2))
            return Response({'status': 'SUCCESS', 'data': "Member Added"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class UpdateMembersData(APIView):
    permission_classes = [LibrarianPermissionClass]

    def get_object(self, profile_id):
        return MemberProfile.objects.get(id=profile_id)

    def patch(self, request, *args, **kwargs):
        try:
            serializer = MemberSerializer(self.get_object(
                request.GET['profile_id']), data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'SUCCESS', 'data': "Member details Updated"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)


class DeleteMember(APIView):
    permission_classes = [LibrarianPermissionClass]

    def delete(self, request, *args, **kwargs):
        try:
            
            profile_id=self.request.GET['profile_id']
            member=MemberProfile.objects.get(id=profile_id)
            user=User.objects.get(username=member.name)
            roles=RolesDefine.objects.get(user=user)
            roles.delete()
            member.delete()
            user.delete()
            return Response({'status': 'SUCCESS', 'data': "Member Delete"}, status=201)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)
