from django.shortcuts import render,redirect
from discussion.models import discussion_Comment
from courses.models import Batch# import course model
from trainee.models import Student
from django.contrib import messages
from rest_framework.views import APIView
#from discussion.serializer import discussion_comment_Serializer # import pizza_choice form seializer file.
from rest_framework import generics # import generic from django rest_framework
from discussion.serializers import discussion_comment_Serializer
from rest_framework.response import Response

# Create your views here.


# logic for the write the replay.
def blogPost(request,slug):
    post = Batch.objects.filter(slug=slug).first()
    post.save()
    comments = discussion_Comment.objects.filter(post=post, parent=None)
    replies = discussion_Comment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "discussion.html", context)

# logic for the write the comments.
def postComment(request):
    if request.method == "POST":
        batch = Batch.objects.filter(batch_name=Student)
        comment = request.POST.get('comment')
        user = request.user
        discussionSno =request.POST.get('postSno')
        discussion = Batch.objects.get(sno=discussionSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = discussion_Comment(comment=comment, user=user, discussion=discussion)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = discussion_Comment.objects.get(sno=parentSno)
            comment = discussion_Comment(comment=comment, user=user, discussion=discussion, parent=parent)
            comment.save()
            messages.success(request, "Your replay has been posted successfully")
    return redirect("discussion.html", {'batch':batch})

class create_discussion(generics.ListCreateAPIView): # api for the post the api
    queryset = discussion_Comment.objects.all()
    serializer_class = discussion_comment_Serializer

class view_discussion(APIView): # api for the get request.
    def get(self,request):
        discussion_form = discussion_Comment.objects.all()
        disccusion_view_api = discussion_comment_Serializer(discussion_form, many=True)
        return Response(disccusion_view_api.data)

