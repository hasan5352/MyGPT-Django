from rest_framework.views import APIView
from backend.utils.responses import send_json
from .serializers import ThreadSerializer, MessageSerializer, MessageInputSerializer
from .models import Thread, Message
from backend.utils.ai import get_ai_response

class ThreadListCreateApi(APIView):     # /api/threads
    def get(self, request):
        threads = Thread.objects.filter(user=request.user)
        serializer = ThreadSerializer(threads, many=True)
        return send_json("Threads retrieval successful", {"threads": serializer.data})

    def post(self, request):            # Create new thread + first message
        msg_serializer = MessageInputSerializer(data=request.data)
        msg_serializer.is_valid(raise_exception=True)
        message = msg_serializer.validated_data['message']

        title = get_ai_response(f"Ans in very short without formatting. 1-3 word title for: {message}")
        ai_response = get_ai_response(f"give short ans on: {message}")

        thread_serializer = ThreadSerializer(data={"title": title}, context={"request": request})
        thread_serializer.is_valid(raise_exception=True)
        thread = thread_serializer.save()

        msgs = [
            Message(role="user", content=message, thread=thread),
            Message(role="robot", content=ai_response, thread=thread)
        ]
        Message.objects.bulk_create(msgs)

        return send_json(
            'AI response generation successful', 
            body={"aiResponse": ai_response, "title": title, "threadId": thread.id}
        )

class ThreadDetailApi(APIView):         # /api/threads/<thread_id>
    def get(self, request, thread_id):          # Get all messages in thread
        thread = Thread.objects.filter(id=thread_id, user=request.user).first()

        if not thread:
            return send_json(f"Thread {thread_id} does not exist", {}, 404)

        messages = Message.objects.filter(thread=thread).order_by('created_at')
        serializer = MessageSerializer(messages, many=True)

        return send_json(
            "Thread successfully retrieved",
            {"title": thread.title, "messages": serializer.data}
        )

    def post(self, request, thread_id):         # Add message to thread
        thread = Thread.objects.filter(id=thread_id, user=request.user).first()

        if not thread:
            return send_json(f"Thread {thread_id} does not exist", {}, 404)

        msg_serializer = MessageInputSerializer(data=request.data)
        msg_serializer.is_valid(raise_exception=True)
        message = msg_serializer.validated_data['message']

        ai_response = get_ai_response(f"give short ans on: {message}")

        msgs = [
            Message(role="user", content=message, thread=thread),
            Message(role="robot", content=ai_response, thread=thread)
        ]
        Message.objects.bulk_create(msgs)

        return send_json("AI response successfully generated", {"aiResponse": ai_response})

    def delete(self, request, thread_id):           #delete thread and related messages
        thread = Thread.objects.filter(id=thread_id, user=request.user).first()

        if not thread:
            return send_json(f"Thread {thread_id} does not exist", {}, 404)

        thread.delete()     # deletes related messages too due to cascade

        return send_json(f"Thread {thread_id} successfully deleted", {})